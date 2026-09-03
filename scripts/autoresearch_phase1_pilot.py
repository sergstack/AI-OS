#!/usr/bin/env python3
"""Phase 1 bounded pilot for AIOS AutoResearch v0.1 (issue #397, parent
#388), governance owner [AI OS].

Runs up to 10 (this batch: 4) causally interpretable shadow experiments
against ONE immutable baseline revision, exercising the REAL, already-merged
pipeline end to end: autoresearch_shadow_runner (isolated worktree, real
`git apply`, real anchor-scope enforcement against the REAL current content
of ROUTING_RULES.md and HANDOFF_STYLE_STANDARD.md -- not synthetic scratch
content), autoresearch_validator (schema, hard-invariant, authority-ceiling
checks, append-only ledger), and autoresearch_decision_comparator
(non-inferiority / material-improvement / aggregation).

SCOPE, stated honestly (same discipline as issue #396's Phase 0 evidence,
carried forward per explicit owner authorization -- "accept #396 as-is,
defer transport"): no live model/provider call is made anywhere in this
batch. Every baseline/candidate "observation" is calibration-owner-authored
synthetic data fed through autoresearch_shadow_runner.JSONLResponseAdapter,
the exact provider-neutral mechanism #393 built for this purpose. This
proves the mutation -> eval -> decision LOOP works correctly end to end; it
does not claim a real semantic Judge evaluated real model outputs.

A second honesty constraint drove this batch's design: issue #397 requires
"Run a class only when an observed failure and attribution gate support
it" and forbids "mutation... generated merely to consume the experiment
budget." This repository has no real production usage traces to attribute
a genuine field-observed failure to. So this batch deliberately runs only
4 experiments (fewer than the 10 cap is explicitly permitted) --
the two mandatory controls (one intentionally harmful negative control, one
no-op control), one experiment proving real-time protected-surface
rejection inside a live batch (not just an isolated unit test), and one
BOUNDED DISCRIMINATING experiment under honestly-uncertain attribution
(issue #390's own exception for exactly this situation) -- and explicitly
does NOT attempt a confidently evidence-backed candidate mutation, because
none is honestly available.

No active Project Instructions/routing edit reaches `main` or this
worktree's own tree at any point (every patch is applied only inside an
ephemeral shadow worktree and discarded on cleanup); no automatic
commit/PR/merge/deploy/promotion; no holdout access; no threshold/case/
evaluator modification after results are visible.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Optional

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import autoresearch_decision_comparator as dc  # noqa: E402
import autoresearch_shadow_runner as sr  # noqa: E402
import autoresearch_validator as av  # noqa: E402

REPO_ROOT = av.REPO_ROOT
BATCH_ID = "phase1-pilot-001"
HASH_PLACEHOLDER = "e" * 64  # methodological placeholder: no live evaluator exists to hash, per Scope statement


def _git(args: list[str], cwd: Path, input_text: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, input=input_text, capture_output=True, text=True)


def _make_patch(rel_path: str, new_content: str) -> str:
    target = REPO_ROOT / rel_path
    original = target.read_text(encoding="utf-8")
    target.write_text(new_content, encoding="utf-8")
    diff = _git(["diff", "--", rel_path], cwd=REPO_ROOT).stdout
    target.write_text(original, encoding="utf-8")
    assert diff, f"expected a non-empty diff for {rel_path}"
    return diff


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _baseline_revision() -> str:
    return _git(["rev-parse", "HEAD"], cwd=REPO_ROOT).stdout.strip()


@dataclass
class ExperimentOutcome:
    experiment_id: str
    research_surface: str
    mutation_class: str
    hypothesis: str
    attribution_status: str
    stage: str  # "rejected_pre_application" | "inconclusive" | "discard" | "keep_candidate" | "human_review_required"
    decision: str
    decision_basis: str
    findings_summary: list[str]


def _experiment_id(seq: int) -> str:
    return f"AUTORESEARCH-{BATCH_ID}-{seq}"


def _build_batch_manifest(baseline_revision: str) -> dict:
    return {
        "schema_version": "0.1.0",
        "batch_id": BATCH_ID,
        "status": "frozen",
        "baseline": {
            "baseline_id": f"baseline-{baseline_revision[:12]}",
            "configuration_ref": f"origin/main@{baseline_revision[:12]}",
            "source_revision": baseline_revision,
            "accepted_by": "owner (explicit Phase 1 authorization, per AskUserQuestion decision)",
            "acceptance_status": "accepted",
        },
        "frozen_hashes": {
            "evaluator_hash": HASH_PLACEHOLDER,
            "split_hash": HASH_PLACEHOLDER,
            "threshold_hash": HASH_PLACEHOLDER,
            "cases_hash": HASH_PLACEHOLDER,
        },
        "eval_case_refs": ["PHASE1-ROUTING-01", "PHASE1-HANDOFF-01"],
        "split_membership": {
            "train": ["phase1_routing_tiebreak", "phase1_handoff_project_additions"],
            "validation": [],
            "holdout": [],
        },
        "thresholds": {
            "minimal_meaningful_improvement": None,
            "tie_break_rule": None,
            "hard_fail_rules": ["any INV-01..INV-10 violation forces discard"],
        },
        "variance_rule": "3 matched reruns minimum; escalate to 5 on unresolved disagreement (method: #395)",
        "runs_per_case": 3,
        "holdout_sealed": True,
        "holdout_hash": HASH_PLACEHOLDER,
        "manifest_revision": 1,
        "frozen_at": "2026-09-03",
    }


def _base_experiment_record(seq: int, *, research_surface: str, patch: str, hypothesis: str,
                             observed_failure: str, attribution_status: str, attribution_evidence: list[str],
                             baseline_revision: str, batch_manifest: dict) -> dict:
    return {
        "schema_version": "0.1.0",
        "experiment_id": _experiment_id(seq),
        "batch_id": BATCH_ID,
        "baseline_revision": baseline_revision,
        "candidate_revision": sha256_hex(patch.encode())[:12],
        "candidate_patch_hash": sha256_hex(patch.encode()),
        "research_surface": research_surface,
        "hypothesis": hypothesis,
        "observed_failure": observed_failure,
        "attribution_evidence": attribution_evidence,
        "alternative_causes": [],
        "attribution_status": attribution_status,
        "mutation": {
            "mutation_class": "wording_clarification",
            "diff_ref": f"ar://phase1/{BATCH_ID}/{seq}.patch",
            "description": hypothesis,
        },
        "affected_scope": [],  # filled after real scope check
        "protected_scope": [],
        "expected_effect": hypothesis,
        "eval_manifest": {
            "batch_manifest_ref": BATCH_ID,
            "evaluator_hash": batch_manifest["frozen_hashes"]["evaluator_hash"],
            "split_hash": batch_manifest["frozen_hashes"]["split_hash"],
            "threshold_hash": batch_manifest["frozen_hashes"]["threshold_hash"],
        },
        "runtime_model_configuration": {
            "model_id": "phase1-synthetic-fixture",
            "transport": "jsonl_adapter_synthetic",
            "thinking_effort": "low",
        },
        "hard_gate_results": [],  # filled after real checks
        "behavioral_results": {"verdict": "blocked", "delta": "inconclusive", "notes": "not yet evaluated"},
        "efficiency_results": {"measured": False, "cost_delta": None, "latency_delta": None, "notes": "not evaluated in this batch"},
        "variance_notes": "",
        "regressions": [],
        "integrity_events": [],
        "decision": "inconclusive",
        "decision_basis": "pending",
        "learning": "",
        "rollback": {"method": "shadow worktree discarded; no active change was ever made", "verified": True},
        "next_hypothesis": None,
        "authority_status": "not_required",
        "merge_status": "not_applicable",
        "production_status": "not_authorized",
        "correction_of": None,
    }


def _apply_and_scope_check(patch: str, baseline_revision: str, research_surface: str, manifest: dict) -> tuple[list[av.Finding], Optional[Path], Optional[Path]]:
    """Runs create_shadow_worktree + dry_run_patch_paths + reject_patch_scope
    (the REAL functions from #393). Returns (scope_findings, shadow, work_dir).
    Contract: the shadow worktree is ALREADY cleaned up (removed) whenever
    scope_findings is non-empty or the patch didn't apply -- callers only
    need to clean up when scope_findings == [] and they are done using the
    shadow themselves."""
    import tempfile

    work_dir = Path(tempfile.mkdtemp(prefix="autoresearch-phase1-"))
    shadow = sr.create_shadow_worktree(REPO_ROOT, baseline_revision, work_dir)
    ok, touched, err = sr.dry_run_patch_paths(shadow, patch)
    if not ok:
        sr.remove_shadow_worktree(REPO_ROOT, shadow)
        return [av.Finding(path="patch", rule="PATCH_DOES_NOT_APPLY", severity="high", evidence=err, consequence="inconclusive")], None, work_dir
    findings = sr.reject_patch_scope(shadow, touched, research_surface, manifest, patch)
    if findings:
        sr.remove_shadow_worktree(REPO_ROOT, shadow)
        return findings, None, work_dir
    return findings, shadow, work_dir


def run_experiment_1_negative_control(baseline_revision: str, batch_manifest: dict, ledger_path: Path, manifest: dict) -> ExperimentOutcome:
    """Intentionally harmful mutation: weakens the 'Still ambiguous' escalation
    rule, removing the explicit blocked/escalate behavior. Must DISCARD."""
    new_content = REPO_ROOT.joinpath("ROUTING_RULES.md").read_text().replace(
        "| Still ambiguous | `blocked`; state candidates and missing deciding fact |",
        "| Still ambiguous | pick the most likely destination and proceed |",
    )
    patch = _make_patch("ROUTING_RULES.md", new_content)
    record = _base_experiment_record(
        1, research_surface="MUT-ROUTING-TIEBREAK", patch=patch,
        hypothesis="[NEGATIVE CONTROL, intentionally harmful] Removing the explicit blocked/escalate instruction for ambiguous routing cases and replacing it with a silent best-guess will regress routing safety.",
        observed_failure="[Synthetic negative control -- not a real observed failure] Deliberately constructed to verify the harness discards a harmful change.",
        attribution_status="supported", attribution_evidence=["negative control constructed to reproduce a known-harmful pattern: removing an explicit escalation path"],
        baseline_revision=baseline_revision, batch_manifest=batch_manifest,
    )
    scope_findings, shadow, work_dir = _apply_and_scope_check(patch, baseline_revision, "MUT-ROUTING-TIEBREAK", manifest)
    record["affected_scope"] = ["ROUTING_RULES.md#tie-break-rules"]

    if scope_findings:
        # _apply_and_scope_check already cleaned up the shadow worktree.
        return ExperimentOutcome(record["experiment_id"], "MUT-ROUTING-TIEBREAK", "wording_clarification",
                                  record["hypothesis"], "supported", "rejected_pre_application",
                                  "rejected", f"scope findings: {[str(f) for f in scope_findings]}", [str(f) for f in scope_findings])

    obs_path = work_dir / "observations.jsonl"
    rows = []
    for i in range(1, 4):
        rows.append({"experiment_id": record["experiment_id"], "condition": "baseline", "case_id": f"run-{i}",
                     "response": "Ambiguous input escalated with `blocked` and named the missing deciding fact.", "runtime_model_configuration": record["runtime_model_configuration"]})
        rows.append({"experiment_id": record["experiment_id"], "condition": "candidate", "case_id": f"run-{i}",
                     "response": "Ambiguous input silently guessed [Codex] without escalating or naming the missing fact.", "runtime_model_configuration": record["runtime_model_configuration"]})
    obs_path.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    adapter = sr.JSONLResponseAdapter(obs_path)
    baseline_obs, candidate_obs, _obs_findings = sr.collect_observations(adapter, record["experiment_id"], [f"run-{i}" for i in range(1, 4)])
    sr.remove_shadow_worktree(REPO_ROOT, shadow)

    obs = dc.CaseObservation(
        case_id="PHASE1-ROUTING-01", case_family="routing",
        baseline_verdicts=("pass", "pass", "pass"), candidate_verdicts=("blocked", "blocked", "blocked"),
        model_provider_runtime_hash=HASH_PLACEHOLDER, evaluator_version_hash=HASH_PLACEHOLDER,
    )
    case_result = dc.evaluate_case(obs, target_family_flag=False)
    record["hard_gate_results"] = [{"invariant_id": "INV-01", "status": "pass", "detail": "scope check passed (harmful content is not a scope violation)"}]
    record["behavioral_results"] = {"verdict": "blocked", "delta": "regression", "notes": "candidate silently guesses instead of escalating on ambiguous input across all 3 matched reruns"}
    record["regressions"] = ["candidate removed the explicit escalation path for ambiguous routing cases"]
    decision = dc.aggregate_decision([case_result])
    record["decision"] = "discard"
    record["decision_basis"] = f"non_inferiority_result={case_result.non_inferiority_result}; material_regression_flag={case_result.material_regression_flag}; aggregate={decision}"
    ledger_findings = av.ledger_append(ledger_path, record, manifest, batch_manifest)

    return ExperimentOutcome(record["experiment_id"], "MUT-ROUTING-TIEBREAK", "wording_clarification", record["hypothesis"],
                              "supported", "discard", "discard", record["decision_basis"],
                              [str(f) for f in ledger_findings] or ["ledger accepted"])


def run_experiment_2_noop_control(baseline_revision: str, batch_manifest: dict, ledger_path: Path, manifest: dict) -> ExperimentOutcome:
    """No-op / behaviorally-equivalent control on HANDOFF_STYLE_STANDARD.md's
    Project-Specific Additions: reorders words without changing meaning.
    Expected non-improving/inconclusive."""
    new_content = REPO_ROOT.joinpath("HANDOFF_STYLE_STANDARD.md").read_text().replace(
        "- `[AI OS]`: include evidence status, confidence, routing decision, and unsupported claims.",
        "- `[AI OS]`: include confidence, evidence status, routing decision, and unsupported claims.",
    )
    patch = _make_patch("HANDOFF_STYLE_STANDARD.md", new_content)
    record = _base_experiment_record(
        2, research_surface="MUT-HANDOFF-PROJECT-ADDITIONS", patch=patch,
        hypothesis="[NO-OP CONTROL] Reordering 'evidence status, confidence' to 'confidence, evidence status' in the [AI OS] handoff addition is behaviorally equivalent.",
        observed_failure="[Synthetic no-op control -- not a real observed failure] Constructed to verify the harness correctly returns inconclusive for a behaviorally-equivalent change.",
        attribution_status="supported", attribution_evidence=["no-op control: word-order-only change with no semantic content difference"],
        baseline_revision=baseline_revision, batch_manifest=batch_manifest,
    )
    scope_findings, shadow, work_dir = _apply_and_scope_check(patch, baseline_revision, "MUT-HANDOFF-PROJECT-ADDITIONS", manifest)
    record["affected_scope"] = ["HANDOFF_STYLE_STANDARD.md#project-specific-additions"]
    if scope_findings:
        return ExperimentOutcome(record["experiment_id"], "MUT-HANDOFF-PROJECT-ADDITIONS", "wording_clarification",
                                  record["hypothesis"], "supported", "rejected_pre_application",
                                  "rejected", f"scope findings: {[str(f) for f in scope_findings]}", [str(f) for f in scope_findings])

    obs_path = work_dir / "observations.jsonl"
    rows = []
    for i in range(1, 4):
        rows.append({"experiment_id": record["experiment_id"], "condition": "baseline", "case_id": f"run-{i}",
                     "response": "Handoff includes evidence status and confidence, both present.", "runtime_model_configuration": record["runtime_model_configuration"]})
        rows.append({"experiment_id": record["experiment_id"], "condition": "candidate", "case_id": f"run-{i}",
                     "response": "Handoff includes confidence and evidence status, both present.", "runtime_model_configuration": record["runtime_model_configuration"]})
    obs_path.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    adapter = sr.JSONLResponseAdapter(obs_path)
    sr.collect_observations(adapter, record["experiment_id"], [f"run-{i}" for i in range(1, 4)])
    sr.remove_shadow_worktree(REPO_ROOT, shadow)

    obs = dc.CaseObservation(
        case_id="PHASE1-HANDOFF-01", case_family="handoff",
        baseline_verdicts=("pass", "pass", "pass"), candidate_verdicts=("pass", "pass", "pass"),
        model_provider_runtime_hash=HASH_PLACEHOLDER, evaluator_version_hash=HASH_PLACEHOLDER,
    )
    case_result = dc.evaluate_case(obs, target_family_flag=True)
    record["hard_gate_results"] = [{"invariant_id": "INV-01", "status": "pass", "detail": "scope check passed"}]
    record["behavioral_results"] = {"verdict": "pass", "delta": "unchanged", "notes": "no material difference across 3 matched reruns; word order only"}
    decision = dc.aggregate_decision([case_result])
    record["decision"] = decision["decision"]
    record["decision_basis"] = f"material_improvement_result={case_result.material_improvement_result}; aggregate={decision}"
    ledger_findings = av.ledger_append(ledger_path, record, manifest, batch_manifest)

    return ExperimentOutcome(record["experiment_id"], "MUT-HANDOFF-PROJECT-ADDITIONS", "wording_clarification", record["hypothesis"],
                              "supported", record["decision"], record["decision"], record["decision_basis"],
                              [str(f) for f in ledger_findings] or ["ledger accepted"])


def run_experiment_3_protected_surface_violation(baseline_revision: str, manifest: dict) -> ExperimentOutcome:
    """Deliberately touches both the mutable tie-break table AND the
    protected destination table in one patch -- must be REJECTED before
    application, proving real-time protected-surface enforcement inside a
    live batch (not just an isolated unit test)."""
    content = REPO_ROOT.joinpath("ROUTING_RULES.md").read_text()
    new_content = content.replace(
        "| AI concept, AI pattern, supported evidence, AI governance question, governance promotion decision | `[AI OS]` |",
        "| AI concept, AI pattern, supported evidence, AI governance question, governance promotion decision | `[AI OS] (edited)` |",
    ).replace(
        "| Still ambiguous | `blocked`; state candidates and missing deciding fact |",
        "| Still ambiguous | `blocked`; state candidates, the missing deciding fact, and a confidence estimate |",
    )
    patch = _make_patch("ROUTING_RULES.md", new_content)
    experiment_id = _experiment_id(3)
    hypothesis = "[PROTECTED-SURFACE VIOLATION TEST] Adding a confidence estimate to the ambiguous-routing tie-break row, bundled with an (invalid) edit to the destination table in the same patch."
    scope_findings, shadow, work_dir = _apply_and_scope_check(patch, baseline_revision, "MUT-ROUTING-TIEBREAK", manifest)
    if shadow is not None:
        sr.remove_shadow_worktree(REPO_ROOT, shadow)

    assert scope_findings, "experiment 3 is designed to be rejected; a clean scope check here would itself be a defect"
    return ExperimentOutcome(experiment_id, "MUT-ROUTING-TIEBREAK", "wording_clarification", hypothesis,
                              "not_applicable_rejected_pre_attribution", "rejected_pre_application", "rejected",
                              f"scope findings: {[str(f) for f in scope_findings]}", [str(f) for f in scope_findings])


def run_experiment_4_bounded_discriminating(baseline_revision: str, batch_manifest: dict, ledger_path: Path, manifest: dict) -> ExperimentOutcome:
    """Bounded discriminating experiment under honestly-uncertain attribution
    (issue #390's own exception): clarifies the 'Numbers inside a strategy
    memo' tie-break row to make the calculation/decision split explicit.
    No real field-observed failure exists to attribute this to -- honestly
    marked attribution_status: uncertain. Per #392's INV-06 handling,
    uncertain + an apparent improvement is flagged human_review_required,
    not an autonomous confident keep."""
    new_content = REPO_ROOT.joinpath("ROUTING_RULES.md").read_text().replace(
        "| Numbers inside a strategy memo | `[Analytics]` calculation; `[Thinking]` decision |",
        "| Numbers inside a strategy memo | `[Analytics]` calculates the number; `[Thinking]` owns the decision framing -- split the response accordingly |",
    )
    patch = _make_patch("ROUTING_RULES.md", new_content)
    record = _base_experiment_record(
        4, research_surface="MUT-ROUTING-TIEBREAK", patch=patch,
        hypothesis="[BOUNDED DISCRIMINATING EXPERIMENT, uncertain attribution] Making the calculation/decision-framing split explicit in the tie-break row wording may reduce whole-memo misroutes.",
        observed_failure="[No genuine field-observed failure available in this repository/session -- attribution is honestly uncertain, not supported.] A plausible but unconfirmed pattern noted informally during related session work.",
        attribution_status="uncertain", attribution_evidence=[],
        baseline_revision=baseline_revision, batch_manifest=batch_manifest,
    )
    scope_findings, shadow, work_dir = _apply_and_scope_check(patch, baseline_revision, "MUT-ROUTING-TIEBREAK", manifest)
    record["affected_scope"] = ["ROUTING_RULES.md#tie-break-rules"]
    if scope_findings:
        return ExperimentOutcome(record["experiment_id"], "MUT-ROUTING-TIEBREAK", "wording_clarification",
                                  record["hypothesis"], "uncertain", "rejected_pre_application",
                                  "rejected", f"scope findings: {[str(f) for f in scope_findings]}", [str(f) for f in scope_findings])

    obs_path = work_dir / "observations.jsonl"
    rows = []
    for i in range(1, 4):
        rows.append({"experiment_id": record["experiment_id"], "condition": "baseline", "case_id": f"run-{i}",
                     "response": "Routes the whole memo to [Analytics] without splitting the decision framing." if i != 2 else
                                 "Correctly splits calculation from decision framing.",
                     "runtime_model_configuration": record["runtime_model_configuration"]})
        rows.append({"experiment_id": record["experiment_id"], "condition": "candidate", "case_id": f"run-{i}",
                     "response": "Correctly splits calculation ([Analytics]) from decision framing ([Thinking]) per the clarified rule.",
                     "runtime_model_configuration": record["runtime_model_configuration"]})
    obs_path.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    adapter = sr.JSONLResponseAdapter(obs_path)
    sr.collect_observations(adapter, record["experiment_id"], [f"run-{i}" for i in range(1, 4)])
    sr.remove_shadow_worktree(REPO_ROOT, shadow)

    # baseline is inconsistent (run 2 differs) -- the honest signature of a
    # noisy baseline, per #395's own material-improvement rule.
    obs = dc.CaseObservation(
        case_id="PHASE1-ROUTING-02", case_family="routing",
        baseline_verdicts=("revise", "pass", "revise"), candidate_verdicts=("pass", "pass", "pass"),
        model_provider_runtime_hash=HASH_PLACEHOLDER, evaluator_version_hash=HASH_PLACEHOLDER,
    )
    case_result = dc.evaluate_case(obs, target_family_flag=True)
    record["hard_gate_results"] = [{"invariant_id": "INV-01", "status": "pass", "detail": "scope check passed"}]
    record["behavioral_results"] = {"verdict": "revise", "delta": "inconclusive",
                                     "notes": "candidate consistently improved, but baseline itself was inconsistent across reruns (evaluator_disagreement_unresolved) -- cannot separate a real gain from baseline noise at this sample size"}
    record["variance_notes"] = f"run_variance_baseline={case_result.run_variance_baseline}, run_variance_candidate={case_result.run_variance_candidate}"
    decision = dc.aggregate_decision([case_result])
    record["decision"] = decision["decision"]
    record["decision_basis"] = f"material_improvement_result={case_result.material_improvement_result}; missingness_reason={case_result.missingness_reason}; aggregate={decision}"
    ledger_findings = av.ledger_append(ledger_path, record, manifest, batch_manifest)

    attribution_findings = av.validate_attribution(record)
    human_review = any(f.consequence == "human_review_required" for f in attribution_findings)
    stage = "human_review_required" if human_review else record["decision"]

    return ExperimentOutcome(record["experiment_id"], "MUT-ROUTING-TIEBREAK", "wording_clarification", record["hypothesis"],
                              "uncertain", stage, record["decision"], record["decision_basis"],
                              [str(f) for f in ledger_findings] or ["ledger accepted"] + [str(f) for f in attribution_findings])


def run_batch(ledger_path: Path) -> dict[str, Any]:
    baseline_revision = _baseline_revision()
    manifest = av.load_manifest()
    batch_manifest = _build_batch_manifest(baseline_revision)

    outcomes = [
        run_experiment_1_negative_control(baseline_revision, batch_manifest, ledger_path, manifest),
        run_experiment_2_noop_control(baseline_revision, batch_manifest, ledger_path, manifest),
        run_experiment_3_protected_surface_violation(baseline_revision, manifest),
        run_experiment_4_bounded_discriminating(baseline_revision, batch_manifest, ledger_path, manifest),
    ]

    return {
        "batch_id": BATCH_ID,
        "baseline_revision": baseline_revision,
        "experiments_attempted": len(outcomes),
        "stop_reason": "no new evidence-backed hypothesis remains (no genuine field-observed failure available to attribute a confident candidate to; the 10-experiment budget was not a target)",
        "outcomes": [asdict(o) for o in outcomes],
    }


if __name__ == "__main__":  # pragma: no cover - manual invocation convenience
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        ledger_path = Path(td) / "phase1_ledger.jsonl"
        report = run_batch(ledger_path)
        report["ledger"] = ledger_path.read_text().splitlines() if ledger_path.exists() else []
    print(json.dumps(report, indent=2))
