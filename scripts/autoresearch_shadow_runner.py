#!/usr/bin/env python3
"""Provider-neutral shadow runner and isolated-worktree boundary for AIOS
AutoResearch v0.1 (issue #393, parent #388).

One invocation handles one experiment_id and one baseline/candidate pair
(issue #393 Grain). This module never calls a live model/provider API, never
commits/pushes/opens an issue or PR, never merges or deploys, and never
mutates `main`, the parent working tree, or active ChatGPT Project settings.
Provider integration is explicitly out of scope for this child: candidate
and baseline "observations" are consumed through a documented, provider-
neutral adapter -- a JSONL file of pre-generated responses (JSONLResponseAdapter)
or any caller-supplied `AdapterCallable` with the same (experiment_id,
condition, case_id) -> dict | None contract. No adapter implementation in
this module performs network I/O.

Everything this module produces is handed to scripts/autoresearch_validator.py
(issue #392) for the actual accept/reject decision; this module only proves
isolation, patch-scope safety, and observation collection.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

import sys

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import autoresearch_validator as av  # noqa: E402  (reuse Finding/manifest, not reimplemented)


class ShadowRunnerError(RuntimeError):
    """Raised only for a safety-invariant violation this module must never
    silently absorb (e.g. the parent tree changed during a shadow run).
    Ordinary failures (bad patch, missing observation, config mismatch)
    are reported as RunResult(status='inconclusive'|'rejected', ...),
    never as an exception."""


@dataclass(frozen=True)
class RunResult:
    status: str  # "ready_for_validation" | "inconclusive" | "rejected"
    findings: list  # list[av.Finding]
    shadow_worktree: Optional[Path]
    baseline_observations: Optional[dict]
    candidate_observations: Optional[dict]
    notes: str


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _run_git(args: list[str], cwd: Path, input_text: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=cwd, input=input_text, capture_output=True, text=True
    )


# ---------------------------------------------------------------------------
# Isolated ephemeral worktree
# ---------------------------------------------------------------------------


def create_shadow_worktree(repo_root: Path, baseline_revision: str, work_dir: Path) -> Path:
    """Create a detached, isolated worktree of repo_root at baseline_revision.
    Never touches repo_root's own working tree or HEAD."""
    result = _run_git(["worktree", "add", "--detach", str(work_dir), baseline_revision], cwd=repo_root)
    if result.returncode != 0:
        raise ShadowRunnerError(f"worktree add failed: {result.stderr.strip()}")
    return work_dir


def remove_shadow_worktree(repo_root: Path, work_dir: Path) -> None:
    """Scoped cleanup only: `git worktree remove` on this one worktree, then
    a directory removal if anything is left. Never `git reset --hard` on
    repo_root, never touches any path outside work_dir."""
    _run_git(["worktree", "remove", "--force", str(work_dir)], cwd=repo_root)
    if work_dir.exists():
        shutil.rmtree(work_dir, ignore_errors=True)
    _run_git(["worktree", "prune"], cwd=repo_root)


def parent_tree_fingerprint(repo_root: Path) -> str:
    """Deterministic fingerprint of repo_root's own HEAD + working-tree
    status, used to prove the parent tree and `main` were not mutated by
    this module (issue #393's required 'parent tree and main remain
    unchanged' proof). Deliberately excludes `git worktree list`: that
    listing is EXPECTED to change transiently while a shadow worktree
    exists -- that transient registration is the isolation mechanism
    itself, not a mutation of the parent tree's own HEAD or content."""
    head = _run_git(["rev-parse", "HEAD"], cwd=repo_root).stdout.strip()
    status = _run_git(["status", "--short"], cwd=repo_root).stdout
    return sha256_hex((head + "\n" + status).encode("utf-8"))


# ---------------------------------------------------------------------------
# Candidate patch: fingerprint, scope, application
# ---------------------------------------------------------------------------


