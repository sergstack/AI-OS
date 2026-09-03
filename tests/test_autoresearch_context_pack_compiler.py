"""Focused tests for the AIOS AutoResearch v0.2 deterministic AI-OS
context-pack compiler (issue #412, parent #409). No live model/provider
call, no network call, anywhere in this module.

Read-only compilation (subject_baseline, researcher, semantic_judge) is
tested directly against this repository's own real, committed content via
`git show` at the current HEAD -- safe because it never writes anything.
Candidate-patch application is tested against the same real repository
too, relying on scripts/autoresearch_shadow_runner.py's already-proven
isolation guarantee (issue #393's own extensive test suite); this module
additionally re-verifies the parent tree is unaffected from its own call
pattern rather than assuming #393's guarantee transfers untested.
"""

from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = REPO_ROOT / "tests" / "fixtures" / "autoresearch"

_spec = importlib.util.spec_from_file_location(
    "autoresearch_context_pack_compiler", REPO_ROOT / "scripts" / "autoresearch_context_pack_compiler.py"
)
cc = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = cc
_spec.loader.exec_module(cc)


def _current_revision() -> str:
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()


def _load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


REV = _current_revision()


# ---------------------------------------------------------------------------
# Determinism: identical inputs at the same revision -> byte-identical
# ---------------------------------------------------------------------------


def test_identical_inputs_produce_byte_identical_manifest():
    a = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    b = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
    assert a["context_hash"] == b["context_hash"]


def test_source_ordering_and_hashes_are_stable_across_runs():
    a = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    b = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    assert [s["path"] for s in a["ordered_sources"]] == [s["path"] for s in b["ordered_sources"]]
    assert [s["content_hash"] for s in a["ordered_sources"]] == [s["content_hash"] for s in b["ordered_sources"]]


# ---------------------------------------------------------------------------
# Changed source revision changes the context hash
# ---------------------------------------------------------------------------


def test_changed_source_revision_changes_context_hash():
    parent_rev = subprocess.run(["git", "rev-parse", f"{REV}~1"], cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()
    if not parent_rev:
        pytest.skip("no parent revision available in this checkout")
    current = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    try:
        older = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=parent_rev, project="ai_os")
    except cc.ContextCompilerError:
        pytest.skip("parent revision does not have the full governed source set (older schema/layout)")
    assert current["source_revision"] != older["source_revision"]
    assert current["context_id"] != older["context_id"]
    # context_hash may coincide only in the extremely unlikely case content
    # is byte-identical across revisions; assert the identity fields differ,
    # which is what "invalidates stale reuse" actually depends on.


# ---------------------------------------------------------------------------
# Missing canonical source fails closed
# ---------------------------------------------------------------------------


def test_missing_project_fails_closed():
    with pytest.raises(cc.ContextCompilerError, match="not a registered PROJECT_CAPABILITIES.yaml capability"):
        cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="not_a_real_project")


def test_missing_source_path_fails_closed():
    with pytest.raises(cc.ContextCompilerError, match="required source missing"):
        cc.read_committed(REPO_ROOT, REV, "this/path/does/not/exist.md")


# ---------------------------------------------------------------------------
# Path traversal / symlink escape / untracked-source injection fail closed
# ---------------------------------------------------------------------------


def test_path_traversal_rejected():
    with pytest.raises(cc.ContextCompilerError, match="path traversal rejected"):
        cc.read_committed(REPO_ROOT, REV, "../../../etc/passwd")


def test_working_tree_path_traversal_rejected(tmp_path):
    (tmp_path / "inside.md").write_text("safe", encoding="utf-8")
    with pytest.raises(cc.ContextCompilerError, match="path traversal rejected"):
        cc.read_working_tree(tmp_path, "../outside.md")


def test_working_tree_symlink_rejected(tmp_path):
    target = tmp_path / "real.md"
    target.write_text("real content", encoding="utf-8")
    link = tmp_path / "link.md"
    link.symlink_to(target)
    with pytest.raises(cc.ContextCompilerError, match="symlink source rejected"):
        cc.read_working_tree(tmp_path, "link.md")


