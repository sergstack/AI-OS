#!/usr/bin/env python3
"""Validate AI-OS manifest and governance path consistency."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_PROJECTS = {
    "[AI OS]": "ChatGPT/[AI OS]",
    "[Thinking]": "ChatGPT/[Thinking]",
    "[Analytics]": "ChatGPT/[Analytics]",
    "[LLM]": "ChatGPT/[LLM]",
    "[Codex]": "ChatGPT/[Codex]",
    "[Inbox Router]": "ChatGPT/[Inbox Router]",
}
EXPECTED_PROJECT_INSTRUCTIONS = {
    f"{path}/PROJECT_INSTRUCTIONS.md" for path in EXPECTED_PROJECTS.values()
}
EXPECTED_REPO_PATHS = list(EXPECTED_PROJECTS.values()) + ["Codex APP"]
LEGACY_PATH_PATTERNS = [
    (re.compile(r"(?<!ChatGPT/)\[AI OS\]/Project"), "[AI OS]/Project"),
    (re.compile(r"(?<!ChatGPT/)\[AI OS\]/Knowledge"), "[AI OS]/Knowledge"),
    (re.compile(r"(?<!ChatGPT/)\[AI OS\]/PROJECT_INSTRUCTIONS\.md"), "[AI OS]/PROJECT_INSTRUCTIONS.md"),
    (re.compile(r"AI_OS_Project_Settings_v04"), "AI_OS_Project_Settings_v04"),
]
RAW_LOCAL_PATH_PATTERN = re.compile(
    r"(?:(?<![A-Za-z0-9:])/(?:Users|home|Volumes)/[^\s)`'\"]+|[A-Za-z]:\\Users\\[^\s)`'\"]+)"
)
GOVERNANCE_DOCS = [
    "README.md",
    "MASTER_STATUS.md",
    "PROJECT_REGISTRY.md",
    "REPO_PATHS.md",
    "MANIFEST.md",
    "MANIFEST.json",
    "ARCHIVE_MAP.md",
    "UPLOAD_GUIDE.md",
    "CURRENT_STATUS.md",
]


@dataclass
class CheckResult:
    group: str
    ok: bool
    rule: str
    path: str
    value: str
    suggested_fix: str


def repo_root() -> Path:
    root = Path(__file__).resolve().parents[1]
    if not (root / ".git").exists() or not (root / "MANIFEST.json").exists():
        raise SystemExit(
            "FAIL repo root\n"
            "rule: script must be installed under the AI-OS repository\n"
            f"path: {root}\n"
            "suggested_fix: run this script from scripts/check_manifest_paths.py in the repository"
        )
    return root


def result(group: str, ok: bool, rule: str, path: str, value: str = "", suggested_fix: str = "") -> CheckResult:
    return CheckResult(group, ok, rule, path, value, suggested_fix)


def read_text(root: Path, rel: str) -> str | None:
    path = root / rel
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def contains_all(text: str, values: list[str]) -> bool:
    return all(value in text for value in values)


def path_exists(root: Path, rel: str) -> bool:
    return (root / rel).exists()


def check_manifest_json(root: Path) -> list[CheckResult]:
    group = "Manifest JSON"
    rel = "MANIFEST.json"
    path = root / rel
    results: list[CheckResult] = []
    if not path.exists():
        return [result(group, False, "file must exist", rel, suggested_fix="add MANIFEST.json")]
    results.append(result(group, True, "file exists", rel))

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [
            result(
                group,
                False,
                "JSON must parse",
                rel,
                value=str(exc),
                suggested_fix="fix MANIFEST.json syntax",
            )
        ]
    results.append(result(group, True, "JSON parses", rel))

    for key in ("knowledge_files", "local_files"):
        for item in data.get(key, []):
            exists = path_exists(root, item)
            results.append(
                result(
                    group,
                    exists,
                    f"{key} paths must exist",
                    item,
                    value=item,
                    suggested_fix=f"update MANIFEST.json or add {item}",
                )
            )

    limit = data.get("validation_gates", {}).get(
        "project_instructions_chars_limit", data.get("project_instructions_chars_limit")
    )
    results.append(
        result(
            group,
            limit == 8000,
            "validation_gates.project_instructions_chars_limit must equal 8000",
            rel,
            value=str(limit),
            suggested_fix="set validation_gates.project_instructions_chars_limit to 8000",
        )
    )

    promotion = data.get("production_promotion")
    results.append(
        result(
            group,
            promotion == "no",
            "production_promotion must be present and equal no",
            rel,
            value=str(promotion),
            suggested_fix="set production_promotion to no until a future acceptance file exists",
        )
    )
    return results


def check_manifest_markdown(root: Path) -> list[CheckResult]:
    group = "Manifest Markdown"
    rel = "MANIFEST.md"
    text = read_text(root, rel)
    if text is None:
        return [result(group, False, "file must exist", rel, suggested_fix="add MANIFEST.md")]
    results = [result(group, True, "file exists", rel)]
    results.append(
        result(
            group,
            "AI_OS_Project_Settings_v05" in text and "v05" in text,
            "current package/version must be referenced consistently",
            rel,
            value="AI_OS_Project_Settings_v05 / v05",
            suggested_fix="update package/version references to AI_OS_Project_Settings_v05",
        )
    )
    results.append(
        result(
            group,
            "PROJECT_INSTRUCTIONS.md" in text and "8000" in text,
            "must include PROJECT_INSTRUCTIONS.md <= 8000 characters rule",
            rel,
            suggested_fix="add the PROJECT_INSTRUCTIONS.md <= 8000 characters validation rule",
        )
    )
    results.append(
        result(
            group,
            "ChatGPT/[AI OS]/" in text,
            "must use canonical ChatGPT/[AI OS]/... paths",
            rel,
            suggested_fix="replace legacy AI OS paths with ChatGPT/[AI OS]/...",
        )
    )
    return results


def check_upload_guide(root: Path) -> list[CheckResult]:
    group = "Upload Guide"
    rel = "UPLOAD_GUIDE.md"
    text = read_text(root, rel)
    if text is None:
        return [result(group, False, "file must exist", rel, suggested_fix="add UPLOAD_GUIDE.md")]
    checks = [
        ("ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md", "must use canonical Project Instructions repo path"),
        ("ChatGPT/[AI OS]/Knowledge/", "must use canonical Knowledge repo paths"),
        ("Project Instructions", "must identify Project Instructions paste target"),
        ("Project Knowledge", "must identify Project Knowledge upload target"),
        ("только эти файлы", "must state only Knowledge files are uploaded to Project Knowledge"),
        ("README.md", "must state README.md remains local or is not uploaded as Knowledge"),
        ("8000", "must include or reference <=8000 chars rule"),
    ]
    results = [result(group, True, "file exists", rel)]
    for value, rule in checks:
        results.append(result(group, value in text, rule, rel, value=value, suggested_fix=f"add or correct: {value}"))
    return results


def check_repo_paths(root: Path) -> list[CheckResult]:
    group = "Repo Paths"
    rel = "REPO_PATHS.md"
    text = read_text(root, rel)
    if text is None:
        return [result(group, False, "file must exist", rel, suggested_fix="add REPO_PATHS.md")]
    results = [result(group, True, "file exists", rel)]
    for placeholder in ("<LOCAL_AI_OS_ROOT>", "<LOCAL_REPO_ROOT>"):
        results.append(
            result(
                group,
                placeholder in text,
                "must define canonical local path placeholders",
                rel,
                value=placeholder,
                suggested_fix=f"document {placeholder} in REPO_PATHS.md",
            )
        )
    for canonical in EXPECTED_REPO_PATHS:
        results.append(
            result(
                group,
                canonical in text and path_exists(root, canonical),
                "canonical repo path must be listed and exist",
                canonical,
                value=canonical,
                suggested_fix=f"add {canonical} to REPO_PATHS.md or create the missing path",
            )
        )
    return results


def check_project_registry(root: Path) -> list[CheckResult]:
    group = "Project Registry"
    rel = "PROJECT_REGISTRY.md"
    text = read_text(root, rel)
    if text is None:
        return [result(group, False, "file must exist", rel, suggested_fix="add PROJECT_REGISTRY.md")]
    results = [result(group, True, "file exists", rel)]
    for project, path in EXPECTED_PROJECTS.items():
        instruction = f"{path}/PROJECT_INSTRUCTIONS.md"
        results.append(
            result(
                group,
                project in text and path in text and path_exists(root, instruction),
                "ChatGPT project entry and PROJECT_INSTRUCTIONS.md path must exist",
                instruction,
                value=f"{project} -> {path}",
                suggested_fix=f"add {project} with canonical path {path} to PROJECT_REGISTRY.md",
            )
        )
        knowledge = f"{path}/Knowledge"
        if path_exists(root, knowledge):
            results.append(
                result(
                    group,
                    True,
                    "Knowledge path exists for project using Knowledge",
                    knowledge,
                    value=knowledge,
                )
            )
    results.append(
        result(
            group,
            "Codex APP" in text and "not a ChatGPT Project" in text,
            "Codex APP must be clearly marked as not a ChatGPT Project",
            rel,
            value="Codex APP",
            suggested_fix="mark Codex APP as an execution layer, not a ChatGPT Project",
        )
    )
    return results


def check_master_status(root: Path) -> list[CheckResult]:
    group = "Master Status"
    rel = "MASTER_STATUS.md"
    text = read_text(root, rel)
    if text is None:
        return [result(group, False, "file must exist", rel, suggested_fix="add MASTER_STATUS.md")]
    required = [
        "8000",
        "Public safety scan",
        "No raw absolute local paths",
        "Manifest/path consistency",
        "Smoke QA",
        "Pilot case",
    ]
    results = [result(group, True, "file exists", rel)]
    for value in required:
        results.append(
            result(
                group,
                value in text,
                "must include required validation gate",
                rel,
                value=value,
                suggested_fix=f"add validation gate: {value}",
            )
        )
    results.append(
        result(
            group,
            "production_promotion: yes" not in text,
            "must not say production_promotion: yes",
            rel,
            value="production_promotion: yes",
            suggested_fix="set production_promotion to no until promotion is accepted",
        )
    )
    return results


def check_project_instruction_coverage(root: Path) -> list[CheckResult]:
    group = "Project Instructions Coverage"
    found = {str(path.relative_to(root)) for path in root.rglob("PROJECT_INSTRUCTIONS.md")}
    results: list[CheckResult] = []
    for expected in sorted(EXPECTED_PROJECT_INSTRUCTIONS):
        results.append(
            result(
                group,
                expected in found,
                "expected PROJECT_INSTRUCTIONS.md must exist",
                expected,
                value=expected,
                suggested_fix=f"add or restore {expected}",
            )
        )
    extras = sorted(found - EXPECTED_PROJECT_INSTRUCTIONS)
    for extra in extras:
        documented = extra.startswith("ChatGPT/")
        results.append(
            result(
                group,
                documented,
                "extra PROJECT_INSTRUCTIONS.md must be under ChatGPT/ or documented in PROJECT_REGISTRY.md",
                extra,
                value=extra,
                suggested_fix="move under ChatGPT/ or document it in PROJECT_REGISTRY.md",
            )
        )
    results.append(
        result(
            group,
            len(found) >= 6,
            "expected PROJECT_INSTRUCTIONS.md count must be at least 6",
            "PROJECT_INSTRUCTIONS.md",
            value=str(len(found)),
            suggested_fix="restore missing ChatGPT project instructions files",
        )
    )
    return results


def check_legacy_path_drift(root: Path) -> list[CheckResult]:
    group = "Legacy Path Drift"
    results: list[CheckResult] = []
    for rel in GOVERNANCE_DOCS:
        text = read_text(root, rel)
        if text is None:
            continue
        for pattern, legacy in LEGACY_PATH_PATTERNS:
            results.append(
                result(
                    group,
                    pattern.search(text) is None,
                    "legacy path variant must not appear in governance docs",
                    rel,
                    value=legacy,
                    suggested_fix="replace with canonical ChatGPT/[AI OS]/... path",
                )
            )
        for match in RAW_LOCAL_PATH_PATTERN.finditer(text):
            results.append(
                result(
                    group,
                    False,
                    "raw local absolute path must not appear in governance docs",
                    rel,
                    value=match.group(0),
                    suggested_fix="replace with a documented <LOCAL_...> placeholder",
                )
            )
    if not results:
        results.append(result(group, True, "no governance docs found for legacy scan", "governance docs"))
    return results


def print_group(name: str, results: list[CheckResult]) -> tuple[int, int]:
    print(f"{name}:")
    passed = 0
    failed = 0
    for item in results:
        if item.ok:
            passed += 1
            print(f"- PASS {item.rule}: {item.path}")
        else:
            failed += 1
            print(f"- FAIL {item.rule}")
            print(f"  path: {item.path}")
            if item.value:
                print(f"  value: {item.value}")
            if item.suggested_fix:
                print(f"  suggested_fix: {item.suggested_fix}")
    print()
    return passed, failed


def main() -> int:
    root = repo_root()
    groups = [
        ("Manifest JSON", check_manifest_json(root)),
        ("Manifest Markdown", check_manifest_markdown(root)),
        ("Upload Guide", check_upload_guide(root)),
        ("Repo Paths", check_repo_paths(root)),
        ("Project Registry", check_project_registry(root)),
        ("Master Status", check_master_status(root)),
        ("Project Instructions Coverage", check_project_instruction_coverage(root)),
        ("Legacy Path Drift", check_legacy_path_drift(root)),
    ]

    total_passed = 0
    total_failed = 0
    for name, results in groups:
        passed, failed = print_group(name, results)
        total_passed += passed
        total_failed += failed

    print("Summary:")
    print(f"- checked: {total_passed + total_failed}")
    print(f"- passed: {total_passed}")
    print(f"- failed: {total_failed}")
    return 1 if total_failed else 0


if __name__ == "__main__":
    sys.exit(main())