def verify_patch_fingerprint(patch_text: str, expected_hash: str) -> list[av.Finding]:
    """Required safety rule: candidate patch fingerprint must match the
    preflight record before application. Checked before any worktree is
    touched."""
    actual = sha256_hex(patch_text.encode("utf-8"))
    if actual != expected_hash:
        return [
            av.Finding(
                path="candidate_patch_hash",
                rule="FINGERPRINT_MISMATCH",
                severity="critical",
                evidence=f"declared {expected_hash} != actual patch hash {actual}",
                consequence="reject",
            )
        ]
    return []


def dry_run_patch_paths(shadow_worktree: Path, patch_text: str) -> tuple[bool, list[str], str]:
    """`git apply --check` (does it apply cleanly?) then `--numstat` (which
    paths would it touch?), without actually applying anything yet."""
    check = _run_git(["apply", "--check", "-"], cwd=shadow_worktree, input_text=patch_text)
    if check.returncode != 0:
        return False, [], check.stderr.strip()
    numstat = _run_git(["apply", "--numstat", "-"], cwd=shadow_worktree, input_text=patch_text)
    paths = [line.split("\t")[-1] for line in numstat.stdout.splitlines() if line.strip()]
    return True, paths, ""


_HEADING_RE = re.compile(r"(#{1,6})\s*([^,>()]+)")
_HUNK_HEADER_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))?")


def _extract_leaf_headings(anchor: str) -> list[str]:
    """Extract the markdown heading(s) that actually bound a mutable
    surface's own content, given a manifest anchor string. An anchor of the
    form 'PARENT > CHILD1, CHILD2' (e.g. MUT-AIOS-HANDOFF-WORDING's
    '## 7. Routing > ### Goal Mode handoff, ### Quick Goal Mode') names
    CHILD1/CHILD2 as the mutable leaf sections; the parent heading is
    context only and its own section may contain protected content
    elsewhere (e.g. the 'Маршруты:' destination list earlier in the same
    ## 7. Routing section) -- so only text after the first '>' is used."""
    if ">" in anchor:
        anchor = anchor.split(">", 1)[1]
    heads = []
    for level_marks, text in _HEADING_RE.findall(anchor):
        heads.append(f"{level_marks} {text.strip().rstrip(':').strip()}")
    return heads


def _heading_section_range(file_lines: list[str], heading: str) -> tuple[int, int] | None:
    """1-indexed [start, end) line range for one markdown heading's own
    section: from the heading line itself up to (not including) the next
    heading of equal-or-shallower depth, or end of file."""
    level = len(heading) - len(heading.lstrip("#"))
    start = None
    for i, line in enumerate(file_lines):
        if line.strip() == heading.strip():
            start = i + 1
            break
    if start is None:
        return None
    end = len(file_lines) + 1
    for j in range(start, len(file_lines)):
        line = file_lines[j]
        if line.startswith("#"):
            this_level = len(line) - len(line.lstrip("#"))
            if this_level <= level:
                end = j + 1
                break
    return start, end


def mutable_surface_line_ranges(file_text: str, anchor: str) -> list[tuple[int, int]] | None:
    """Returns None (fail-closed) if any named heading cannot be located in
    file_text -- callers must then reject rather than assume safety."""
    lines = file_text.splitlines()
    headings = _extract_leaf_headings(anchor)
    if not headings:
        return None
    ranges = []
    for h in headings:
        r = _heading_section_range(lines, h)
        if r is None:
            return None
        ranges.append(r)
    return ranges


def hunk_changed_old_lines_for_file(patch_text: str, rel_path: str) -> list[int]:
    """1-indexed OLD-file line numbers that are actually modified by
    `patch_text` for `rel_path` -- deliberately NOT the full contextual hunk
    span (`@@ -a,b @@`'s b), which includes unchanged context lines that
    default `git diff` context (3 lines) can spill past a section boundary
    even when nothing in that neighboring section actually changed. A
    deleted/replaced line is attributed to its own old-line number; a pure
    insertion is attributed to the old-line position immediately before it,
    so an addition at the very start or end of a section is still correctly
    bound to that section."""
    changed: set[int] = set()
    for block in ("\n" + patch_text).split("\ndiff --git "):
        if not block.strip():
            continue
        header = re.search(r"^\+\+\+ (?:b/)?(.+)$", block, re.MULTILINE)
        if not header or rel_path not in header.group(1):
            continue
        old_line: int | None = None
        for line in block.splitlines():
            m = _HUNK_HEADER_RE.match(line)
            if m:
                old_line = int(m.group(1))
                continue
            if old_line is None or line.startswith(("---", "+++")):
                continue
            if line.startswith("-"):
                changed.add(old_line)
                old_line += 1
            elif line.startswith("+"):
                changed.add(max(old_line - 1, 1))
                changed.add(old_line)
                # old_line does not advance: this line has no old-side position
            elif line.startswith(" "):
                old_line += 1
            # "\ No newline at end of file" and similar are ignored
    return sorted(changed)


