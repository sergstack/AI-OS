#!/usr/bin/env python3
"""Advisory bounded project-context contract check (Issue #369 P0).

Two independent, additive checks — neither replaces existing machinery:

  (A) Required-knowledge presence: for each capability in
      PROJECT_CAPABILITIES.yaml, verify its declared `required_knowledge`
      entries actually exist and (for `delivery: bundle`) are actually
      embedded in a bundle that capability's own UPLOAD_LIST.md lists.
  (B) Status-artifact freshness: for a project's CURRENT_STATUS.md, if it
      declares a `status_scope:` / `status_verified_revision:` block, verify
      no commit touching that scope is newer than the verified revision.

Both are advisory by default (`--advisory`, the default: always exit 0) and
can be switched to blocking (`--enforce`: exit 1 if any finding exists).
Not wired as a blocking step anywhere; see
docs/standards/BOUNDED_PROJECT_CONTEXT_FRESHNESS.md for the promotion
trigger. This script does not write, regenerate, or modify anything, and
does not touch the AES execution record.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

from check_knowledge_bundles import listed_files, section_between

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "PROJECT_CAPABILITIES.yaml"
FROM_SECTION_PATTERN = re.compile(r"^## From: `([^`]+)`\s*$", re.MULTILINE)
STATUS_BLOCK_PATTERN = re.compile(
    r"^-\s*status_scope:\s*(.+)$\n^-\s*status_verified_revision:\s*([0-9a-f]{7,40})\s*$",
    re.MULTILINE,
)


class Finding:
    def __init__(self, code: str, capability_id: str, message: str, actionable: bool = True) -> None:
        self.code = code
        self.capability_id = capability_id
        self.message = message
        self.actionable = actionable

    def __str__(self) -> str:
        return f"{self.code}: [{self.capability_id}] {self.message}"


def load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def project_instructions_text(canonical_path: str) -> str:
    path = REPO_ROOT / canonical_path / "PROJECT_INSTRUCTIONS.md"
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def bundle_embedded_paths(canonical_path: str) -> set[str]:
    """Every source path embedded as `## From:` content in any bundle this
    capability's own UPLOAD_LIST.md actually lists (required or optional)."""
    upload_list = REPO_ROOT / canonical_path / "Knowledge_Bundles" / "UPLOAD_LIST.md"
    if not upload_list.is_file():
        return set()
    text = upload_list.read_text(encoding="utf-8")
    names = listed_files(section_between(text, "## Required upload files", "## Optional upload files"))
    names += listed_files(section_between(text, "## Optional upload files", "## Do not upload"))
    embedded: set[str] = set()
    for name in names:
        bundle_path = REPO_ROOT / canonical_path / "Knowledge_Bundles" / name
        if not bundle_path.is_file():
            continue
        content = bundle_path.read_text(encoding="utf-8")
        content = content.split("# Content", 1)[-1] if "# Content" in content else content
        embedded.update(FROM_SECTION_PATTERN.findall(content))
    return embedded


def check_required_knowledge(capability_id: str, capability: dict) -> list[Finding]:
    findings: list[Finding] = []
    canonical_path = capability["canonical_path"]

    entries = capability.get("required_knowledge")
    if entries is None:
        return [Finding("BLOCKED_UNDECLARED", capability_id,
                         "capability has no required_knowledge block (mandatory at schema_version >= 3)")]

    instructions = project_instructions_text(canonical_path)
    embedded = None  # computed lazily, only if a bundle-delivery entry exists

    for entry in entries:
        path = entry["path"]
        delivery = entry["delivery"]

        if delivery == "external":
            findings.append(Finding(
                "UNVERIFIABLE_EXTERNAL", capability_id,
                f"{path} — {entry.get('reason', 'declared external, not checked by design')}",
                actionable=False,
            ))
            continue

        if delivery == "project_instructions":
            basename = Path(path).name
            if basename not in instructions:
                findings.append(Finding("MISSING_REQUIRED_KNOWLEDGE", capability_id,
                                         f"{path} — declared as project_instructions content, not named in PROJECT_INSTRUCTIONS.md"))
            continue

        if delivery == "repo_only":
            if not (REPO_ROOT / path).exists():
                findings.append(Finding("MISSING_REQUIRED_KNOWLEDGE", capability_id, f"{path} — path does not exist"))
            continue

        if delivery == "bundle":
            if not (REPO_ROOT / path).exists():
                findings.append(Finding("MISSING_REQUIRED_KNOWLEDGE", capability_id, f"{path} — path does not exist"))
                continue
            if embedded is None:
                embedded = bundle_embedded_paths(canonical_path)
            if path not in embedded:
                findings.append(Finding(
                    "MISSING_REQUIRED_KNOWLEDGE", capability_id,
                    f"{path} — required but not embedded as '## From:' content in any bundle "
                    f"listed in {canonical_path}/Knowledge_Bundles/UPLOAD_LIST.md",
                ))
            continue

        findings.append(Finding("INVALID_DECLARATION", capability_id, f"{path} — unknown delivery value: {delivery}"))

    # Reverse drift guard: a declared entry whose basename no longer appears
    # in PROJECT_INSTRUCTIONS.md may mean the declaration is stale (advisory
    # signal only — PROJECT_INSTRUCTIONS.md prose is not a reliable oracle,
    # see the standard's "known residual" note).
    for entry in entries:
        basename = Path(entry["path"]).name
        if basename not in instructions:
            findings.append(Finding(
                "DECLARATION_DRIFT", capability_id,
                f"{entry['path']} — declared required_knowledge no longer named in PROJECT_INSTRUCTIONS.md; "
                f"confirm it is still required or remove the declaration",
                actionable=False,
            ))

    return findings


