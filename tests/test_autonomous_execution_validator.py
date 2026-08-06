"""Unit tests for scripts/validate_autonomous_execution_record.py.

Covers:
(a) all five Phase 1 example records under docs/autonomous_execution/examples/
    validate cleanly (zero violations) against the Phase 6 semantic validator.
(b) synthetic fixture records, each deliberately violating exactly one rule
    (SEM-001 .. SEM-008), asserting the validator catches it and does not
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
