from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "live_project_verifier.py"
SPEC = importlib.util.spec_from_file_location("live_project_verifier", SCRIPT)
assert SPEC and SPEC.loader
lpv = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = lpv
SPEC.loader.exec_module(lpv)


def write_contracts(tmp_path: Path, smoke: str | None = None) -> None:
    (tmp_path / "PROJECT_REGISTRY.md").write_text(
        "| `[AI OS]` | `ChatGPT/[AI OS]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |\n"
        "| `[LLM]` | `ChatGPT/[LLM]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |\n"
        "| `[Analytics]` | `ChatGPT/[Analytics]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |\n",
        encoding="utf-8",
    )
    plan_path = tmp_path / "docs/operations/SMOKE_QA_REFRESH_PLAN.md"
    plan_path.parent.mkdir(parents=True)
    plan_path.write_text(
        smoke
        or """## [AI OS] Smoke QA
Test ID: `LIVE-AIOS-SMOKE-001`
Question: Q
Expected result: E
Pass condition: P
Fail condition: F
Deterministic required groups: `alpha|beta`; `gamma`
Deterministic forbidden phrases: `forbidden`
""",
        encoding="utf-8",
    )


def init_repo(tmp_path: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=tmp_path, check=True)


def test_canonical_project_resolution(tmp_path: Path) -> None:
    write_contracts(tmp_path)
    projects = lpv.parse_project_registry(tmp_path / "PROJECT_REGISTRY.md")
    assert projects["[LLM]"].path == "ChatGPT/[LLM]"


def test_stable_test_id_parsing() -> None:
    cases = lpv.parse_smoke_cases(ROOT / "docs/operations/SMOKE_QA_REFRESH_PLAN.md")
    assert set(cases) >= {
        "LIVE-AIOS-SMOKE-001",
        "LIVE-AIOS-SMOKE-002",
        "LIVE-AIOS-SMOKE-003",
        "LIVE-LLM-SMOKE-001",
        "LIVE-LLM-SMOKE-002",
        "LIVE-ANALYTICS-SMOKE-001",
        "LIVE-ANALYTICS-SMOKE-002",
    }


def test_missing_test_id_fails_for_mvp_project(tmp_path: Path) -> None:
    write_contracts(tmp_path, "## [AI OS] Smoke QA\nQuestion: unregistered\n")
    with pytest.raises(lpv.ContractError, match="missing Test ID"):
        lpv.parse_smoke_cases(tmp_path / "docs/operations/SMOKE_QA_REFRESH_PLAN.md")


def test_duplicate_test_id_fails(tmp_path: Path) -> None:
    block = """## [AI OS] Smoke QA
Test ID: `DUPLICATE`
Question: Q
Expected result: E
Pass condition: P
Fail condition: F
Test ID: `DUPLICATE`
Question: Q2
Expected result: E2
Pass condition: P2
Fail condition: F2
"""
    write_contracts(tmp_path, block)
    with pytest.raises(lpv.ContractError, match="duplicate Test ID"):
        lpv.parse_smoke_cases(tmp_path / "docs/operations/SMOKE_QA_REFRESH_PLAN.md")


def make_history(tmp_path: Path, first: str, second: str) -> tuple[str, str]:
    init_repo(tmp_path)
    (tmp_path / first).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / first).write_text("one\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "base"], cwd=tmp_path, check=True)
    base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True).strip()
    (tmp_path / second).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / second).write_text("two\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "head"], cwd=tmp_path, check=True)
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True).strip()
    return base, head


def test_changed_project_path_selects_affected_smoke(tmp_path: Path) -> None:
    write_contracts(tmp_path)
    base, head = make_history(tmp_path, "base.txt", "ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md")
    plan = lpv.plan_impact(tmp_path, base, head)
    assert plan["affected_projects"] == ["[LLM]"]


def test_shared_governance_selects_mvp_regression(tmp_path: Path) -> None:
    write_contracts(tmp_path)
    base, head = make_history(tmp_path, "base.txt", "docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md")
    assert set(lpv.plan_impact(tmp_path, base, head)["affected_projects"]) == set(lpv.MVP_PROJECTS)


def test_readme_only_requires_no_live_test(tmp_path: Path) -> None:
    write_contracts(tmp_path)
    base, head = make_history(tmp_path, "base.txt", "README.md")
    plan = lpv.plan_impact(tmp_path, base, head)
    assert plan["affected_projects"] == []
    assert plan["impact_status"] == "KNOWN"


def test_unknown_path_is_conservative(tmp_path: Path) -> None:
    write_contracts(tmp_path)
    base, head = make_history(tmp_path, "base.txt", "mystery.contract")
    plan = lpv.plan_impact(tmp_path, base, head)
    assert plan["impact_status"] == "UNKNOWN"
    assert set(plan["affected_projects"]) == set(lpv.MVP_PROJECTS)


def test_sync_not_verified(tmp_path: Path) -> None:
    write_contracts(tmp_path)
    checklist_path = tmp_path / "docs/operations/CHATGPT_PROJECT_SYNC_CHECKLIST.md"
    checklist_path.parent.mkdir(parents=True, exist_ok=True)
    checklist_path.write_text("# no rows\n", encoding="utf-8")
    result = lpv.sync_gate(
        tmp_path,
        lpv.ProjectRef("[AI OS]", "ChatGPT/[AI OS]"),
        checklist_path,
    )
    assert result["state"] == "SYNC_NOT_VERIFIED"


