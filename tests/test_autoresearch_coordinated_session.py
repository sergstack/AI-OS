"""Tests for the AIOS AutoResearch v0.2 coordinated-session transport-binding
seam (issue #433, follow-up to #416).

NO live / network / model call anywhere. `FakeBrowserTransport` and
`FakeJudgeModel` are deterministic and do no I/O; the injected `mcp_call`
stubs raise if they are ever invoked, proving the seam makes no live call in
CI.
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
acs = _load("autoresearch_coordinated_session")

jsonschema = pytest.importorskip("jsonschema")

REV = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------


def _finding(**ov) -> dict:
    base = {
        "case_family": "routing",
        "finding": "A and B route identically to the correct owner with a hand-off.",
        "evidence": "both name the same destination and include the required context.",
        "severity": "low",
        "affected_invariant_or_metric": "routing_correctness",
        "verdict": "pass",
        "confidence": "medium",
        "limitations": "none material",
    }
    base.update(ov)
    return base


def _arr(*f) -> str:
    return json.dumps(list(f))


def _tiebreak_patch(replace: str = "a prompt or workflow deliverable",
                    with_: str = "a prompt/workflow deliverable") -> tuple[str, str]:
    """Reproduce the frozen C1 shape: one line of ROUTING_RULES.md's
    tie-break table body. Returns (patch_text, sha256)."""
    target = REPO_ROOT / "ROUTING_RULES.md"
    original = target.read_text(encoding="utf-8")
    assert replace in original
    target.write_text(original.replace(replace, with_), encoding="utf-8")
    try:
        diff = subprocess.run(["git", "diff", "--", "ROUTING_RULES.md"], cwd=REPO_ROOT,
                              capture_output=True, text=True).stdout
    finally:
        target.write_text(original, encoding="utf-8")
    assert diff
    return diff, cli.av.sha256_hex(diff.encode("utf-8"))


def _protected_patch() -> tuple[str, str]:
    target = REPO_ROOT / "ROUTING_RULES.md"
    original = target.read_text(encoding="utf-8")
    target.write_text(original.replace("| Raw input, capture, unclear thought | `[Inbox Router]` |",
                                       "| Raw input, capture, unclear thought | `[Codex]` |"), encoding="utf-8")
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
        "authority_evidence_ref": "docs/evidence/TEST.md#owner",
        "call_timeout_seconds": 180,
        "retry_limit": 1,
        "target_url_prefix": "https://chatgpt.com/",
        "target_product": "openai_chatgpt_ui",
        "session_policy": "fresh_conversation",
    }
    base.update(ov)
    return base


def _spec(patch_text: str, patch_hash: str, run_count: int = 3, target_family: bool = True) -> cli.ManualCandidateSpec:
    return cli.ManualCandidateSpec(
        experiment_id="AR-433-TEST",
        baseline_revision=REV,
        project="ai_os",
        research_surface="MUT-ROUTING-TIEBREAK",
        target_file="ROUTING_RULES.md",
        patch_text=patch_text,
        candidate_patch_hash=patch_hash,
        cases=[{"case_id": "tiebreak-c1", "case_family": "routing",
                "target_family_flag": target_family,
                "input": "A user asks to prepare a coding task whose deliverable is a workflow. Which owner?"}],
        run_count=run_count,
    )


def _authorized_budget() -> cli.RoleBudget:
    return cli.RoleBudget(max_provider_calls=40, max_cost_amount=0.0, max_cost_currency="USD")


def _fake_controller(scripted: str = "OK: route to [LLM] for the workflow deliverable.") -> cli.Controller:
    transport = lba.FakeBrowserTransport(scripted_response=scripted, page_url="https://chatgpt.com/c/fake")
    judge = lj.FakeJudgeModel({0: _arr(_finding()), 1: _arr(_finding())})
    return cli.Controller(transport=transport, judge_model=judge)


# --------------------------------------------------------------------------
# fail-closed: structural block preserved and extended
# --------------------------------------------------------------------------


def test_run_experiment_blocked_without_transport():
    patch, h = _tiebreak_patch()
    res = cli.Controller().run_experiment(
        spec=_spec(patch, h), batch_config=_batch_config(), budget=_authorized_budget()
    )
    assert res["status"] == "blocked"
    assert "coordinated" in res["reason"].lower() or "autoresearch_coordinated_session" in res["reason"]


def test_run_experiment_blocked_when_budget_unauthorized():
    patch, h = _tiebreak_patch()
    res = _fake_controller().run_experiment(
        spec=_spec(patch, h), batch_config=_batch_config(),
        budget=cli.RoleBudget(max_provider_calls=None, max_cost_amount=None, max_cost_currency=None),
    )
    assert res["status"] == "blocked" and "budget" in res["reason"].lower()


def test_run_experiment_blocked_when_batch_not_authorized():
    patch, h = _tiebreak_patch()
    res = _fake_controller().run_experiment(
        spec=_spec(patch, h), batch_config=_batch_config(authority_status="owner_review_pending"),
        budget=_authorized_budget(),
    )
    assert res["status"] == "blocked" and "authority_status" in res["reason"]


# --------------------------------------------------------------------------
# end-to-end with fakes: reaches transport + judge, returns a bounded decision
# --------------------------------------------------------------------------


def test_run_experiment_end_to_end_with_fakes(tmp_path):
    patch, h = _tiebreak_patch()
    ctrl = _fake_controller()
    res = ctrl.run_experiment(
        spec=_spec(patch, h), batch_config=_batch_config(), budget=_authorized_budget(),
        evidence_dir=tmp_path,
    )
    assert res["status"] == "completed"
    assert res["pilot_decision"] in {"reject", "inconclusive", "candidate_for_owner_review"}
    assert res["raw_decision"] != "keep_candidate"
    assert res["pilot_decision"] != "keep_candidate"
    # the frozen transport double was actually driven (6 subject calls for 3 reruns x 2 sides)
    assert ctrl.transport.submissions >= 2
    evidence = json.loads((tmp_path / "AR-433-TEST_evidence.json").read_text())
    assert evidence["mode"] == "manual_candidate_evaluation"
    assert evidence["context_equivalence"]["equivalent"] is True
    assert evidence["context_equivalence"]["differences"] == ["ROUTING_RULES.md"]
    assert evidence["cases"] and "semantic" in evidence["cases"][0]
    assert "pending [AI OS]/[Analytics] sign-off" in " ".join(evidence["limitations"])


def test_run_experiment_identical_outputs_never_reach_candidate_for_owner_review(tmp_path):
    # FakeBrowserTransport returns the same text for baseline and candidate =>
    # no distinguishable behavioral improvement => must be inconclusive, never
    # candidate_for_owner_review (which requires a real target-family gain).
    patch, h = _tiebreak_patch()
    res = _fake_controller().run_experiment(
        spec=_spec(patch, h), batch_config=_batch_config(), budget=_authorized_budget(),
    )
    assert res["pilot_decision"] == "inconclusive"


# --------------------------------------------------------------------------
# deterministic hard gate dominates
# --------------------------------------------------------------------------


def test_run_experiment_rejects_protected_scope_patch():
    patch, h = _protected_patch()
    res = _fake_controller().run_experiment(
        spec=_spec(patch, h), batch_config=_batch_config(), budget=_authorized_budget(),
    )
    assert res["status"] == "completed"
    assert res["pilot_decision"] == "reject"
    assert "hard gate" in res["reason"].lower()


# --------------------------------------------------------------------------
# MD-2 / MD-4 unit behaviour (isolated, review-flagged glue)
# --------------------------------------------------------------------------


class _Sem:
    def __init__(self, contributes):
        self.contributes = contributes


def test_md2_semantic_to_case_observation_mapping():
    case = {"case_id": "c", "case_family": "routing"}
    stable = {"baseline": ["same", "same", "same"], "candidate": ["same", "same", "same"]}

    o_pass = cli._semantic_to_case_observation(sem=_Sem("pass"), case=case, rerun_outputs=stable,
                                               run_count=3, evaluator_version_hash="e" * 64)
    assert o_pass.baseline_verdicts == ("pass", "pass", "pass")
    assert o_pass.candidate_verdicts == ("pass", "pass", "pass")

    o_block = cli._semantic_to_case_observation(sem=_Sem("blocked"), case=case, rerun_outputs=stable,
                                                run_count=3, evaluator_version_hash="e" * 64)
    assert o_block.candidate_verdicts == ("blocked", "blocked", "blocked")
    assert o_block.baseline_verdicts == ("pass", "pass", "pass")

    o_inc = cli._semantic_to_case_observation(sem=_Sem("inconclusive"), case=case, rerun_outputs=stable,
                                              run_count=3, evaluator_version_hash="e" * 64)
    assert o_inc.baseline_verdicts == (None, None, None)

    variant = {"baseline": ["a", "b", "c"], "candidate": ["x", "x", "x"]}
    o_var = cli._semantic_to_case_observation(sem=_Sem("pass"), case=case, rerun_outputs=variant,
                                              run_count=3, evaluator_version_hash="e" * 64)
    assert o_var.baseline_verdicts == (None, None, None)  # subject flakiness -> null pairs


def test_md4_pilot_decision_map_never_emits_keep_candidate():
    assert "keep_candidate" not in set(cli._PILOT_DECISION.values())
    assert cli._PILOT_DECISION["keep_candidate"] == "candidate_for_owner_review"
    assert cli._PILOT_DECISION["discard"] == "reject"
    assert cli._PILOT_DECISION["inconclusive"] == "inconclusive"


# --------------------------------------------------------------------------
# coordinated-session module: guards + wiring, no I/O
# --------------------------------------------------------------------------


def _raising_mcp(*_a, **_k):
    raise AssertionError("mcp_call must not be invoked in a CI test")


def test_coordinated_session_guards_block_before_any_call():
    patch, h = _tiebreak_patch()
    res = acs.run_manual_candidate_evaluation(
        mcp_call=_raising_mcp, batch_config=_batch_config(authority_status="owner_review_pending"),
        spec=_spec(patch, h), budget=_authorized_budget(),
    )
    assert res["status"] == "blocked"


def test_coordinated_session_requires_authority_evidence_ref():
    patch, h = _tiebreak_patch()
    bc = _batch_config()
    bc.pop("authority_evidence_ref")
    res = acs.run_manual_candidate_evaluation(
        mcp_call=_raising_mcp, batch_config=bc, spec=_spec(patch, h), budget=_authorized_budget(),
    )
    assert res["status"] == "blocked" and "authority_evidence_ref" in res["reason"]


def test_build_live_controller_wires_real_transport_and_judge_without_io():
    ctrl = acs.build_live_controller(
        mcp_call=_raising_mcp, batch_config=_batch_config(),
        budget=_authorized_budget(), authority_evidence_ref="docs/evidence/TEST.md#owner",
    )
    assert isinstance(ctrl.transport, lba.PlaywrightMcpBrowserTransport)
    assert ctrl.transport.transport_id == "playwright_mcp"
    assert isinstance(ctrl.judge_model, lj.BrowserJudgeModel)
    # constructing the binding performs no I/O -> the raising stub was never called


# --------------------------------------------------------------------------
# CLI wiring: bound run reaches run_experiment; bare run still blocked
# --------------------------------------------------------------------------


def test_cli_experiment_bare_still_blocked_and_points_to_coordinated_session(capsys, tmp_path):
    cfgp = tmp_path / "batch.json"
    cfgp.write_text(json.dumps(_batch_config()), encoding="utf-8")
    code = cli.main(["experiment", "--batch-config", str(cfgp), "--cases", "c1",
                     "--max-calls", "40", "--max-cost", "0", "--cost-currency", "USD"])
    out = capsys.readouterr().out
    assert code == cli.EXIT_BLOCKED
    payload = json.loads(out)
    assert payload["status"] == "blocked"
    assert "coordinated_session" in payload["reason"] or "coordinated live session" in payload["reason"]


def test_cli_experiment_bound_controller_reaches_run_experiment(capsys, monkeypatch, tmp_path):
    patch, h = _tiebreak_patch()
    spec_file = tmp_path / "spec.json"
    spec_file.write_text(json.dumps({
        "experiment_id": "AR-433-CLI",
        "baseline_revision": REV,
        "project": "ai_os",
        "research_surface": "MUT-ROUTING-TIEBREAK",
        "target_file": "ROUTING_RULES.md",
        "patch_text": patch,
        "candidate_patch_hash": h,
        "cases": [{"case_id": "c1", "case_family": "routing", "target_family_flag": True,
                   "input": "coding task prep, deliverable is a workflow; owner?"}],
        "run_count": 3,
    }), encoding="utf-8")
    cfg_file = tmp_path / "batch.json"
    cfg_file.write_text(json.dumps(_batch_config()), encoding="utf-8")

    monkeypatch.setattr(cli, "_CONTROLLER_FACTORY", _fake_controller)
    code = cli.main(["experiment", "--batch-config", str(cfg_file), "--spec-file", str(spec_file),
                     "--evidence-dir", str(tmp_path / "ev"),
                     "--max-calls", "40", "--max-cost", "0", "--cost-currency", "USD"])
    out = capsys.readouterr().out
    assert code == cli.EXIT_OK
    payload = json.loads(out)
    assert payload["status"] == "completed"
    assert payload["pilot_decision"] in {"reject", "inconclusive", "candidate_for_owner_review"}


# --------------------------------------------------------------------------
# no live-call imports
# --------------------------------------------------------------------------


def test_no_network_or_mcp_imports_in_seam():
    import inspect

    for mod in (acs, cli):
        src = inspect.getsource(mod)
        assert "import requests" not in src
        assert "urllib.request" not in src
        assert "mcp__playwright" not in src.replace("mcp__playwright__browser_*", "")  # doc mention only
