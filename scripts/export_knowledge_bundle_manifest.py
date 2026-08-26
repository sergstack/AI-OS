#!/usr/bin/env python3
"""Export the current reviewable bundle composition into declarative JSON."""

from __future__ import annotations

import json
from pathlib import Path

from check_knowledge_bundles import PROJECTS, listed_files, section_between, source_files_from_bundle


TARGETS = {"[AI OS]", "[Thinking]", "[Analytics]", "[LLM]", "[Codex]"}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    bundles = []
    for project, project_dir in PROJECTS.items():
        if project not in TARGETS:
            continue
        upload = (root / project_dir / "Knowledge_Bundles/UPLOAD_LIST.md").read_text(encoding="utf-8")
        names = listed_files(section_between(upload, "## Required upload files", "## Optional upload files"))
        names += listed_files(section_between(upload, "## Optional upload files", "## Do not upload"))
        for name in names:
            path = root / project_dir / "Knowledge_Bundles" / name
            bundles.append({"project": project, "output": str(path.relative_to(root)), "sources": source_files_from_bundle(path.read_text(encoding="utf-8"))})
    payload = {"schema_version": 1, "status": "audit_pending", "bundles": bundles}
    target = root / "knowledge_bundle_manifest.json"
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(target.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
