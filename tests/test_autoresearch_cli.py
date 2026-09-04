"""Focused tests for the AIOS AutoResearch v0.2 CLI / controller
(issue #416, parent #409).

No network / model call anywhere. `--dry-run` and the fake controller paths
are exercised with deterministic doubles from #413/#414/#415.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "autoresearch_cli.py"
RUN_MANIFEST_SCHEMA = REPO_ROOT / "schemas" / "autoresearch_run_manifest.schema.json"

_spec = importlib.util.spec_from_file_location("autoresearch_cli", MODULE_PATH)
cli = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = cli
_spec.loader.exec_module(cli)

jsonschema = pytest.importorskip("jsonschema")


def _run(*argv: str, capsys) -> tuple[int, str]:
    code = cli.main(list(argv))
    out = capsys.readouterr()
    return code, out.out + out.err


def _authorized_batch(tmp_path: Path) -> Path:
    p = tmp_path / "batch.json"
    p.write_text(
        json.dumps(
            {
                "transport_id": "playwright_mcp",
                "context_manifest_hash": "a" * 64,
                "authority_status": "authorized",
            }
        ),
        encoding="utf-8",
    )
    return p


# --------------------------------------------------------------------------
# CLI surface: help, version, exit codes, config validation
# --------------------------------------------------------------------------


def test_all_verbs_have_help_and_stable_exit_code(capsys):
    for verb in cli.VERBS:
        with pytest.raises(SystemExit) as ei:
            cli.build_parser().parse_args([verb, "--help"])
        assert ei.value.code == 0
    capsys.readouterr()


def test_version_and_bad_usage_exit_codes(capsys):
    with pytest.raises(SystemExit) as ei:
        cli.main(["--version"])
    assert ei.value.code == 0
    with pytest.raises(SystemExit) as ei2:
        cli.main(["experiment"])  # missing required --batch-config
    assert ei2.value.code == cli.EXIT_USAGE


def test_help_documents_exit_codes_and_precedence(capsys):
    with pytest.raises(SystemExit):
        cli.main(["--help"])
    out = capsys.readouterr().out
    assert "Exit codes:" in out and "Config precedence:" in out


# --------------------------------------------------------------------------
# doctor
# --------------------------------------------------------------------------


def test_doctor_fails_before_calls_when_identity_missing(capsys):
    code, out = _run("doctor", "--max-calls", "40", "--max-cost", "0", "--cost-currency", "USD", capsys=capsys)
    assert code == cli.EXIT_PREFLIGHT
    assert "batch config supplied" in out and "NOT READY" in out


def test_doctor_ready_with_authorized_batch_and_budget(tmp_path, capsys):
    code, out = _run(
        "doctor", "--batch-config", str(_authorized_batch(tmp_path)),
        "--max-calls", "40", "--max-cost", "0", "--cost-currency", "USD", capsys=capsys,
    )
    assert code == cli.EXIT_OK
    assert "READY" in out


def test_doctor_unauthorized_budget_fails(tmp_path, capsys):
    code, out = _run("doctor", "--batch-config", str(_authorized_batch(tmp_path)), capsys=capsys)
    assert code == cli.EXIT_PREFLIGHT
    assert "budget authorized" in out


# --------------------------------------------------------------------------
# context (no model call)
# --------------------------------------------------------------------------


def test_context_compiles_without_a_model_call(capsys):
    code, out = _run("context", "--project", "ai_os", "--source-revision", "HEAD", capsys=capsys)
    assert code == cli.EXIT_OK
    manifest = json.loads(out)
    assert manifest["fidelity_mode"] == "repo_replay"
    assert manifest["role"] == "subject_baseline"


# --------------------------------------------------------------------------
# dry-run: zero external calls, accurate preview
# --------------------------------------------------------------------------


def test_experiment_dry_run_makes_zero_calls_and_previews_counts(tmp_path, capsys):
    code, out = _run(
        "experiment", "--batch-config", str(_authorized_batch(tmp_path)),
        "--cases", "c1,c2,c3", "--run-count", "3",
        "--max-calls", "40", "--max-cost", "0", "--cost-currency", "USD", "--dry-run", capsys=capsys,
    )
    assert code == cli.EXIT_OK
    payload = json.loads(out)
    assert payload["dry_run"] is True
    ec = payload["preview"]["external_calls"]
    # issue #433 minimal-for-C1 scope: run_experiment always performs exactly
    # adc.MIN_MATCHED_RERUNS (3) matched reruns per case, and the Judge runs a
    # blind A/B pass (both orders) on EVERY matched rerun, not just once --
    # so both legs scale with reruns * cases, regardless of --run-count.
    assert ec["subject"] == 2 * 3 * 3 and ec["judge"] == 2 * 3 * 3
    assert ec["total"] == ec["subject"] + ec["judge"] + ec["researcher"]
    assert set(ec) == {"subject", "researcher", "judge", "total"}
    assert "not authorization" in payload["preview"]["note"]


def test_experiment_without_dry_run_and_without_binding_is_blocked(tmp_path, capsys):
    code, out = _run(
        "experiment", "--batch-config", str(_authorized_batch(tmp_path)),
        "--cases", "c1", "--run-count", "2",
        "--max-calls", "40", "--max-cost", "0", "--cost-currency", "USD", capsys=capsys,
    )
    assert code == cli.EXIT_BLOCKED
    assert json.loads(out)["status"] == "blocked"


def test_experiment_blocked_path_still_runs_doctor_first(tmp_path, capsys):
    # unauthorized budget -> doctor fails -> exit 3, not 4
    code, out = _run(
        "experiment", "--batch-config", str(_authorized_batch(tmp_path)),
        "--cases", "c1", "--run-count", "2", capsys=capsys,
    )
    assert code == cli.EXIT_PREFLIGHT


# --------------------------------------------------------------------------
# reproduce / propose
# --------------------------------------------------------------------------


def test_reproduce_field_observation_without_runs_is_not_reproduced(tmp_path, capsys):
    rec = tmp_path / "f.json"
    rec.write_text(json.dumps({"failure_id": "F1", "source_type": "field_observation"}), encoding="utf-8")
    code, out = _run("reproduce", "--failure-record", str(rec), capsys=capsys)
    assert code == cli.EXIT_OK
    assert json.loads(out)["reproduction_status"] == "not_reproduced"


def test_propose_dry_run_states_one_call_plus_retry(tmp_path, capsys):
    rec = tmp_path / "f.json"
    rec.write_text(json.dumps({"failure_id": "F1"}), encoding="utf-8")
    code, out = _run("propose", "--failure-record", str(rec), "--dry-run", capsys=capsys)
    assert code == cli.EXIT_OK
    payload = json.loads(out)
    assert payload["researcher_calls_planned"] == 1 and payload["retry_allowed"] == 1


# --------------------------------------------------------------------------
# run manifest: schema, resume idempotence, cleanup scope
# --------------------------------------------------------------------------


def test_run_manifest_schema_valid_and_roundtrips(tmp_path):
    schema = json.loads(RUN_MANIFEST_SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft7Validator.check_schema(schema)
    rm = cli.RunManifest.new(
        run_id="run-001", batch_id="b-001", source_revision="abcdef1",
        context_manifest_hash="a" * 64, evaluator_version_hash="b" * 64,
        authority_evidence_ref="docs/evidence/x.md#owner",
    )
    p = tmp_path / "run.json"
    rm.save(p)
    jsonschema.Draft7Validator(schema).validate(json.loads(p.read_text(encoding="utf-8")))
    back = cli.RunManifest.load(p)
    assert back.steps["loaded"] == "done" and back.steps["decision"] == "pending"


def test_cleanup_removes_only_registered_worktrees_and_preserves_state(tmp_path, capsys):
    rm = cli.RunManifest.new(
        run_id="run-002", batch_id="b-002", source_revision="abcdef1",
        context_manifest_hash=None, evaluator_version_hash=None,
        authority_evidence_ref="docs/evidence/x.md#owner",
    )
    rm.registered_worktrees = []  # nothing registered -> nothing removed
    p = tmp_path / "run.json"
    rm.save(p)
    code, out = _run("cleanup", "--run-manifest", str(p), capsys=capsys)
    assert code == cli.EXIT_OK
    assert json.loads(out)["removed"] == []
    assert cli.RunManifest.load(p).steps["cleanup"] == "done"


def test_report_reconciles_and_flags_ledger_integrity(tmp_path, capsys):
    rm = cli.RunManifest.new(
        run_id="run-003", batch_id="b-003", source_revision="abcdef1",
        context_manifest_hash=None, evaluator_version_hash=None,
        authority_evidence_ref="docs/evidence/x.md#owner",
    )
    p = tmp_path / "run.json"
    rm.save(p)
    bad_ledger = tmp_path / "ledger.jsonl"
    bad_ledger.write_text('{"seq": 1, "prev_hash": "deadbeef", "line_hash": "nope", "record": {"experiment_id": "e1"}}\n', encoding="utf-8")
    code, out = _run("report", "--run-manifest", str(p), "--ledger", str(bad_ledger), "--decision", "keep_candidate", capsys=capsys)
    payload = json.loads(out)
    assert payload["ledger_status"] == "integrity_failure"
    assert code == cli.EXIT_INTEGRITY
    assert payload["authority_merge_production"]["authority_status"] == "owner_review_pending"


def test_report_keep_candidate_never_advances_baseline_or_opens_pr(tmp_path, capsys):
    rm = cli.RunManifest.new(
        run_id="run-004", batch_id="b-004", source_revision="abcdef1",
        context_manifest_hash=None, evaluator_version_hash=None, authority_evidence_ref="x#o",
    )
    p = tmp_path / "run.json"
    rm.save(p)
    code, out = _run("report", "--run-manifest", str(p), "--decision", "keep_candidate", capsys=capsys)
    payload = json.loads(out)
    assert payload["authority_merge_production"]["merge_status"] == "not_applicable"
    assert payload["authority_merge_production"]["production_status"] == "not_applicable"
    assert "never advances a baseline" in payload["limitations"]


# --------------------------------------------------------------------------
# integration: real components wired, not reimplemented
# --------------------------------------------------------------------------


def test_controller_integrates_real_v01_and_v02_modules():
    assert cli.av.verify_ledger and cli.asr.run_shadow_experiment
    assert cli.adc.aggregate_decision and cli.cpc.compile_subject_baseline
    assert cli.lba.invoke and cli.lj.run_blind_ab and cli.fi.run_researcher


def test_preview_counts_subject_researcher_judge_separately():
    c = cli.Controller()
    budget = cli.RoleBudget(max_provider_calls=40, max_cost_amount=0.0, max_cost_currency="USD")
    preview = c.preview_experiment(batch_config={"transport_id": "playwright_mcp"}, case_ids=["a", "b"], run_count=3, budget=budget)
    ec = preview["external_calls"]
    assert set(ec) == {"subject", "researcher", "judge", "total"}
    assert ec["researcher"] == 0  # experiment verb makes no researcher call


def test_no_network_imports_in_cli():
    import inspect

    src = inspect.getsource(cli)
    assert "import requests" not in src and "urllib.request" not in src


def test_active_repo_fingerprint_unchanged_by_cli_report(tmp_path, capsys):
    before = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    rm = cli.RunManifest.new(
        run_id="run-x", batch_id="b-x", source_revision="abcdef1",
        context_manifest_hash=None, evaluator_version_hash=None, authority_evidence_ref="x#o",
    )
    p = tmp_path / "r.json"
    rm.save(p)
    _run("report", "--run-manifest", str(p), capsys=capsys)
    after = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    assert before == after
