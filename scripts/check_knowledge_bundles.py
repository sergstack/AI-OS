#!/usr/bin/env python3
"""Validate compact Knowledge bundle folders for ChatGPT projects."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys


PROJECTS = {
    "[AI OS]": Path("ChatGPT/[AI OS]"),
    "[Thinking]": Path("ChatGPT/[Thinking]"),
    "[Analytics]": Path("ChatGPT/[Analytics]"),
    "[LLM]": Path("ChatGPT/[LLM]"),
    "[Codex]": Path("ChatGPT/[Codex]"),
    "[Inbox Router]": Path("ChatGPT/[Inbox Router]"),
    "[Thinkers OS]": Path("ChatGPT/[Thinkers OS]"),
}
REQUIRED_UPLOAD_SECTIONS = [
    "## Required upload files",
    "## Optional upload files",
    "## Do not upload",
    "## File count",
    "Limit: 40",
    "Status: pass",
]
REQUIRED_BUNDLE_SECTIONS = [
    "## Purpose",
    "## Source files",
    "## Upload target",
    "## Status",
    "# Content",
]
RAW_LOCAL_PATH_PATTERN = re.compile(
    r"(?:(?<![A-Za-z0-9:])/(?:Users|home|Volumes)/[^\s)`'\"]+|[A-Za-z]:\\Users\\[^\s)`'\"]+)"
)
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[opsu]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
]
SOURCE_FINGERPRINT_PATTERN = re.compile(r"source_fingerprint:\s*(sha256:[0-9a-f]{64})")


@dataclass
class ProjectReport:
    project: str
    bundle_folder: bool
    upload_list: bool
    required_files: int
    optional_files: int
    total_upload_files: int
    source_paths: bool
    forbidden_content: bool
    failures: list[str]


def repo_root() -> Path:
    root = Path(__file__).resolve().parents[1]
    if not (root / ".git").exists():
        raise SystemExit("FAIL: script must run from inside the AI-OS repository")
    return root


def listed_files(section: str) -> list[str]:
    files = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("- `"):
            continue
        value = stripped.split("`", 2)[1]
        if value != "none":
            files.append(value)
    return files


def section_between(text: str, start: str, end: str) -> str:
    if start not in text:
        return ""
    tail = text.split(start, 1)[1]
    if end in tail:
        return tail.split(end, 1)[0]
    return tail


def source_files_from_bundle(text: str) -> list[str]:
    source_section = section_between(text, "## Source files", "## Upload target")
    return listed_files(source_section)


def source_fingerprint(root: Path, sources: list[str]) -> str:
    digest = hashlib.sha256()
    for source in sources:
        digest.update(source.encode("utf-8"))
        digest.update(b"\0")
        digest.update((root / source).read_bytes())
        digest.update(b"\0")
    return f"sha256:{digest.hexdigest()}"


def declared_source_fingerprint(text: str) -> str | None:
    status_section = section_between(text, "## Status", "---")
    match = SOURCE_FINGERPRINT_PATTERN.search(status_section)
    if not match:
        return None
    return match.group(1)


def validate_upload_list(root: Path, project_dir: Path, upload_text: str, failures: list[str]) -> tuple[list[str], list[str]]:
    for section in REQUIRED_UPLOAD_SECTIONS:
        if section not in upload_text:
            failures.append(f"UPLOAD_LIST.md missing section/value: {section}")

    required_section = section_between(upload_text, "## Required upload files", "## Optional upload files")
    optional_section = section_between(upload_text, "## Optional upload files", "## Do not upload")
    required = listed_files(required_section)
    optional = listed_files(optional_section)

    total = len(required) + len(optional)
    if total > 40:
        failures.append(f"upload file count exceeds 40: {total}")
    if len(required) > 12:
        failures.append(f"required bundle count exceeds 12: {len(required)}")

    for file_name in required + optional:
        if file_name == "PROJECT_INSTRUCTIONS.md":
            failures.append("PROJECT_INSTRUCTIONS.md must not be an upload bundle file")
        if "/" in file_name or "\\" in file_name:
            failures.append(f"upload bundle file must be local file name only: {file_name}")
        if not (root / project_dir / "Knowledge_Bundles" / file_name).exists():
            failures.append(f"listed bundle file does not exist: {project_dir}/Knowledge_Bundles/{file_name}")

    if "`PROJECT_INSTRUCTIONS.md` — paste into Project Instructions instead." not in upload_text:
        failures.append("PROJECT_INSTRUCTIONS.md must be mentioned only as paste into Project Instructions")

    return required, optional


def validate_forbidden_content(rel: str, text: str, failures: list[str]) -> None:
    if RAW_LOCAL_PATH_PATTERN.search(text):
        failures.append(f"raw absolute local path found in {rel}")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            failures.append(f"secret-looking pattern found in {rel}")
    lowered = text.lower()
    unsafe_recommendations = [
        "upload raw transcripts",
        "upload source-card dumps",
        "upload chunks",
        "upload embeddings",
        "upload vector db",
        "upload vector database",
        "use embeddings as current upload",
        "use vector db as current upload",
    ]
    for phrase in unsafe_recommendations:
        if phrase in lowered:
            failures.append(f"forbidden upload recommendation in {rel}: {phrase}")


def validate_bundle(root: Path, project_dir: Path, bundle_name: str, failures: list[str]) -> tuple[bool, bool]:
    path = root / project_dir / "Knowledge_Bundles" / bundle_name
    rel = str(path.relative_to(root))
    text = path.read_text(encoding="utf-8")
    source_ok = True
    forbidden_ok = True

    for section in REQUIRED_BUNDLE_SECTIONS:
        if section not in text:
            failures.append(f"{rel} missing required section: {section}")

    sources = source_files_from_bundle(text)
    if not sources:
        failures.append(f"{rel} has no source files")
        source_ok = False
    for source in sources:
        if "PROJECT_INSTRUCTIONS.md" in source:
            failures.append(f"{rel} must not list PROJECT_INSTRUCTIONS.md as source/upload bundle content")
            source_ok = False
        if not (root / source).exists():
            failures.append(f"{rel} source file missing: {source}")
            source_ok = False

    declared_fingerprint = declared_source_fingerprint(text)
    if not declared_fingerprint:
        failures.append(f"{rel} missing source_fingerprint in Status")
        source_ok = False
    elif source_ok:
        current_fingerprint = source_fingerprint(root, sources)
        if declared_fingerprint != current_fingerprint:
            failures.append(
                f"{rel} source_fingerprint mismatch: expected {current_fingerprint}, found {declared_fingerprint}"
            )
            source_ok = False

    before_failures = len(failures)
    validate_forbidden_content(rel, text, failures)
    forbidden_ok = len(failures) == before_failures
    return source_ok, forbidden_ok


def check_project(root: Path, project: str, project_dir: Path) -> ProjectReport:
    failures: list[str] = []
    bundle_dir = root / project_dir / "Knowledge_Bundles"
    bundle_folder = bundle_dir.exists() and bundle_dir.is_dir()
    if not bundle_folder:
        failures.append(f"bundle folder missing: {project_dir}/Knowledge_Bundles")
        return ProjectReport(project, False, False, 0, 0, 0, False, False, failures)

    readme = bundle_dir / "README.md"
    upload_list = bundle_dir / "UPLOAD_LIST.md"
    if not readme.exists():
        failures.append(f"README.md missing: {project_dir}/Knowledge_Bundles/README.md")
    upload_ok = upload_list.exists()
    if not upload_ok:
        failures.append(f"UPLOAD_LIST.md missing: {project_dir}/Knowledge_Bundles/UPLOAD_LIST.md")
        return ProjectReport(project, True, False, 0, 0, 0, False, False, failures)

    upload_text = upload_list.read_text(encoding="utf-8")
    validate_forbidden_content(str(upload_list.relative_to(root)), upload_text, failures)
    required, optional = validate_upload_list(root, project_dir, upload_text, failures)

    source_ok = True
    forbidden_ok = True
    for bundle_name in required + optional:
        current_source_ok, current_forbidden_ok = validate_bundle(root, project_dir, bundle_name, failures)
        source_ok = source_ok and current_source_ok
        forbidden_ok = forbidden_ok and current_forbidden_ok

    extra_bundles = [
        path.name
        for path in bundle_dir.glob("*.md")
        if path.name not in {"README.md", "UPLOAD_LIST.md"} and path.name not in set(required + optional)
    ]
    for extra in sorted(extra_bundles):
        failures.append(f"bundle file not listed in UPLOAD_LIST.md: {project_dir}/Knowledge_Bundles/{extra}")

    return ProjectReport(
        project=project,
        bundle_folder=True,
        upload_list=upload_ok,
        required_files=len(required),
        optional_files=len(optional),
        total_upload_files=len(required) + len(optional),
        source_paths=source_ok,
        forbidden_content=forbidden_ok,
        failures=failures,
    )


def generated_drift_failures(root: Path) -> list[str]:
    """Recompute ready manifest outputs instead of trusting stored hashes."""
    manifest_path = root / "knowledge_bundle_manifest.json"
    if not manifest_path.is_file():
        return []
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("status") != "ready":
        return []
    declared_outputs = {
        item["output"]
        for item in manifest.get("bundles", [])
        if isinstance(item, dict) and isinstance(item.get("output"), str)
    }
    contract_failures: list[str] = []
    for _project, project_dir in PROJECTS.items():
        upload_list = root / project_dir / "Knowledge_Bundles/UPLOAD_LIST.md"
        if not upload_list.is_file():
            continue
        upload_text = upload_list.read_text(encoding="utf-8")
        bundle_names = listed_files(section_between(upload_text, "## Required upload files", "## Optional upload files"))
        bundle_names += listed_files(section_between(upload_text, "## Optional upload files", "## Do not upload"))
        for bundle_name in bundle_names:
            relative = str(project_dir / "Knowledge_Bundles" / bundle_name)
            if relative not in declared_outputs:
                contract_failures.append(f"UNDECLARED_UPLOAD_BUNDLE: {relative}")
    builder_path = Path(__file__).with_name("build_knowledge_bundles.py")
    spec = importlib.util.spec_from_file_location("knowledge_bundle_builder", builder_path)
    assert spec and spec.loader
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    return contract_failures + builder.check(root, manifest)


def main() -> int:
    root = repo_root()
    reports = [check_project(root, project, project_dir) for project, project_dir in PROJECTS.items()]
    drift_failures = generated_drift_failures(root)
    failed = 0
    bundles_checked = 0
    upload_max = 0

    print("Knowledge Bundle Check")
    print()
    for report in reports:
        failed += len(report.failures)
        bundles_checked += report.total_upload_files
        upload_max = max(upload_max, report.total_upload_files)
        print(f"Project: {report.project}")
        print(f"- bundle folder: {'pass' if report.bundle_folder else 'fail'}")
        print(f"- upload list: {'pass' if report.upload_list else 'fail'}")
        print(f"- required files: {report.required_files}")
        print(f"- optional files: {report.optional_files}")
        print(f"- total upload files: {report.total_upload_files} / 40")
        print(f"- source paths: {'pass' if report.source_paths else 'fail'}")
        print(f"- forbidden content: {'pass' if report.forbidden_content else 'fail'}")
        for failure in report.failures:
            print(f"  FAIL: {failure}")
        print()

    failed += len(drift_failures)
    print("Summary:")
    print(f"- projects checked: {len(reports)}")
    print(f"- bundles checked: {bundles_checked}")
    print(f"- upload files max: {upload_max}")
    print(f"- failed: {failed}")
    if drift_failures:
        print("- generated drift failures:")
        for failure in drift_failures:
            print(f"  FAIL: {failure}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
