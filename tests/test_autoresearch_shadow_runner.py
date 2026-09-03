"""Focused tests for the AIOS AutoResearch v0.1 provider-neutral shadow
runner and isolated-worktree boundary (issue #393, parent #388).

Every test runs against a disposable scratch git repository built fresh in
tmp_path -- never against this session's own working tree or worktrees, and
never against a live network. No test in this module makes a socket
connection or imports a network client library.
"""

from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = REPO_ROOT / "tests" / "fixtures" / "autoresearch"

_spec = importlib.util.spec_from_file_location(
    "autoresearch_shadow_runner", REPO_ROOT / "scripts" / "autoresearch_shadow_runner.py"
)
sr = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = sr
_spec.loader.exec_module(sr)

av = sr.av  # the shadow runner re-exports its autoresearch_validator import


def _load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def _git(args: list[str], cwd: Path, input_text: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, input=input_text, capture_output=True, text=True, check=True)


ROUTING_CONTENT = """# Canonical Routing Rules

## Registered capability destinations

| Input type | Destination |
| --- | --- |
| AI concept | `[AI OS]` |

## Tie-break rules

| Case | Rule |
| --- | --- |
| Coding task preparation | `[Codex]` |
| Still ambiguous | `blocked` |

## Boundary

`[Inbox Router]` sorts and formulates.
"""

AIOS_INSTRUCTIONS_CONTENT = """# [AI OS] Project Instruction

## 2. Индексы и источники

Приоритет проверки KB:
1. old first item

## 5. Governance

Blocked capabilities list.
"""


@pytest.fixture()
def scratch_repo(tmp_path: Path) -> tuple[Path, str]:
    repo = tmp_path / "scratch_repo"
    repo.mkdir()
    _git(["init", "-q"], cwd=repo)
    _git(["config", "user.email", "test@example.com"], cwd=repo)
    _git(["config", "user.name", "Test"], cwd=repo)
    (repo / "ROUTING_RULES.md").write_text(ROUTING_CONTENT, encoding="utf-8")
    aios_dir = repo / "ChatGPT" / "[AI OS]"
    aios_dir.mkdir(parents=True)
    (aios_dir / "PROJECT_INSTRUCTIONS.md").write_text(AIOS_INSTRUCTIONS_CONTENT, encoding="utf-8")
    (repo / "HANDOFF_STYLE_STANDARD.md").write_text("# Handoff\n\n## Project-Specific Additions\n\nold text\n", encoding="utf-8")
    _git(["add", "-A"], cwd=repo)
    _git(["commit", "-q", "-m", "baseline"], cwd=repo)
    baseline_rev = _git(["rev-parse", "HEAD"], cwd=repo).stdout.strip()
    return repo, baseline_rev


def _make_patch(repo: Path, rel_path: str, new_content: str) -> str:
    target = repo / rel_path
    original = target.read_text(encoding="utf-8")
    target.write_text(new_content, encoding="utf-8")
    diff = _git(["diff", "--", rel_path], cwd=repo).stdout
    target.write_text(original, encoding="utf-8")  # restore scratch repo's own working tree
    assert diff, f"expected a non-empty diff for {rel_path}"
    return diff


@pytest.fixture()
def manifest() -> dict:
    return av.load_manifest()


def _keep_record_for(baseline_rev: str) -> dict:
    rec = _load("experiment_record_valid_keep_candidate.json")
    rec["baseline_revision"] = baseline_rev
    return rec