def verify_anchor_scope(shadow_worktree: Path, touched_paths: list[str], declared: dict, patch_text: str) -> list[av.Finding]:
    """Anchor-level (within-file) enforcement: every hunk touching the
    declared mutable surface's own file must fall entirely within that
    surface's own declared heading section(s) in the BASELINE content (read
    before the patch is applied). This is what actually keeps a patch from
    e.g. claiming MUT-ROUTING-TIEBREAK while quietly also editing
    ROUTING_RULES.md's protected destination table in the same file."""
    declared_file = declared["path"]
    if not any(declared_file in p for p in touched_paths):
        return []  # nothing to check; file-level check already covers this
    file_path = shadow_worktree / declared_file
    if not file_path.is_file():
        return [
            av.Finding(
                path=declared_file,
                rule="INV-01",
                severity="critical",
                evidence=f"declared mutable surface file {declared_file!r} does not exist at baseline revision",
                consequence="reject",
            )
        ]
    ranges = mutable_surface_line_ranges(file_path.read_text(encoding="utf-8"), declared.get("anchor", ""))
    if ranges is None:
        return [
            av.Finding(
                path=declared_file,
                rule="ANCHOR_UNVERIFIABLE",
                severity="high",
                evidence=f"could not locate the declared anchor heading(s) for {declared['surface_id']} in {declared_file}; scope cannot be proven safe",
                consequence="reject",
            )
        ]
    changed_lines = hunk_changed_old_lines_for_file(patch_text, declared_file)
    findings: list[av.Finding] = []
    out_of_range = [ln for ln in changed_lines if not any(r_start <= ln < r_end for r_start, r_end in ranges)]
    if out_of_range:
        findings.append(
            av.Finding(
                path=declared_file,
                rule="INV-01",
                severity="critical",
                evidence=(
                    f"patch changes line(s) {out_of_range} outside "
                    f"{declared['surface_id']}'s declared anchor range(s) {ranges}"
                ),
                consequence="discard",
            )
        )
    return findings


def reject_patch_scope(
    shadow_worktree: Path, touched_paths: list[str], research_surface: str, manifest: dict, patch_text: str
) -> list[av.Finding]:
    """Verifies the REAL diff, not the record's self-reported affected_scope
    claim (that is #392's job, on the record). This is the actual
    enforcement point: a patch that claims one research_surface but really
    touches another file, multiple mutable surfaces, an anchor outside its
    own declared surface, or a wholly different protected surface is
    rejected here before it is ever applied."""
    mutable = {s["surface_id"]: s for s in manifest["mutable_surfaces"]}
    protected = manifest["protected_surfaces"]
    findings: list[av.Finding] = []

    declared = mutable.get(research_surface)
    if declared is None:
        return [
            av.Finding(
                path="research_surface",
                rule="INV-01",
                severity="critical",
                evidence=f"{research_surface!r} is not a declared mutable surface",
                consequence="reject",
            )
        ]

    declared_file = declared["path"]
    outside = [p for p in touched_paths if declared_file not in p]
    if outside:
        findings.append(
            av.Finding(
                path="patch",
                rule="INV-01",
                severity="critical",
                evidence=f"patch touches path(s) outside the declared mutable surface {research_surface!r}: {sorted(outside)}",
                consequence="reject",
            )
        )

    touched_mutable_files = {s["path"] for s in mutable.values() if any(s["path"] in p for p in touched_paths)}
    if len(touched_mutable_files) > 1:
        findings.append(
            av.Finding(
                path="patch",
                rule="INV-05",
                severity="high",
                evidence=f"patch spans more than one mutable-surface file: {sorted(touched_mutable_files)}",
                consequence="discard",
            )
        )

    if not outside:
        findings.extend(verify_anchor_scope(shadow_worktree, touched_paths, declared, patch_text))

    # Protected surfaces living in a DIFFERENT file than the declared
    # mutable surface: a plain path check is sufficient and safe (no
    # same-file false positive risk, since verify_anchor_scope already
    # bounds the declared file precisely).
    for entry in protected:
        base = entry["path"].split(",")[0].strip()
        if not base or base == declared_file or base.startswith(("main (", "the live", "(future)", "this manifest")):
            continue
        if any(base in p for p in touched_paths):
            findings.append(
                av.Finding(
                    path="patch",
                    rule="INV-01",
                    severity="critical",
                    evidence=f"patch touches protected surface {entry['surface_id']} ({base})",
                    consequence="discard",
                )
            )
    return findings