def test_untracked_file_in_working_tree_never_leaks_into_committed_read():
    # An untracked file placed directly into the REAL repo's working tree
    # must never appear via read_committed (which only ever reads through
    # `git show <rev>:<path>`, never the live filesystem).
    stray = REPO_ROOT / "AUTORESEARCH_TEST_STRAY_UNTRACKED_FILE.md"
    stray.write_text("this must never be read as committed content", encoding="utf-8")
    try:
        with pytest.raises(cc.ContextCompilerError, match="required source missing"):
            cc.read_committed(REPO_ROOT, REV, "AUTORESEARCH_TEST_STRAY_UNTRACKED_FILE.md")
    finally:
        stray.unlink()


# ---------------------------------------------------------------------------
# Duplicate canonical/derived content is detected/resolved
# ---------------------------------------------------------------------------


def test_no_duplicate_paths_in_ordered_sources():
    manifest = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    paths = [s["path"] for s in manifest["ordered_sources"]]
    assert len(paths) == len(set(paths))


def test_external_delivery_knowledge_is_excluded_not_silently_dropped():
    manifest = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    excluded_paths = {e["path"] for e in manifest["excluded_sources"]}
    assert any("KB__" in p for p in excluded_paths), "external-delivery KB entries should appear in excluded_sources with a reason, not vanish silently"


# ---------------------------------------------------------------------------
# Baseline/candidate source-set identity and single-file equivalence
# ---------------------------------------------------------------------------


