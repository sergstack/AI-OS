#!/usr/bin/env python3
"""Read-only validator, hard-veto engine, immutable ledger, and comparator
for AIOS AutoResearch v0.1 (issue #392, parent #388).

This module NEVER calls a provider or model, executes an experiment, mutates
a worktree, or opens a Project/PR/commit. It only validates already-produced
eval cases, experiment records, and batch manifests against the schemas from
issue #391 and the frozen contract/manifest from issue #390
(docs/standards/AUTORESEARCH_V01_CONTRACT.md,
docs/standards/autoresearch_v01_manifest.json), applies deterministic hard
vetoes, appends accepted records to a tamper-evident JSONL ledger, and emits
a transparent comparison artifact with explicit behavioral/efficiency
vectors -- never a single weighted score.

Decision hierarchy (issue #392):
    Layer 1: hard invariants (dominates everything else)
    Layer 2: behavioral non-regression / improvement
    Layer 3: efficiency, only after Layer 2 non-inferiority

A Finding means the record/action is REJECTED (fail-closed): callers must
treat any non-empty finding list as "do not append / do not accept",
regardless of what the record's own `decision` field claims.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = REPO_ROOT / "schemas"
MANIFEST_PATH = REPO_ROOT / "docs" / "standards" / "autoresearch_v01_manifest.json"

EVAL_CASE_SCHEMA_PATH = SCHEMAS / "autoresearch_eval_case.schema.json"
EXPERIMENT_SCHEMA_PATH = SCHEMAS / "autoresearch_experiment_record.schema.json"
BATCH_MANIFEST_SCHEMA_PATH = SCHEMAS / "autoresearch_batch_manifest.schema.json"
SEMANTIC_FINDING_SCHEMA_PATH = SCHEMAS / "autoresearch_semantic_finding.schema.json"

VERDICT_PRECEDENCE = {"pass": 0, "revise": 1, "blocked": 2}  # higher wins in worst_verdict()

# Ceiling on authority/merge/production a ledger append may ever carry.
# The ledger only ever receives Researcher-authored records; a legitimate
# owner acceptance/merge/production event happens outside this module
# entirely (issue #390 authority_separation: researcher/evaluator/owner are
# separate roles; this module plays researcher+evaluator, never owner).
LEDGER_MAX_AUTHORITY_STATUS = {"not_required", "owner_review_pending"}
LEDGER_MAX_MERGE_STATUS = {"not_applicable", "not_opened", "open", "checks_pending", "owner_review_pending"}
LEDGER_MAX_PRODUCTION_STATUS = {"not_applicable", "not_authorized"}


class ContractError(ValueError):
    """Raised when the schemas/manifest inputs to this module are themselves
    malformed. Never raised for a bad experiment/case record -- those
    produce Findings instead."""


@dataclass(frozen=True)
class Finding:
    """One validator finding: one invariant or schema violation."""

    path: str
    rule: str
    severity: str  # "critical" | "high" | "medium"
    evidence: str
    consequence: str  # e.g. "reject", "discard", "batch_invalidated", "human_review_required"

    def __str__(self) -> str:  # pragma: no cover - convenience only
        return f"[{self.severity}] {self.rule} @ {self.path}: {self.evidence} -> {self.consequence}"


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_validator(schema_path: Path):
    try:
        import jsonschema
    except ImportError as exc:  # pragma: no cover - dev dependency, present in CI
        raise ContractError(
            "jsonschema is required to run this validator (pip install -r requirements-dev.txt)"
        ) from exc
    return jsonschema.Draft7Validator(_load_json(schema_path))


def _schema_findings(doc: dict, schema_path: Path, kind: str) -> list[Finding]:
    validator = _schema_validator(schema_path)
    out = []
    for e in sorted(validator.iter_errors(doc), key=lambda e: list(e.path)):
        p = "/".join(str(x) for x in e.path) or "<root>"
        out.append(Finding(path=p, rule=f"SCHEMA:{kind}", severity="critical", evidence=e.message, consequence="reject"))
    return out


def load_manifest() -> dict:
    return _load_json(MANIFEST_PATH)


def canonical_bytes(doc: dict, *, exclude: tuple[str, ...] = ()) -> bytes:
    """Deterministic canonicalization used for both content-hash checks and
    ledger line hashing: sort_keys, no extra whitespace, excluded top-level
    keys removed."""
    trimmed = {k: v for k, v in doc.items() if k not in exclude}
    return json.dumps(trimmed, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# 1-2. Schema + content-hash validation
# ---------------------------------------------------------------------------


def validate_eval_case(doc: dict) -> list[Finding]:
    findings = _schema_findings(doc, EVAL_CASE_SCHEMA_PATH, "eval_case")
    if findings:
        return findings  # a schema-invalid doc cannot be hash-checked meaningfully
    expected = sha256_hex(canonical_bytes(doc, exclude=("content_hash", "case_revision", "schema_version")))
    if doc["content_hash"] != expected:
        findings.append(
            Finding(
                path="content_hash",
                rule="CONTENT_HASH_MISMATCH",
                severity="critical",
                evidence=f"declared {doc['content_hash']} != recomputed {expected}",
                consequence="reject",
            )
        )
    return findings


def validate_experiment_record_schema(doc: dict) -> list[Finding]:
    return _schema_findings(doc, EXPERIMENT_SCHEMA_PATH, "experiment_record")


def validate_batch_manifest(doc: dict) -> list[Finding]:
    findings = _schema_findings(doc, BATCH_MANIFEST_SCHEMA_PATH, "batch_manifest")
    if not findings:
        findings.extend(check_split_lineage_disjoint(doc))
    return findings


# ---------------------------------------------------------------------------
# Semantic evaluator findings (issue #394): schema validation and worst-case
# aggregation only. The evaluator itself -- and any de-blinding of A/B back
# to baseline/candidate -- is not implemented here; issue #394's contract
# (ChatGPT/[LLM]/Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md)
# explicitly routes a real runner integration to a separate [Codex] task.
# ---------------------------------------------------------------------------


def validate_semantic_finding(doc: dict) -> list[Finding]:
    return _schema_findings(doc, SEMANTIC_FINDING_SCHEMA_PATH, "semantic_finding")


def worst_verdict(findings: list[dict]) -> str:
    """Deterministic aggregation across a set of semantic findings for one
    case: blocked > revise > pass (AES precedence -- a single blocked or
    revise finding is never silently outvoted by several pass findings).
    Raises on an empty list: an evaluator run that produced zero findings is
    a validator/caller bug, not a legitimate 'pass'."""
    if not findings:
        raise ContractError("worst_verdict() called with no findings; an empty result must never be treated as pass")
    return max(findings, key=lambda f: VERDICT_PRECEDENCE[f["verdict"]])["verdict"]


def check_split_lineage_disjoint(batch_manifest: dict) -> list[Finding]:
    """Validation/holdout lineages must never overlap train lineages
    (issue #391/#392). JSON Schema cannot express this; it is a plain
    structural check, same function shape as tests/test_autoresearch_schemas.py's
    lineages_disjoint() -- reused here rather than reimplemented."""
    sm = batch_manifest.get("split_membership", {})
    train = set(sm.get("train", []))
    findings = []
    for other in ("validation", "holdout"):
        overlap = train & set(sm.get(other, []))
        if overlap:
            findings.append(
                Finding(
                    path=f"split_membership/{other}",
                    rule="SPLIT_LINEAGE_OVERLAP",
                    severity="critical",
                    evidence=f"{other} overlaps train: {sorted(overlap)}",
                    consequence="reject",
                )
            )
    return findings


# ---------------------------------------------------------------------------
# 3. Protected-surface / mutable-surface enforcement (INV-01)
# ---------------------------------------------------------------------------


def _mutable_surface_ids(manifest: dict) -> set[str]:
    return {s["surface_id"] for s in manifest["mutable_surfaces"]}


def _protected_surface_ids(manifest: dict) -> set[str]:
    return {s["surface_id"] for s in manifest["protected_surfaces"]}


def reject_protected_surface_touch(record: dict, manifest: dict) -> list[Finding]:
    findings: list[Finding] = []
    mutable_ids = _mutable_surface_ids(manifest)
    protected_ids = _protected_surface_ids(manifest)

    surface = record.get("research_surface")
    if surface not in mutable_ids:
        findings.append(
            Finding(
                path="research_surface",
                rule="INV-01",
                severity="critical",
                evidence=f"research_surface {surface!r} is not a declared mutable surface",
                consequence="discard",
            )
        )

    for entry in record.get("protected_scope", []):
        if entry not in protected_ids:
            findings.append(
                Finding(
                    path="protected_scope",
                    rule="INV-01",
                    severity="medium",
                    evidence=f"protected_scope entry {entry!r} is not a declared protected surface id",
                    consequence="reject",
                )
            )

    for entry in record.get("affected_scope", []):
        if entry in protected_ids:
            findings.append(
                Finding(
                    path="affected_scope",
                    rule="INV-01",
                    severity="critical",
                    evidence=f"affected_scope touches protected surface {entry!r}",
                    consequence="discard",
                )
            )
    return findings


# ---------------------------------------------------------------------------
# 4. Multi-mechanism detection (INV-05)
# ---------------------------------------------------------------------------


def reject_multi_mechanism(record: dict, manifest: dict) -> list[Finding]:
    """One experiment = one target_surface_id (issue #388 Grain). A record
    whose affected_scope resolves to more than one distinct mutable surface
    -- other than its own declared research_surface -- has widened scope
    mid-experiment."""
    mutable = {s["surface_id"]: s for s in manifest["mutable_surfaces"]}
    declared = record.get("research_surface")
    touched_paths = set(record.get("affected_scope", []))
    other_surfaces_touched = set()
    for sid, s in mutable.items():
        if sid == declared:
            continue
        # A path counts as "touched" only if the record literally names that
        # surface's file among affected_scope entries.
        if any(s["path"] in p for p in touched_paths):
            other_surfaces_touched.add(sid)
    if other_surfaces_touched:
        return [
            Finding(
                path="affected_scope",
                rule="INV-05",
                severity="high",
                evidence=(
                    f"affected_scope touches surfaces beyond the declared research_surface "
                    f"{declared!r}: {sorted(other_surfaces_touched)}"
                ),
                consequence="discard",
            )
        ]
    return []


# ---------------------------------------------------------------------------
# 5. Causal attribution (INV-06)
# ---------------------------------------------------------------------------


def validate_attribution(record: dict) -> list[Finding]:
    status = record.get("attribution_status")
    decision = record.get("decision")
    findings: list[Finding] = []
    if status == "rejected" and decision == "keep_candidate":
        findings.append(
            Finding(
                path="attribution_status",
                rule="INV-06",
                severity="critical",
                evidence="rejected causal attribution can never support keep_candidate",
                consequence="discard",
            )
        )
    elif status == "uncertain" and decision == "keep_candidate":
        # Contract exception: uncertain attribution permits only a bounded
        # discriminating experiment. Issue #391's schema has no
        # discriminating_experiment field to check deterministically, so
        # this module does NOT auto-reject (a false reject would block a
        # legitimate discriminating experiment) -- it flags for human
        # review instead. See README/PR notes: a future schema revision
        # should add an explicit field to close this gap deterministically.
        findings.append(
            Finding(
                path="attribution_status",
                rule="INV-06",
                severity="high",
                evidence="uncertain attribution + keep_candidate is only valid as a bounded discriminating experiment; not deterministically verifiable from the current schema",
                consequence="human_review_required",
            )
        )
    return findings


# ---------------------------------------------------------------------------
# 6. NOT RUN != PASS
# ---------------------------------------------------------------------------


def reject_not_run_as_pass(record: dict) -> list[Finding]:
    not_run_gates = [g for g in record.get("hard_gate_results", []) if g.get("status") == "not_run"]
    if not_run_gates and record.get("decision") == "keep_candidate":
        return [
            Finding(
                path="hard_gate_results",
                rule="NOT_RUN_NE_PASS",
                severity="critical",
                evidence=f"{len(not_run_gates)} hard gate(s) were not_run but decision is keep_candidate",
                consequence="reject",
            )
        ]
    return []


# ---------------------------------------------------------------------------
# 7. Implicit authority conversion
# ---------------------------------------------------------------------------


def reject_authority_escalation(record: dict) -> list[Finding]:
    """A Researcher-authored record (the only kind this module ever produces
    or accepts into the ledger) may never claim owner acceptance, a merged
    PR, or production authorization -- regardless of decision or verdict.
    This generalizes issue #391's schema-level keep_candidate restriction to
    every record the ledger will accept, closing issue #392's broader
    'Judge pass paired with owner approval/merge/production conversion
    without authority evidence' check."""
    findings = []
    if record.get("authority_status") not in LEDGER_MAX_AUTHORITY_STATUS:
        findings.append(
            Finding(
                path="authority_status",
                rule="INV-08",
                severity="critical",
                evidence=f"authority_status {record.get('authority_status')!r} exceeds what a Researcher-authored record may claim",
                consequence="reject",
            )
        )
    if record.get("merge_status") not in LEDGER_MAX_MERGE_STATUS:
        findings.append(
            Finding(
                path="merge_status",
                rule="INV-08",
                severity="critical",
                evidence=f"merge_status {record.get('merge_status')!r} exceeds what a Researcher-authored record may claim",
                consequence="reject",
            )
        )
    if record.get("production_status") not in LEDGER_MAX_PRODUCTION_STATUS:
        findings.append(
            Finding(
                path="production_status",
                rule="INV-08",
                severity="critical",
                evidence=f"production_status {record.get('production_status')!r} exceeds what a Researcher-authored record may claim",
                consequence="reject",
            )
        )
    return findings


# ---------------------------------------------------------------------------
# 8. Hard-invariant veto dominance (Layer 1 over Layer 2/3)
# ---------------------------------------------------------------------------


def enforce_hard_veto_dominance(record: dict) -> list[Finding]:
    violated = [g for g in record.get("hard_gate_results", []) if g.get("status") == "violated"]
    has_integrity_event = bool(record.get("integrity_events"))
    if (violated or has_integrity_event) and record.get("decision") != "discard":
        return [
            Finding(
                path="decision",
                rule="HARD_VETO_DOMINANCE",
                severity="critical",
                evidence=(
                    f"{len(violated)} violated hard gate(s) / "
                    f"{len(record.get('integrity_events', []))} integrity event(s) present, "
                    f"but decision is {record.get('decision')!r}, not discard "
                    "(a Layer 1 veto must dominate any Layer 2/3 improvement)"
                ),
                consequence="reject",
            )
        ]
    return []


# ---------------------------------------------------------------------------
# 9. Environment/configuration mismatch and batch integrity (INV-03, INV-09)
# ---------------------------------------------------------------------------


def reject_environment_mismatch(record: dict, batch_manifest: dict) -> list[Finding]:
    findings: list[Finding] = []
    baseline_rev = batch_manifest["baseline"]["source_revision"]
    if record.get("baseline_revision") != baseline_rev:
        findings.append(
            Finding(
                path="baseline_revision",
                rule="INV-09",
                severity="critical",
                evidence=f"record baseline_revision {record.get('baseline_revision')!r} != batch baseline {baseline_rev!r}",
                consequence="reject",
            )
        )
    frozen = batch_manifest["frozen_hashes"]
    em = record.get("eval_manifest", {})
    for key in ("evaluator_hash", "split_hash", "threshold_hash"):
        if em.get(key) != frozen.get(key):
            findings.append(
                Finding(
                    path=f"eval_manifest/{key}",
                    rule="INV-03",
                    severity="critical",
                    evidence=f"{key} {em.get(key)!r} != frozen batch value {frozen.get(key)!r}",
                    consequence="batch_invalidated",
                )
            )
    return findings


def infra_failure_maps_to_inconclusive(record: dict) -> list[Finding]:
    """Layer 3 (efficiency) may only inform keep_candidate after Layer 2
    non-inferiority AND an actual measurement. An unmeasured efficiency
    result behind a keep_candidate decision is an infrastructure gap, not
    evidence of a good candidate, and must never be silently treated as a
    pass."""
    eff = record.get("efficiency_results", {})
    if eff.get("measured") is False and record.get("decision") == "keep_candidate":
        return [
            Finding(
                path="efficiency_results/measured",
                rule="INFRA_FAILURE_NOT_DEGRADATION",
                severity="high",
                evidence="efficiency was not measured but decision is keep_candidate; unmeasured infrastructure must map to inconclusive, never a pass",
                consequence="reject",
            )
        ]
    return []


# ---------------------------------------------------------------------------
# Composite record validation (schema + all deterministic checks)
# ---------------------------------------------------------------------------


def validate_experiment_record(record: dict, manifest: dict, batch_manifest: dict) -> list[Finding]:
    findings = validate_experiment_record_schema(record)
    if findings:
        return findings  # schema-invalid: downstream checks would be meaningless
    findings += reject_protected_surface_touch(record, manifest)
    findings += reject_multi_mechanism(record, manifest)
    findings += validate_attribution(record)
    findings += reject_not_run_as_pass(record)
    findings += reject_authority_escalation(record)
    findings += enforce_hard_veto_dominance(record)
    findings += reject_environment_mismatch(record, batch_manifest)
    findings += infra_failure_maps_to_inconclusive(record)
    return findings


# ---------------------------------------------------------------------------
# Append-only ledger (tamper-evident JSONL hash chain)
# ---------------------------------------------------------------------------


GENESIS_HASH = "0" * 64


def _ledger_line_hash(seq: int, prev_hash: str, record: dict) -> str:
    payload = json.dumps({"seq": seq, "prev_hash": prev_hash, "record": record}, sort_keys=True, separators=(",", ":"))
    return sha256_hex(payload.encode("utf-8"))


def read_ledger(ledger_path: Path) -> list[dict]:
    if not ledger_path.exists():
        return []
    lines = []
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            lines.append(json.loads(line))
    return lines


def verify_ledger(ledger_path: Path) -> list[Finding]:
    """Re-walks the ledger and recomputes the hash chain. Any edit, delete,
    or reorder of a past line breaks the chain and is reported here -- this
    is the deterministic 'past ledger row edited, deleted, or reordered ->
    reject' check from issue #392."""
    lines = read_ledger(ledger_path)
    findings: list[Finding] = []
    prev_hash = GENESIS_HASH
    seen_experiment_ids: set[str] = set()
    for i, line in enumerate(lines):
        expected_seq = i
        expected_hash = _ledger_line_hash(line.get("seq"), line.get("prev_hash"), line.get("record", {}))
        if line.get("seq") != expected_seq:
            findings.append(
                Finding(
                    path=f"ledger[{i}]",
                    rule="LEDGER_REORDERED",
                    severity="critical",
                    evidence=f"line {i} declares seq={line.get('seq')}, expected {expected_seq}",
                    consequence="reject",
                )
            )
        if line.get("prev_hash") != prev_hash:
            findings.append(
                Finding(
                    path=f"ledger[{i}]",
                    rule="LEDGER_TAMPERED",
                    severity="critical",
                    evidence=f"line {i} prev_hash {line.get('prev_hash')!r} != expected {prev_hash!r} (an earlier line was edited, deleted, or reordered)",
                    consequence="reject",
                )
            )
        if line.get("line_hash") != expected_hash:
            findings.append(
                Finding(
                    path=f"ledger[{i}]",
                    rule="LEDGER_TAMPERED",
                    severity="critical",
                    evidence=f"line {i} line_hash does not match its own recomputed content (edited in place)",
                    consequence="reject",
                )
            )
        record = line.get("record", {})
        exp_id = record.get("experiment_id")
        correction_of = record.get("correction_of")
        if exp_id in seen_experiment_ids and not correction_of:
            findings.append(
                Finding(
                    path=f"ledger[{i}]",
                    rule="DUPLICATE_WITHOUT_CORRECTION",
                    severity="critical",
                    evidence=f"experiment_id {exp_id!r} reappears without correction_of",
                    consequence="reject",
                )
            )
        if correction_of and correction_of not in seen_experiment_ids:
            findings.append(
                Finding(
                    path=f"ledger[{i}]",
                    rule="CORRECTION_WITHOUT_VALID_TARGET",
                    severity="critical",
                    evidence=f"correction_of {correction_of!r} does not reference a prior ledger entry",
                    consequence="reject",
                )
            )
        seen_experiment_ids.add(exp_id)
        prev_hash = line.get("line_hash", prev_hash)
    return findings


def ledger_append(ledger_path: Path, record: dict, manifest: dict, batch_manifest: dict) -> list[Finding]:
    """Validate `record` fully, then append it to the JSONL ledger as a new
    hash-chained line. Returns the finding list; a non-empty list means the
    record was REJECTED and nothing was written (fail-closed, read-only
    until a record actually clears every gate)."""
    findings = validate_experiment_record(record, manifest, batch_manifest)
    if findings:
        return findings

    existing = read_ledger(ledger_path)
    seen_ids = {line["record"].get("experiment_id") for line in existing}
    exp_id = record.get("experiment_id")
    correction_of = record.get("correction_of")
    if exp_id in seen_ids and not correction_of:
        return [
            Finding(
                path="experiment_id",
                rule="DUPLICATE_WITHOUT_CORRECTION",
                severity="critical",
                evidence=f"experiment_id {exp_id!r} already exists in the ledger without correction_of",
                consequence="reject",
            )
        ]
    if correction_of and correction_of not in seen_ids:
        return [
            Finding(
                path="correction_of",
                rule="CORRECTION_WITHOUT_VALID_TARGET",
                severity="critical",
                evidence=f"correction_of {correction_of!r} does not reference an existing ledger entry",
                consequence="reject",
            )
        ]

    seq = len(existing)
    prev_hash = existing[-1]["line_hash"] if existing else GENESIS_HASH
    line_hash = _ledger_line_hash(seq, prev_hash, record)
    line = {"seq": seq, "prev_hash": prev_hash, "record": record, "line_hash": line_hash}
    with ledger_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(line, sort_keys=True, separators=(",", ":")) + "\n")
    return []


# ---------------------------------------------------------------------------
# Comparator: inspectable comparison artifact, no scalar score
# ---------------------------------------------------------------------------

_SCORE_LIKE_KEY_FRAGMENTS = ("score", "rating", "quality_index", "weighted")


def build_comparison_artifact(candidate_record: dict, batch_manifest: dict) -> dict:
    """Emit a transparent comparison artifact. Every field is an explicit,
    inspectable dimension; no field aggregates behavior+efficiency into one
    number (issue #388/#390: no opaque weighted AIOS quality score)."""
    artifact = {
        "artifact_version": "0.1.0",
        "batch_id": batch_manifest["batch_id"],
        "baseline_revision": batch_manifest["baseline"]["source_revision"],
        "candidate_revision": candidate_record["candidate_revision"],
        "experiment_id": candidate_record["experiment_id"],
        "research_surface": candidate_record["research_surface"],
        "hard_gate_results": candidate_record["hard_gate_results"],
        "behavioral_vector": {
            "verdict": candidate_record["behavioral_results"]["verdict"],
            "delta": candidate_record["behavioral_results"]["delta"],
            "notes": candidate_record["behavioral_results"]["notes"],
        },
        "efficiency_vector": {
            "measured": candidate_record["efficiency_results"]["measured"],
            "cost_delta": candidate_record["efficiency_results"]["cost_delta"],
            "latency_delta": candidate_record["efficiency_results"]["latency_delta"],
            "notes": candidate_record["efficiency_results"]["notes"],
        },
        "regressions": candidate_record["regressions"],
        "variance_notes": candidate_record["variance_notes"],
        "integrity_events": candidate_record["integrity_events"],
        "decision": candidate_record["decision"],
        "decision_basis": candidate_record["decision_basis"],
    }
    return artifact


def assert_no_scalar_score(artifact: dict) -> list[Finding]:
    findings = []
    for key in artifact:
        lowered = key.lower()
        if any(frag in lowered for frag in _SCORE_LIKE_KEY_FRAGMENTS):
            findings.append(
                Finding(
                    path=key,
                    rule="NO_SCALAR_SCORE",
                    severity="critical",
                    evidence=f"comparison artifact top-level key {key!r} reads as an aggregate/weighted score",
                    consequence="reject",
                )
            )
    return findings
