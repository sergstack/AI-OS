from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "response_quality_evaluator.py"
SPEC = importlib.util.spec_from_file_location("response_quality_evaluator", SCRIPT)
assert SPEC and SPEC.loader
rqe = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rqe
SPEC.loader.exec_module(rqe)


FIXTURE = ROOT / "tests" / "fixtures" / "response_quality_cases.json"


def cases() -> list[dict[str, object]]:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))["cases"]


def test_fixture_covers_pass_revise_and_blocked() -> None:
    records = rqe.evaluate_fixture(FIXTURE)
    assert [record["final_quality_status"] for record in records] == ["pass", "revise", "blocked"]


def test_record_hashes_response_without_storing_it() -> None:
    record = rqe.record_for(cases()[0])
    assert len(record["response_sha256"]) == 64
    assert "response" not in record
    assert record["schema_version"] == "response-quality-eval-v1"


def test_missing_required_marker_requires_revision() -> None:
    case = dict(cases()[0])
    case["response"] = "Ответ: выполните локальную проверку."
    case["expected_verdict"] = "revise"
    assert rqe.record_for(case)["final_quality_status"] == "revise"


def test_unresolved_material_finding_blocks_after_revision() -> None:
    case = dict(cases()[1])
    case["unsupported_claims"] = []
    case["judge_verdict"] = "pass"
    case["revision_count"] = 1
    case["unresolved_material_findings"] = ["evidence owner did not resolve the claim"]
    case["expected_verdict"] = "blocked"
    assert rqe.record_for(case)["final_quality_status"] == "blocked"


def test_rejects_duplicate_case_ids(tmp_path: Path) -> None:
    payload = {"cases": [cases()[0], cases()[0]]}
    path = tmp_path / "duplicate.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(rqe.ContractError, match="case_id"):
        rqe.evaluate_fixture(path)