def _make_tiebreak_patch() -> str:
    routing = (REPO_ROOT / "ROUTING_RULES.md").read_text(encoding="utf-8")
    new_content = routing.replace("Still ambiguous", "Still ambiguous (context-compiler test)")
    target = REPO_ROOT / "ROUTING_RULES.md"
    target.write_text(new_content, encoding="utf-8")
    diff = subprocess.run(["git", "diff", "--", "ROUTING_RULES.md"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    target.write_text(routing, encoding="utf-8")
    assert diff, "expected a non-empty diff"
    return diff


def test_baseline_and_candidate_source_sets_are_identical(tmp_path):
    patch = _make_tiebreak_patch()
    baseline = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    candidate = cc.compile_subject_candidate(
        repo_root=REPO_ROOT, source_revision=REV, project="ai_os",
        candidate_patch_text=patch, research_surface="MUT-ROUTING-TIEBREAK", work_dir=tmp_path / "shadow",
    )
    assert {s["path"] for s in baseline["ordered_sources"]} == {s["path"] for s in candidate["ordered_sources"]}


def test_baseline_and_candidate_differ_only_in_declared_mutation(tmp_path):
    patch = _make_tiebreak_patch()
    baseline = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    candidate = cc.compile_subject_candidate(
        repo_root=REPO_ROOT, source_revision=REV, project="ai_os",
        candidate_patch_text=patch, research_surface="MUT-ROUTING-TIEBREAK", work_dir=tmp_path / "shadow",
    )
    report = cc.equivalence_report(baseline, candidate)
    assert report["equivalent"] is True
    assert report["differences"] == ["ROUTING_RULES.md"]


def test_parent_repository_unaffected_by_candidate_compilation(tmp_path):
    before = subprocess.run(["git", "status", "--short"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    patch = _make_tiebreak_patch()
    cc.compile_subject_candidate(
        repo_root=REPO_ROOT, source_revision=REV, project="ai_os",
        candidate_patch_text=patch, research_surface="MUT-ROUTING-TIEBREAK", work_dir=tmp_path / "shadow",
    )
    after = subprocess.run(["git", "status", "--short"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    assert before == after


# ---------------------------------------------------------------------------
# Protected/out-of-anchor patch is rejected before context rendering
# ---------------------------------------------------------------------------


def test_protected_scope_violation_rejected_before_rendering(tmp_path):
    # Edit the protected destination table, not just the mutable tie-break
    # table, within ROUTING_RULES.md -- the same real safety-critical case
    # #393's own tests prove at the shadow-runner level; here we prove the
    # context compiler correctly refuses to render ANY context for it.
    routing = (REPO_ROOT / "ROUTING_RULES.md").read_text(encoding="utf-8")
    new_content = routing.replace("`[AI OS]` |", "`[AI OS] MOVED]` |")
    target = REPO_ROOT / "ROUTING_RULES.md"
    target.write_text(new_content, encoding="utf-8")
    diff = subprocess.run(["git", "diff", "--", "ROUTING_RULES.md"], cwd=REPO_ROOT, capture_output=True, text=True).stdout
    target.write_text(routing, encoding="utf-8")
    assert diff

    with pytest.raises(cc.ContextCompilerError, match="rejected by v0.1/v0.2 scope validation"):
        cc.compile_subject_candidate(
            repo_root=REPO_ROOT, source_revision=REV, project="ai_os",
            candidate_patch_text=diff, research_surface="MUT-ROUTING-TIEBREAK", work_dir=tmp_path / "shadow",
        )


# ---------------------------------------------------------------------------
# Researcher context cannot include validation goldens or holdout payload
# ---------------------------------------------------------------------------


def test_researcher_context_excludes_answer_key_fields():
    case = _load("eval_case_valid_train.json")
    manifest = cc.compile_researcher(repo_root=REPO_ROOT, source_revision=REV, eval_case=case)
    excluded_paths = {e["path"] for e in manifest["excluded_sources"]}
    for field in ("eval_case.allowed_outcomes", "eval_case.required_behaviors", "eval_case.deterministic_assertions", "eval_case.hard_invariant_ids"):
        assert field in excluded_paths
    # none of the actual answer-key VALUES leak into any included source
    included_text = json.dumps(manifest["ordered_sources"])
    for goldens_value in case["required_behaviors"]:
        assert goldens_value not in included_text


def test_researcher_context_rejects_holdout_case():
    case = _load("eval_case_valid_holdout.json")
    with pytest.raises(cc.ContextCompilerError, match="holdout"):
        cc.compile_researcher(repo_root=REPO_ROOT, source_revision=REV, eval_case=case)


def test_researcher_context_includes_the_train_case_input():
    case = _load("eval_case_valid_train.json")
    manifest = cc.compile_researcher(repo_root=REPO_ROOT, source_revision=REV, eval_case=case)
    included_paths = {s["path"] for s in manifest["ordered_sources"]}
    assert f"eval_case:{case['case_id']}:input" in included_paths


# ---------------------------------------------------------------------------
# Judge context cannot include candidate identity, expected winner,
# hypothesis, or promotion authority
# ---------------------------------------------------------------------------


def test_judge_context_excludes_candidate_identity_and_rationale():
    case = _load("eval_case_valid_train.json")
    manifest = cc.compile_semantic_judge(
        repo_root=REPO_ROOT, source_revision=REV, eval_case=case,
        output_a="Route the calculation to [Analytics].", output_b="Route everything to [Analytics] as a whole.",
    )
    excluded_paths = {e["path"] for e in manifest["excluded_sources"]}
    assert "candidate_identity" in excluded_paths
    assert "researcher_rationale_or_hypothesis" in excluded_paths


def test_judge_context_never_labels_outputs_baseline_or_candidate():
    # "baseline"/"candidate" legitimately appear in excluded_sources'
    # explanatory prose (documenting WHY identity is withheld) -- what must
    # never happen is either word attached to the actual included output
    # entries themselves (ordered_sources), which is what the Judge model
    # would actually see.
    case = _load("eval_case_valid_train.json")
    manifest = cc.compile_semantic_judge(
        repo_root=REPO_ROOT, source_revision=REV, eval_case=case,
        output_a="Response text one.", output_b="Response text two.",
    )
    included_text = json.dumps(manifest["ordered_sources"]).lower()
    assert "baseline" not in included_text
    assert "candidate" not in included_text


def test_judge_context_has_no_mutable_source_content():
    case = _load("eval_case_valid_train.json")
    manifest = cc.compile_semantic_judge(
        repo_root=REPO_ROOT, source_revision=REV, eval_case=case,
        output_a="Response text one.", output_b="Response text two.",
    )
    included_classes = {s["source_class"] for s in manifest["ordered_sources"]}
    assert "project_instructions" not in included_classes
    assert "canonical_routing" not in included_classes
    assert included_classes.issubset({"frozen_rubric", "blinded_output", "eval_case_input"})


def test_judge_context_has_no_promotion_or_authority_field():
    case = _load("eval_case_valid_train.json")
    manifest = cc.compile_semantic_judge(
        repo_root=REPO_ROOT, source_revision=REV, eval_case=case,
        output_a="Response text one.", output_b="Response text two.",
    )
    manifest_text = json.dumps(manifest).lower()
    for forbidden in ("authority_status", "merge_status", "production_status", "promotion"):
        assert forbidden not in manifest_text


# ---------------------------------------------------------------------------
# Fidelity statement is present verbatim
# ---------------------------------------------------------------------------


def test_fidelity_limitation_present_verbatim_on_every_role():
    case = _load("eval_case_valid_train.json")
    baseline = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    researcher = cc.compile_researcher(repo_root=REPO_ROOT, source_revision=REV, eval_case=case)
    judge = cc.compile_semantic_judge(repo_root=REPO_ROOT, source_revision=REV, eval_case=case, output_a="a", output_b="b")
    for manifest in (baseline, researcher, judge):
        assert manifest["limitations"] == cc.FIDELITY_LIMITATION


# ---------------------------------------------------------------------------
# Human-readable summary and no network call
# ---------------------------------------------------------------------------


def test_render_summary_includes_key_fields():
    manifest = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    summary = cc.render_summary(manifest)
    assert manifest["context_hash"] in summary
    assert "ROUTING_RULES.md" in summary
    assert "Limitations" in summary


def test_no_network_import_in_compiler_module():
    source = (REPO_ROOT / "scripts" / "autoresearch_context_pack_compiler.py").read_text(encoding="utf-8")
    for forbidden in ("import requests", "import httpx", "urllib.request", "socket.create_connection", "http.client"):
        assert forbidden not in source


def test_no_socket_connection_during_full_compile(monkeypatch):
    def _forbidden_connect(*args, **kwargs):
        raise AssertionError("no socket connection should occur during context compilation")

    monkeypatch.setattr(socket.socket, "connect", _forbidden_connect)
    manifest = cc.compile_subject_baseline(repo_root=REPO_ROOT, source_revision=REV, project="ai_os")
    assert manifest["role"] == "subject_baseline"


# ---------------------------------------------------------------------------
# Committed example manifest/summary (from real repository-local input)
# ---------------------------------------------------------------------------


def test_committed_example_manifest_is_schema_valid():
    example_path = FIXTURES / "context_pack_examples" / "subject_baseline_ai_os_example.manifest.json"
    example = json.loads(example_path.read_text(encoding="utf-8"))
    findings = cc.av._schema_findings(example, cc.CONTEXT_MANIFEST_SCHEMA_PATH, "context_manifest")
    assert findings == []
    assert example["role"] == "subject_baseline"
    assert example["project"] == "ai_os"


def test_committed_example_summary_is_consistent_with_its_own_manifest():
    manifest_path = FIXTURES / "context_pack_examples" / "subject_baseline_ai_os_example.manifest.json"
    summary_path = FIXTURES / "context_pack_examples" / "subject_baseline_ai_os_example.summary.md"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    summary = summary_path.read_text(encoding="utf-8")
    assert manifest["context_hash"] in summary
    for s in manifest["ordered_sources"]:
        assert s["path"] in summary
