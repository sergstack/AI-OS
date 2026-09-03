"""Focused tests for the AIOS AutoResearch v0.1 semantic evaluator finding
schema and worst-case aggregation (issue #394, parent #388).

This is a specification/contract test suite: it validates the frozen finding
schema and calibration fixtures. No live model call, no Judge prompt is
actually executed here -- issue #394 explicitly defers a real runner
integration to a separate [Codex] task.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = REPO_ROOT / "tests" / "fixtures" / "autoresearch" / "semantic_findings"
CONTRACT_DOC = REPO_ROOT / "ChatGPT" / "[LLM]" / "Knowledge" / "AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md"
FINDING_SCHEMA = REPO_ROOT / "schemas" / "autoresearch_semantic_finding.schema.json"

_spec = importlib.util.spec_from_file_location(
    "autoresearch_validator", REPO_ROOT / "scripts" / "autoresearch_validator.py"
)
av = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = av
_spec.loader.exec_module(av)

jsonschema = pytest.importorskip("jsonschema")


def _load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Schema self-validity
# ---------------------------------------------------------------------------


def test_finding_schema_is_valid_draft7():
    jsonschema.Draft7Validator.check_schema(json.loads(FINDING_SCHEMA.read_text(encoding="utf-8")))


# ---------------------------------------------------------------------------
# Calibration fixtures cover pass / revise / blocked
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "fixture_name,expected_verdict",
    [
        ("pass_example.json", "pass"),
        ("revise_example.json", "revise"),
        ("blocked_example.json", "blocked"),
        ("disagreement_example.json", "revise"),
        ("rationale_leakage_resistant_example.json", "pass"),
    ],
)
def test_calibration_fixtures_valid_and_correct_verdict(fixture_name, expected_verdict):
    doc = _load(fixture_name)
    assert av.validate_semantic_finding(doc) == []
    assert doc["verdict"] == expected_verdict


def test_all_three_verdicts_are_covered():
    verdicts = {_load(n)["verdict"] for n in ("pass_example.json", "revise_example.json", "blocked_example.json")}
    assert verdicts == {"pass", "revise", "blocked"}


# ---------------------------------------------------------------------------
# Schema structurally cannot carry authority/merge/production/identity/
# rationale/score (issue #394: "by construction, not by convention")
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "forbidden_field,value",
    [
        ("authority_status", "approved"),
        ("merge_status", "merged"),
        ("production_status", "authorized"),
        ("candidate_identity", "B"),
        ("hypothesis", "leaked researcher rationale"),
        ("expected_winner", "B"),
        ("aios_quality_score", 91.2),
    ],
)
def test_finding_schema_rejects_forbidden_fields(forbidden_field, value):
    doc = _load("pass_example.json")
    doc[forbidden_field] = value
    findings = av.validate_semantic_finding(doc)
    assert findings != [], f"schema must reject a finding carrying {forbidden_field!r}"


def test_finding_schema_has_no_optional_authority_or_score_property():
    schema = json.loads(FINDING_SCHEMA.read_text(encoding="utf-8"))
    props = set(schema["properties"].keys())
    for forbidden in ("authority_status", "merge_status", "production_status", "score", "quality_score", "candidate_identity"):
        assert forbidden not in props


# ---------------------------------------------------------------------------
# Invalid enums / missing fields fail
# ---------------------------------------------------------------------------


def test_invalid_verdict_enum_rejected():
    doc = _load("pass_example.json")
    doc["verdict"] = "fail"  # not a real verdict value in this contract
    assert av.validate_semantic_finding(doc) != []


def test_not_run_verdict_rejected_use_blocked_instead():
    doc = _load("pass_example.json")
    doc["verdict"] = "not_run"
    assert av.validate_semantic_finding(doc) != []


def test_invalid_case_family_rejected():
    doc = _load("pass_example.json")
    doc["case_family"] = "not_a_registered_family"
    assert av.validate_semantic_finding(doc) != []


def test_missing_limitations_rejected():
    doc = _load("pass_example.json")
    del doc["limitations"]
    assert av.validate_semantic_finding(doc) != []


def test_missing_evidence_rejected():
    doc = _load("revise_example.json")
    del doc["evidence"]
    assert av.validate_semantic_finding(doc) != []


# ---------------------------------------------------------------------------
# worst_verdict aggregation: blocked > revise > pass, never outvoted
# ---------------------------------------------------------------------------


def test_worst_verdict_blocked_dominates_many_passes():
    findings = [_load("pass_example.json") for _ in range(5)] + [_load("blocked_example.json")]
    assert av.worst_verdict(findings) == "blocked"


def test_worst_verdict_revise_dominates_pass():
    findings = [_load("pass_example.json"), _load("revise_example.json")]
    assert av.worst_verdict(findings) == "revise"


def test_worst_verdict_all_pass_is_pass():
    findings = [_load("pass_example.json"), _load("pass_example.json")]
    assert av.worst_verdict(findings) == "pass"


def test_worst_verdict_empty_list_raises():
    with pytest.raises(av.ContractError):
        av.worst_verdict([])


# ---------------------------------------------------------------------------
# Contract document self-consistency: every required section from issue
# #394's output layer is actually present (structural completeness check,
# not a semantic review)
# ---------------------------------------------------------------------------


REQUIRED_SECTIONS = [
    "## 1. Evaluator objective and context boundary",
    "## 2. Blind A/B comparison prompt family",
    "## 3. Deterministic-first gating rule",
    "## 4. Randomized / order-reversed evaluation protocol",
    "## 5. Case-family rubric",
    "## 6. Finding schema",
    "## 7. Evaluator/model-class routing and pinned configuration",
    "## 8. Human/owner escalation triggers",
    "## 9. Disagreement handling",
    "## 10. Evaluator versioning and content-hash contract",
    "## 11. Anti-leakage rules for validation and holdout",
    "## 12. Calibration cases",
]


def test_contract_document_has_all_required_sections():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    assert missing == [], f"contract doc is missing required sections: {missing}"


def test_contract_document_names_all_six_case_families():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    for family in ("routing", "scope_execution", "evidence", "authority", "handoff", "adversarial"):
        assert f"`{family}`" in text, f"case_family {family!r} not named in the contract"


def test_contract_document_references_existing_golden_cases_not_a_new_framework():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    for case_id in (
        "JUDGE-SELF-PREFERENCE",
        "JUDGE-AMBIGUITY-CALIBRATION",
        "JUDGE-REFERENCE-AVAILABLE",
        "JUDGE-LANGUAGE-PARITY",
    ):
        assert case_id in text, f"contract should reuse existing golden case {case_id!r}, not silently duplicate it"


def test_contract_document_is_candidate_not_active():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    assert "Status: `candidate`" in text
    assert "Not `active`" in text


def test_contract_document_states_no_owner_authority_embedded():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    assert "pass` is review evidence only" in text
