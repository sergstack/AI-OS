"""Phase 0 calibration test wrapper for AIOS AutoResearch v0.1 (issue #396,
parent #388). Proves, reproducibly under pytest/CI, that the real
deterministic pipeline (issues #392/#393/#395) correctly separates every
hand-authored good/bad calibration case across all 10 required calibration
classes from issue #396. See scripts/autoresearch_phase0_calibration.py's
module docstring for the explicit, honest scope statement: this does not
calibrate a live semantic Judge (out of scope, consistent with #392-#395's
own "no live model call" rule); it calibrates the deterministic machinery
that any real Judge's output would flow through.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location(
    "autoresearch_phase0_calibration", REPO_ROOT / "scripts" / "autoresearch_phase0_calibration.py"
)
cal = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = cal
_spec.loader.exec_module(cal)


REQUIRED_CALIBRATION_CLASSES = [
    "routing_ownership_vs_substitution",
    "handoff_completeness",
    "evidence_support_vs_fabrication",
    "honest_not_run_vs_fabricated_pass",
    "authority_separation_vs_escalation",
    "bounded_action_vs_false_abstention",
    "protected_mutation_or_hash_mismatch",
    "matched_vs_config_mismatch",
    "stable_vs_order_sensitive",
    "infrastructure_failure_to_inconclusive",
]


def test_all_ten_required_calibration_classes_are_present(tmp_path):
    results = cal.run_all(tmp_path)
    observed_classes = {r.calibration_class for r in results}
    assert observed_classes == set(REQUIRED_CALIBRATION_CLASSES), (
        f"missing classes: {set(REQUIRED_CALIBRATION_CLASSES) - observed_classes}"
    )


def test_every_calibration_case_matches_its_expected_label(tmp_path):
    results = cal.run_all(tmp_path)
    failed = [r for r in results if not r.passed]
    assert failed == [], f"calibration cases that did not match expected label: {failed}"


def test_phase0_verdict_is_pass(tmp_path):
    results = cal.run_all(tmp_path)
    assert cal.phase0_verdict(results) == "pass"


def test_no_case_is_silently_skipped_grain_check(tmp_path):
    """issue #396 Grain: one observation per case x run x side x evaluator
    version/configuration; do not report only aggregate percentages. This
    proves every individual case result is inspectable, not just a count."""
    results = cal.run_all(tmp_path)
    assert len(results) >= 20  # at least 2 per required class
    for r in results:
        assert r.case_id  # every row individually identified, not aggregated away
        assert r.detail  # every row carries its own evidence, not just pass/fail


@pytest.mark.parametrize("calibration_class", REQUIRED_CALIBRATION_CLASSES)
def test_each_class_has_at_least_one_good_and_one_bad_case(tmp_path, calibration_class):
    results = [r for r in cal.run_all(tmp_path) if r.calibration_class == calibration_class]
    labels = {r.expected_label for r in results}
    assert "good" in labels
    assert "bad" in labels


def test_calibration_run_leaves_no_stray_worktree_in_repo_root():
    """The one shadow-worktree calibration class (#7, #10) must operate only
    against disposable scratch repos in tmp_path, never against this
    session's own repository -- proven by asserting the real repo's own
    worktree list is unaffected by running the full batch."""
    import subprocess
    import tempfile

    before = subprocess.run(["git", "worktree", "list"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    with tempfile.TemporaryDirectory() as td:
        cal.run_all(Path(td))
    after = subprocess.run(["git", "worktree", "list"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    assert before == after


def test_repository_working_tree_unchanged_by_calibration_run():
    import subprocess
    import tempfile

    before = subprocess.run(["git", "status", "--short"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    with tempfile.TemporaryDirectory() as td:
        cal.run_all(Path(td))
    after = subprocess.run(["git", "status", "--short"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    assert before == after
