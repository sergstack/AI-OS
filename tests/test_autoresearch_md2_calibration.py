"""Deterministic four-control calibration for the issue #435 MD-2 directional
observation contract (2026-09-05): known beneficial / known harmful /
semantic no-op / mixed candidates, exercised through the REAL
Controller.run_experiment -> lj.run_blind_ab -> adc.evaluate_case ->
adc.aggregate_decision wiring (not isolated fixtures). Only the transport
and Judge are fakes (deterministic, no I/O); every hard gate, blinding
mechanism, and comparator function is the real, unmodified code.

This is calibration, not a live pilot: no real model/browser call anywhere.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


cli = _load("autoresearch_cli")
lba = _load("autoresearch_live_browser_adapter")
lj = _load("autoresearch_live_judge")

REV = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()


def _tiebreak_patch() -> tuple[str, str]:
    target = REPO_ROOT / "ROUTING_RULES.md"
    original = target.read_text(encoding="utf-8")
    replace, with_ = "a prompt or workflow deliverable", "a prompt/workflow deliverable"
    assert replace in original
    target.write_text(original.replace(replace, with_), encoding="utf-8")
    try:
        diff = subprocess.run(["git", "diff", "--", "ROUTING_RULES.md"], cwd=REPO_ROOT,
                              capture_output=True, text=True).stdout
    finally:
        target.write_text(original, encoding="utf-8")
    assert diff
    return diff, cli.av.sha256_hex(diff.encode("utf-8"))


def _batch_config(**ov) -> dict:
    base = {
        "contract_version": "0.2.0",
        "transport_id": "playwright_mcp",
        "transport_version": "test",
        "context_manifest_hash": "a" * 64,
        "authority_status": "authorized",
        "authority_evidence_ref": "docs/evidence/AUTORESEARCH_MD2_DECISION_PACKAGE_2026-09-05.md#calibration",
        "call_timeout_seconds": 180,
        "retry_limit": 1,
        "target_url_prefix": "https://chatgpt.com/",
        "target_product": "openai_chatgpt_ui",
        "session_policy": "fresh_conversation",
        "subject_context_scope": "non_project_controlled",
        "memory_personalization_isolation_status": "verified_disabled",
    }
    base.update(ov)
    return base


def _authorized_budget() -> "cli.RoleBudget":
    return cli.RoleBudget(max_provider_calls=40, max_cost_amount=0.0, max_cost_currency="USD")


def _spec(patch_text: str, patch_hash: str, cases: list, experiment_id: str) -> "cli.ManualCandidateSpec":
    return cli.ManualCandidateSpec(
        experiment_id=experiment_id, baseline_revision=REV, project="ai_os",
        research_surface="MUT-ROUTING-TIEBREAK", target_file="ROUTING_RULES.md",
        patch_text=patch_text, candidate_patch_hash=patch_hash, cases=cases, run_count=3,
    )


def _case(case_id: str, target_family_flag: bool = True) -> dict:
    return {
        "case_id": case_id, "case_family": "routing", "target_family_flag": target_family_flag,
        "input": "A user asks to prepare a coding task whose deliverable is a workflow. Which owner?",
    }


def _make_ground_truth_judge(cases_directions: dict, seed: int = 0):
    """cases_directions: case_id -> (baseline_verdict, candidate_verdict).

    A calibration fixture legitimately encodes ground truth the way no real
    Judge implementation could (a real Judge never learns which side is
    baseline/candidate) -- it independently computes, for each presentation
    order, the SAME primary_assignment/reversed_assignment the real pipeline
    computes, and emits POSITIONAL findings ("subject": "A"/"B") that
    de-blind to the desired (baseline_verdict, candidate_verdict) pair
    consistently across both orders. This proves the full de-blinding path
    end-to-end without needing a real model to actually produce the
    judgment."""

    class _GroundTruthJudge:
        independence_level = "limited_same_model_class"

        def evaluate(self, prompt_text, *, invocation_id: str) -> "lj.RawJudgeCapture":
            suffix = ":rev" if invocation_id.endswith(":rev") else ""
            body = invocation_id[: -len(":rev")] if suffix else invocation_id
            exp_part, case_id, _attempts = body.rsplit(":", 2)
            baseline_v, candidate_v = cases_directions[case_id]
            assignment = (
                lj.reversed_assignment(lj.primary_assignment(exp_part, seed))
                if suffix else lj.primary_assignment(exp_part, seed)
            )
            findings = []
            if baseline_v != "pass":
                subj = "A" if assignment.a_is == "baseline" else "B"
                findings.append({
                    "case_family": "routing",
                    "finding": "baseline-side defect (calibration ground truth)", "evidence": "calibration fixture",
                    "severity": "high", "affected_invariant_or_metric": "routing_correctness",
                    "subject": subj, "verdict": baseline_v, "confidence": "high", "limitations": "none material",
                })
            if candidate_v != "pass":
                subj = "A" if assignment.a_is == "candidate" else "B"
                findings.append({
                    "case_family": "routing",
                    "finding": "candidate-side defect (calibration ground truth)", "evidence": "calibration fixture",
                    "severity": "high", "affected_invariant_or_metric": "routing_correctness",
                    "subject": subj, "verdict": candidate_v, "confidence": "high", "limitations": "none material",
                })
            if not findings:
                findings.append({
                    "case_family": "routing",
                    "finding": "no material difference (calibration ground truth)", "evidence": "calibration fixture",
                    "severity": "low", "affected_invariant_or_metric": "routing_correctness",
                    "subject": "both", "verdict": "pass", "confidence": "high", "limitations": "none material",
                })
            text = json.dumps(findings)
            return lj.RawJudgeCapture(
                response_text=text, invocation_id=invocation_id,
                response_hash=lba.sha256_hex(lba.normalize_response(text).encode("utf-8")),
                termination_status="completed", model_identity_status="not_observable", model="calibration-ground-truth",
            )

    return _GroundTruthJudge()


def _controller(cases_directions: dict) -> "cli.Controller":
    transport = lba.FakeBrowserTransport(
        scripted_response="OK: route to [LLM] for the workflow deliverable.",
        page_url="https://chatgpt.com/c/fake",
    )
    return cli.Controller(transport=transport, judge_model=_make_ground_truth_judge(cases_directions))


# ---------------------------------------------------------------------------
# Control 1: known beneficial candidate -> improvement signal
# ---------------------------------------------------------------------------


def test_control_beneficial_candidate_yields_candidate_for_owner_review(tmp_path):
    patch, h = _tiebreak_patch()
    spec = _spec(patch, h, cases=[_case("beneficial-case")], experiment_id="CAL-BENEFICIAL")
    ctrl = _controller({"beneficial-case": ("blocked", "pass")})
    result = ctrl.run_experiment(spec=spec, batch_config=_batch_config(), budget=_authorized_budget(), evidence_dir=tmp_path)
    assert result["status"] == "completed"
    assert result["raw_decision"] == "keep_candidate"
    assert result["pilot_decision"] == "candidate_for_owner_review"


# ---------------------------------------------------------------------------
# Control 2: known harmful candidate -> regression/reject
# ---------------------------------------------------------------------------


def test_control_harmful_candidate_yields_reject(tmp_path):
    patch, h = _tiebreak_patch()
    spec = _spec(patch, h, cases=[_case("harmful-case")], experiment_id="CAL-HARMFUL")
    ctrl = _controller({"harmful-case": ("pass", "blocked")})
    result = ctrl.run_experiment(spec=spec, batch_config=_batch_config(), budget=_authorized_budget(), evidence_dir=tmp_path)
    assert result["status"] == "completed"
    assert result["raw_decision"] == "discard"
    assert result["pilot_decision"] == "reject"


# ---------------------------------------------------------------------------
# Control 3: semantic no-op -> no stable improvement signal
# ---------------------------------------------------------------------------


def test_control_semantic_no_op_stays_inconclusive(tmp_path):
    patch, h = _tiebreak_patch()
    spec = _spec(patch, h, cases=[_case("no-op-case")], experiment_id="CAL-NOOP")
    ctrl = _controller({"no-op-case": ("pass", "pass")})
    result = ctrl.run_experiment(spec=spec, batch_config=_batch_config(), budget=_authorized_budget(), evidence_dir=tmp_path)
    assert result["status"] == "completed"
    assert result["raw_decision"] == "inconclusive"
    assert result["pilot_decision"] == "inconclusive"


# ---------------------------------------------------------------------------
# Control 4: mixed candidate -> regression veto overrides local target gain
# ---------------------------------------------------------------------------


def test_control_mixed_candidate_regression_vetoes_local_gain(tmp_path):
    patch, h = _tiebreak_patch()
    spec = _spec(
        patch, h,
        cases=[_case("mixed-gain-case", target_family_flag=True),
               _case("mixed-regression-case", target_family_flag=False)],
        experiment_id="CAL-MIXED",
    )
    ctrl = _controller({
        "mixed-gain-case": ("blocked", "pass"),       # local target-family gain
        "mixed-regression-case": ("pass", "blocked"),  # regression elsewhere
    })
    result = ctrl.run_experiment(spec=spec, batch_config=_batch_config(), budget=_authorized_budget(), evidence_dir=tmp_path)
    assert result["status"] == "completed"
    assert result["raw_decision"] == "discard"
    assert result["pilot_decision"] == "reject"
    assert result["reason"].startswith("material regression")


# ---------------------------------------------------------------------------
# Controlled-L1 context-boundary guards ([LLM]->[Codex] handoff, 2026-09-05)
# ---------------------------------------------------------------------------


def test_native_project_subject_context_scope_blocked_zero_calls(tmp_path):
    """Blocked by the top-of-function guard, before budget.as_shared_state()
    is ever called -- structurally zero Subject/Judge calls, not merely
    zero observed on a freshly-constructed BudgetState."""
    patch, h = _tiebreak_patch()
    spec = _spec(patch, h, cases=[_case("scope-case")], experiment_id="CAL-SCOPE")
    ctrl = _controller({})
    result = ctrl.run_experiment(
        spec=spec,
        batch_config=_batch_config(subject_context_scope="native_project"),
        budget=_authorized_budget(),
        evidence_dir=tmp_path,
    )
    assert result["status"] == "blocked"
    assert "subject_context_scope" in result["reason"]
    assert "record" not in result


def test_unverified_memory_isolation_blocked_zero_calls(tmp_path):
    patch, h = _tiebreak_patch()
    spec = _spec(patch, h, cases=[_case("isolation-case")], experiment_id="CAL-ISOLATION")
    ctrl = _controller({})
    result = ctrl.run_experiment(
        spec=spec,
        batch_config=_batch_config(memory_personalization_isolation_status="unverifiable"),
        budget=_authorized_budget(),
        evidence_dir=tmp_path,
    )
    assert result["status"] == "blocked"
    assert "memory_personalization_isolation_status" in result["reason"]
    assert "record" not in result


def test_mutation_not_rendered_in_payload_discarded_zero_calls(tmp_path, monkeypatch):
    """A patch existing in Git is not itself experimental treatment -- if the
    declared mutation never actually reaches the rendered Subject payload
    (mutable_surface_excerpt absent or unchanged), the comparison must be
    discarded before any Subject/Judge call, not silently trusted."""
    patch, h = _tiebreak_patch()
    spec = _spec(patch, h, cases=[_case("invisible-mutation-case")], experiment_id="CAL-INVISIBLE")
    ctrl = _controller({})

    real_equivalence_report = cli.cpc.equivalence_report

    def _fake_equivalence_report(baseline_ctx, candidate_ctx):
        real = real_equivalence_report(baseline_ctx, candidate_ctx)
        real["mutable_surface_excerpt"] = {"present": True, "excerpt_differs": False}
        return real

    monkeypatch.setattr(cli.cpc, "equivalence_report", _fake_equivalence_report)
    result = ctrl.run_experiment(spec=spec, batch_config=_batch_config(), budget=_authorized_budget(), evidence_dir=tmp_path)
    assert result["status"] == "completed"
    assert result["raw_decision"] == "discard"
    assert "not visible in the rendered subject payload" in result["reason"]
    assert result["record"]["budget"]["calls_used"] == 0


# ---------------------------------------------------------------------------
# Ledger integrity across all four control runs
# ---------------------------------------------------------------------------


def test_all_four_controls_ledger_hash_chain_verifies(tmp_path):
    import autoresearch_validator as av

    scenarios = [
        ("CAL-BENEFICIAL", [_case("beneficial-case")], {"beneficial-case": ("blocked", "pass")}),
        ("CAL-HARMFUL", [_case("harmful-case")], {"harmful-case": ("pass", "blocked")}),
        ("CAL-NOOP", [_case("no-op-case")], {"no-op-case": ("pass", "pass")}),
        ("CAL-MIXED",
         [_case("mixed-gain-case", True), _case("mixed-regression-case", False)],
         {"mixed-gain-case": ("blocked", "pass"), "mixed-regression-case": ("pass", "blocked")}),
    ]
    for exp_id, cases, directions in scenarios:
        patch, h = _tiebreak_patch()
        spec = _spec(patch, h, cases=cases, experiment_id=exp_id)
        ctrl = _controller(directions)
        result = ctrl.run_experiment(spec=spec, batch_config=_batch_config(), budget=_authorized_budget(), evidence_dir=tmp_path)
        assert result["status"] == "completed"

    ledger_path = tmp_path / "autoresearch_manual_evaluations.jsonl"
    assert ledger_path.exists()
    findings = av.verify_ledger(ledger_path)
    assert findings == []
    lines = ledger_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 4
