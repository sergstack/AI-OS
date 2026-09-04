#!/usr/bin/env python3
"""Failure-to-experiment front end for AIOS AutoResearch v0.2
(issue #415, parent #409).

Turns EITHER a sanitized field-observed AI-OS failure OR a reproducible live
baseline failure into ONE bounded, falsifiable, minimal, reversible experiment
proposal -- and fails closed whenever the evidence does not support a
control-surface change.

The flow keeps these states separate and machine-checkable, never collapsed:

    observed
    -> sanitized / provenance-checked
    -> reproduction_attempted
    -> reproduced | not_reproduced | reproduction_inconclusive
    -> attribution_assessed
    -> supported | uncertain | rejected
    -> proposal_eligible | discriminating_experiment_only | ineligible
    -> one bounded Researcher proposal
    -> deterministic preflight
    -> ready_for_experiment | rejected

It does NOT: apply, accept, promote, or iterate a patch; run an experiment or
A/B comparison; make a Judge decision; access holdout; advance a baseline;
commit / PR / merge / deploy. It reuses `FAILURE_REGISTRY.md`'s
`attributable | uncertain | ineligible` attribution vocabulary and does not
create a second failure registry -- these records carry only AutoResearch
linkage fields and reference the canonical ones.

No real browser / network / model call happens in this module's own code;
`FakeResearcherModel` is deterministic and does no I/O.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Protocol

import sys

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import autoresearch_live_browser_adapter as lba  # noqa: E402
import autoresearch_shadow_runner as asr  # noqa: E402  (reuse patch-scope / worktree, unchanged)
import autoresearch_validator as av  # noqa: E402


SOURCE_TYPES = frozenset({"field_observation", "live_baseline", "calibration_fixture"})
REPRODUCTION_STATUSES = frozenset(
    {"not_attempted", "reproduced", "not_reproduced", "reproduction_inconclusive"}
)
#: Reuses FAILURE_REGISTRY.md's vocabulary; `supported` here == that doc's
#: `attributable` (the #415 issue text uses `supported`).
ATTRIBUTION_STATUSES = frozenset({"supported", "uncertain", "rejected"})
ELIGIBILITY = frozenset({"proposal_eligible", "discriminating_experiment_only", "ineligible"})
PREFLIGHT_RESULTS = frozenset({"ready_for_experiment", "rejected"})
SENSITIVITY_CLASSES = frozenset({"none", "low", "business_sensitive", "personal", "restricted"})
PROVENANCE = frozenset({"none", "sanitized", "synthetic", "raw_restricted"})

MUTATION_CLASSES = frozenset(
    {"wording_clarification", "ordering_adjustment", "tiebreak_rule_text", "context_priority_text"}
)


class FailureIntakeError(RuntimeError):
    """A fail-closed intake/attribution/preflight invariant break."""


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# Field-trace sanitisation (fail-closed)
# ---------------------------------------------------------------------------

_SECRET_RE = tuple(pat for _n, pat in lba._SECRET_PATTERNS)  # reuse #413's set unchanged


def sanitization_findings(record: dict) -> list[str]:
    """Reasons this record must NOT enter public evidence. Empty list == ok."""
    problems: list[str] = []
    prov = record.get("field_trace_provenance")
    if prov not in PROVENANCE:
        problems.append(f"field_trace_provenance missing/invalid: {prov!r}")
    if prov == "raw_restricted":
        problems.append("raw_restricted trace is never committed to the public repo")
    if record.get("sanitization_status") != "sanitized":
        problems.append("sanitization_status is not 'sanitized'")
    if record.get("sensitivity_class") not in SENSITIVITY_CLASSES:
        problems.append(f"sensitivity_class missing/invalid: {record.get('sensitivity_class')!r}")
    blob = json.dumps(record, ensure_ascii=False)
    for pat in _SECRET_RE:
        if pat.search(blob):
            problems.append(f"secret-shaped content in record ({pat.pattern[:24]}...)")
            break
    return problems


def intake_field_observation(record: dict) -> tuple[Optional[dict], list[str]]:
    """A field observation establishes only that an output occurred. It is
    never `reproduced` on intake, and unknown revision/model/context stay
    unknown -- no fabricated replay equivalence."""
    problems = sanitization_findings(record)
    if record.get("source_type") != "field_observation":
        problems.append("source_type must be 'field_observation' for this intake path")
    if problems:
        return None, problems
    normalised = dict(record)
    normalised.setdefault("source_revision_if_known", None)
    normalised["reproduction_status"] = "not_attempted"
    for k in ("reproduction_context_hash", "reproduction_model_hash"):
        normalised.setdefault(k, None)
    return normalised, []


# ---------------------------------------------------------------------------
# Reproduction assessment
# ---------------------------------------------------------------------------


def assess_reproduction(record: dict, reproduction_runs: list[dict]) -> dict:
    """`reproduced` requires >= 2 repo-replay runs that each carry real
    invocation + context_hash + model_hash evidence AND all show the failure
    signal. A field observation with zero qualifying runs is
    `not_reproduced`, never `reproduced` (#415 non-acceptance: 'A field trace
    with unknown context is called reproduced')."""
    out = dict(record)
    qualifying = [
        r
        for r in reproduction_runs
        if r.get("invocation_id")
        and re.fullmatch(r"[0-9a-f]{64}", str(r.get("context_hash", "")))
        and re.fullmatch(r"[0-9a-f]{64}", str(r.get("model_hash", "")))
    ]
    if not qualifying:
        out["reproduction_status"] = "not_reproduced"
        out["reproduction_run_refs"] = []
        out["reproduction_context_hash"] = None
        out["reproduction_model_hash"] = None
        return out
    signals = [bool(r.get("failure_signal_present")) for r in qualifying]
    ctxs = {r["context_hash"] for r in qualifying}
    models = {r["model_hash"] for r in qualifying}
    if len(qualifying) >= 2 and all(signals) and len(ctxs) == 1 and len(models) == 1:
        out["reproduction_status"] = "reproduced"
    elif any(signals):
        out["reproduction_status"] = "reproduction_inconclusive"
    else:
        out["reproduction_status"] = "not_reproduced"
    out["reproduction_run_refs"] = [r["invocation_id"] for r in qualifying]
    out["reproduction_context_hash"] = next(iter(ctxs)) if len(ctxs) == 1 else None
    out["reproduction_model_hash"] = next(iter(models)) if len(models) == 1 else None
    return out


# ---------------------------------------------------------------------------
# Causal attribution
# ---------------------------------------------------------------------------


def assess_attribution(record: dict) -> dict:
    """supported | uncertain | rejected.

    - `rejected` when the recorded `attribution_evidence` explicitly rules out
      a mutable-surface cause, or `candidate_cause` is empty.
    - `supported` requires: reproduction_status == 'reproduced',
      non-empty trace-grounded `attribution_evidence`, a `cause_target` in the
      mutable allowlist, AND every `plausible_alternative_causes` entry marked
      addressed (`minimal_discriminating_test` present).
    - everything else is `uncertain` -- a reproduced behavior with no causal
      evidence stays `uncertain`, never upgraded for convenience.
    """
    out = dict(record)
    cause = (record.get("candidate_cause") or "").strip()
    evidence = (record.get("attribution_evidence") or "").strip()
    alts = record.get("plausible_alternative_causes") or []
    disc = (record.get("minimal_discriminating_test") or "").strip()
    target = (record.get("cause_target") or "").strip()

    if not cause or record.get("attribution_explicitly_rejected") is True:
        out["attribution_status"] = "rejected"
        return out
    reproduced = record.get("reproduction_status") == "reproduced"
    unresolved_alts = [a for a in alts if not str(a).strip().endswith("[addressed]")]
    if reproduced and evidence and target and not unresolved_alts and disc:
        out["attribution_status"] = "supported"
    else:
        out["attribution_status"] = "uncertain"
    return out


def eligibility_for(attribution_status: str) -> str:
    return {
        "supported": "proposal_eligible",
        "uncertain": "discriminating_experiment_only",
        "rejected": "ineligible",
    }[attribution_status]


# ---------------------------------------------------------------------------
# Frozen Researcher contract + context boundary
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ResearcherContract:
    contract_version: str
    prompt_text: str
    context_boundary_allow: tuple
    context_boundary_forbid: tuple
    output_schema_version: str
    model_class_pin: str

    def frozen_hash(self) -> str:
        payload = json.dumps(
            {
                "prompt_text": self.prompt_text,
                "context_boundary_allow": list(self.context_boundary_allow),
                "context_boundary_forbid": list(self.context_boundary_forbid),
                "output_schema_version": self.output_schema_version,
                "model_class_pin": self.model_class_pin,
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        return sha256_hex(payload.encode("utf-8"))

    @classmethod
    def load(cls, path: Path) -> "ResearcherContract":
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        c = cls(
            contract_version=raw["contract_version"],
            prompt_text=raw["prompt_text"],
            context_boundary_allow=tuple(raw["context_boundary_allow"]),
            context_boundary_forbid=tuple(raw["context_boundary_forbid"]),
            output_schema_version=raw["output_schema_version"],
            model_class_pin=raw["model_class_pin"],
        )
        declared = raw.get("contract_hash")
        if declared and declared != c.frozen_hash():
            raise FailureIntakeError(
                f"Researcher contract drift: declared {declared} != computed {c.frozen_hash()}"
            )
        return c


_RESEARCHER_FORBIDDEN_TOKENS = (
    "holdout",
    "validation label",
    "golden",
    "expected winner",
    "promotion decision",
    "keep_candidate",
    "per-case hidden",
    "threshold change",
    "continue indefinitely",
    "loop forever",
)


def researcher_context_findings(context: dict) -> list[str]:
    """Reasons a would-be Researcher context violates the #415 boundary.

    The forbidden-token / secret scan targets ONLY the free-text, potentially
    externally-sourced regions -- `train_diagnostics`, `baseline_excerpt`, and
    the `failure_record` subdict. It deliberately does not scan
    `mutable_protected_manifest` / `required_hard_invariants`, which
    legitimately *name* protected surfaces such as the benchmark holdout and
    the eval-registry goldens (the Researcher must know what is off-limits)."""
    problems: list[str] = []
    scanned = json.dumps(
        {
            "train_diagnostics": context.get("train_diagnostics"),
            "baseline_excerpt": context.get("baseline_excerpt"),
            "failure_record": context.get("failure_record"),
            "instruction": context.get("instruction"),
        },
        ensure_ascii=False,
    )
    low = scanned.lower()
    for tok in _RESEARCHER_FORBIDDEN_TOKENS:
        if tok in low:
            problems.append(f"forbidden content in Researcher context: {tok!r}")
    for pat in _SECRET_RE:
        if pat.search(scanned):
            problems.append("secret-shaped content in Researcher context")
            break
    if "budget_remaining" not in context:
        problems.append("Researcher context must state budget_remaining")
    if context.get("mutable_protected_manifest") is None:
        problems.append("Researcher context must include the mutable/protected manifest")
    return problems


def build_researcher_context(
    *,
    failure_record: dict,
    manifest: dict,
    budget_remaining: int,
    train_diagnostics: Optional[list] = None,
    baseline_excerpt: str = "",
) -> dict:
    """Assembles ONLY the allowed inputs (#415 'Researcher context
    boundary')."""
    context = {
        "failure_record": {
            k: failure_record.get(k)
            for k in (
                "failure_id",
                "source_type",
                "reproduction_status",
                "reproduction_context_hash",
                "reproduction_model_hash",
                "expected_contract",
                "actual_failure_signal",
                "candidate_cause",
                "cause_target",
                "attribution_evidence",
                "attribution_status",
                "repair_eligibility",
                "limitations",
            )
        },
        "train_diagnostics": train_diagnostics or [],
        "mutable_protected_manifest": {
            "mutable_surfaces": manifest["mutable_surfaces"],
            "protected_surfaces": manifest["protected_surfaces"],
        },
        "baseline_excerpt": baseline_excerpt,
        "required_hard_invariants": [s["surface_id"] for s in manifest["protected_surfaces"]],
        "output_schema": "schemas/autoresearch_researcher_proposal.schema.json",
        "budget_remaining": budget_remaining,
        "instruction": "Propose at most ONE minimal, reversible, one-mechanism shadow patch, or decline.",
    }
    problems = researcher_context_findings(context)
    if problems:
        raise FailureIntakeError(f"refusing to build Researcher context: {problems}")
    return context


# ---------------------------------------------------------------------------
# Researcher model: protocol + fake + browser-backed
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RawResearcherCapture:
    response_text: str
    invocation_id: str
    response_hash: Optional[str]
    termination_status: str
    model: str


class ResearcherModel(Protocol):
    def propose(self, prompt_text: str, *, invocation_id: str) -> RawResearcherCapture: ...


class FakeResearcherModel:
    """Deterministic, no I/O. `scripted` is a JSON string proposal (or ''
    to simulate an empty/failed call). Test-only; never counts as live."""

    provenance = "calibration_fixture"

    def __init__(self, scripted: str, *, model: str = "fake-researcher") -> None:
        self._scripted = scripted
        self._model = model
        self.calls = 0

    def propose(self, prompt_text: str, *, invocation_id: str) -> RawResearcherCapture:
        self.calls += 1
        text = self._scripted
        return RawResearcherCapture(
            response_text=text,
            invocation_id=invocation_id,
            response_hash=sha256_hex(lba.normalize_response(text).encode()) if text.strip() else None,
            termination_status="completed" if text.strip() else "empty_response",
            model=self._model,
        )


class BrowserResearcherModel:
    """Routes the single Researcher call through the #413 transport
    (`lba.invoke`), sharing the batch `BudgetState`."""

    provenance = "live"

    def __init__(
        self,
        *,
        policy: "lba.TransportPolicy",
        budget: "lba.BudgetState",
        transport: "lba.BrowserSessionTransport",
        context_id: str,
        context_hash: str,
        authority_evidence_ref: str,
    ) -> None:
        self._policy = policy
        self._budget = budget
        self._transport = transport
        self._ctx_id = context_id
        self._ctx_hash = context_hash
        self._auth_ref = authority_evidence_ref

    def propose(self, prompt_text: str, *, invocation_id: str) -> RawResearcherCapture:
        req = lba.LiveInvocationRequest(
            invocation_id=invocation_id,
            experiment_id=invocation_id.split(":")[0],
            condition="baseline",
            case_id="researcher",
            context_id=self._ctx_id,
            context_hash=self._ctx_hash,
            payload_text=prompt_text,
            authority_evidence_ref=self._auth_ref,
            external_action_preview_ref=f"researcher-preview:{invocation_id}",
        )
        r = lba.invoke(req, self._policy, self._budget, self._transport)
        return RawResearcherCapture(
            response_text=r.response_text_or_ref or "",
            invocation_id=invocation_id,
            response_hash=r.response_hash,
            termination_status=r.termination_status,
            model=r.model,
        )


# ---------------------------------------------------------------------------
# Proposal parsing + one-mechanism / boundary validation
# ---------------------------------------------------------------------------

_REQUIRED_PROPOSAL_FIELDS = (
    "proposal_id",
    "failure_id",
    "attribution_status",
    "falsifiable_hypothesis",
    "candidate_cause",
    "alternative_causes_considered",
    "minimal_discriminating_test",
    "mutation_class",
    "target_file",
    "target_anchor",
    "patch_text_or_ref",
    "patch_hash",
    "one_causal_mechanism_statement",
    "expected_effect",
    "affected_eval_families",
    "possible_downside",
    "required_checks",
    "rollback",
    "confidence",
    "limitations",
)


def parse_researcher_proposal(text: str) -> Optional[dict]:
    if not text or not text.strip():
        return None
    candidate = text.strip()
    if not candidate.startswith("{"):
        m = re.search(r"\{.*\}", candidate, re.DOTALL)
        if not m:
            return None
        candidate = m.group(0)
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        return None
    if not isinstance(parsed, dict):
        return None
    return parsed


@dataclass
class ProposalOutcome:
    status: str  # "ready_for_experiment" | "rejected"
    proposal: Optional[dict]
    findings: list
    researcher_invocation_id: Optional[str] = None
    researcher_provenance: str = "unknown"
    limitations: str = "none material"


def _proposal_schema_findings(proposal: dict, schema: dict) -> list[str]:
    import jsonschema

    return [f"schema: {e.message}" for e in jsonschema.Draft7Validator(schema).iter_errors(proposal)]


def deterministic_preflight(
    *,
    proposal: dict,
    manifest: dict,
    repo_root: Path,
    baseline_revision: str,
    proposal_schema: dict,
) -> ProposalOutcome:
    """Proves the #415 preflight bullets. Does NOT decide the candidate is
    good. Reuses the v0.1 shadow runner's patch-scope / worktree / fingerprint
    machinery unchanged."""
    findings: list[str] = []
    findings.extend(_proposal_schema_findings(proposal, proposal_schema))

    if proposal.get("attribution_status") == "rejected":
        findings.append("rejected attribution is ineligible for an instruction/routing mutation")
    if proposal.get("attribution_status") == "uncertain" and not proposal.get("discriminating_experiment_only"):
        findings.append("uncertain attribution permits only a labelled bounded discriminating experiment")
    if proposal.get("mutation_class") not in MUTATION_CLASSES:
        findings.append(f"mutation_class not in allowlist: {proposal.get('mutation_class')!r}")

    patch_text = proposal.get("patch_text_or_ref", "")
    declared_hash = proposal.get("patch_hash", "")
    if not patch_text or sha256_hex(patch_text.encode("utf-8")) != declared_hash:
        findings.append("patch_hash does not match patch_text")

    for field_name in ("rollback", "required_checks", "possible_downside"):
        if not proposal.get(field_name):
            findings.append(f"missing mandatory field: {field_name}")
    if not proposal.get("affected_eval_families"):
        findings.append("required regression families not declared")

    # real-diff scope check in an isolated worktree at the baseline revision
    if not findings:
        import tempfile

        work = Path(tempfile.mkdtemp(prefix="autoresearch-preflight-"))
        shadow = None
        try:
            fp = asr.verify_patch_fingerprint(patch_text, declared_hash)
            if fp:
                findings.extend(f.evidence for f in fp)
            shadow = asr.create_shadow_worktree(repo_root, baseline_revision, work)
            ok, touched, err = asr.dry_run_patch_paths(shadow, patch_text)
            if not ok:
                findings.append(f"patch does not apply at baseline revision: {err}")
            else:
                if len(touched) != 1:
                    findings.append(f"patch touches {len(touched)} files; exactly one required: {touched}")
                scope = asr.reject_patch_scope(
                    shadow, touched, _surface_id_for_target(manifest, proposal), manifest, patch_text
                )
                findings.extend(f"{f.rule}: {f.evidence}" for f in scope)
        except asr.ShadowRunnerError as exc:
            findings.append(f"preflight worktree error: {exc}")
        finally:
            if shadow is not None:
                asr.remove_shadow_worktree(repo_root, shadow)
            import shutil

            shutil.rmtree(work, ignore_errors=True)

    status = "rejected" if findings else "ready_for_experiment"
    return ProposalOutcome(
        status=status,
        proposal=None if findings else proposal,
        findings=findings,
        limitations="; ".join(findings) if findings else "none material",
    )


def _surface_id_for_target(manifest: dict, proposal: dict) -> str:
    tgt = proposal.get("target_file", "")
    for s in manifest["mutable_surfaces"]:
        if s["path"] and s["path"] in tgt:
            return s["surface_id"]
    return proposal.get("target_file", "UNKNOWN")


def run_researcher(
    *,
    failure_record: dict,
    context: dict,
    contract: ResearcherContract,
    model: ResearcherModel,
    manifest: dict,
    repo_root: Path,
    baseline_revision: str,
    proposal_schema: dict,
    experiment_id: str,
    retry_limit: int = 1,
) -> ProposalOutcome:
    """One bounded live Researcher invocation (+ one allowed retry) -> a
    schema-valid, one-mechanism proposal -> deterministic preflight. Fails
    closed on `rejected`/`ineligible` attribution and on repeated invalid
    output."""
    if failure_record.get("attribution_status") == "rejected":
        return ProposalOutcome(
            status="rejected", proposal=None,
            findings=["attribution rejected: no mutation proposal permitted"],
            limitations="attribution rejected",
        )
    elig = failure_record.get("repair_eligibility")
    if elig == "ineligible":
        return ProposalOutcome(
            status="rejected", proposal=None,
            findings=["repair_eligibility ineligible"], limitations="ineligible",
        )

    prompt = f"{contract.prompt_text}\n\nCONTEXT:\n{json.dumps(context, ensure_ascii=False, indent=2)}"
    proposal: Optional[dict] = None
    inv_id = None
    attempts = 0
    notes: list[str] = []
    while proposal is None and attempts <= retry_limit:
        inv_id = f"{experiment_id}:researcher:{attempts}"
        cap = model.propose(prompt, invocation_id=inv_id)
        if cap.termination_status != "completed":
            attempts += 1
            notes.append(f"attempt {attempts}: {cap.termination_status}")
            continue
        parsed = parse_researcher_proposal(cap.response_text)
        if parsed is None or any(f not in parsed for f in _REQUIRED_PROPOSAL_FIELDS):
            attempts += 1
            notes.append(f"attempt {attempts}: incomplete/invalid proposal")
            continue
        parsed.setdefault("researcher_invocation_id", inv_id)
        if elig == "discriminating_experiment_only":
            parsed["discriminating_experiment_only"] = True
        proposal = parsed

    if proposal is None:
        return ProposalOutcome(
            status="rejected", proposal=None,
            findings=["no schema-valid one-mechanism proposal within bounded retry"],
            researcher_invocation_id=inv_id,
            researcher_provenance=getattr(model, "provenance", "unknown"),
            limitations="Researcher failure: " + " | ".join(notes),
        )

    outcome = deterministic_preflight(
        proposal=proposal,
        manifest=manifest,
        repo_root=repo_root,
        baseline_revision=baseline_revision,
        proposal_schema=proposal_schema,
    )
    outcome.researcher_invocation_id = inv_id
    outcome.researcher_provenance = getattr(model, "provenance", "unknown")
    return outcome