def sample_case() -> lpv.TestCase:
    return lpv.TestCase("T", "[AI OS]", "Q", "E", "P", "F", (("alpha", "beta"), ("gamma",)), ("forbidden",))


def test_deterministic_pass() -> None:
    assert lpv.deterministic_evaluate(sample_case(), "Beta and gamma are present").result == "pass"


def test_deterministic_critical_fail() -> None:
    result = lpv.deterministic_evaluate(sample_case(), "alpha gamma forbidden")
    assert result.result == "fail"
    assert result.critical is True


def judge(verdict: str = "pass") -> lpv.JudgeResult:
    return lpv.JudgeResult("independent-codex-judge", verdict, (), (), (), (), ())


def live(status: str = "completed") -> lpv.LiveResponse:
    return lpv.LiveResponse("[AI OS]", "T", "CONTROLLED_BROWSER_TRANSPORT", "s", "e", "r", status, "https://chatgpt.com/g/g-p-x/c/y")


def test_judge_cannot_override_critical_fail() -> None:
    deterministic = lpv.DeterministicResult("fail", True, ("critical",))
    assert lpv.final_verdict("SYNC_VERIFIED", live(), deterministic, judge("pass")) == "fail"


def test_judge_material_fail() -> None:
    deterministic = lpv.DeterministicResult("pass", False, ())
    assert lpv.final_verdict("SYNC_VERIFIED", live(), deterministic, judge("fail")) == "fail"


def test_sync_blocked_precedes_behavior_classification() -> None:
    deterministic = lpv.DeterministicResult("fail", True, ("critical",))
    assert lpv.final_verdict("SYNC_STALE", live(), deterministic, judge("fail")) == "blocked"


def test_run_record_validation_rejects_runtime_response() -> None:
    record = {
        "schema_version": "live-project-verifier-v1",
        "run_id": "R",
        "test_id": "T",
        "project": "[AI OS]",
        "source_binding": {},
        "sync_state": "SYNC_VERIFIED",
        "sync_evidence": {},
        "transport": {},
        "response_sha256": "x",
        "response_hash_scope": "full response",
        "bounded_excerpt": "safe",
        "deterministic_result": {"result": "pass", "critical": False},
        "judge_result": {},
        "final_verdict": "pass",
        "limitations": [],
        "recorded_at": "now",
        "response": "must stay runtime-only",
    }
    with pytest.raises(lpv.ContractError, match="must not be stored"):
        lpv.validate_record(record)


def test_synthetic_negative_fixture_cannot_pass() -> None:
    case = lpv.parse_smoke_cases(ROOT / "docs/operations/SMOKE_QA_REFRESH_PLAN.md")["LIVE-AIOS-SMOKE-002"]
    capture = json.loads((ROOT / "tests/fixtures/live_project_bad_response.json").read_text(encoding="utf-8"))
    result = lpv.deterministic_evaluate(case, capture["response"])
    assert result.result == "fail"
    assert lpv.final_verdict("SYNC_VERIFIED", lpv.CapturedLiveTransport(capture).run(lpv.ProjectRef("[AI OS]", "ChatGPT/[AI OS]"), case), result, judge("pass")) == "fail"


def test_capture_hash_scope_is_preserved() -> None:
    capture = json.loads((ROOT / "tests/fixtures/live_project_bad_response.json").read_text(encoding="utf-8"))
    capture["capture_scope"] = "bounded exact excerpt"
    case = lpv.parse_smoke_cases(ROOT / "docs/operations/SMOKE_QA_REFRESH_PLAN.md")["LIVE-AIOS-SMOKE-002"]
    response = lpv.CapturedLiveTransport(capture).run(
        lpv.ProjectRef("[AI OS]", "ChatGPT/[AI OS]"), case
    )
    assert response.response_scope == "bounded exact excerpt"


def test_independent_judge_rejects_target_surface() -> None:
    payload = {
        "judge_surface": "[LLM]",
        "judge_verdict": "pass",
        "material_findings": [],
        "unsupported_claims": [],
        "routing_defects": [],
        "evidence_defects": [],
        "limitations": [],
    }
    with pytest.raises(lpv.ContractError, match="own independent Judge"):
        lpv.parse_judge(payload, "[LLM]")


def test_real_behavior_failure_creates_bounded_codex_handoff() -> None:
    deterministic = lpv.DeterministicResult("fail", True, ("forbidden capability",))
    record = lpv.failure_record(
        "fail",
        lpv.ProjectRef("[AI OS]", "ChatGPT/[AI OS]"),
        sample_case(),
        {"repo_revision": "abc", "sources": [{"path": "ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md"}]},
        "response-hash",
        "SYNC_VERIFIED",
        deterministic,
        judge("pass"),
    )
    assert record is not None
    handoff = record["corrective_handoff"]
    assert handoff["target"] == "[Codex]"
    assert handoff["required_rerun"] == ["T", "materially affected sibling cases"]
    assert "response" not in handoff["actual_behavior_evidence"]
