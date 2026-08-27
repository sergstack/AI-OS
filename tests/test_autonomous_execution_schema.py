"""Structural conformance tests for the current AES execution-record schema."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft7Validator


ROOT = Path(__file__).resolve().parents[1]
CURRENT_SCHEMA = json.loads((ROOT / "schemas/autonomous_execution_record.schema.json").read_text())
HISTORICAL_SCHEMA = json.loads((ROOT / "schemas/autonomous_execution_record.v1.schema.json").read_text())


def test_schema_accepts_closure_iteration_limit_terminal_reason():
    validator = Draft7Validator(CURRENT_SCHEMA["properties"]["terminal_reason"])
    assert not list(validator.iter_errors("closure_iteration_limit_reached"))


def test_schema_accepts_continuation_no_progress_terminal_reason():
    validator = Draft7Validator(CURRENT_SCHEMA["properties"]["terminal_reason"])
    assert not list(validator.iter_errors("continuation_no_progress_limit_reached"))


def test_schema_rejects_unknown_terminal_reason():
    validator = Draft7Validator(CURRENT_SCHEMA["properties"]["terminal_reason"])
    errors = list(validator.iter_errors("made_up"))
    assert errors


def test_canonical_examples_conform_to_historical_schema_contract():
    validator = Draft7Validator(HISTORICAL_SCHEMA)
    examples = ROOT.glob("docs/autonomous_execution/examples/*.json")

    for example in examples:
        record = json.loads(example.read_text())
        errors = list(validator.iter_errors(record))
        assert not errors, f"{example}: {errors[0].message}"


def test_current_contract_rejects_a_new_v1_success_record_without_closure_review():
    errors = list(Draft7Validator(CURRENT_SCHEMA).iter_errors({
        "schema_version": "1.0.0",
        "standard_version": "1.0.0",
        "overall_delivery": "pass",
    }))
    paths = {tuple(error.absolute_path) for error in errors}
    assert ("schema_version",) in paths
    assert ("standard_version",) in paths
    assert () in paths  # closure_review is required at the record root


def test_continuation_envelope_requires_durable_resume_state():
    validator = Draft7Validator(CURRENT_SCHEMA["definitions"]["continuation"])
    continuation = {
        "original_goal": "Continue the original AI-OS execution.",
        "original_acceptance_criteria": ["original goal is rechecked"],
        "resolved_owner": "[AI OS]",
        "resume_stage": "owner_execution",
        "record_ref": "docs/autonomous_execution/records/exec-fixture.json",
        "scope_ref": "scope:fixture",
        "routing_state_ref": "routing:fixture",
        "source_revision": "rev-b",
        "goal_boundary_hash": "sha256:" + "a" * 64,
        "acceptance_criteria_hash": "sha256:" + "b" * 64,
        "state_hash": "sha256:" + "c" * 64,
        "updated_at": "2026-01-01T01:00:00Z",
    }
    assert not list(validator.iter_errors(continuation))

    record_errors = list(Draft7Validator(CURRENT_SCHEMA).iter_errors({
        "continuation": continuation,
    }))
    assert not any(tuple(error.absolute_path)[:1] == ("continuation",) for error in record_errors)

    del continuation["record_ref"]
    assert list(validator.iter_errors(continuation))


def test_continuation_control_plane_fields_are_additive_and_allow_unset_thresholds():
    validator = Draft7Validator(CURRENT_SCHEMA["definitions"]["continuation"])
    continuation = {
        "original_goal": "Continue the original AI-OS execution.",
        "original_acceptance_criteria": ["original goal is rechecked"],
        "resolved_owner": "[AI OS]",
        "resume_stage": "owner_execution",
        "record_ref": "docs/autonomous_execution/records/exec-fixture.json",
        "scope_ref": "scope:fixture",
        "routing_state_ref": "routing:fixture",
        "source_revision": "rev-b",
        "goal_boundary_hash": "sha256:" + "a" * 64,
        "acceptance_criteria_hash": "sha256:" + "b" * 64,
        "state_hash": "sha256:" + "c" * 64,
        "updated_at": "2026-01-01T01:00:00Z",
        "route_trace": [{
            "route_id": "route-001", "from_owner": "[AI OS]", "to_owner": "[Codex]",
            "resume_stage": "owner_execution", "criteria_addressed": ["original goal is rechecked"],
            "route_signature": "aios:codex", "evidence_delta": ["implementation_feedback"],
            "outcome": "completed", "refusal_reason": None, "evidence_refs": [],
        }],
        "progress": {"satisfied_criteria": [], "remaining_criteria": ["original goal is rechecked"], "last_real_progress_route_id": None, "evidence_refs": []},
        "guards": {"max_continuation_hops": None, "max_retries_per_owner": None, "max_no_progress_hops": None, "route_signature_history_window": None, "tripped_guard": None, "tripped_guards": [], "terminal_report_ref": None},
    }
    assert not list(validator.iter_errors(continuation))
