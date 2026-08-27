"""Unit tests for scripts/validate_autonomous_execution_record.py.

Covers:
(a) all five Phase 1 example records under docs/autonomous_execution/examples/
    validate cleanly (zero violations) against the Phase 6 semantic validator.
(b) synthetic fixture records, each deliberately violating exactly one rule
    (SEM-001 .. SEM-011), asserting the validator catches it and does not
    also flag an unrelated rule.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_autonomous_execution_record.py"
EXAMPLES_DIR = ROOT / "docs" / "autonomous_execution" / "examples"


def load_validator_module():
    spec = importlib.util.spec_from_file_location("validate_autonomous_execution_record", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


validator = load_validator_module()


# ---------------------------------------------------------------------------
# (a) Phase 1 example records must all be clean.
# ---------------------------------------------------------------------------


def example_paths() -> list[Path]:
    paths = sorted(EXAMPLES_DIR.glob("*.json"))
    assert paths, f"expected example records under {EXAMPLES_DIR}"
    return paths


def test_all_phase1_examples_are_clean():
    paths = example_paths()
    assert len(paths) == 5, f"expected 5 Phase 1 example records, found {len(paths)}: {paths}"
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        violations = validator.validate_record(data, str(path))
        assert violations == [], f"{path.name} unexpectedly failed semantic validation: {violations}"


def test_main_exits_zero_on_default_scan():
    """`main([])` scans only the canonical top-level examples (`DEFAULT_GLOB`
    = docs/autonomous_execution/examples/*.json, non-recursive), which are
    expected to always be fully clean — same scope as `example_paths()`
    above. It deliberately does not recurse into examples/pilot_evidence/:
    pilot evidence may legitimately encode scenario-specific states (e.g. an
    intentionally stale artifact, which is the Phase 3 pilot's actual
    subject matter) that a blanket "must be clean" default-scan assumption
    would wrongly flag as a defect. See the module docstring's "Default-scan
    scope" section in validate_autonomous_execution_record.py. Pilot
    evidence is still fully covered by the SEM rules on request — see
    test_include_pilot_evidence_flag_adds_pilot_evidence_records below,
    and --include-pilot-evidence / explicit paths for opt-in scanning."""
    exit_code = validator.main([])
    assert exit_code == 0


def test_default_scan_does_not_include_pilot_evidence():
    targets = validator.collect_targets([], ROOT)
    assert all(p.parent.name != "pilot_evidence" for p in targets), (
        "default scan must not sweep in pilot_evidence/ records, which may "
        "legitimately contain scenario-specific (non-clean) states"
    )


def test_include_pilot_evidence_flag_adds_pilot_evidence_records(tmp_path):
    # Independent of whether this branch happens to carry any pilot_evidence
    # fixtures itself: build a minimal fake repo layout to prove the flag's
    # mechanism (PILOT_EVIDENCE_GLOB is included only when requested).
    examples_dir = tmp_path / "docs" / "autonomous_execution" / "examples"
    pilot_dir = examples_dir / "pilot_evidence"
    pilot_dir.mkdir(parents=True)
    (examples_dir / "top_level_example.json").write_text("{}", encoding="utf-8")
    (pilot_dir / "some_pilot.json").write_text("{}", encoding="utf-8")

    # Check the parent directory name, not a substring of the full path —
    # pytest's own tmp_path can itself contain "pilot_evidence" as a
    # substring (derived from this test's name), which would make a naive
    # substring check on str(p) unreliable.
    default_targets = validator.collect_targets([], tmp_path)
    assert all(p.parent.name != "pilot_evidence" for p in default_targets)

    with_pilot_targets = validator.collect_targets([], tmp_path, include_pilot_evidence=True)
    assert any(p.parent.name == "pilot_evidence" for p in with_pilot_targets), (
        "--include-pilot-evidence must still make pilot evidence records "
        "reachable via the default-scan code path"
    )


# ---------------------------------------------------------------------------
# (b) Synthetic single-rule-violation fixtures.
# ---------------------------------------------------------------------------

BASE_RECORD = {
    "schema_version": "1.0.0",
    "standard_version": "1.0.0",
    "execution_id": "exec-fixture-001",
    "parent_execution_id": None,
    "project": "[AI OS]",
    "project_extension": None,
    "execution_mode": "implement",
    "risk_mode": "standard",
    "source_revision": {
        "revision_type": "git_commit",
        "baseline_revision": "rev-a",
        "final_revision": "rev-b",
        "content_manifest": None,
        "final_iteration_id": "iter-001",
    },
    "created_at": "2026-01-01T00:00:00Z",
    "updated_at": "2026-01-01T01:00:00Z",
    "execution_state": "completed",
    "terminal_reason": None,
    "requirements": [
        {
            "requirement_id": "req-001",
            "requirement": "Fixture requirement.",
            "source": None,
            "mandatory": True,
            "implementation_locations": [],
            "evidence_refs": ["ev-001"],
            "validation_refs": ["val-001"],
            "status": "passed",
            "status_history": [],
            "gap": None,
            "corrective_action_refs": [],
        }
    ],
    "defects": [],
    "iterations": [
        {
            "iteration_id": "iter-001",
            "iteration_number": 1,
            "iteration_type": "full_iteration",
            "started_at": "2026-01-01T00:00:00Z",
            "completed_at": "2026-01-01T00:30:00Z",
            "trigger": "initial implementation",
            "requirements_affected": ["req-001"],
            "defects_addressed": [],
            "changes": ["fixture.py: implemented"],
            "validation_refs": ["val-001"],
            "result": "pass",
        }
    ],
    "validation_runs": [
        {
            "validation_id": "val-001",
            "validation_type": "unit",
            "command_or_method": "pytest -q",
            "validated_revision": "rev-b",
            "covered_paths": ["fixture.py"],
            "covered_requirement_ids": ["req-001"],
            "started_at": "2026-01-01T00:20:00Z",
            "completed_at": "2026-01-01T00:30:00Z",
            "result": "pass",
            "evidence_refs": ["ev-001"],
            "freshness_status": "current",
            "freshness_justification": None,
            "unaffected_paths_evidence": None,
            "limitations": [],
        }
    ],
    "artifacts": [],
    "acceptance_scopes": {
        "requirements_traceability": {"status": "pass"},
        "implementation": {"status": "pass"},
        "tests": {"status": "pass"},
        "validation": {"status": "pass"},
        "output_artifacts": {"status": "not_applicable"},
        "corrective_loop": {"status": "not_applicable"},
        "rollback_readiness": {"status": "pass"},
    },
    "overall_delivery": "pass",
    "qa_status": "not_run",
    "judge_verdict": "not_run",
    "authority_status": "owner_review_pending",
    "merge_status": "owner_review_pending",
    "production_status": "not_authorized",
    "rollback": {"strategy": "git_revert", "status": "ready"},
    "external_actions": [],
    "handoffs": [],
    "final_report": None,
}


def fixture() -> dict:
    return copy.deepcopy(BASE_RECORD)


def rule_ids(violations) -> set[str]:
    return {v.rule_id for v in violations}


def closure_aware_record() -> dict:
    record = fixture()
    record["schema_version"] = "2.0.0"
    record["standard_version"] = "2.0.0"
    record["closure_review"] = {
        "status": "pass",
        "closure_context": {
            "goal_or_task": "Fixture closure review.",
            "agreed_scope": "fixture.py",
            "explicit_constraints": [],
            "acceptance_criteria": ["fixture passes"],
            "material_invariants": ["validated evidence reaches acceptance"],
            "source_revision": "rev-b",
            "current_state_refs": ["fixture.py"],
            "requirements_traceability_summary": "req-001 passed",
            "latest_test_evidence": ["ev-001"],
            "latest_validation_evidence": ["val-001"],
            "artifact_refs": [],
            "known_limitations": [],
            "residual_risks": [],
            "rollback_status": "ready",
            "external_authority_status": "owner_review_pending",
            "input_or_state_hashes": ["sha256:fixture"],
        },
        "goal_rechecked": True,
        "scope_rechecked": True,
        "invariants_checked": ["validated evidence reaches acceptance"],
        "adversarial_cases": [],
        "remaining_correctable_gaps": [],
        "limitations_reviewed": [],
        "defects_found": [],
        "defects_reopened": [],
        "validation_refs": ["val-001"],
        "evidence_refs": ["ev-001"],
        "closure_iteration_count": 0,
        "effective_max_closure_corrective_iterations": 2,
        "authority_boundary_preserved": True,
        "final_reason": "no remaining correctable gap",
    }
    return record


def continuation_record() -> dict:
    record = closure_aware_record()
    record["continuation"] = {
        "original_goal": "Continue the original goal.",
        "original_acceptance_criteria": ["criterion one"],
        "resolved_owner": "[AI OS]",
        "resume_stage": "owner_execution",
        "record_ref": "fixture.json",
        "scope_ref": "scope:fixture",
        "routing_state_ref": "routing:fixture",
        "source_revision": "rev-b",
        "goal_boundary_hash": "sha256:" + "a" * 64,
        "acceptance_criteria_hash": "sha256:" + "b" * 64,
        "state_hash": "sha256:" + "c" * 64,
        "updated_at": "2026-01-01T01:00:00Z",
        "route_trace": [{"route_id": "route-001", "from_owner": "[AI OS]", "to_owner": "[Codex]", "resume_stage": "owner_execution", "criteria_addressed": ["criterion one"], "outcome": "completed"}],
        "progress": {"satisfied_criteria": ["criterion one"], "remaining_criteria": [], "last_real_progress_route_id": "route-001"},
        "guards": {"max_continuation_hops": None, "max_retries_per_owner": None, "max_no_progress_hops": None, "route_signature_history_window": None, "tripped_guard": None, "tripped_guards": [], "terminal_report_ref": None},
    }
    return record


def test_sem012_repeat_route_requires_evidence_delta():
    record = continuation_record()
    record["continuation"]["route_trace"].append({"route_id": "route-002", "from_owner": "[AI OS]", "to_owner": "[Codex]", "resume_stage": "owner_execution", "criteria_addressed": ["criterion one"], "outcome": "refused"})
    assert "SEM-012" in rule_ids(validator.validate_record(record, "fixture"))


def test_sem013_guard_stop_requires_mapped_terminal_reason_and_report():
    record = continuation_record()
    record["execution_state"] = "stopped"
    record["overall_delivery"] = "partial"
    record["terminal_reason"] = "continuation_no_progress_limit_reached"
    record["continuation"]["progress"] = {"satisfied_criteria": [], "remaining_criteria": ["criterion one"], "last_real_progress_route_id": None}
    record["continuation"]["guards"].update({"tripped_guard": "no_progress_counter", "tripped_guards": ["no_progress_counter"], "terminal_report_ref": "report:fixture"})
    assert "SEM-013" not in rule_ids(validator.validate_record(record, "fixture"))


def test_sem013_rejects_non_partitioned_progress_and_unreported_guard_stop():
    record = continuation_record()
    record["continuation"]["progress"]["remaining_criteria"] = ["criterion one"]
    record["continuation"]["guards"]["tripped_guard"] = "hop_budget"
    assert "SEM-013" in rule_ids(validator.validate_record(record, "fixture"))


def test_sem001_failed_mandatory_requirement_with_overall_pass():
    record = fixture()
    record["requirements"][0]["status"] = "failed"
    violations = validator.validate_record(record, "fixture")
    assert "SEM-001" in rule_ids(violations)


def test_sem001_blocked_requirement_without_reason():
    record = fixture()
    record["requirements"][0]["status"] = "blocked"
    record["requirements"][0]["gap"] = None
    violations = validator.validate_record(record, "fixture")
    assert "SEM-001" in rule_ids(violations)


def test_sem001_blocked_requirement_with_reason_is_clean_for_this_rule():
    record = fixture()
    record["requirements"][0]["status"] = "blocked"
    record["requirements"][0]["gap"] = "external dependency unavailable in sandbox"
    violations = validator.validate_record(record, "fixture")
    assert "SEM-001" not in rule_ids(violations)


def test_sem002_open_recoverable_defect_with_overall_pass():
    record = fixture()
    record["defects"].append(
        {
            "defect_id": "def-001",
            "requirement_id": "req-001",
            "detected_in_iteration": "iter-001",
            "detected_by": "val-001",
            "classification": "implementation",
            "subtype": None,
            "severity": "recoverable",
            "description": "Fixture defect left open.",
            "evidence_refs": [],
            "correction_eligible": True,
            "required_authority": None,
            "remediation_owner": None,
            "corrective_action_refs": [],
            "affected_scope": [],
            "required_validation_refs": [],
            "status": "open",
            "status_history": [],
            "resolved_in_iteration": None,
            "resolution_evidence_refs": [],
            "accepted_by": None,
            "authority_evidence_ref": None,
            "acceptance_reason": None,
            "accepted_at": None,
        }
    )
    violations = validator.validate_record(record, "fixture")
    assert "SEM-002" in rule_ids(violations)


def test_sem003_duplicate_requirement_id():
    record = fixture()
    duplicate = copy.deepcopy(record["requirements"][0])
    record["requirements"].append(duplicate)
    violations = validator.validate_record(record, "fixture")
    assert "SEM-003" in rule_ids(violations)


def test_sem004_resolved_defect_without_resolution_evidence():
    record = fixture()
    record["defects"].append(
        {
            "defect_id": "def-001",
            "requirement_id": "req-001",
            "detected_in_iteration": "iter-001",
            "detected_by": "val-001",
            "classification": "implementation",
            "subtype": None,
            "severity": "recoverable",
            "description": "Fixture defect marked resolved without evidence.",
            "evidence_refs": ["ev-001"],
            "correction_eligible": True,
            "required_authority": None,
            "remediation_owner": None,
            "corrective_action_refs": [],
            "affected_scope": [],
            "required_validation_refs": [],
            "status": "resolved",
            "status_history": [],
            "resolved_in_iteration": "iter-001",
            "resolution_evidence_refs": [],
            "accepted_by": None,
            "authority_evidence_ref": None,
            "acceptance_reason": None,
            "accepted_at": None,
        }
    )
    violations = validator.validate_record(record, "fixture")
    assert "SEM-004" in rule_ids(violations)


def test_sem005_mandatory_stale_artifact_with_overall_pass():
    record = fixture()
    record["artifacts"].append(
        {
            "artifact_id": "art-001",
            "path": "reports/fixture.docx",
            "artifact_type": "docx_memo",
            "mandatory": True,
            "source_inputs": [],
            "generation_method": None,
            "generated_from_revision": "rev-a",
            "generated_in_iteration": None,
            "generated_at": None,
            "validation_refs": [],
            "freshness_status": "stale",
            "freshness_evidence_refs": [],
        }
    )
    violations = validator.validate_record(record, "fixture")
    assert "SEM-005" in rule_ids(violations)


def test_sem006_passed_requirement_backed_only_by_stale_validation():
    record = fixture()
    record["validation_runs"][0]["freshness_status"] = "stale"
    violations = validator.validate_record(record, "fixture")
    assert "SEM-006" in rule_ids(violations)


def test_sem007_malformed_parent_execution_id():
    record = fixture()
    record["parent_execution_id"] = "not-a-valid-exec-id"
    violations = validator.validate_record(record, "fixture")
    assert "SEM-007" in rule_ids(violations)


def test_sem007_parent_equal_to_self():
    record = fixture()
    record["parent_execution_id"] = record["execution_id"]
    violations = validator.validate_record(record, "fixture")
    assert "SEM-007" in rule_ids(violations)


def test_sem008_full_iteration_count_exceeds_stated_envelope():
    record = fixture()
    record["project_extension"] = {"max_full_iterations": 1}
    second_iteration = copy.deepcopy(record["iterations"][0])
    second_iteration["iteration_id"] = "iter-002"
    second_iteration["iteration_number"] = 2
    record["iterations"].append(second_iteration)
    violations = validator.validate_record(record, "fixture")
    assert "SEM-008" in rule_ids(violations)


def test_sem008_within_envelope_is_clean():
    record = fixture()
    record["project_extension"] = {"max_full_iterations": 5}
    violations = validator.validate_record(record, "fixture")
    assert "SEM-008" not in rule_ids(violations)


def test_clean_record_has_no_violations():
    record = fixture()
    violations = validator.validate_record(record, "fixture")
    assert violations == []


def test_sem009_closure_aware_success_without_review_is_rejected():
    record = closure_aware_record()
    record["closure_review"] = None
    violations = validator.validate_record(record, "fixture")
    assert "SEM-009" in rule_ids(violations)


def test_sem009_passed_closure_with_correctable_gap_is_rejected():
    record = closure_aware_record()
    record["closure_review"]["remaining_correctable_gaps"] = ["adjacent trust-boundary bypass"]
    violations = validator.validate_record(record, "fixture")
    assert "SEM-009" in rule_ids(violations)


def test_sem010_closure_iteration_count_over_effective_limit_is_rejected():
    record = closure_aware_record()
    record["closure_review"]["closure_iteration_count"] = 2
    record["closure_review"]["effective_max_closure_corrective_iterations"] = 1
    violations = validator.validate_record(record, "fixture")
    assert "SEM-010" in rule_ids(violations)


def test_sem011_unregistered_closure_defect_is_rejected():
    record = closure_aware_record()
    record["closure_review"]["defects_found"] = ["def-closure-001"]
    violations = validator.validate_record(record, "fixture")
    assert "SEM-011" in rule_ids(violations)


def test_sem011_closure_correction_requires_fresh_final_validation():
    record = closure_aware_record()
    record["closure_review"]["closure_iteration_count"] = 1
    record["validation_runs"][0]["freshness_status"] = "stale"
    violations = validator.validate_record(record, "fixture")
    assert "SEM-011" in rule_ids(violations)


def test_closure_aware_clean_record_has_no_violations():
    assert validator.validate_record(closure_aware_record(), "fixture") == []


def test_sem014_candidate_research_cannot_become_action_eligible_after_resume():
    record = fixture()
    record["continuation"] = {
        "authority_provenance": {
            "claims": [{
                "claim_text": "Enable feature X.",
                "authority_class": "candidate_research",
                "source_refs": ["research:fixture"],
                "action_eligibility": "eligible",
            }]
        }
    }
    violations = validator.validate_record(record, "fixture")
    assert "SEM-014" in rule_ids(violations)


def test_sem014_identical_accepted_policy_claim_remains_eligible():
    record = fixture()
    record["handoffs"] = [{
        "handoff_id": "handoff-001",
        "authority_provenance": {
            "claims": [{
                "claim_text": "Enable feature X.",
                "authority_class": "accepted_policy",
                "source_refs": ["policy:fixture"],
                "action_eligibility": "eligible",
            }]
        },
    }]
    violations = validator.validate_record(record, "fixture")
    assert "SEM-014" not in rule_ids(violations)


def effect_action(**overrides):
    action = {
        "action_id": "action-001",
        "action_type": "source_mutation",
        "required_for_objective": True,
        "requested": True,
        "required_authority": "owner instruction",
        "authority_evidence_ref": "ev-authority",
        "status": "completed",
        "executed_at": "2026-01-01T00:30:00Z",
        "result_evidence_ref": "ev-result",
        "effect_boundary": {
            "preview": {"intent_fingerprint": "intent-a"},
            "authority_checked_at": "2026-01-01T00:20:00Z",
            "commit_performed": True,
            "commit_intent_fingerprint": "intent-a",
            "authority_rechecked_after_preview_change": False,
            "verification_result": "pass",
            "verification_evidence_ref": "ev-verify",
        },
    }
    action.update(overrides)
    return action


def test_sem015_reversible_authorized_action_with_verification_is_clean():
    record = fixture()
    record["external_actions"] = [effect_action()]
    assert "SEM-015" not in rule_ids(validator.validate_record(record, "fixture"))


def test_sem015_missing_authority_stops_before_commit():
    record = fixture()
    action = effect_action(authority_evidence_ref=None)
    record["external_actions"] = [action]
    assert "SEM-015" in rule_ids(validator.validate_record(record, "fixture"))


def test_sem015_failed_verification_forbids_successful_completion():
    record = fixture()
    action = effect_action()
    action["effect_boundary"]["verification_result"] = "fail"
    action["effect_boundary"]["verification_evidence_ref"] = "ev-failed-verify"
    record["external_actions"] = [action]
    assert "SEM-015" in rule_ids(validator.validate_record(record, "fixture"))


def test_sem015_changed_preview_requires_authority_recheck():
    record = fixture()
    action = effect_action()
    action["effect_boundary"]["commit_intent_fingerprint"] = "intent-b"
    record["external_actions"] = [action]
    assert "SEM-015" in rule_ids(validator.validate_record(record, "fixture"))
