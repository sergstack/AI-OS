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
    # issue #433 minimal-for-C1 scope: exactly MIN_MATCHED_RERUNS (3) reruns,
    # each with a per-case Judge pass recorded under evidence["reruns"].
    assert len(evidence["reruns"]) == 3
    assert all("tiebreak-c1" in rr["cases"] for rr in evidence["reruns"])
    assert "contributes" in evidence["reruns"][0]["cases"]["tiebreak-c1"]
    assert evidence["case_results"] and evidence["case_results"][0]["case_id"] == "tiebreak-c1"
    assert "minimal-for-C1 scope" in " ".join(evidence["limitations"])
    # a schema-valid manual_candidate_evaluation record was ledgered (MD-3)
    record = json.loads((tmp_path / "AR-433-TEST_record.json").read_text())
    assert record["record_kind"] == "manual_candidate_evaluation"
    assert record["pilot_decision"] != "keep_candidate"
    # issue #433 fix #2: real captured hashes, honest status flags (no
    # fabricated placeholders now that context did compile).
    assert record["baseline_file_hash_status"] == "captured"
    assert record["context_identities"]["context_capture_status"] == "captured"
    assert record["context_identities"]["baseline_context_hash"] is not None
    assert record["context_identities"]["evaluator_version_hash"] is not None
    # issue #433 fix #4: a Judge finding for EVERY matched rerun (3), not
    # just the first.
    assert len(record["judge_findings"]) == 3
    assert sorted(f["rerun"] for f in record["judge_findings"]) == [0, 1, 2]
    assert all(f["case_id"] == "tiebreak-c1" for f in record["judge_findings"])
    # issue #433 fix #5: honestly-labeled judge_invocation_ids (not a generic
    # live_invocation_ids) plus the subject's own baseline/candidate
    # invocation ids, actually recorded (not reconstructed).
    assert len(record["matched_observations"]) == 3
    for obs in record["matched_observations"]:
        assert "judge_invocation_ids" in obs and "live_invocation_ids" not in obs
        assert obs["baseline_invocation_id"] is not None
        assert obs["candidate_invocation_id"] is not None
        assert "baseline" in obs["baseline_invocation_id"]
        assert "candidate" in obs["candidate_invocation_id"]
    ledger = tmp_path / "autoresearch_manual_evaluations.jsonl"
    assert ledger.exists()
    assert cli.av.verify_ledger(ledger) == []


def test_preview_experiment_c1_shaped_single_case_yields_exactly_12_calls():
    """issue #433 fix #7: the exact planned C1 live call count, verified via
    the real preview_experiment output (not just claimed arithmetic). C1 is
    one case; with adc.MIN_MATCHED_RERUNS == 3: subject = 2*3*1 = 6,
    judge = 2*3*1 = 6, total = 12."""
    c = cli.Controller()
    preview = c.preview_experiment(
        batch_config=_batch_config(), case_ids=["tiebreak-c1"], run_count=3,
        budget=_authorized_budget(),
    )
    assert preview["external_calls"] == {"subject": 6, "researcher": 0, "judge": 6, "total": 12}


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
    # issue #433 fix #1: a hard gate that fires BEFORE any matched rerun
    # (compile_subject_candidate raises before baseline/candidate context
    # both exist) must record zero observations honestly -- never a
    # synthetic placeholder row.
    record = res["record"]
    assert record["matched_observations"] == []
    assert record["judge_findings"] == []
    # issue #433 fix #2: no fabricated zero-hash / filename-hash anywhere;
    # honest null + explicit not_captured status instead.
    assert record["baseline_file_hash"] is None
    assert record["baseline_file_hash_status"] == "not_captured"
    assert record["context_identities"]["baseline_context_hash"] is None
    assert record["context_identities"]["candidate_context_hash"] is None
    assert record["context_identities"]["evaluator_version_hash"] is None
    assert record["context_identities"]["context_capture_status"] == "not_captured"