def git_log_touches(scope_path: str, since_revision: str) -> list[str]:
    result = subprocess.run(
        ["git", "log", "--oneline", f"{since_revision}..HEAD", "--", scope_path],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        return []  # revision does not resolve; caller reports unverifiable separately
    return [line for line in result.stdout.splitlines() if line.strip()]


def revision_resolves(revision: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", revision], cwd=REPO_ROOT, capture_output=True, check=False,
    )
    return result.returncode == 0


def check_status_freshness(capability_id: str, capability: dict) -> list[Finding]:
    canonical_path = capability["canonical_path"]
    status_path = REPO_ROOT / canonical_path / "CURRENT_STATUS.md"
    if not status_path.is_file():
        return [Finding("STATUS_NOT_APPLICABLE", capability_id,
                         f"{canonical_path}/CURRENT_STATUS.md does not exist", actionable=False)]

    text = status_path.read_text(encoding="utf-8")
    match = STATUS_BLOCK_PATTERN.search(text)
    if not match:
        return [Finding("STATUS_UNVERIFIABLE", capability_id,
                         f"{canonical_path}/CURRENT_STATUS.md has no declared status_scope/"
                         f"status_verified_revision block", actionable=False)]

    scope_paths = [p.strip().strip(",") for p in match.group(1).split(",") if p.strip()]
    revision = match.group(2).strip()

    if not revision_resolves(revision):
        return [Finding("STATUS_UNVERIFIABLE", capability_id,
                         f"status_verified_revision {revision} does not resolve in this clone", actionable=False)]

    stale_evidence = []
    for scope_path in scope_paths:
        commits = git_log_touches(scope_path, revision)
        if commits:
            stale_evidence.append(f"{scope_path} ({len(commits)} commit(s) since {revision}: {commits[0]})")

    if stale_evidence:
        return [Finding("STATUS_STALE", capability_id,
                         f"{canonical_path}/CURRENT_STATUS.md not re-verified since scope changed: "
                         + "; ".join(stale_evidence))]

    return [Finding("STATUS_CURRENT", capability_id,
                     f"{canonical_path}/CURRENT_STATUS.md verified current as of {revision}", actionable=False)]


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--advisory", action="store_true", help="default: report only, always exit 0")
    mode.add_argument("--enforce", action="store_true", help="exit 1 if any actionable finding exists")
    args = parser.parse_args()
    enforce = args.enforce

    registry = load_registry()
    all_findings: list[Finding] = []
    for capability_id, capability in registry["capabilities"].items():
        all_findings += check_required_knowledge(capability_id, capability)
        all_findings += check_status_freshness(capability_id, capability)

    actionable = [f for f in all_findings if f.actionable]
    informational = [f for f in all_findings if not f.actionable]

    print("Bounded Project-Context Contract Check (advisory unless --enforce)")
    print()
    for capability_id in registry["capabilities"]:
        cap_findings = [f for f in all_findings if f.capability_id == capability_id]
        print(f"Capability: {capability_id}")
        if not cap_findings:
            print("  (no findings)")
        for f in cap_findings:
            marker = "FINDING" if f.actionable else "info"
            print(f"  {marker}: {f}")
        print()

    print("Summary:")
    print(f"- capabilities checked: {len(registry['capabilities'])}")
    print(f"- actionable findings: {len(actionable)}")
    print(f"- informational notes: {len(informational)}")
    print(f"- mode: {'enforce' if enforce else 'advisory'}")

    if not enforce:
        return 0
    return 1 if actionable else 0


if __name__ == "__main__":
    sys.exit(main())
