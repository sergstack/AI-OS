"""Tests for the subagent dispatch evidence schema + linter.

Covers the commissioning gate for "Supervised AI-OS subagent dispatch (pilot)".
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schemas" / "subagent_dispatch_evidence.schema.json"
EVIDENCE_PATH = REPO_ROOT / "docs" / "evidence" / "subagent_dispatch_records_2026-09-02.json"

import importlib.util

_spec = importlib.util.spec_from_file_location(
    "check_subagent_dispatch_evidence",
    REPO_ROOT / "scripts" / "check_subagent_dispatch_evidence.py",
)
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)


def _schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _valid_record() -> dict:
    return {
        "dispatch_id": "T-1",
        "execution_id": "exec-test-1",
        "owner_capability": "analytics",
        "agent_type": "Plan",
        "isolation": "worktree",
        "workspace_observation": {
            "path": "/x/.claude/worktrees/agent-abc123",
            "clean_tree": True,
            "head": "0a7ee18",
        },
        "outcome": "completed",
        "defect_ref": None,
        "telemetry": {"duration_ms": 1000, "subagent_tokens": 500, "tool_uses": 3},
        "scenario_tags": ["routing"],
    }


def _doc(records: list[dict], generated_for: str = "unit test") -> dict:
    return {"schema_version": "1.0.0", "generated_for": generated_for, "records": records}


def _errors(doc: dict) -> list[str]:
    return checker.schema_validate(doc, _schema())


def test_schema_is_valid_draft7() -> None:
    jsonschema = pytest.importorskip("jsonschema")
    jsonschema.Draft7Validator.check_schema(_schema())


def test_minimal_valid_doc_passes_schema_and_crosscheck() -> None:
    doc = _doc([_valid_record()])
    assert _errors(doc) == []
    assert checker.cross_check(doc, checker.registry_executors()) == []


def test_missing_agent_type_fails_schema() -> None:
    rec = _valid_record()
    del rec["agent_type"]
    assert _errors(_doc([rec])) != []


def test_write_capable_agent_type_rejected_by_enum() -> None:
    rec = _valid_record()
    rec["agent_type"] = "general-purpose"
    assert _errors(_doc([rec])) != []


def test_non_worktree_isolation_rejected() -> None:
    rec = _valid_record()
    rec["isolation"] = "shared"
    assert _errors(_doc([rec])) != []


def test_workspace_path_must_be_isolated_worktree() -> None:
    rec = _valid_record()
    # a parent-tree checkout path, not a .claude/worktrees/agent- worktree
    rec["workspace_observation"]["path"] = "/repo/main-checkout"
    assert _errors(_doc([rec])) != []


def test_telemetry_null_rejected_not_captured_and_number_allowed() -> None:
    rec = _valid_record()
    rec["telemetry"]["duration_ms"] = None
    assert _errors(_doc([rec])) != []

    rec2 = _valid_record()
    rec2["telemetry"]["subagent_tokens"] = "not_captured"
    assert _errors(_doc([rec2])) == []

    rec3 = _valid_record()
    rec3["telemetry"]["tool_uses"] = 7
    assert _errors(_doc([rec3])) == []


def test_telemetry_arbitrary_string_rejected() -> None:
    rec = _valid_record()
    rec["telemetry"]["duration_ms"] = "fast"
    assert _errors(_doc([rec])) != []


def test_unknown_owner_capability_fails_crosscheck() -> None:
    rec = _valid_record()
    rec["owner_capability"] = "not_a_capability"
    problems = checker.cross_check(_doc([rec]), checker.registry_executors())
    assert any("not in PROJECT_CAPABILITIES" in p for p in problems)


def test_agent_type_must_match_registry() -> None:
    rec = _valid_record()
    rec["agent_type"] = "Explore"  # schema-valid, but registry says Plan
    problems = checker.cross_check(_doc([rec]), checker.registry_executors())
    assert any("!= registry" in p for p in problems)


def test_defect_outcome_requires_defect_ref() -> None:
    rec = _valid_record()
    rec["outcome"] = "defect"
    rec["defect_ref"] = None
    problems = checker.cross_check(_doc([rec]), checker.registry_executors())
    assert any("defect_ref" in p for p in problems)


def test_commissioning_doc_enforces_min_records_owners_and_scenarios() -> None:
    doc = _doc([_valid_record()], generated_for="commissioning PR test")
    problems = checker.acceptance_check(doc)
    assert any(">= 15" in p for p in problems)
    assert any("distinct owners" in p for p in problems)
    assert any("scenario coverage" in p for p in problems)


def test_acceptance_gate_applies_by_filename_not_only_free_text(tmp_path: Path) -> None:
    # A file named like a dispatch-records file gets the gate even when
    # `generated_for` does not contain the word "commissioning".
    p = tmp_path / "subagent_dispatch_records_x.json"
    p.write_text("{}", encoding="utf-8")
    assert checker.acceptance_gate_applies(p, {"generated_for": "routine capture"})
    # An unrelated filename only gets the gate via the free-text signal.
    q = tmp_path / "something_else.json"
    q.write_text("{}", encoding="utf-8")
    assert not checker.acceptance_gate_applies(q, {"generated_for": "routine capture"})
    assert checker.acceptance_gate_applies(q, {"generated_for": "commissioning run"})


def test_check_file_returns_problems_and_doc() -> None:
    problems, doc = checker.check_file(
        EVIDENCE_PATH, _schema(), checker.registry_executors()
    )
    assert problems == [], f"commissioning evidence must be clean: {problems}"
    assert isinstance(doc, dict) and len(doc["records"]) >= 15


def test_committed_commissioning_evidence_passes_full_linter() -> None:
    assert EVIDENCE_PATH.is_file(), "commissioning evidence file must exist"
    problems, _ = checker.check_file(
        EVIDENCE_PATH, _schema(), checker.registry_executors()
    )
    assert problems == [], f"commissioning evidence must be clean: {problems}"
