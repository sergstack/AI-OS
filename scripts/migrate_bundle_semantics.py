#!/usr/bin/env python3
"""Migrate legacy bundle-only semantic lines into canonical Knowledge files."""

from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path

from audit_bundle_provenance import TARGET_PROJECTS, normalize
from check_knowledge_bundles import PROJECTS, listed_files, section_between, source_files_from_bundle


INDEXES = {
    "[AI OS]": ["ChatGPT/[AI OS]/Knowledge/AI_OS_PROJECT_FILES_INDEX.md"],
    "[Thinking]": ["ChatGPT/[Thinking]/Knowledge/INDEX.md"],
    "[Analytics]": ["ChatGPT/[Analytics]/Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md"],
    "[LLM]": ["ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md", "ChatGPT/[LLM]/README.md"],
    "[Codex]": ["ChatGPT/[Codex]/Knowledge/INDEX.md"],
}


def bundle_only_lines(bundle: str, sources: dict[str, str]) -> list[tuple[str, list[str]]]:
    content = bundle.split("# Content", 1)[1] if "# Content" in bundle else bundle
    migrated = []
    for source, text in sources.items():
        marker = f"## From: `{source}`"
        if marker not in content:
            continue
        segment = content.split(marker, 1)[1].split("## From: `", 1)[0]
        source_lines = normalize(text).splitlines()
        bundle_lines = normalize(segment).splitlines()
        extra = []
        for tag, _i1, _i2, j1, j2 in difflib.SequenceMatcher(a=source_lines, b=bundle_lines, autojunk=False).get_opcodes():
            if tag in {"insert", "replace"}:
                extra.extend(bundle_lines[j1:j2])
        if extra:
            migrated.append((source, extra))
    return migrated


def migration_path(project_dir: Path, bundle_name: str) -> Path:
    return project_dir / "Knowledge" / f"{Path(bundle_name).stem}_BUNDLE_SEMANTICS.md"


def render(bundle_path: str, fragments: list[tuple[str, list[str]]]) -> str:
    parts = [
        "# Migrated Bundle Semantics",
        "",
        "Canonical source created during Issue #285 provenance migration.",
        f"Legacy bundle provenance: `{bundle_path}`.",
        "",
    ]
    for source, lines in fragments:
        parts.extend([f"## Legacy section: `{source}`", "", *lines, ""])
    return "\n".join(parts).rstrip() + "\n"


def update_indexes(root: Path, by_project: dict[str, list[str]]) -> None:
    for project, sources in by_project.items():
        names = [Path(source).name for source in sources]
        for index in INDEXES[project]:
            path = root / index
            text = path.read_text(encoding="utf-8")
            missing = [name for name in names if name not in text]
            if missing:
                text += "\n## Bundle semantic migration sources\n\n" + "\n".join(f"- `{name}`" for name in missing) + "\n"
                path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if not args.write:
        raise SystemExit("use --write after review; this command never writes Knowledge_Bundles")
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / "knowledge_bundle_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    items = {item["output"]: item for item in manifest["bundles"]}
    written = []
    by_project: dict[str, list[str]] = {project: [] for project in TARGET_PROJECTS}
    for project, project_dir in PROJECTS.items():
        if project not in TARGET_PROJECTS:
            continue
        upload = (root / project_dir / "Knowledge_Bundles/UPLOAD_LIST.md").read_text(encoding="utf-8")
        names = listed_files(section_between(upload, "## Required upload files", "## Optional upload files"))
        names += listed_files(section_between(upload, "## Optional upload files", "## Do not upload"))
        for name in names:
            bundle = root / project_dir / "Knowledge_Bundles" / name
            relative = str(bundle.relative_to(root))
            declared = source_files_from_bundle(bundle.read_text(encoding="utf-8"))
            sources = {source: (root / source).read_text(encoding="utf-8") for source in declared}
            fragments = bundle_only_lines(bundle.read_text(encoding="utf-8"), sources)
            if not fragments:
                continue
            destination = root / migration_path(project_dir, name)
            destination.write_text(render(relative, fragments), encoding="utf-8")
            migration_source = str(destination.relative_to(root))
            items[relative]["migration_sources"] = [migration_source]
            written.append(migration_source)
            by_project[project].append(migration_source)
    update_indexes(root, by_project)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"migration_sources_written": written, "count": len(written)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
