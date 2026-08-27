#!/usr/bin/env python3
"""Read-only provenance audit for declared Knowledge bundle inputs."""

from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path
import re

from check_knowledge_bundles import PROJECTS, listed_files, section_between, source_files_from_bundle


TARGET_PROJECTS = frozenset({"[AI OS]", "[Codex]", "[Analytics]", "[Thinking]", "[LLM]"})
DETAIL_LIMIT = 5
EXCERPT_LIMIT = 160


def normalize(text: str) -> str:
    """Bundles deliberately collapse blank lines; that is not semantic drift."""
    return "\n".join(line.rstrip() for line in text.splitlines() if line.strip())


def classify(bundle: str, sources: dict[str, str]) -> tuple[str, list[dict[str, str]], list[dict[str, str]]]:
    """Classify exact source inclusion; unmatched bundle text is never discarded."""
    content = bundle.split("# Content", 1)[1] if "# Content" in bundle else bundle
    bundle_only: list[dict[str, str]] = []
    source_only: list[dict[str, str]] = []
    section_paths = re.findall(r"^## From: `([^`]+)`\s*$", content, flags=re.MULTILINE)
    expected_paths = set(sources)
    unexpected = [path for path in section_paths if path not in expected_paths]
    missing = [path for path in sources if path not in section_paths]
    duplicated = sorted({path for path in section_paths if section_paths.count(path) > 1})
    if unexpected or missing or duplicated:
        details = ([f"unexpected section: {path}" for path in unexpected]
                   + [f"missing section: {path}" for path in missing]
                   + [f"duplicate section: {path}" for path in duplicated])
        return "bundle_only_structural", [{"path": "bundle", "excerpt": detail} for detail in details], []
    for path, text in sources.items():
        marker = f"## From: `{path}`"
        after = content.split(marker, 1)[1] if marker in content else ""
        segment = after.split("## From: `", 1)[0]
        source_lines = [line for line in normalize(text).splitlines() if line]
        bundle_lines = [line for line in normalize(segment).splitlines() if line]
        matcher = difflib.SequenceMatcher(a=source_lines, b=bundle_lines, autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag in {"delete", "replace"}:
                source_only.extend({"path": path, "excerpt": line[:EXCERPT_LIMIT]} for line in source_lines[i1:i2])
            if tag in {"insert", "replace"}:
                for line in bundle_lines[j1:j2]:
                    bundle_only.append({"path": path, "excerpt": line[:EXCERPT_LIMIT]})
    if bundle_only:
        return "bundle_only_semantic", bundle_only[:DETAIL_LIMIT], source_only[:DETAIL_LIMIT]
    if source_only:
        return "source_only", [], source_only[:DETAIL_LIMIT]
    return "equivalent", [], []


def candidate_source_paths(root: Path, findings: list[dict[str, str]]) -> list[str]:
    """Surface review candidates without changing a declared mapping."""
    candidates: set[str] = set()
    for finding in findings:
        needle = " ".join(finding["excerpt"].replace("`", "").split()[:8])
        if len(needle) < 24:
            continue
        for path in root.rglob("*.md"):
            relative = path.relative_to(root)
            if ("Knowledge_Bundles" in relative.parts or "archive" in relative.parts
                    or str(relative).startswith("docs/knowledge_bundle_provenance_")):
                continue
            if needle in normalize(path.read_text(encoding="utf-8")):
                candidates.add(str(relative))
    return sorted(candidates)


def render_markdown(payload: dict[str, object]) -> str:
    metrics = payload["metrics"]
    records = payload["records"]
    assert isinstance(metrics, dict)
    assert isinstance(records, list)
    lines = [
        "# Knowledge Bundle Provenance Audit",
        "",
        f"Audit scope: {', '.join(sorted(TARGET_PROJECTS))}",
        "",
        f"Unresolved bundle-only semantic count: **{metrics['unresolved_bundle_only_semantic_count']}**",
        f"Blocking record count: **{metrics['blocking_record_count']}**",
        "",
        "| Project | Bundle | Classification | Mapping | Action |",
        "| --- | --- | --- | --- | --- |",
    ]
    lines += [f"| {r['project']} | `{r['bundle_path']}` | {r['classification']} | {r['mapping_status']} | {r['recommended_action']} |" for r in records]
    for record in records:
        lines.extend([
            "",
            f"## `{record['bundle_path']}`",
            "",
            f"- Project: {record['project']}",
            f"- Source paths: {', '.join(f'`{path}`' for path in record['source_paths']) or 'none'}",
            f"- Source bytes: {record['source_bytes']}",
            f"- Bundle bytes: {record['bundle_bytes']}",
            f"- Classification: {record['classification']}",
            f"- Mapping status: {record['mapping_status']}",
            f"- Recommended action: {record['recommended_action']}",
            f"- Candidate canonical source paths: {', '.join(f'`{path}`' for path in record['candidate_source_paths']) or 'none'}",
            f"- Bundle-only excerpt or reference: {json.dumps(record['bundle_only_excerpt_or_ref'], ensure_ascii=False)}",
            f"- Source-only excerpt or reference: {json.dumps(record['source_only_excerpt_or_ref'], ensure_ascii=False)}",
        ])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--markdown-out", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    records = []
    for project, project_dir in PROJECTS.items():
        if project not in TARGET_PROJECTS:
            continue
        upload = (root / project_dir / "Knowledge_Bundles/UPLOAD_LIST.md").read_text(encoding="utf-8")
        required = listed_files(section_between(upload, "## Required upload files", "## Optional upload files"))
        optional = listed_files(section_between(upload, "## Optional upload files", "## Do not upload"))
        for name in required + optional:
            path = root / project_dir / "Knowledge_Bundles" / name
            text = path.read_text(encoding="utf-8")
            declared = source_files_from_bundle(text)
            missing = [source for source in declared if not (root / source).is_file()]
            sources = {source: (root / source).read_text(encoding="utf-8") for source in declared if source not in missing}
            status, bundle_only, source_only = classify(text, sources) if not missing else ("unmapped", [], [])
            records.append({"project": project, "bundle_path": str(path.relative_to(root)), "source_paths": declared,
                            "source_bytes": sum(len(value.encode()) for value in sources.values()), "bundle_bytes": len(text.encode()),
                            "classification": status, "bundle_only_excerpt_or_ref": bundle_only,
                            "source_only_excerpt_or_ref": source_only, "mapping_status": "unmapped" if missing else "mapped",
                            "candidate_source_paths": candidate_source_paths(root, bundle_only),
                            "recommended_action": "eligible_after_review" if status == "equivalent" else "block_generation_and_migrate_or_classify"})
    unresolved = sum(record["classification"] in {"unmapped", "bundle_only_semantic"} for record in records)
    blocking = sum(record["classification"] != "equivalent" for record in records)
    payload = {"audit_scope": sorted(TARGET_PROJECTS), "records": records, "metrics": {"bundles": len(records), "unresolved_bundle_only_semantic_count": unresolved, "blocking_record_count": blocking}}
    args.json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.markdown_out.write_text(render_markdown(payload), encoding="utf-8")
    print(json.dumps(payload["metrics"]))
    return 1 if blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
