#!/usr/bin/env python3
"""Read-only provenance audit for declared Knowledge bundle inputs."""

from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path

from check_knowledge_bundles import PROJECTS, listed_files, section_between, source_files_from_bundle


def normalize(text: str) -> str:
    """Bundles deliberately collapse blank lines; that is not semantic drift."""
    return "\n".join(line.rstrip() for line in text.splitlines() if line.strip())


def classify(bundle: str, sources: dict[str, str]) -> tuple[str, list[dict[str, str]], list[dict[str, str]]]:
    """Classify exact source inclusion; unmatched bundle text is never discarded."""
    content = bundle.split("# Content", 1)[1] if "# Content" in bundle else bundle
    bundle_only: list[dict[str, str]] = []
    source_only: list[dict[str, str]] = []
    for path, text in sources.items():
        marker = f"## From: `{path}`"
        after = content.split(marker, 1)[1] if marker in content else ""
        segment = after.split("## From: `", 1)[0]
        source_lines = [line for line in normalize(text).splitlines() if line]
        bundle_lines = [line for line in normalize(segment).splitlines() if line]
        matcher = difflib.SequenceMatcher(a=source_lines, b=bundle_lines, autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag in {"delete", "replace"}:
                source_only.extend({"path": path, "excerpt": line[:240]} for line in source_lines[i1:i2])
            if tag in {"insert", "replace"}:
                for line in bundle_lines[j1:j2]:
                    if line.startswith("#"):
                        continue
                    bundle_only.append({"path": path, "excerpt": line[:240]})
    if bundle_only:
        return "bundle_only_semantic", bundle_only[:20], source_only[:20]
    if source_only:
        return "source_only", [], source_only[:20]
    return "equivalent", [], []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--markdown-out", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    records = []
    for project, project_dir in PROJECTS.items():
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
                            "recommended_action": "block_generation_and_migrate_or_classify" if status in {"unmapped", "bundle_only_semantic"} else "eligible_after_review"})
    unresolved = sum(record["classification"] in {"unmapped", "bundle_only_semantic"} for record in records)
    payload = {"records": records, "metrics": {"bundles": len(records), "unresolved_bundle_only_semantic_count": unresolved}}
    args.json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Knowledge Bundle Provenance Audit", "", f"Unresolved bundle-only semantic count: **{unresolved}**", "", "| Project | Bundle | Classification | Mapping | Action |", "| --- | --- | --- | --- | --- |"]
    lines += [f"| {r['project']} | `{r['bundle_path']}` | {r['classification']} | {r['mapping_status']} | {r['recommended_action']} |" for r in records]
    args.markdown_out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(payload["metrics"]))
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
