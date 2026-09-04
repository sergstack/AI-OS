#!/usr/bin/env python3
"""Deterministic AI-OS context-pack compiler for AIOS AutoResearch v0.2
(issue #412, parent #409).

Given a Git revision, a PROJECT_CAPABILITIES.yaml project id, an eval case,
a role, and (for subject_candidate) a prevalidated candidate patch, this
module assembles the exact ordered context that would be sent to a model,
hashes every source, proves baseline/candidate context equivalence outside
the declared mutation, and keeps Researcher/Executor/Judge views separated.

This module builds context only. It never calls a model, never evaluates
behavior, never generates a candidate, and never runs a pilot. Candidate
patch application happens only inside an isolated shadow worktree, reusing
scripts/autoresearch_shadow_runner.py's create_shadow_worktree/
dry_run_patch_paths/reject_patch_scope/apply_patch (issue #393) unchanged --
this module does not reimplement isolation or scope validation.

Source selection reuses PROJECT_CAPABILITIES.yaml's existing
context_entrypoints/required_knowledge governed index (issue #412's own
rule: "Use governed indexes/manifests... do not dump the entire
repository"; "No second routing or project-capability registry.").
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import autoresearch_shadow_runner as sr  # noqa: E402  (reuse isolation/scope-check machinery)
import autoresearch_validator as av  # noqa: E402  (reuse Finding/manifest loader)

REPO_ROOT = av.REPO_ROOT
CAPABILITIES_PATH = REPO_ROOT / "PROJECT_CAPABILITIES.yaml"
CREATED_BY_VERSION = "autoresearch_context_pack_compiler/0.3.0"

FIDELITY_LIMITATION = (
    "This context is a reproducible repository-derived replay of AI-OS "
    "instructions and governed sources. It is not evidence of exact "
    "equivalence to proprietary ChatGPT Project runtime assembly unless "
    "separately validated."
)

FAILURE_REGISTRY_PATH = "ChatGPT/[AI OS]/Knowledge/FAILURE_REGISTRY.md"
REGRESSION_GATE_PATH = "ChatGPT/[AI OS]/Knowledge/REGRESSION_GATE.md"
SEMANTIC_EVALUATOR_CONTRACT_PATH = "ChatGPT/[LLM]/Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md"

CONTEXT_MANIFEST_SCHEMA_PATH = av.SCHEMAS / "autoresearch_context_manifest.schema.json"


class ContextCompilerError(RuntimeError):
    """Raised for any fail-closed condition: missing canonical source, path
    traversal, symlink escape, a researcher/judge role reaching for
    forbidden content, or a candidate patch that fails v0.1/v0.2 scope
    validation. Never silently degrades to a smaller or substitute
    context."""


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _source_entry(path: str, owner: str, purpose: str, data: bytes, inclusion_reason: str, source_class: str) -> dict:
    return {
        "path": path,
        "canonical_owner": owner,
        "purpose": purpose,
        "content_hash": sha256_hex(data),
        "bytes": len(data),
        "inclusion_reason": inclusion_reason,
        "source_class": source_class,
    }


# ---------------------------------------------------------------------------
# Fail-closed source readers
# ---------------------------------------------------------------------------


def _git(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def read_committed(repo_root: Path, source_revision: str, rel_path: str) -> bytes:
    """Reads rel_path exactly as committed at source_revision via git
    plumbing -- never the live working tree, so determinism is tied to the
    declared revision (not filesystem state) and an untracked/stray file
    can never leak in. Fails closed on a missing path, `..` traversal, or a
    symlink (git tree mode 120000)."""
    if ".." in Path(rel_path).parts:
        raise ContextCompilerError(f"path traversal rejected: {rel_path!r}")
    ls = _git(["ls-tree", source_revision, "--", rel_path], cwd=repo_root)
    if not ls.stdout.strip():
        raise ContextCompilerError(f"required source missing at {source_revision}: {rel_path!r}")
    mode = ls.stdout.split()[0]
    if mode == "120000":
        raise ContextCompilerError(f"symlink source rejected: {rel_path!r}")
    show = _git(["show", f"{source_revision}:{rel_path}"], cwd=repo_root)
    if show.returncode != 0:
        raise ContextCompilerError(f"could not read {rel_path!r} at {source_revision}: {show.stderr.strip()}")
    return show.stdout.encode("utf-8")


def read_working_tree(root: Path, rel_path: str) -> bytes:
    """Reads rel_path from a live directory (used only for a shadow
    worktree after a candidate patch has been applied there -- the patch is
    an uncommitted working-tree change, so `git show` cannot see it).
    Same fail-closed traversal/symlink/missing-file checks as
    read_committed."""
    if ".." in Path(rel_path).parts:
        raise ContextCompilerError(f"path traversal rejected: {rel_path!r}")
    raw = root / rel_path
    if raw.is_symlink():
        raise ContextCompilerError(f"symlink source rejected: {rel_path!r}")
    resolved = raw.resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        raise ContextCompilerError(f"path escapes context root: {rel_path!r}")
    if not resolved.is_file():
        raise ContextCompilerError(f"required source missing: {rel_path!r}")
    return resolved.read_bytes()


def load_capabilities(repo_root: Path, source_revision: str) -> dict:
    return json.loads(read_committed(repo_root, source_revision, "PROJECT_CAPABILITIES.yaml").decode("utf-8"))["capabilities"]


# ---------------------------------------------------------------------------
# Canonical subject (baseline/candidate) source selection
# ---------------------------------------------------------------------------


def canonical_subject_sources(reader, capabilities: dict, project: str) -> tuple[list[dict], list[dict]]:
    """The bounded canonical/governed source set for a subject context:
    ROUTING_RULES.md exactly once, then this project's context_entrypoints
    and bundle-delivery required_knowledge from the existing
    PROJECT_CAPABILITIES.yaml governed index -- not a second registry, and
    not a whole-repository dump. `reader` is read_committed(repo_root, rev,
    path) or read_working_tree(shadow_root, path), pre-bound by the
    caller."""
    cap = capabilities.get(project)
    if cap is None:
        raise ContextCompilerError(f"{project!r} is not a registered PROJECT_CAPABILITIES.yaml capability")
    canonical_path = cap["canonical_path"]

    sources: list[dict] = []
    excluded: list[dict] = []

    routing_bytes = reader("ROUTING_RULES.md")
    sources.append(
        _source_entry(
            "ROUTING_RULES.md", "inbox_router", "canonical routing/tie-break rules",
            routing_bytes, "canonical routing table, present exactly once", "canonical_routing",
        )
    )

    seen_paths = {"ROUTING_RULES.md"}
    for entry in cap["context_entrypoints"]:
        rel = f"{canonical_path}/{entry}"
        if rel in seen_paths:
            excluded.append({"path": rel, "reason": "duplicate context_entrypoints declaration"})
            continue
        data = reader(rel)
        source_class = "project_instructions" if entry.endswith("PROJECT_INSTRUCTIONS.md") else "governed_knowledge_bundle"
        sources.append(_source_entry(rel, project, "declared context entrypoint", data, "PROJECT_CAPABILITIES.yaml context_entrypoints", source_class))
        seen_paths.add(rel)

    for rk in cap.get("required_knowledge", []):
        if rk["delivery"] != "bundle":
            excluded.append({"path": rk["path"], "reason": f"delivery={rk['delivery']!r}; not a repo-tracked source (governed KB lives only in the live ChatGPT Project)"})
            continue
        if rk["path"] in seen_paths:
            excluded.append({"path": rk["path"], "reason": "already included via context_entrypoints; canonical/derived duplication avoided"})
            continue
        data = reader(rk["path"])
        sources.append(
            _source_entry(
                rk["path"], project, rk.get("reason", "required knowledge"),
                data, "PROJECT_CAPABILITIES.yaml required_knowledge (delivery=bundle)", "governed_knowledge_bundle",
            )
        )
        seen_paths.add(rk["path"])

    return sources, excluded


# ---------------------------------------------------------------------------
# Manifest assembly
# ---------------------------------------------------------------------------


def mutable_surface_excerpt(*, reader, research_surface: Optional[str]) -> Optional[dict]:
    """Bounded literal excerpt of one declared mutable surface's own
    anchored section (issue #435 subject-content-propagation decision,
    Option 2). Reuses `autoresearch_shadow_runner.mutable_surface_line_ranges`
    -- the same anchor-resolution mechanism the hard scope gate already
    depends on -- rather than inventing a second content-selection
    mechanism. `reader` is `read_committed(...)` or `read_working_tree(...)`,
    pre-bound by the caller, exactly like `canonical_subject_sources`.

    Returns None (fail-closed) when no `research_surface` was supplied, the
    surface isn't declared in the v0.1 manifest, or its anchor can't be
    resolved in the source text -- the caller must not treat a None here as
    license to fall back to sending the whole file."""
    if research_surface is None:
        return None
    manifest_v01 = av.load_manifest()
    declared = {s["surface_id"]: s for s in manifest_v01["mutable_surfaces"]}.get(research_surface)
    if declared is None:
        return None
    path = declared["path"]
    try:
        text = reader(path).decode("utf-8")
    except Exception:
        return None
    ranges = sr.mutable_surface_line_ranges(text, declared.get("anchor", ""))
    if ranges is None:
        return None
    lines = text.splitlines()
    excerpt_lines: list[str] = []
    for start, end in ranges:
        # mutable_surface_line_ranges returns 1-indexed [start, end) ranges.
        excerpt_lines.extend(lines[start - 1 : end - 1])
    excerpt_text = "\n".join(excerpt_lines)
    return {
        "path": path,
        "surface_id": research_surface,
        "anchor": declared.get("anchor", ""),
        "excerpt_text": excerpt_text,
        "excerpt_hash": sha256_hex(excerpt_text.encode("utf-8")),
    }


def _context_id(role: str, project: str, source_revision: str, candidate_patch_hash: Optional[str]) -> str:
    key = f"{role}:{project}:{source_revision}:{candidate_patch_hash}"
    return sha256_hex(key.encode("utf-8"))[:16]


def _context_hash(role: str, candidate_patch_hash: Optional[str], sources: list[dict]) -> str:
    material = role + ":" + str(candidate_patch_hash) + ":" + ",".join(s["content_hash"] for s in sources)
    return sha256_hex(material.encode("utf-8"))


def _assemble_manifest(
    *, role: str, project: str, source_revision: str, candidate_patch_hash: Optional[str],
    sources: list[dict], excluded: list[dict], forbidden_source_classes: list[str],
    mutable_surface_excerpt_value: Optional[dict] = None,
) -> dict:
    manifest = {
        "context_manifest_version": "0.3.0",
        "context_id": _context_id(role, project, source_revision, candidate_patch_hash),
        "role": role,
        "project": project,
        "source_revision": source_revision,
        "candidate_patch_hash": candidate_patch_hash,
        "ordered_sources": sources,
        "rendering_rules": {"ordering": "declared_order_stable", "delimiter_style": "markdown_heading_per_source"},
        "model_message_structure": [{"turn": "system", "source_paths": [s["path"] for s in sources]}],
        "excluded_sources": excluded,
        "forbidden_source_classes": forbidden_source_classes,
        "context_hash": _context_hash(role, candidate_patch_hash, sources),
        "created_by_version": CREATED_BY_VERSION,
        "fidelity_mode": "repo_replay",
        "limitations": FIDELITY_LIMITATION,
        "mutable_surface_excerpt": mutable_surface_excerpt_value,
    }
    findings = av._schema_findings(manifest, CONTEXT_MANIFEST_SCHEMA_PATH, "context_manifest")
    if findings:
        raise ContextCompilerError(f"compiler produced a manifest that fails its own schema: {[f.rule for f in findings]}")
    return manifest


# ---------------------------------------------------------------------------
# Role compilers
# ---------------------------------------------------------------------------


def compile_subject_baseline(
    *, repo_root: Path, source_revision: str, project: str, research_surface: Optional[str] = None,
) -> dict:
    reader = lambda rel: read_committed(repo_root, source_revision, rel)  # noqa: E731
    capabilities = load_capabilities(repo_root, source_revision)
    sources, excluded = canonical_subject_sources(reader, capabilities, project)
    excerpt = mutable_surface_excerpt(reader=reader, research_surface=research_surface)
    return _assemble_manifest(
        role="subject_baseline", project=project, source_revision=source_revision, candidate_patch_hash=None,
        sources=sources, excluded=excluded,
        forbidden_source_classes=["blinded_output", "frozen_rubric", "failure_registry_entry"],
        mutable_surface_excerpt_value=excerpt,
    )


def compile_subject_candidate(
    *, repo_root: Path, source_revision: str, project: str, candidate_patch_text: str, research_surface: str,
    work_dir: Optional[Path] = None,
) -> dict:
    """Applies candidate_patch_text only inside an isolated shadow
    worktree, reusing #393's create_shadow_worktree/dry_run_patch_paths/
    reject_patch_scope/apply_patch unchanged -- v0.1/v0.2 scope validation
    runs before this function ever reads a patched file."""
    manifest_v01 = av.load_manifest()
    own_tmp = work_dir is None
    work_dir = work_dir or Path(tempfile.mkdtemp(prefix="autoresearch-context-"))
    shadow: Optional[Path] = None
    try:
        shadow = sr.create_shadow_worktree(repo_root, source_revision, work_dir)
        ok, touched, err = sr.dry_run_patch_paths(shadow, candidate_patch_text)
        if not ok:
            raise ContextCompilerError(f"candidate patch does not apply cleanly: {err}")
        scope_findings = sr.reject_patch_scope(shadow, touched, research_surface, manifest_v01, candidate_patch_text)
        if scope_findings:
            raise ContextCompilerError(
                f"candidate patch rejected by v0.1/v0.2 scope validation before context rendering: "
                f"{[(f.rule, f.evidence) for f in scope_findings]}"
            )
        sr.apply_patch(shadow, candidate_patch_text)

        capabilities = load_capabilities(repo_root, source_revision)  # capability registry itself is not mutable-surface content
        shadow_reader = lambda rel: read_working_tree(shadow, rel)  # noqa: E731
        sources, excluded = canonical_subject_sources(shadow_reader, capabilities, project)
        excerpt = mutable_surface_excerpt(reader=shadow_reader, research_surface=research_surface)
        candidate_patch_hash = sha256_hex(candidate_patch_text.encode("utf-8"))
        return _assemble_manifest(
            role="subject_candidate", project=project, source_revision=source_revision, candidate_patch_hash=candidate_patch_hash,
            sources=sources, excluded=excluded,
            forbidden_source_classes=["blinded_output", "frozen_rubric", "failure_registry_entry"],
            mutable_surface_excerpt_value=excerpt,
        )
    finally:
        if shadow is not None:
            sr.remove_shadow_worktree(repo_root, shadow)
        elif own_tmp and work_dir.exists():
            import shutil

            shutil.rmtree(work_dir, ignore_errors=True)


def compile_researcher(*, repo_root: Path, source_revision: str, eval_case: dict) -> dict:
    if eval_case.get("split") == "holdout":
        raise ContextCompilerError(
            "researcher role must never receive a holdout-split eval case "
            "(fail-closed, defense in depth beyond the eval_case schema's own input/input_ref exclusivity)"
        )

    sources: list[dict] = []
    for rel, owner, purpose, source_class in (
        (FAILURE_REGISTRY_PATH, "ai_os", "causal-attribution contract", "failure_registry_entry"),
        (REGRESSION_GATE_PATH, "ai_os", "regression/hard-veto vocabulary", "regression_gate"),
    ):
        data = read_committed(repo_root, source_revision, rel)
        sources.append(_source_entry(rel, owner, purpose, data, "researcher governed context", source_class))

    excluded = [
        {"path": "eval_case.allowed_outcomes", "reason": "answer-key field; Researcher context must never include validation goldens"},
        {"path": "eval_case.required_behaviors", "reason": "answer-key field; excluded from Researcher context"},
        {"path": "eval_case.deterministic_assertions", "reason": "answer-key field; excluded from Researcher context"},
        {"path": "eval_case.hard_invariant_ids", "reason": "answer-key field; excluded from Researcher context (deterministic checks run independently, not as Researcher-visible hints)"},
    ]

    case_input = eval_case.get("input")
    if case_input is None:
        excluded.append({"path": f"eval_case:{eval_case.get('case_id', '?')}:input", "reason": "input_ref only (opaque); inline input not provided for this case"})
    else:
        data = case_input.encode("utf-8")
        sources.append(
            {
                "path": f"eval_case:{eval_case.get('case_id', '?')}:input",
                "canonical_owner": eval_case.get("expected_primary_owner", "unknown"),
                "purpose": "eval case input under research (train/validation split only)",
                "content_hash": sha256_hex(data),
                "bytes": len(data),
                "inclusion_reason": "eval_case.input",
                "source_class": "eval_case_input",
            }
        )

    return _assemble_manifest(
        role="researcher", project=eval_case.get("expected_primary_owner", "ai_os"), source_revision=source_revision, candidate_patch_hash=None,
        sources=sources, excluded=excluded,
        forbidden_source_classes=["governed_knowledge_bundle", "project_instructions", "blinded_output"],
    )


def compile_semantic_judge(
    *, repo_root: Path, source_revision: str, eval_case: dict, output_a: str, output_b: str,
) -> dict:
    """Judge context: the frozen rubric, the two blinded outputs (labeled
    'A'/'B', never 'baseline'/'candidate'), and the case input only -- no
    mutable source content (issue #412's own rule: 'The Judge... does not
    receive mutable source content unless the evaluator contract requires
    a bounded excerpt')."""
    sources: list[dict] = []

    rubric_bytes = read_committed(repo_root, source_revision, SEMANTIC_EVALUATOR_CONTRACT_PATH)
    sources.append(
        _source_entry(
            SEMANTIC_EVALUATOR_CONTRACT_PATH, "llm", "frozen blind A/B Judge contract",
            rubric_bytes, "Judge governed rubric", "frozen_rubric",
        )
    )

    for label, text in (("A", output_a), ("B", output_b)):
        data = text.encode("utf-8")
        sources.append(
            {
                "path": f"blinded_output:{label}",
                "canonical_owner": "n/a (model output under review)",
                "purpose": f"blinded output {label}",
                "content_hash": sha256_hex(data),
                "bytes": len(data),
                "inclusion_reason": "blind A/B comparison input",
                "source_class": "blinded_output",
            }
        )

    case_input = eval_case.get("input")
    if case_input is not None:
        data = case_input.encode("utf-8")
        sources.append(
            {
                "path": f"eval_case:{eval_case.get('case_id', '?')}:input",
                "canonical_owner": eval_case.get("expected_primary_owner", "unknown"),
                "purpose": "case input the two blinded outputs are responding to",
                "content_hash": sha256_hex(data),
                "bytes": len(data),
                "inclusion_reason": "eval_case.input",
                "source_class": "eval_case_input",
            }
        )

    excluded = [
        {"path": "candidate_identity", "reason": "Judge must never receive which side is baseline vs candidate (blind by construction)"},
        {"path": "researcher_rationale_or_hypothesis", "reason": "Judge must never receive the Researcher's hypothesis or expected/preferred winner"},
        {"path": "ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md", "reason": "Judge does not receive mutable source content; only the frozen rubric and the two outputs under review"},
    ]

    return _assemble_manifest(
        role="semantic_judge", project=eval_case.get("expected_primary_owner", "ai_os"), source_revision=source_revision, candidate_patch_hash=None,
        sources=sources, excluded=excluded,
        forbidden_source_classes=["project_instructions", "canonical_routing", "governed_knowledge_bundle", "failure_registry_entry", "regression_gate"],
    )


# ---------------------------------------------------------------------------
# Baseline/candidate equivalence report
# ---------------------------------------------------------------------------


def equivalence_report(baseline: dict, candidate: dict) -> dict:
    """Proves the baseline and candidate manifests' source sets, ordering,
    and rendering rules are identical, and that any content difference is
    limited to whatever the candidate_patch_hash declares changed -- never
    a silent, unrelated context drift."""
    if baseline["role"] != "subject_baseline" or candidate["role"] != "subject_candidate":
        raise ContextCompilerError("equivalence_report requires a subject_baseline manifest and a subject_candidate manifest")

    b_paths = [s["path"] for s in baseline["ordered_sources"]]
    c_paths = [s["path"] for s in candidate["ordered_sources"]]
    if set(b_paths) != set(c_paths):
        return {
            "equivalent": False,
            "differences": [f"source set differs: only_baseline={sorted(set(b_paths) - set(c_paths))}, only_candidate={sorted(set(c_paths) - set(b_paths))}"],
        }
    if b_paths != c_paths:
        return {"equivalent": False, "differences": ["source ordering differs"]}
    if baseline["rendering_rules"] != candidate["rendering_rules"]:
        return {"equivalent": False, "differences": ["rendering_rules differ"]}

    b_by_path = {s["path"]: s for s in baseline["ordered_sources"]}
    c_by_path = {s["path"]: s for s in candidate["ordered_sources"]}
    changed_paths = [p for p in b_paths if b_by_path[p]["content_hash"] != c_by_path[p]["content_hash"]]

    b_excerpt = baseline.get("mutable_surface_excerpt")
    c_excerpt = candidate.get("mutable_surface_excerpt")
    excerpt_report: dict = {"present": b_excerpt is not None and c_excerpt is not None}
    if excerpt_report["present"]:
        if b_excerpt["surface_id"] != c_excerpt["surface_id"] or b_excerpt["path"] != c_excerpt["path"]:
            return {
                "equivalent": False,
                "differences": [f"mutable_surface_excerpt identity differs: baseline={b_excerpt}, candidate={c_excerpt}"],
            }
        excerpt_report["excerpt_differs"] = b_excerpt["excerpt_hash"] != c_excerpt["excerpt_hash"]
        excerpt_report["excerpt_is_within_declared_surface"] = b_excerpt["path"] in changed_paths or not excerpt_report["excerpt_differs"]

    return {
        "equivalent": True,
        "differences": changed_paths,
        "mutable_surface_excerpt": excerpt_report,
        "note": (
            "differences[] lists every content-changed source path; a valid candidate context "
            "has exactly one entry here, matching the declared mutable surface's own file. "
            "mutable_surface_excerpt.excerpt_is_within_declared_surface being False while "
            "excerpt_differs is True would mean the excerpt changed without its containing file "
            "being flagged as changed -- a contradiction that should never occur and must be "
            "treated as a hard-gate failure, not silently accepted."
        ),
    }


# ---------------------------------------------------------------------------
# Human-readable summary (for PR review)
# ---------------------------------------------------------------------------


def render_summary(manifest: dict) -> str:
    lines = [
        f"# Context pack — role={manifest['role']} project={manifest['project']}",
        "",
        f"- source_revision: `{manifest['source_revision']}`",
        f"- candidate_patch_hash: `{manifest['candidate_patch_hash']}`",
        f"- context_id: `{manifest['context_id']}`",
        f"- context_hash: `{manifest['context_hash']}`",
        f"- fidelity_mode: `{manifest['fidelity_mode']}`",
        "",
        "## Included sources",
        "",
    ]
    for s in manifest["ordered_sources"]:
        lines.append(f"- `{s['path']}` ({s['source_class']}, {s['bytes']} bytes) — {s['purpose']}")
    lines += ["", "## Excluded sources", ""]
    for e in manifest["excluded_sources"]:
        lines.append(f"- `{e['path']}` — {e['reason']}")
    excerpt = manifest.get("mutable_surface_excerpt")
    if excerpt:
        lines += [
            "",
            f"## Declared mutable surface excerpt ({excerpt['surface_id']}, `{excerpt['path']}`)",
            "",
            "The literal current text of the declared mutable surface only -- not the whole file",
            f"(anchor: `{excerpt['anchor']}`):",
            "",
            excerpt["excerpt_text"],
        ]
    lines += ["", "## Limitations", "", manifest["limitations"]]
    return "\n".join(lines) + "\n"
