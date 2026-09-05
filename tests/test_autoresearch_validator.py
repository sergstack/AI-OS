"""Focused tests for the AIOS AutoResearch v0.1 validator/hard-veto engine/
ledger/comparator (issue #392, parent #388).

No provider call, no experiment execution, no worktree mutation is exercised
here -- every fixture is a static, already-produced record.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = REPO_ROOT / "tests" / "fixtures" / "autoresearch"

_spec = importlib.util.spec_from_file_location(
    "autoresearch_validator", REPO_ROOT / "scripts" / "autoresearch_validator.py"
)
av = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = av  # dataclasses needs the module registered before exec
_spec.loader.exec_module(av)


def _load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


@pytest.fixture()
def manifest() -> dict:
    return av.load_manifest()


@pytest.fixture()
def batch_manifest() -> dict:
    return _load("batch_manifest_valid.json")


@pytest.fixture()
def keep_record() -> dict:
    return _load("experiment_record_valid_keep_candidate.json")


@pytest.fixture()
def discard_record() -> dict:
    return _load("experiment_record_valid_discard.json")


@pytest.fixture()
def inconclusive_record() -> dict:
    return _load("experiment_record_valid_inconclusive.json")


# ---------------------------------------------------------------------------
# valid keep/discard/inconclusive records pass
# ---------------------------------------------------------------------------


def test_valid_keep_candidate_record_passes(keep_record, manifest, batch_manifest):
    assert av.validate_experiment_record(keep_record, manifest, batch_manifest) == []


def test_valid_discard_record_passes(discard_record, manifest, batch_manifest):
    assert av.validate_experiment_record(discard_record, manifest, batch_manifest) == []


def test_valid_inconclusive_record_passes(inconclusive_record, manifest, batch_manifest):
    assert av.validate_experiment_record(inconclusive_record, manifest, batch_manifest) == []


def test_valid_eval_cases_pass(manifest):
    for name in ("eval_case_valid_train.json", "eval_case_valid_holdout.json"):
        assert av.validate_eval_case(_load(name)) == []


def test_valid_batch_manifest_passes():
    assert av.validate_batch_manifest(_load("batch_manifest_valid.json")) == []


# ---------------------------------------------------------------------------
# content hash / baseline verification
# ---------------------------------------------------------------------------


def test_tampered_eval_case_content_fails_hash_check():
    doc = _load("eval_case_valid_train.json")
    doc["input"] = doc["input"] + " (silently altered)"
    findings = av.validate_eval_case(doc)
    assert any(f.rule == "CONTENT_HASH_MISMATCH" for f in findings)


def test_missing_baseline_revision_fails(keep_record, manifest, batch_manifest):
    del keep_record["baseline_revision"]
    findings = av.validate_experiment_record(keep_record, manifest, batch_manifest)
    assert findings != []  # schema-level: required field


def test_baseline_revision_mismatch_rejected(keep_record, manifest, batch_manifest):
    keep_record["baseline_revision"] = "0" * 7
    findings = av.reject_environment_mismatch(keep_record, batch_manifest)
    assert any(f.rule == "INV-09" for f in findings)


# ---------------------------------------------------------------------------
# protected-path mutation fails
# ---------------------------------------------------------------------------


def test_protected_path_in_affected_scope_rejected(keep_record, manifest):
    keep_record["affected_scope"].append("PROT-ROUTING-DESTINATIONS")
    findings = av.reject_protected_surface_touch(keep_record, manifest)
    assert any(f.rule == "INV-01" and f.consequence == "discard" for f in findings)


def test_unregistered_research_surface_rejected(keep_record, manifest):
    keep_record["research_surface"] = "MUT-DOES-NOT-EXIST"
    # schema rejects it first (closed enum); prove the deterministic layer
    # would also catch it if the enum were ever loosened.
    findings = av.reject_protected_surface_touch(keep_record, manifest)
    assert any(f.rule == "INV-01" for f in findings)


# ---------------------------------------------------------------------------
# evaluator hash mismatch invalidates batch
# ---------------------------------------------------------------------------


def test_evaluator_hash_mismatch_invalidates_batch(keep_record, batch_manifest):
    keep_record["eval_manifest"]["evaluator_hash"] = "0" * 64
    findings = av.reject_environment_mismatch(keep_record, batch_manifest)
    assert any(f.rule == "INV-03" and f.consequence == "batch_invalidated" for f in findings)


# ---------------------------------------------------------------------------
# two independent mutations fail
# ---------------------------------------------------------------------------


def test_two_independent_mutations_rejected(keep_record, manifest):
    # research_surface declares the routing tie-break surface; also touching
    # the AI OS PROJECT_INSTRUCTIONS.md handoff surface is a second mechanism.
    keep_record["affected_scope"].append("ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md#7")
    findings = av.reject_multi_mechanism(keep_record, manifest)
    assert any(f.rule == "INV-05" for f in findings)


def test_single_mechanism_within_declared_surface_passes(keep_record, manifest):
    assert av.reject_multi_mechanism(keep_record, manifest) == []


# ---------------------------------------------------------------------------
# NOT RUN -> PASS fails
# ---------------------------------------------------------------------------


def test_not_run_gate_with_keep_candidate_rejected(keep_record):
    keep_record["hard_gate_results"].append(
        {"invariant_id": "INV-02", "status": "not_run", "detail": "gate skipped"}
    )
    findings = av.reject_not_run_as_pass(keep_record)
    assert any(f.rule == "NOT_RUN_NE_PASS" for f in findings)


def test_not_run_gate_with_discard_is_fine(discard_record):
    discard_record["hard_gate_results"].append(
        {"invariant_id": "INV-02", "status": "not_run", "detail": "gate skipped"}
    )
    assert av.reject_not_run_as_pass(discard_record) == []


# ---------------------------------------------------------------------------
# Judge pass -> approved/merge-ready/production-authorized fails
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "field,value",
    [
        ("authority_status", "approved"),
        ("merge_status", "merged"),
        ("merge_status", "merge_ready"),
        ("production_status", "authorized"),
        ("production_status", "deployed"),
    ],
)
def test_researcher_record_cannot_claim_acceptance_authority(keep_record, field, value):
    keep_record[field] = value
    findings = av.reject_authority_escalation(keep_record)
    assert any(f.rule == "INV-08" for f in findings)


def test_valid_record_authority_ceiling_respected(keep_record, discard_record, inconclusive_record):
    for rec in (keep_record, discard_record, inconclusive_record):
        assert av.reject_authority_escalation(rec) == []


# ---------------------------------------------------------------------------
# hard veto dominates aggregate improvement
# ---------------------------------------------------------------------------


def test_hard_veto_dominates_improvement_delta(keep_record):
    # even though behavioral_results.delta says "improvement", a violated
    # hard gate must force discard, not keep_candidate.
    assert keep_record["behavioral_results"]["delta"] == "improvement"
    keep_record["hard_gate_results"].append(
        {"invariant_id": "INV-01", "status": "violated", "detail": "touched a protected surface"}
    )
    findings = av.enforce_hard_veto_dominance(keep_record)
    assert any(f.rule == "HARD_VETO_DOMINANCE" for f in findings)


def test_hard_veto_with_correct_discard_decision_passes():
    doc = _load("experiment_record_valid_discard.json")
    assert any(g["status"] == "violated" for g in doc["hard_gate_results"])
    assert doc["decision"] == "discard"
    assert av.enforce_hard_veto_dominance(doc) == []


def test_integrity_event_without_discard_rejected(keep_record):
    keep_record["integrity_events"].append(
        {"invariant_id": "INV-04", "description": "ledger append-only violation observed"}
    )
    findings = av.enforce_hard_veto_dominance(keep_record)
    assert any(f.rule == "HARD_VETO_DOMINANCE" for f in findings)


# ---------------------------------------------------------------------------
# infrastructure failure maps to inconclusive, not a behavioral pass
# ---------------------------------------------------------------------------


def test_unmeasured_efficiency_with_keep_candidate_rejected(keep_record):
    keep_record["efficiency_results"]["measured"] = False
    findings = av.infra_failure_maps_to_inconclusive(keep_record)
    assert any(f.rule == "INFRA_FAILURE_NOT_DEGRADATION" for f in findings)


def test_unmeasured_efficiency_with_inconclusive_is_fine(inconclusive_record):
    inconclusive_record["efficiency_results"]["measured"] = False
    assert av.infra_failure_maps_to_inconclusive(inconclusive_record) == []


# ---------------------------------------------------------------------------
# causal attribution (INV-06)
# ---------------------------------------------------------------------------


def test_rejected_attribution_with_keep_candidate_rejected(keep_record):
    keep_record["attribution_status"] = "rejected"
    findings = av.validate_attribution(keep_record)
    assert any(f.rule == "INV-06" and f.consequence == "discard" for f in findings)


def test_uncertain_attribution_with_keep_candidate_flags_human_review(keep_record):
    keep_record["attribution_status"] = "uncertain"
    findings = av.validate_attribution(keep_record)
    assert any(f.rule == "INV-06" and f.consequence == "human_review_required" for f in findings)


# ---------------------------------------------------------------------------
# split-lineage overlap fails
# ---------------------------------------------------------------------------


def test_split_lineage_overlap_rejected(batch_manifest):
    lineage = batch_manifest["split_membership"]["train"][0]
    batch_manifest["split_membership"]["holdout"].append(lineage)
    findings = av.validate_batch_manifest(batch_manifest)
    assert any(f.rule == "SPLIT_LINEAGE_OVERLAP" for f in findings)


# ---------------------------------------------------------------------------
# append-only ledger: edit/delete/reorder fails; valid appends pass
# ---------------------------------------------------------------------------


def test_ledger_append_accepts_valid_records_in_sequence(tmp_path, manifest, batch_manifest, keep_record, discard_record):
    ledger = tmp_path / "ledger.jsonl"
    assert av.ledger_append(ledger, keep_record, manifest, batch_manifest) == []
    assert av.ledger_append(ledger, discard_record, manifest, batch_manifest) == []
    assert av.verify_ledger(ledger) == []
    lines = av.read_ledger(ledger)
    assert [line["record"]["experiment_id"] for line in lines] == [
        keep_record["experiment_id"],
        discard_record["experiment_id"],
    ]


def test_ledger_rejects_invalid_record_and_does_not_write(tmp_path, manifest, batch_manifest, keep_record):
    ledger = tmp_path / "ledger.jsonl"
    keep_record["authority_status"] = "approved"  # illegal escalation
    findings = av.ledger_append(ledger, keep_record, manifest, batch_manifest)
    assert findings != []
    assert not ledger.exists() or av.read_ledger(ledger) == []


def test_ledger_detects_in_place_edit(tmp_path, manifest, batch_manifest, keep_record):
    ledger = tmp_path / "ledger.jsonl"
    av.ledger_append(ledger, keep_record, manifest, batch_manifest)
    lines = ledger.read_text(encoding="utf-8").splitlines()
    tampered = json.loads(lines[0])
    tampered["record"]["decision_basis"] = "silently rewritten"
    lines[0] = json.dumps(tampered)
    ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
    findings = av.verify_ledger(ledger)
    assert any(f.rule == "LEDGER_TAMPERED" for f in findings)


def test_ledger_detects_deleted_line(tmp_path, manifest, batch_manifest, keep_record, discard_record, inconclusive_record):
    ledger = tmp_path / "ledger.jsonl"
    av.ledger_append(ledger, keep_record, manifest, batch_manifest)
    av.ledger_append(ledger, discard_record, manifest, batch_manifest)
    av.ledger_append(ledger, inconclusive_record, manifest, batch_manifest)
    lines = ledger.read_text(encoding="utf-8").splitlines()
    del lines[1]  # delete the middle line
    ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
    findings = av.verify_ledger(ledger)
    assert any(f.rule in ("LEDGER_TAMPERED", "LEDGER_REORDERED") for f in findings)


def test_ledger_detects_reordering(tmp_path, manifest, batch_manifest, keep_record, discard_record):
    ledger = tmp_path / "ledger.jsonl"
    av.ledger_append(ledger, keep_record, manifest, batch_manifest)
    av.ledger_append(ledger, discard_record, manifest, batch_manifest)
    lines = ledger.read_text(encoding="utf-8").splitlines()
    lines[0], lines[1] = lines[1], lines[0]
    ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
    findings = av.verify_ledger(ledger)
    assert findings != []


def test_duplicate_experiment_id_without_correction_rejected(tmp_path, manifest, batch_manifest, keep_record):
    ledger = tmp_path / "ledger.jsonl"
    av.ledger_append(ledger, keep_record, manifest, batch_manifest)
    dup = copy.deepcopy(keep_record)  # same experiment_id, no correction_of
    findings = av.ledger_append(ledger, dup, manifest, batch_manifest)
    assert any(f.rule == "DUPLICATE_WITHOUT_CORRECTION" for f in findings)


def test_correction_with_valid_target_accepted(tmp_path, manifest, batch_manifest, keep_record):
    ledger = tmp_path / "ledger.jsonl"
    av.ledger_append(ledger, keep_record, manifest, batch_manifest)
    correction = copy.deepcopy(keep_record)
    correction["experiment_id"] = "AUTORESEARCH-batch-001-9"
    correction["correction_of"] = keep_record["experiment_id"]
    assert av.ledger_append(ledger, correction, manifest, batch_manifest) == []


def test_correction_with_dangling_target_rejected(tmp_path, manifest, batch_manifest, keep_record):
    ledger = tmp_path / "ledger.jsonl"
    correction = copy.deepcopy(keep_record)
    correction["experiment_id"] = "AUTORESEARCH-batch-001-9"
    correction["correction_of"] = "AUTORESEARCH-batch-001-999"  # never appended
    findings = av.ledger_append(ledger, correction, manifest, batch_manifest)
    assert any(f.rule == "CORRECTION_WITHOUT_VALID_TARGET" for f in findings)


# ---------------------------------------------------------------------------
# comparison artifact: no scalar weighted score
# ---------------------------------------------------------------------------


def test_comparison_artifact_has_no_scalar_score(keep_record, batch_manifest):
    artifact = av.build_comparison_artifact(keep_record, batch_manifest)
    assert av.assert_no_scalar_score(artifact) == []
    for forbidden in ("score", "quality_index", "aios_quality_score", "rating"):
        assert forbidden not in artifact


def test_comparison_artifact_exposes_required_dimensions(keep_record, batch_manifest):
    artifact = av.build_comparison_artifact(keep_record, batch_manifest)
    for key in (
        "behavioral_vector",
        "efficiency_vector",
        "regressions",
        "variance_notes",
        "decision",
        "decision_basis",
    ):
        assert key in artifact


def test_a_planted_scalar_score_key_is_detected():
    fake_artifact = {"aios_quality_score": 87.5, "decision": "keep_candidate"}
    findings = av.assert_no_scalar_score(fake_artifact)
    assert any(f.rule == "NO_SCALAR_SCORE" for f in findings)


# ---------------------------------------------------------------------------
# Committed examples (ledger format/example, comparison artifact
# format/example -- issue #392 Allowed files) stay self-consistent with the
# code that produced them, not stale hand-written documentation.
# ---------------------------------------------------------------------------


def test_committed_ledger_example_verifies_clean():
    findings = av.verify_ledger(FIXTURES / "ledger_example.jsonl")
    assert findings == []
    lines = av.read_ledger(FIXTURES / "ledger_example.jsonl")
    assert [line["record"]["decision"] for line in lines] == [
        "keep_candidate",
        "discard",
        "inconclusive",
    ]


def test_committed_comparison_artifact_example_matches_builder(keep_record, batch_manifest):
    committed = _load("comparison_artifact_example.json")
    rebuilt = av.build_comparison_artifact(keep_record, batch_manifest)
    assert committed == rebuilt
    assert av.assert_no_scalar_score(committed) == []


# ---------------------------------------------------------------------------
# manual_candidate_evaluation ledger (issue #433, MD-3): distinct evidence
# class, SAME hash-chained append-only ledger mechanism as the failure-driven
# experiment_record ledger above -- not a second ledger or state machine.
# ---------------------------------------------------------------------------


def _manual_evaluation_record(**ov) -> dict:
    base = {
        "schema_version": "0.2.0",
        "record_kind": "manual_candidate_evaluation",
        "experiment_id": "AR-433-PILOT-1",
        "batch_id": "AR-433-BATCH-1",
        "created_at": "2026-09-04T00:00:00Z",
        "baseline_revision": "a" * 40,
        "baseline_file_hash": "b" * 64,
        "baseline_file_hash_status": "captured",
        "candidate_patch_ref": "sha256:" + "c" * 64,
        "candidate_patch_hash": "c" * 64,
        "target_file": "ROUTING_RULES.md",
        "research_surface": "MUT-ROUTING-TIEBREAK",
        "authority_evidence_ref": "docs/evidence/TEST.md#owner",
        "budget": {
            "max_provider_calls": 40, "max_cost_amount": 0.0, "max_cost_currency": "USD",
            "calls_used": 18, "call_timeout_seconds": 180,
        },
        "context_identities": {
            "baseline_context_hash": "d" * 64, "candidate_context_hash": "e" * 64,
            "context_equivalence": {"equivalent": True, "differences": ["ROUTING_RULES.md"]},
            "transport_id": "playwright_mcp", "subject_model_identity": "not_observable",
            "subject_model_identity_status": "not_observable",
            "evaluator_version_hash": "f" * 64, "evaluator_contract_version": "0.2.0",
            "context_capture_status": "captured",
        },
        "rerun_policy": {
            "min_matched_reruns": 3, "ceiling": 5,
            "escalation_trigger": "#395 §8 escalation trigger (run_variance_or_disagreement) fired for",
            "per_case_reruns_used": {"tiebreak-c1": 3}, "escalated_cases": [], "budget_limited_cases": [],
        },
        "matched_observations": [
            {"case_id": "tiebreak-c1", "case_family": "routing", "rerun": k,
             "baseline_response_hash": "1" * 64, "candidate_response_hash": "2" * 64,
             "baseline_verdict": "pass", "candidate_verdict": "pass",
             "baseline_invocation_id": f"AR-433-PILOT-1-r{k}:baseline:tiebreak-c1",
             "candidate_invocation_id": f"AR-433-PILOT-1-r{k}:candidate:tiebreak-c1",
             "judge_invocation_ids": [f"AR-433-PILOT-1-r{k}:tiebreak-c1:0"],
             "judge_consistency": "order_consistent"}
            for k in range(3)
        ],
        "judge_findings": [
            {"case_id": "tiebreak-c1", "rerun": k, "consistency": "order_consistent",
             "baseline_verdict": "pass", "candidate_verdict": "pass"}
            for k in range(3)
        ],
        "comparator_raw_decision": {"decision": "inconclusive", "reason": "no material improvement shown"},
        "pilot_decision": "inconclusive",
        "causal_validity_status": {
            "subject_context_scope_verification": "machine_verified_per_call_observed_url",
            "memory_personalization_isolation_verification": "self_declared_not_machine_verified",
        },
        "limitations": ["repo_replay is a lower-fidelity approximation; no UI-equivalence claim."],
        "rollback": "Candidate exists only in ephemeral shadow worktrees; nothing applied to main.",
        "evidence_hashes": {"evidence_package_sha256": "9" * 64, "patch_sha256": "c" * 64},
    }
    base.update(ov)
    return base


def test_manual_evaluation_record_round_trips_through_verify_ledger(tmp_path):
    ledger = tmp_path / "manual_evaluations.jsonl"
    record = _manual_evaluation_record()
    assert av.manual_evaluation_ledger_append(ledger, record) == []
    assert av.verify_ledger(ledger) == []
    lines = av.read_ledger(ledger)
    assert [line["record"]["experiment_id"] for line in lines] == ["AR-433-PILOT-1"]

    # tamper-evidence: an in-place edit to the appended record breaks the chain,
    # exactly like the failure-driven ledger above (same mechanism, not a
    # second one).
    raw_lines = ledger.read_text(encoding="utf-8").splitlines()
    tampered = json.loads(raw_lines[0])
    tampered["record"]["pilot_decision"] = "candidate_for_owner_review"
    raw_lines[0] = json.dumps(tampered)
    ledger.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")
    findings = av.verify_ledger(ledger)
    assert any(f.rule == "LEDGER_TAMPERED" for f in findings)


def test_manual_evaluation_record_never_allows_keep_candidate_pilot_decision():
    bad = _manual_evaluation_record(
        pilot_decision="keep_candidate",
        comparator_raw_decision={"decision": "keep_candidate", "reason": "x"},
    )
    findings = av.validate_manual_evaluation_record(bad)
    assert findings != []
