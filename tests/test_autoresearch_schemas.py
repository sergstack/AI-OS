"""Focused schema tests for AIOS AutoResearch v0.1 (issue #391, parent #388).

Covers: eval case, experiment record, and frozen batch/eval manifest schemas,
plus their canonical fixtures. Structure only -- no runner, no provider call,
no candidate mutation is exercised here.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = REPO_ROOT / "schemas"
FIXTURES = REPO_ROOT / "tests" / "fixtures" / "autoresearch"
MANIFEST_PATH = REPO_ROOT / "docs" / "standards" / "autoresearch_v01_manifest.json"

EVAL_CASE_SCHEMA = SCHEMAS / "autoresearch_eval_case.schema.json"
EXPERIMENT_SCHEMA = SCHEMAS / "autoresearch_experiment_record.schema.json"
BATCH_MANIFEST_SCHEMA = SCHEMAS / "autoresearch_batch_manifest.schema.json"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _errors(doc: dict, schema: dict) -> list[str]:
    validator = jsonschema.Draft7Validator(schema)
    return [
        f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}"
        for e in sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
    ]


def lineages_disjoint(split_membership: dict) -> list[str]:
    """Pure structural check: issue #391 requires validation/holdout lineages
    to never overlap train lineages. JSON Schema cannot express cross-array
    set constraints, so this is a plain Python check, reused by child #392's
    validator rather than duplicated there."""
    train = set(split_membership.get("train", []))
    problems = []
    for other_split in ("validation", "holdout"):
        overlap = train & set(split_membership.get(other_split, []))
        if overlap:
            problems.append(f"{other_split} overlaps train: {sorted(overlap)}")
    return problems


# ---------------------------------------------------------------------------
# Schema self-validity
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "schema_path", [EVAL_CASE_SCHEMA, EXPERIMENT_SCHEMA, BATCH_MANIFEST_SCHEMA]
)
def test_schema_is_valid_draft7(schema_path: Path) -> None:
    jsonschema.Draft7Validator.check_schema(_load(schema_path))


def test_schema_references_resolve_from_clean_checkout() -> None:
    # No $ref is used across these three schemas (each is self-contained via
    # inline definitions), so "resolves from a clean checkout" reduces to:
    # every schema file parses and compiles as a validator with no I/O.
    for path in (EVAL_CASE_SCHEMA, EXPERIMENT_SCHEMA, BATCH_MANIFEST_SCHEMA):
        jsonschema.Draft7Validator(_load(path))


# ---------------------------------------------------------------------------
# Manifest / schema lockstep (drift detection)
# ---------------------------------------------------------------------------


def test_research_surface_enum_matches_manifest_mutable_surfaces() -> None:
    manifest = _load(MANIFEST_PATH)
    manifest_ids = {s["surface_id"] for s in manifest["mutable_surfaces"]}
    schema = _load(EXPERIMENT_SCHEMA)
    schema_enum = set(schema["properties"]["research_surface"]["enum"])
    assert schema_enum == manifest_ids, (
        "autoresearch_experiment_record.schema.json research_surface enum "
        "has drifted from autoresearch_v01_manifest.json mutable_surfaces"
    )


def test_mutation_class_enum_matches_manifest_allowed_mutation_classes() -> None:
    manifest = _load(MANIFEST_PATH)
    schema = _load(EXPERIMENT_SCHEMA)
    schema_enum = set(
        schema["properties"]["mutation"]["properties"]["mutation_class"]["enum"]
    )
    assert schema_enum == set(manifest["allowed_mutation_classes"])


def test_decision_enum_matches_manifest_decision_semantics() -> None:
    manifest = _load(MANIFEST_PATH)
    schema = _load(EXPERIMENT_SCHEMA)
    schema_enum = set(schema["properties"]["decision"]["enum"])
    assert schema_enum == set(manifest["decision_semantics"].keys())


# ---------------------------------------------------------------------------
# Positive fixtures validate
# ---------------------------------------------------------------------------


def test_eval_case_valid_train_fixture_passes() -> None:
    doc = _load(FIXTURES / "eval_case_valid_train.json")
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) == []


def test_eval_case_valid_holdout_fixture_passes() -> None:
    doc = _load(FIXTURES / "eval_case_valid_holdout.json")
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) == []
    assert "input" not in doc, "holdout fixture must not carry inline payload"
    assert doc["input_ref"]


@pytest.mark.parametrize(
    "fixture_name",
    [
        "experiment_record_valid_keep_candidate.json",
        "experiment_record_valid_discard.json",
        "experiment_record_valid_inconclusive.json",
    ],
)
def test_experiment_record_valid_fixtures_pass(fixture_name: str) -> None:
    doc = _load(FIXTURES / fixture_name)
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) == []


def test_batch_manifest_valid_fixture_passes() -> None:
    doc = _load(FIXTURES / "batch_manifest_valid.json")
    assert _errors(doc, _load(BATCH_MANIFEST_SCHEMA)) == []
    assert lineages_disjoint(doc["split_membership"]) == []


# ---------------------------------------------------------------------------
# Boundary / decision-coverage fixtures cover keep_candidate, discard,
# inconclusive (issue #391 artifact/content acceptance)
# ---------------------------------------------------------------------------


def test_fixtures_cover_all_three_decisions() -> None:
    decisions = set()
    for name in (
        "experiment_record_valid_keep_candidate.json",
        "experiment_record_valid_discard.json",
        "experiment_record_valid_inconclusive.json",
    ):
        decisions.add(_load(FIXTURES / name)["decision"])
    assert decisions == {"keep_candidate", "discard", "inconclusive"}


# ---------------------------------------------------------------------------
# Backward-incompatible fixture fails
# ---------------------------------------------------------------------------


def test_backward_incompatible_eval_case_fails() -> None:
    doc = _load(FIXTURES / "eval_case_backward_incompatible.json")
    assert doc["schema_version"] == "0.0.1"
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) != []


# ---------------------------------------------------------------------------
# Invalid enum values fail
# ---------------------------------------------------------------------------


def test_invalid_case_family_enum_fails() -> None:
    doc = _load(FIXTURES / "eval_case_valid_train.json")
    doc["case_family"] = "not_a_registered_family"
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) != []


def test_invalid_split_enum_fails() -> None:
    doc = _load(FIXTURES / "eval_case_valid_train.json")
    doc["split"] = "test"  # not train/validation/holdout
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) != []


def test_invalid_attribution_status_enum_fails() -> None:
    doc = _load(FIXTURES / "experiment_record_valid_keep_candidate.json")
    doc["attribution_status"] = "confirmed"  # not supported/uncertain/rejected
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) != []


def test_invalid_decision_enum_fails() -> None:
    doc = _load(FIXTURES / "experiment_record_valid_keep_candidate.json")
    doc["decision"] = "accepted"  # not a real decision value
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) != []


def test_unregistered_research_surface_fails() -> None:
    doc = _load(FIXTURES / "experiment_record_valid_keep_candidate.json")
    doc["research_surface"] = "MUT-NOT-IN-MANIFEST"
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) != []


# ---------------------------------------------------------------------------
# Missing identity / missing baseline fail
# ---------------------------------------------------------------------------


def test_missing_case_id_fails() -> None:
    doc = _load(FIXTURES / "eval_case_valid_train.json")
    del doc["case_id"]
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) != []


def test_missing_experiment_id_fails() -> None:
    doc = _load(FIXTURES / "experiment_record_valid_keep_candidate.json")
    del doc["experiment_id"]
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) != []


def test_missing_baseline_revision_fails() -> None:
    doc = _load(FIXTURES / "experiment_record_valid_keep_candidate.json")
    del doc["baseline_revision"]
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) != []


def test_missing_baseline_block_in_batch_manifest_fails() -> None:
    doc = _load(FIXTURES / "batch_manifest_valid.json")
    del doc["baseline"]
    assert _errors(doc, _load(BATCH_MANIFEST_SCHEMA)) != []


# ---------------------------------------------------------------------------
# Missing hashes fail
# ---------------------------------------------------------------------------


def test_missing_content_hash_fails() -> None:
    doc = _load(FIXTURES / "eval_case_valid_train.json")
    del doc["content_hash"]
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) != []


def test_malformed_content_hash_fails() -> None:
    doc = _load(FIXTURES / "eval_case_valid_train.json")
    doc["content_hash"] = "not-a-sha256-hash"
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) != []


def test_missing_frozen_hash_fails() -> None:
    doc = _load(FIXTURES / "batch_manifest_valid.json")
    del doc["frozen_hashes"]["evaluator_hash"]
    assert _errors(doc, _load(BATCH_MANIFEST_SCHEMA)) != []


# ---------------------------------------------------------------------------
# Overlapping lineages fail (pure structural check, not schema-expressible)
# ---------------------------------------------------------------------------


def test_overlapping_lineages_detected() -> None:
    doc = _load(FIXTURES / "batch_manifest_valid.json")
    overlapping_lineage = doc["split_membership"]["train"][0]
    doc["split_membership"]["holdout"].append(overlapping_lineage)
    assert lineages_disjoint(doc["split_membership"]) != []
    # the schema itself still accepts the shape (arrays of valid strings);
    # disjointness is enforced by lineages_disjoint, per this module's header.
    assert _errors(doc, _load(BATCH_MANIFEST_SCHEMA)) == []


def test_disjoint_lineages_pass_clean() -> None:
    doc = _load(FIXTURES / "batch_manifest_valid.json")
    assert lineages_disjoint(doc["split_membership"]) == []


# ---------------------------------------------------------------------------
# Illegal authority conversion fails: keep_candidate can never carry
# accepted/merged/production authority (INV-08)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "field,value",
    [
        ("authority_status", "approved"),
        ("merge_status", "merged"),
        ("production_status", "authorized"),
        ("production_status", "deployed"),
    ],
)
def test_keep_candidate_cannot_carry_acceptance_authority(field: str, value: str) -> None:
    doc = _load(FIXTURES / "experiment_record_valid_keep_candidate.json")
    doc[field] = value
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) != [], (
        f"keep_candidate + {field}={value} must be rejected (INV-08)"
    )


def test_supported_attribution_requires_evidence() -> None:
    doc = _load(FIXTURES / "experiment_record_valid_keep_candidate.json")
    doc["attribution_status"] = "supported"
    doc["attribution_evidence"] = []
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) != []


# ---------------------------------------------------------------------------
# Mutable-history / correction_of shape
# ---------------------------------------------------------------------------


def test_correction_of_null_is_valid_for_an_original_record() -> None:
    doc = _load(FIXTURES / "experiment_record_valid_keep_candidate.json")
    assert doc["correction_of"] is None
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) == []


def test_correction_of_must_be_a_well_formed_experiment_id_or_null() -> None:
    doc = _load(FIXTURES / "experiment_record_valid_keep_candidate.json")
    doc["correction_of"] = "not-an-experiment-id"
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) != []

    doc["correction_of"] = "AUTORESEARCH-batch-001-1"
    assert _errors(doc, _load(EXPERIMENT_SCHEMA)) == []


# ---------------------------------------------------------------------------
# Holdout payload exclusion (issue #391: holdout payload must not appear
# in Researcher-readable fixtures; only IDs/hashes/refs are allowed)
# ---------------------------------------------------------------------------


def test_holdout_case_with_inline_input_is_rejected() -> None:
    doc = _load(FIXTURES / "eval_case_valid_holdout.json")
    doc["input"] = "leaked holdout payload"
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) != []


def test_case_with_both_input_and_input_ref_is_rejected() -> None:
    doc = _load(FIXTURES / "eval_case_valid_train.json")
    doc["input_ref"] = "ar://also-a-ref"
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) != []


def test_case_with_neither_input_nor_input_ref_is_rejected() -> None:
    doc = _load(FIXTURES / "eval_case_valid_train.json")
    del doc["input"]
    assert _errors(doc, _load(EVAL_CASE_SCHEMA)) != []


def test_no_committed_fixture_leaks_holdout_payload() -> None:
    """Deterministic repository-wide guard: scan every committed AutoResearch
    fixture for a holdout-split case carrying an inline 'input' field."""
    for path in sorted(FIXTURES.glob("*.json")):
        doc = _load(path)
        if doc.get("split") == "holdout":
            assert "input" not in doc, f"{path} leaks holdout payload inline"