def apply_patch(shadow_worktree: Path, patch_text: str) -> None:
    result = _run_git(["apply", "-"], cwd=shadow_worktree, input_text=patch_text)
    if result.returncode != 0:
        raise ShadowRunnerError(f"git apply failed inside the shadow worktree: {result.stderr.strip()}")


# ---------------------------------------------------------------------------
# Provider-neutral observation adapters (no network I/O anywhere below)
# ---------------------------------------------------------------------------

AdapterCallable = Callable[[str, str, str], Optional[dict]]


class JSONLResponseAdapter:
    """Reference provider-neutral adapter. Reads pre-generated observations
    from a local JSONL file keyed by (experiment_id, condition, case_id).
    Each line: {"experiment_id", "condition": "baseline"|"candidate",
    "case_id", "response": ..., "runtime_model_configuration": {...}}.
    Performs no network or subprocess call of its own."""

    def __init__(self, path: Path) -> None:
        self._by_key: dict[tuple[str, str, str], dict] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            key = (row["experiment_id"], row["condition"], row["case_id"])
            self._by_key[key] = row

    def __call__(self, experiment_id: str, condition: str, case_id: str) -> Optional[dict]:
        return self._by_key.get((experiment_id, condition, case_id))


def config_hash(runtime_model_configuration: dict) -> str:
    return sha256_hex(json.dumps(runtime_model_configuration, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def alternation_order(experiment_id: str, seed: int = 0) -> list[str]:
    """Deterministic, seeded baseline/candidate presentation order -- the
    structural hook for issue #393's 'randomize or alternate baseline/
    candidate order where the adapter permits'. This module has no live
    adapter to actually vary presentation order against (provider
    integration is out of scope here), so this is reproducible and testable
    rather than truly random; a future live adapter can honor it."""
    import random

    rng = random.Random(f"{seed}:{experiment_id}")
    order = ["baseline", "candidate"]
    rng.shuffle(order)
    return order


def collect_observations(
    adapter: AdapterCallable, experiment_id: str, case_ids: list[str], seed: int = 0
) -> tuple[dict, dict, list[av.Finding]]:
    alternation_order(experiment_id, seed)  # computed for auditability; adapters may ignore it
    baseline: dict = {}
    candidate: dict = {}
    findings: list[av.Finding] = []
    for case_id in case_ids:
        for condition, bucket in (("baseline", baseline), ("candidate", candidate)):
            row = adapter(experiment_id, condition, case_id)
            if row is None:
                findings.append(
                    av.Finding(
                        path=f"{condition}/{case_id}",
                        rule="MISSING_OBSERVATION",
                        severity="high",
                        evidence=f"no observation returned for {condition}/{case_id}",
                        consequence="inconclusive",
                    )
                )
            else:
                bucket[case_id] = row
    return baseline, candidate, findings


def reject_config_mismatch(baseline: dict, candidate: dict, case_ids: list[str]) -> list[av.Finding]:
    findings: list[av.Finding] = []
    for case_id in case_ids:
        b_cfg = baseline.get(case_id, {}).get("runtime_model_configuration")
        c_cfg = candidate.get(case_id, {}).get("runtime_model_configuration")
        if b_cfg is not None and c_cfg is not None and config_hash(b_cfg) != config_hash(c_cfg):
            findings.append(
                av.Finding(
                    path=f"runtime_model_configuration/{case_id}",
                    rule="CONFIG_MISMATCH",
                    severity="high",
                    evidence=f"baseline and candidate ran under different configurations for {case_id}",
                    consequence="inconclusive",
                )
            )
    return findings


# ---------------------------------------------------------------------------
# Orchestration: one experiment_id, one baseline/candidate pair
# ---------------------------------------------------------------------------


def run_shadow_experiment(
    *,
    repo_root: Path,
    experiment_record: dict,
    manifest: dict,
    patch_text: str,
    adapter: AdapterCallable,
    case_ids: list[str],
    work_dir: Path | None = None,
) -> RunResult:
    """Orchestrates: fingerprint check -> isolated worktree at
    baseline_revision -> real-diff scope check -> apply -> collect
    baseline/candidate observations -> config-mismatch check -> cleanup.
    Returns a RunResult for the caller to hand to #392's validator
    (validate_experiment_record / ledger_append); this function makes no
    keep_candidate/discard/inconclusive research decision itself -- it only
    ever returns "ready_for_validation", "inconclusive", or "rejected"."""
    fp_findings = verify_patch_fingerprint(patch_text, experiment_record["candidate_patch_hash"])
    if fp_findings:
        return RunResult("rejected", fp_findings, None, None, None, "fingerprint mismatch; no worktree created")

    parent_before = parent_tree_fingerprint(repo_root)
    own_tmp = work_dir is None
    work_dir = work_dir or Path(tempfile.mkdtemp(prefix="autoresearch-shadow-"))
    shadow: Path | None = None
    try:
        try:
            shadow = create_shadow_worktree(repo_root, experiment_record["baseline_revision"], work_dir)
        except ShadowRunnerError as exc:
            return RunResult(
                "inconclusive",
                [av.Finding(path="baseline_revision", rule="WORKTREE_CREATE_FAILED", severity="high", evidence=str(exc), consequence="inconclusive")],
                None, None, None, str(exc),
            )

        ok, touched_paths, err = dry_run_patch_paths(shadow, patch_text)
        if not ok:
            return RunResult(
                "inconclusive",
                [av.Finding(path="patch", rule="PATCH_DOES_NOT_APPLY", severity="high", evidence=err, consequence="inconclusive")],
                shadow, None, None, err,
            )

        scope_findings = reject_patch_scope(shadow, touched_paths, experiment_record["research_surface"], manifest, patch_text)
        if scope_findings:
            return RunResult("rejected", scope_findings, shadow, None, None, "patch scope violation")

        apply_patch(shadow, patch_text)

        baseline_obs, candidate_obs, obs_findings = collect_observations(
            adapter, experiment_record["experiment_id"], case_ids
        )
        if obs_findings:
            return RunResult("inconclusive", obs_findings, shadow, baseline_obs, candidate_obs, "missing observation(s)")

        cfg_findings = reject_config_mismatch(baseline_obs, candidate_obs, case_ids)
        if cfg_findings:
            return RunResult("inconclusive", cfg_findings, shadow, baseline_obs, candidate_obs, "config mismatch")

        return RunResult(
            "ready_for_validation", [], shadow, baseline_obs, candidate_obs,
            "isolated worktree run complete; hand off to autoresearch_validator for the actual decision",
        )
    finally:
        if shadow is not None:
            remove_shadow_worktree(repo_root, shadow)
        elif own_tmp and work_dir.exists():
            shutil.rmtree(work_dir, ignore_errors=True)
        parent_after = parent_tree_fingerprint(repo_root)
        if parent_after != parent_before:
            # This must never happen; it is a hard safety-invariant break,
            # not an ordinary experiment outcome, so it raises rather than
            # returning a RunResult.
            raise ShadowRunnerError(
                "parent tree fingerprint changed during a shadow run -- "
                "the parent working tree or main must never be mutated"
            )
