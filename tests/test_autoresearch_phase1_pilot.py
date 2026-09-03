"""Phase 1 bounded pilot test wrapper for AIOS AutoResearch v0.1 (issue
#397, parent #388). Proves, reproducibly under pytest/CI, that the 4
Phase 1 experiments run correctly against the real pipeline and produce
the expected decisions. See scripts/autoresearch_phase1_pilot.py's module
docstring for the explicit, honest scope statement (no live model call;
synthetic calibration-owner-authored observations, consistent with #396's
Phase 0 discipline and the explicit owner authorization that carried it
forward).
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location(
    "autoresearch_phase1_pilot", REPO_ROOT / "scripts" / "autoresearch_phase1_pilot.py"
)
pilot = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = pilot
_spec.loader.exec_module(pilot)

av = pilot.av
sr = pilot.sr


@pytest.fixture()
def report(tmp_path):
    ledger_path = tmp_path / "phase1_ledger.jsonl"
    return pilot.run_batch(ledger_path), ledger_path


def test_batch_attempts_exactly_four_experiments(report):
    r, _ = report
    assert r["experiments_attempted"] == 4


def test_batch_uses_one_immutable_baseline_for_all_experiments(report):
    r, _ = report
    # every experiment's outcome implicitly shares the same baseline_revision
    # because run_batch() computes it once and threads it through; assert
    # the batch-level field is a real, resolvable git revision.
    assert len(r["baseline_revision"]) == 40
    resolved = subprocess.run(
        ["git", "cat-file", "-e", r["baseline_revision"]], cwd=REPO_ROOT, capture_output=True
    )
    assert resolved.returncode == 0


def test_experiment_1_negative_control_is_discarded(report):
    r, _ = report
    exp1 = r["outcomes"][0]
    assert exp1["stage"] == "discard"
    assert exp1["decision"] == "discard"


def test_experiment_2_noop_control_is_inconclusive(report):
    r, _ = report
    exp2 = r["outcomes"][1]
    assert exp2["decision"] == "inconclusive"


def test_experiment_3_protected_surface_violation_is_rejected(report):
    r, _ = report
    exp3 = r["outcomes"][2]
    assert exp3["stage"] == "rejected_pre_application"
    assert "INV-01" in exp3["decision_basis"]


def test_experiment_4_uncertain_attribution_is_inconclusive_not_a_confident_keep(report):
    r, _ = report
    exp4 = r["outcomes"][3]
    assert exp4["attribution_status"] == "uncertain"
    assert exp4["decision"] == "inconclusive"
    assert exp4["decision"] != "keep_candidate"  # uncertain attribution must never produce a confident autonomous keep


def test_no_experiment_reached_an_unflagged_keep_candidate(report):
    """This batch, by honest design (no genuine evidence-backed hypothesis
    available), should not produce a clean keep_candidate anywhere."""
    r, _ = report
    assert not any(o["decision"] == "keep_candidate" for o in r["outcomes"])


def test_ledger_has_exactly_three_entries_rejected_experiment_never_appended(report):
    """Experiment 3 was rejected pre-application and must never reach the
    append-only ledger; experiments 1, 2, 4 (all of which passed the scope
    check) must all be present."""
    _, ledger_path = report
    lines = av.read_ledger(ledger_path)
    assert len(lines) == 3
    ids = [line["record"]["experiment_id"] for line in lines]
    assert ids == [
        "AUTORESEARCH-phase1-pilot-001-1",
        "AUTORESEARCH-phase1-pilot-001-2",
        "AUTORESEARCH-phase1-pilot-001-4",
    ]


def test_ledger_verifies_clean_hash_chain(report):
    _, ledger_path = report
    assert av.verify_ledger(ledger_path) == []


def test_every_ledger_record_validates_against_experiment_schema(report):
    _, ledger_path = report
    for line in av.read_ledger(ledger_path):
        assert av.validate_experiment_record_schema(line["record"]) == []


def test_no_ledger_record_claims_acceptance_authority(report):
    """Every appended record is Researcher-authored; none may claim owner
    approval, a merged PR, or production authorization (issue #397:
    'keep_candidate remains unpromoted and does not alter active
    configuration')."""
    _, ledger_path = report
    for line in av.read_ledger(ledger_path):
        assert av.reject_authority_escalation(line["record"]) == []


def test_all_experiments_target_declared_mutable_surfaces_only(report):
    r, _ = report
    manifest = av.load_manifest()
    mutable_ids = {s["surface_id"] for s in manifest["mutable_surfaces"]}
    for outcome in r["outcomes"]:
        assert outcome["research_surface"] in mutable_ids


def test_parent_repository_working_tree_unchanged_by_full_batch():
    """No active Project Instructions/routing edit reaches this repository
    at any point -- every patch is applied only inside an ephemeral shadow
    worktree, per issue #397's own Rollback rule."""
    import tempfile

    before = subprocess.run(["git", "status", "--short"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    before_worktrees = subprocess.run(["git", "worktree", "list"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    with tempfile.TemporaryDirectory() as td:
        pilot.run_batch(Path(td) / "ledger.jsonl")
    after = subprocess.run(["git", "status", "--short"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    after_worktrees = subprocess.run(["git", "worktree", "list"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    assert before == after
    assert before_worktrees == after_worktrees


def test_reproducible_across_two_independent_runs():
    """Determinism check: running the batch twice (different tmp ledgers)
    produces identical decisions for every experiment -- this is
    calibration-owner-authored synthetic data, not a live model, so it must
    be exactly reproducible."""
    import tempfile

    with tempfile.TemporaryDirectory() as td1:
        r1 = pilot.run_batch(Path(td1) / "ledger.jsonl")
    with tempfile.TemporaryDirectory() as td2:
        r2 = pilot.run_batch(Path(td2) / "ledger.jsonl")
    decisions1 = [o["decision"] for o in r1["outcomes"]]
    decisions2 = [o["decision"] for o in r2["outcomes"]]
    assert decisions1 == decisions2