class _JsonlAdapterFactory:
    """Builds a temp JSONL observation file + JSONLResponseAdapter, fully
    local, no network."""

    def __init__(self, tmp_path: Path) -> None:
        self._path = tmp_path / "observations.jsonl"

    def write(self, rows: list[dict]) -> "sr.JSONLResponseAdapter":
        with self._path.open("w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row) + "\n")
        return sr.JSONLResponseAdapter(self._path)


def _full_observation_rows(experiment_id: str, case_ids: list[str], cfg: dict | None = None) -> list[dict]:
    rows = []
    for case_id in case_ids:
        for condition in ("baseline", "candidate"):
            row = {"experiment_id": experiment_id, "condition": condition, "case_id": case_id, "response": f"{condition} response for {case_id}"}
            if cfg is not None:
                row["runtime_model_configuration"] = cfg
            rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Isolation: candidate applies only in isolated worktree; parent unchanged
# ---------------------------------------------------------------------------


def test_worktree_created_at_baseline_and_removed_after(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    work_dir = tmp_path / "shadow"
    shadow = sr.create_shadow_worktree(repo, baseline_rev, work_dir)
    assert shadow.is_dir()
    assert (shadow / "ROUTING_RULES.md").is_file()
    head = _git(["rev-parse", "HEAD"], cwd=shadow).stdout.strip()
    assert head == baseline_rev
    sr.remove_shadow_worktree(repo, shadow)
    assert not shadow.exists()
    listing = _git(["worktree", "list"], cwd=repo).stdout
    assert str(shadow) not in listing


def test_parent_tree_unchanged_after_full_run(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    before = sr.parent_tree_fingerprint(repo)
    record = _keep_record_for(baseline_rev)
    patch = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("Coding task preparation", "Coding task preparation (clarified)"))
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write(_full_observation_rows(record["experiment_id"], ["CASE-1"]))
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    after = sr.parent_tree_fingerprint(repo)
    assert before == after
    assert result.status == "ready_for_validation"
    assert result.shadow_worktree is not None
    assert not result.shadow_worktree.exists(), "shadow worktree must be cleaned up after the run"


# ---------------------------------------------------------------------------
# Fingerprint mismatch fails before any worktree/application
# ---------------------------------------------------------------------------


def test_fingerprint_mismatch_rejected_before_worktree(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    patch = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("blocked", "blocked (edited)"))
    record["candidate_patch_hash"] = "0" * 64  # deliberately wrong
    adapter = _JsonlAdapterFactory(tmp_path).write([])
    listing_before = _git(["worktree", "list"], cwd=repo).stdout
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "rejected"
    assert any(f.rule == "FINGERPRINT_MISMATCH" for f in result.findings)
    listing_after = _git(["worktree", "list"], cwd=repo).stdout
    assert listing_before == listing_after, "no worktree should have been created"


# ---------------------------------------------------------------------------
# protected-path and out-of-anchor mismatch fail before application
# ---------------------------------------------------------------------------


def test_patch_outside_declared_file_rejected(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    patch = _make_patch(repo, "HANDOFF_STYLE_STANDARD.md", "# Handoff\n\n## Project-Specific Additions\n\nnew text\n")
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write([])
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "rejected"
    assert any(f.rule == "INV-01" for f in result.findings)


def test_patch_touching_protected_table_in_same_file_rejected(scratch_repo, tmp_path):
    """The real safety-critical case: research_surface declares only the
    tie-break table (MUT-ROUTING-TIEBREAK), but the patch also edits the
    protected destination table earlier in the SAME file."""
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    new_content = ROUTING_CONTENT.replace("`[AI OS]` |", "`[AI OS] MOVED]` |").replace(
        "Still ambiguous | `blocked`", "Still ambiguous | `blocked` (clarified)"
    )
    patch = _make_patch(repo, "ROUTING_RULES.md", new_content)
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write([])
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "rejected"
    assert any(f.rule == "INV-01" for f in result.findings)


def test_patch_confined_to_declared_anchor_passes_scope_check(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    new_content = ROUTING_CONTENT.replace("Still ambiguous | `blocked`", "Still ambiguous | `blocked` (clarified wording)")
    patch = _make_patch(repo, "ROUTING_RULES.md", new_content)
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write(_full_observation_rows(record["experiment_id"], ["CASE-1"]))
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "ready_for_validation", result.findings


# ---------------------------------------------------------------------------
# two independent mutations (multi-file) fail
# ---------------------------------------------------------------------------


def test_multi_file_patch_rejected(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    _git(["add", "-A"], cwd=repo)  # no-op safety
    (repo / "ROUTING_RULES.md").write_text(ROUTING_CONTENT.replace("blocked", "blocked (a)"), encoding="utf-8")
    (repo / "ChatGPT" / "[AI OS]" / "PROJECT_INSTRUCTIONS.md").write_text(
        AIOS_INSTRUCTIONS_CONTENT.replace("old first item", "new first item"), encoding="utf-8"
    )
    diff = _git(["diff", "--", "ROUTING_RULES.md", "ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md"], cwd=repo).stdout
    _git(["checkout", "--", "."], cwd=repo)
    assert diff
    record["candidate_patch_hash"] = sr.sha256_hex(diff.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write([])
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=diff, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "rejected"
    assert any(f.rule == "INV-01" for f in result.findings)  # first file already rejects on "outside" check


# ---------------------------------------------------------------------------
# baseline/candidate config mismatch blocks comparison -> inconclusive
# ---------------------------------------------------------------------------


def test_config_mismatch_yields_inconclusive(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    patch = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("blocked", "blocked (b)"))
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))
    rows = _full_observation_rows(record["experiment_id"], ["CASE-1"], cfg={"model_id": "m1"})
    for row in rows:
        if row["condition"] == "candidate":
            row["runtime_model_configuration"] = {"model_id": "m2"}
    adapter = _JsonlAdapterFactory(tmp_path).write(rows)
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "inconclusive"
    assert any(f.rule == "CONFIG_MISMATCH" for f in result.findings)


def test_missing_observation_yields_inconclusive(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    patch = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("blocked", "blocked (c)"))
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write([])  # no observations at all
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "inconclusive"
    assert any(f.rule == "MISSING_OBSERVATION" for f in result.findings)


def test_worktree_create_failure_yields_inconclusive(scratch_repo, tmp_path):
    repo, _baseline_rev = scratch_repo
    record = _keep_record_for("0" * 40)  # a revision that does not exist
    patch = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("blocked", "blocked (d)"))
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write([])
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "inconclusive"
    assert any(f.rule == "WORKTREE_CREATE_FAILED" for f in result.findings)


def test_patch_that_does_not_apply_yields_inconclusive(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    bogus_patch = (
        "diff --git a/ROUTING_RULES.md b/ROUTING_RULES.md\n"
        "--- a/ROUTING_RULES.md\n+++ b/ROUTING_RULES.md\n"
        "@@ -9999,1 +9999,1 @@\n-nonexistent line\n+replacement\n"
    )
    record["candidate_patch_hash"] = sr.sha256_hex(bogus_patch.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write([])
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=bogus_patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "inconclusive"
    assert any(f.rule == "PATCH_DOES_NOT_APPLY" for f in result.findings)


# ---------------------------------------------------------------------------
# one experiment cannot contain two candidates (integration with #392's
# duplicate-without-correction ledger rule)
# ---------------------------------------------------------------------------


def test_one_experiment_cannot_contain_two_candidates(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    patch_a = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("blocked", "blocked (candidate A)"))
    record["candidate_patch_hash"] = sr.sha256_hex(patch_a.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write(_full_observation_rows(record["experiment_id"], ["CASE-1"]))
    result_a = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch_a, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result_a.status == "ready_for_validation"

    ledger = tmp_path / "ledger.jsonl"
    batch = _load("batch_manifest_valid.json")
    batch["baseline"]["source_revision"] = baseline_rev
    record["eval_manifest"]["evaluator_hash"] = batch["frozen_hashes"]["evaluator_hash"]
    record["eval_manifest"]["split_hash"] = batch["frozen_hashes"]["split_hash"]
    record["eval_manifest"]["threshold_hash"] = batch["frozen_hashes"]["threshold_hash"]
    findings_first = av.ledger_append(ledger, record, av.load_manifest(), batch)
    assert findings_first == []

    # A second, different candidate patch under the SAME experiment_id,
    # without correction_of, must be rejected by the ledger -- proving
    # "one experiment cannot contain two candidates".
    same_id_second_candidate = dict(record)
    patch_b = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("blocked", "blocked (candidate B, different!)"))
    same_id_second_candidate["candidate_patch_hash"] = sr.sha256_hex(patch_b.encode("utf-8"))
    findings_second = av.ledger_append(ledger, same_id_second_candidate, av.load_manifest(), batch)
    assert any(f.rule == "DUPLICATE_WITHOUT_CORRECTION" for f in findings_second)


# ---------------------------------------------------------------------------
# interrupted execution leaves recoverable cleanup state; cleanup never
# deletes evidence living outside the shadow worktree
# ---------------------------------------------------------------------------


def test_interrupted_execution_still_cleans_up(scratch_repo, tmp_path, monkeypatch):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    patch = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("blocked", "blocked (interrupt test)"))
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))

    def _raising_adapter(experiment_id, condition, case_id):
        raise RuntimeError("simulated interruption during observation collection")

    with pytest.raises(RuntimeError, match="simulated interruption"):
        sr.run_shadow_experiment(
            repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
            patch_text=patch, adapter=_raising_adapter, case_ids=["CASE-1"],
        )

    # the finally-block cleanup must still have removed the shadow worktree
    listing = _git(["worktree", "list"], cwd=repo).stdout
    assert "shadow" not in listing or listing.count("\n") <= 1
    after = sr.parent_tree_fingerprint(repo)
    # a fresh scratch_repo fixture instance has no prior fingerprint to
    # compare against here, but the parent HEAD must still be baseline_rev
    head = _git(["rev-parse", "HEAD"], cwd=repo).stdout.strip()
    assert head == baseline_rev


def test_cleanup_never_deletes_evidence_outside_worktree(scratch_repo, tmp_path):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    patch = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("blocked", "blocked (evidence test)"))
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write(_full_observation_rows(record["experiment_id"], ["CASE-1"]))

    evidence_dir = tmp_path / "evidence"
    evidence_dir.mkdir()
    ledger = evidence_dir / "ledger.jsonl"
    ledger.write_text('{"pre-existing": "evidence"}\n', encoding="utf-8")

    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "ready_for_validation"
    assert ledger.exists()
    assert "pre-existing" in ledger.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# provider-neutral fixture import is deterministic; no network call in tests
# ---------------------------------------------------------------------------


def test_committed_observations_example_is_valid_and_deterministic():
    """The committed example doubles as the documented provider-neutral
    input/output contract: one JSON object per line, keyed by
    (experiment_id, condition, case_id), no network I/O involved in
    producing or reading it."""
    adapter = sr.JSONLResponseAdapter(FIXTURES / "observations_example.jsonl")
    first = adapter("AUTORESEARCH-batch-001-1", "baseline", "AR-CASE-ROUTING-001")
    second = adapter("AUTORESEARCH-batch-001-1", "baseline", "AR-CASE-ROUTING-001")
    assert first == second
    assert first["response"]
    assert adapter("AUTORESEARCH-batch-001-1", "candidate", "AR-CASE-ROUTING-001") is not None
    assert adapter("AUTORESEARCH-batch-001-1", "baseline", "NO-SUCH-CASE") is None


def test_jsonl_adapter_import_is_deterministic(tmp_path):
    rows = _full_observation_rows("AUTORESEARCH-batch-x-1", ["CASE-1", "CASE-2"])
    adapter = _JsonlAdapterFactory(tmp_path).write(rows)
    first = {(c,): adapter("AUTORESEARCH-batch-x-1", "baseline", c) for c in ("CASE-1", "CASE-2")}
    second = {(c,): adapter("AUTORESEARCH-batch-x-1", "baseline", c) for c in ("CASE-1", "CASE-2")}
    assert first == second


def test_alternation_order_is_deterministic_for_same_seed():
    a = sr.alternation_order("AUTORESEARCH-batch-x-1", seed=7)
    b = sr.alternation_order("AUTORESEARCH-batch-x-1", seed=7)
    assert a == b
    assert set(a) == {"baseline", "candidate"}


def test_no_network_import_in_shadow_runner_module():
    source = (REPO_ROOT / "scripts" / "autoresearch_shadow_runner.py").read_text(encoding="utf-8")
    for forbidden in ("import requests", "import httpx", "urllib.request", "socket.create_connection", "http.client"):
        assert forbidden not in source, f"shadow runner must not import a network transport ({forbidden!r} found)"


def test_socket_is_never_touched_during_a_full_run(scratch_repo, tmp_path, monkeypatch):
    repo, baseline_rev = scratch_repo
    record = _keep_record_for(baseline_rev)
    record["research_surface"] = "MUT-ROUTING-TIEBREAK"
    patch = _make_patch(repo, "ROUTING_RULES.md", ROUTING_CONTENT.replace("blocked", "blocked (no network)"))
    record["candidate_patch_hash"] = sr.sha256_hex(patch.encode("utf-8"))
    adapter = _JsonlAdapterFactory(tmp_path).write(_full_observation_rows(record["experiment_id"], ["CASE-1"]))

    def _forbidden_connect(*args, **kwargs):
        raise AssertionError("no socket connection should occur during a shadow run")

    monkeypatch.setattr(socket.socket, "connect", _forbidden_connect)
    result = sr.run_shadow_experiment(
        repo_root=repo, experiment_record=record, manifest=av.load_manifest(),
        patch_text=patch, adapter=adapter, case_ids=["CASE-1"],
    )
    assert result.status == "ready_for_validation"