def test_run_experiment_blocked_when_call_timeout_seconds_missing():
    """issue #433 fix #3: a missing/invalid call_timeout_seconds must block
    before any call, not silently default to 180 (or any other value)."""
    patch, h = _tiebreak_patch()
    bc = _batch_config()
    bc.pop("call_timeout_seconds")
    res = _fake_controller().run_experiment(
        spec=_spec(patch, h), batch_config=bc, budget=_authorized_budget(),
    )
    assert res["status"] == "blocked"
    assert "call_timeout_seconds" in res["reason"]


def test_run_experiment_blocked_when_call_timeout_seconds_not_positive_int():
    patch, h = _tiebreak_patch()
    res = _fake_controller().run_experiment(
        spec=_spec(patch, h), batch_config=_batch_config(call_timeout_seconds=0), budget=_authorized_budget(),
    )
    assert res["status"] == "blocked"
    assert "call_timeout_seconds" in res["reason"]


def test_run_experiment_blocked_when_run_count_is_not_min_matched_reruns():
    """issue #433 fix #6: run_count must not be silently ignored -- a
    spec.run_count != adc.MIN_MATCHED_RERUNS is fail-closed blocked rather
    than silently running MIN_MATCHED_RERUNS reruns anyway."""
    patch, h = _tiebreak_patch()
    res = _fake_controller().run_experiment(
        spec=_spec(patch, h, run_count=5), batch_config=_batch_config(), budget=_authorized_budget(),
    )
    assert res["status"] == "blocked"
    assert "run_count" in res["reason"]


# --------------------------------------------------------------------------
# MD-2 / MD-4 unit behaviour (isolated, review-flagged glue)
# --------------------------------------------------------------------------


def test_md2_contributes_to_pair_mapping():
    """Issue #433 owner ruling, minimal-for-C1 scope: the ONLY MD-2 mapping is
    a one-branch, non-directional relabel of the existing comparative
    `contributes` verdict onto the comparator's per-side inputs. No
    directional per-side guessing for revise/blocked/inconclusive."""
    assert cli._contributes_to_pair("pass") == ("pass", "pass")
    assert cli._contributes_to_pair("revise") == (None, None)
    assert cli._contributes_to_pair("blocked") == (None, None)
    assert cli._contributes_to_pair("inconclusive") == (None, None)
    assert cli._contributes_to_pair("some_unexpected_value") == (None, None)


def test_md1_escalation_trigger_detected_but_not_escalated_stays_inconclusive():
    """Issue #433 owner ruling, minimal-for-C1 scope: if the canonical #395
    §8 trigger fires (baseline itself has variance across matched reruns for
    a target-family case -> `missingness_reason ==
    "evaluator_disagreement_unresolved"`), this scope does NOT run any extra
    reruns. adc's own fallback already yields "inconclusive" for that case
    and the batch decision must never be "keep_candidate"; an explicit,
    honest limitation string must be recorded."""
    obs = cli.adc.CaseObservation(
        case_id="tiebreak-c1", case_family="routing",
        baseline_verdicts=("pass", "revise", "pass"),  # baseline itself disagrees across reruns
        candidate_verdicts=("pass", "pass", "pass"),
        model_provider_runtime_hash="h" * 64, evaluator_version_hash="e" * 64,
    )
    result = cli.adc.evaluate_case(obs, target_family_flag=True)
    assert result.missingness_reason == "evaluator_disagreement_unresolved"
    assert result.run_variance_baseline is True

    decision = cli.adc.aggregate_decision([result])
    assert decision["decision"] != "keep_candidate"
    assert decision["decision"] == "inconclusive"

    limitations = cli._escalation_trigger_limitations([result])
    assert len(limitations) == 1
    assert "#395 §8 escalation trigger" in limitations[0]
    assert "tiebreak-c1" in limitations[0]
    assert "deferred to a follow-up" in limitations[0]
    assert "never upgraded" in limitations[0]


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
