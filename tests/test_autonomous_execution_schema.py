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
