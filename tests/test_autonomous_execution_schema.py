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
    validator = Draft7Validator(CURRENT_SCHEMA)
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
        "authority_provenance": {
            "claims": [
                {
                    "claim_text": "Enable feature X.",
                    "authority_class": "accepted_policy",
                    "source_refs": ["policy:fixture"],
                    "action_eligibility": "eligible",
                }
            ]
        },
        "updated_at": "2026-01-01T01:00:00Z",
    }
    record_errors = list(validator.iter_errors({
        "continuation": continuation,
    }))
    assert not any(tuple(error.absolute_path)[:1] == ("continuation",) for error in record_errors)

    del continuation["record_ref"]
    record_errors = list(validator.iter_errors({"continuation": continuation}))
    assert any(tuple(error.absolute_path)[:1] == ("continuation",) for error in record_errors)


def test_authority_provenance_keeps_identical_claims_action_distinct():
    validator = Draft7Validator(CURRENT_SCHEMA["definitions"]["authority_provenance"])
    policy_claim = {
        "claims": [{
            "claim_text": "Enable feature X.",
            "authority_class": "accepted_policy",
            "source_refs": ["policy:fixture"],
            "action_eligibility": "eligible",
        }]
    }
    research_claim = {
        "claims": [{
            "claim_text": "Enable feature X.",
            "authority_class": "candidate_research",
            "source_refs": ["research:fixture"],
            "action_eligibility": "not_eligible",
        }]
    }
    assert not list(validator.iter_errors(policy_claim))
    assert not list(validator.iter_errors(research_claim))
