"""Focused tests for the AIOS AutoResearch v0.2 live-execution/privacy/
budget/evidence contract (issue #411, parent #409). No live model/provider/
Judge call anywhere in this module.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schemas" / "autoresearch_v02_live_batch_config.schema.json"
AUTHORITY_MATRIX_PATH = REPO_ROOT / "docs" / "standards" / "autoresearch_v02_authority_matrix.json"
CONTRACT_DOC = REPO_ROOT / "docs" / "standards" / "AUTORESEARCH_V02_LIVE_CONTRACT.md"

_spec = importlib.util.spec_from_file_location(
    "autoresearch_v02_live_contract_validator", REPO_ROOT / "scripts" / "autoresearch_v02_live_contract_validator.py"
)
lc = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = lc
_spec.loader.exec_module(lc)

av = lc.av
jsonschema = pytest.importorskip("jsonschema")


def _load_authority_matrix() -> dict:
    return json.loads(AUTHORITY_MATRIX_PATH.read_text(encoding="utf-8"))


def _base_batch_config(**overrides) -> dict:
    doc = {
        "contract_version": "0.2.0",
        "execution_mode": "repo_replay",
        "transport_id": "playwright_mcp",
        "transport_version": "latest",
        "credential_source_class": "browser_session_cookie",
        "transport_authority_status": "not_authorized",
        "provider": "openai_chatgpt_ui",
        "model": "gpt-unknown",
        "model_version_or_snapshot": "not_captured",
        "runtime_version": "not_captured",
        "context_manifest_hash": None,
        "evaluator_contract_hash": None,
        "evaluator_model_identity": None,
        "sampling_configuration": {},
        "max_provider_calls": None,
        "max_input_tokens": "not_captured",
        "max_output_tokens": "not_captured",
        "max_wall_clock_minutes": None,
        "max_cost_amount": None,
        "max_cost_currency": None,
        "retry_limit": 2,
        "call_timeout_seconds": 120,
        "redaction_policy_ref": "AUTORESEARCH_V02_LIVE_CONTRACT.md#8-privacy-redaction-retention-and-forbidden-input-rules",
        "raw_payload_retention": "sanitized_excerpt_only",
        "usage_metadata_policy": "estimated_disallowed",
        "field_trace_provenance": "none",
        "live_evidence_required": False,
        "synthetic_evidence_allowed_for": ["unit_test"],
        "abort_conditions": ["no_authorized_reproducible_live_transport"],
        "authority_status": "owner_review_pending",
        "subject_context_scope": "non_project_controlled",
        "memory_personalization_isolation_status": "verified_disabled",
    }
    doc.update(overrides)
    return doc


# ---------------------------------------------------------------------------
# Schema self-validity and structural completeness
# ---------------------------------------------------------------------------


def test_batch_config_schema_is_valid_draft7():
    jsonschema.Draft7Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))


def test_unauthorized_pending_batch_is_valid():
    assert lc.validate_batch_config(_base_batch_config()) == []


def test_all_required_fields_are_present_in_schema():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    required_from_issue = {
        "contract_version", "execution_mode", "transport_id", "transport_version",
        "credential_source_class", "transport_authority_status", "provider", "model",
        "model_version_or_snapshot", "runtime_version", "context_manifest_hash",
        "evaluator_contract_hash", "evaluator_model_identity", "sampling_configuration",
        "max_provider_calls", "max_input_tokens", "max_output_tokens", "max_wall_clock_minutes",
        "max_cost_amount", "max_cost_currency", "retry_limit", "call_timeout_seconds",
        "redaction_policy_ref", "raw_payload_retention", "usage_metadata_policy",
        "field_trace_provenance", "live_evidence_required", "synthetic_evidence_allowed_for",
        "abort_conditions", "authority_status",
    }
    assert required_from_issue.issubset(set(schema["required"]))


# ---------------------------------------------------------------------------
# "authorized requires a positive numeric budget" -- the core fail-closed rule
# ---------------------------------------------------------------------------


def test_authorized_without_positive_cost_amount_rejected():
    doc = _base_batch_config(authority_status="authorized", max_cost_amount=None, max_provider_calls=5)
    findings = lc.validate_batch_config(doc)
    assert any(f.rule == "UNBUDGETED_AUTHORIZATION" for f in findings)


def test_authorized_with_zero_cost_amount_rejected():
    doc = _base_batch_config(authority_status="authorized", max_cost_amount=0, max_cost_currency="USD", max_provider_calls=5)
    findings = lc.validate_batch_config(doc)
    assert any(f.rule == "UNBUDGETED_AUTHORIZATION" for f in findings)


def test_authorized_without_currency_rejected():
    doc = _base_batch_config(authority_status="authorized", max_cost_amount=5.0, max_cost_currency=None, max_provider_calls=5)
    findings = lc.validate_batch_config(doc)
    assert any(f.rule == "UNBUDGETED_AUTHORIZATION" for f in findings)


def test_authorized_without_call_cap_rejected():
    doc = _base_batch_config(authority_status="authorized", max_cost_amount=5.0, max_cost_currency="USD", max_provider_calls=None)
    findings = lc.validate_batch_config(doc)
    assert any(f.rule == "UNBOUNDED_AUTHORIZATION" for f in findings)


def test_fully_authorized_and_budgeted_batch_is_valid():
    doc = _base_batch_config(
        authority_status="authorized", transport_authority_status="authorized",
        max_cost_amount=5.0, max_cost_currency="USD", max_provider_calls=5,
    )
    assert lc.validate_batch_config(doc) == []


def test_transport_authority_status_authorized_also_triggers_budget_check():
    # authority_status stays owner_review_pending, but transport_authority_status
    # alone flipping to authorized must still require a real budget --
    # neither field alone is allowed to bypass the rule.
    doc = _base_batch_config(transport_authority_status="authorized", max_cost_amount=None)
    findings = lc.validate_batch_config(doc)
    assert any(f.rule == "UNBUDGETED_AUTHORIZATION" for f in findings)


# ---------------------------------------------------------------------------
# Available credential/transport does not itself authorize (no implicit
# conversion)
# ---------------------------------------------------------------------------


def test_configured_transport_without_authority_status_stays_unauthorized():
    doc = _base_batch_config(transport_authority_status="authorized_pending_budget")
    findings = lc.validate_batch_config(doc)
    assert findings == []  # structurally valid -- pending is not itself an error
    assert doc["authority_status"] == "owner_review_pending"  # never silently promoted


# ---------------------------------------------------------------------------
# Unaudited transport is rejected
# ---------------------------------------------------------------------------


def test_unaudited_transport_rejected():
    doc = _base_batch_config(transport_id="some_random_sdk_nobody_audited")
    findings = lc.validate_batch_config(doc)
    assert any(f.rule == "UNAUDITED_TRANSPORT" for f in findings)


@pytest.mark.parametrize("transport_id", sorted(lc.AUDITED_TRANSPORT_IDS))
def test_every_audited_transport_is_individually_accepted(transport_id):
    doc = _base_batch_config(transport_id=transport_id)
    findings = lc.validate_batch_config(doc)
    assert not any(f.rule == "UNAUDITED_TRANSPORT" for f in findings)


# ---------------------------------------------------------------------------
# raw_restricted field traces cannot claim retention
# ---------------------------------------------------------------------------


def test_raw_restricted_requires_not_retained():
    doc = _base_batch_config(field_trace_provenance="raw_restricted", raw_payload_retention="sanitized_excerpt_only")
    findings = lc.validate_batch_config(doc)
    assert findings != []  # schema's own allOf conditional catches this


def test_raw_restricted_with_not_retained_is_valid():
    doc = _base_batch_config(field_trace_provenance="raw_restricted", raw_payload_retention="not_retained")
    assert lc.validate_batch_config(doc) == []


def test_field_reproduction_requires_sanitized_or_raw_restricted_provenance():
    doc = _base_batch_config(execution_mode="field_reproduction", field_trace_provenance="none")
    findings = lc.validate_batch_config(doc)
    assert findings != []


def test_field_reproduction_with_sanitized_provenance_is_valid():
    doc = _base_batch_config(execution_mode="field_reproduction", field_trace_provenance="sanitized")
    assert lc.validate_batch_config(doc) == []


# ---------------------------------------------------------------------------
# Judge findings still cannot carry authority/merge/production fields
# (re-confirms #394's guarantee holds under the new contract)
# ---------------------------------------------------------------------------


def test_semantic_finding_schema_still_rejects_authority_fields():
    finding = {
        "schema_version": "0.1.0", "case_id": "C1", "case_family": "routing",
        "finding": "x", "evidence": "y", "severity": "low",
        "affected_invariant_or_metric": "z", "verdict": "pass",
        "confidence": "high", "limitations": "none",
        "authority_status": "approved",
    }
    assert av.validate_semantic_finding(finding) != []


# ---------------------------------------------------------------------------
# Authority matrix structural checks
# ---------------------------------------------------------------------------


def test_authority_matrix_has_all_seven_required_authorities():
    doc = _load_authority_matrix()
    assert lc.validate_authority_matrix(doc) == []
    assert set(doc["authorities"]) == lc.REQUIRED_AUTHORITIES


def test_merge_production_active_config_authority_are_not_granted():
    doc = _load_authority_matrix()
    for name in ("merge_authority", "production_authority", "active_configuration_authority"):
        assert doc["authorities"][name]["level"] == "not_granted"


def test_live_call_and_usage_budget_authority_are_owner_only():
    doc = _load_authority_matrix()
    assert doc["authorities"]["live_call_authority"]["level"] == "owner_only"
    assert doc["authorities"]["usage_budget_authority"]["level"] == "owner_only"


def test_authority_matrix_missing_authority_rejected():
    doc = _load_authority_matrix()
    doc = dict(doc)
    doc["authorities"] = dict(doc["authorities"])
    del doc["authorities"]["merge_authority"]
    findings = lc.validate_authority_matrix(doc)
    assert any(f.rule == "MISSING_AUTHORITY" for f in findings)


def test_authority_matrix_regression_rejected():
    doc = _load_authority_matrix()
    doc = json.loads(json.dumps(doc))  # deep copy
    doc["authorities"]["merge_authority"]["level"] = "bounded_delegate"
    findings = lc.validate_authority_matrix(doc)
    assert any(f.rule == "AUTHORITY_REGRESSION" for f in findings)


def test_authority_matrix_invalid_level_rejected():
    doc = json.loads(json.dumps(_load_authority_matrix()))
    doc["authorities"]["implementation_authority"]["level"] = "always_allowed"
    findings = lc.validate_authority_matrix(doc)
    assert any(f.rule == "INVALID_AUTHORITY_LEVEL" for f in findings)


# ---------------------------------------------------------------------------
# Contract document structural completeness
# ---------------------------------------------------------------------------

REQUIRED_SECTIONS = [
    "## 1–3. Evidence states, transport identity, evaluator identity",
    "## 4. Context-pack identity and source-revision requirements",
    "## 5. External-action preview/authority/commit/verify sequence",
    "## 6. Call/token/time/cost budget contract",
    "## 7. Retry and cancellation policy",
    "## 8. Privacy, redaction, retention, and forbidden-input rules",
    "## 9. Live versus synthetic evidence labels",
    "## 10. Researcher/evaluator/controller/owner authority boundaries",
    "## 11. Reproducibility and model/provider drift rules",
    "## 12. Acceptable limitations when exact UI-runtime reproduction is unavailable",
    "## 13. Hard stop conditions",
    "## 14. Rollback/evidence-preservation ownership",
    "## 15. Phase 0/Phase 1 authorization boundary",
    "## 16. Compatibility map to v0.1 schemas, manifests, and hard invariants",
]


def test_contract_document_has_all_required_sections():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    assert missing == [], f"contract doc is missing required sections: {missing}"


def test_contract_document_is_candidate_not_authorized():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    assert "Status: `candidate`" in text
    assert "Not authorized for any live call" in text


def test_contract_document_names_no_default_paid_budget():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    assert "never a fabricated default" in text


def test_contract_document_cites_v01_reuse_not_restatement():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    for cited in (
        "AUTORESEARCH_V01_CONTRACT.md",
        "autoresearch_v01_manifest.json",
        "FAILURE_REGISTRY.md",
    ):
        assert cited in text
