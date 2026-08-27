from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location("bundle_audit", ROOT / "scripts/audit_bundle_provenance.py")
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


def test_blank_line_compaction_is_equivalent() -> None:
    bundle = "# Content\n\n## From: `Knowledge/a.md`\n\n# Title\n\nText\n"
    status, bundle_only, source_only = AUDIT.classify(bundle, {"Knowledge/a.md": "# Title\n\nText\n"})
    assert status == "equivalent"
    assert bundle_only == []
    assert source_only == []


def test_bundle_only_line_blocks_generation() -> None:
    bundle = "# Content\n## From: `Knowledge/a.md`\n# Title\nText\nAdditional rule\n"
    status, bundle_only, source_only = AUDIT.classify(bundle, {"Knowledge/a.md": "# Title\nText\n"})
    assert status == "bundle_only_semantic"
    assert bundle_only == [{"path": "Knowledge/a.md", "excerpt": "Additional rule"}]
    assert source_only == []


def test_source_only_line_is_reported_without_bundle_semantic_claim() -> None:
    bundle = "# Content\n## From: `Knowledge/a.md`\n# Title\n"
    status, bundle_only, source_only = AUDIT.classify(bundle, {"Knowledge/a.md": "# Title\nMissing\n"})
    assert status == "source_only"
    assert bundle_only == []
    assert source_only == [{"path": "Knowledge/a.md", "excerpt": "Missing"}]


def test_unexpected_content_section_is_structural_drift() -> None:
    bundle = "# Content\n## From: `Knowledge/a.md`\n# Title\n## From: `Knowledge/unmapped.md`\nExtra\n"
    status, bundle_only, source_only = AUDIT.classify(bundle, {"Knowledge/a.md": "# Title\n"})
    assert status == "bundle_only_structural"
    assert bundle_only == [{"path": "bundle", "excerpt": "unexpected section: Knowledge/unmapped.md"}]
    assert source_only == []


def test_markdown_report_has_all_provenance_fields() -> None:
    report = AUDIT.render_markdown({
        "metrics": {"unresolved_bundle_only_semantic_count": 1, "blocking_record_count": 1},
        "records": [{
            "project": "[AI OS]", "bundle_path": "bundle.md", "source_paths": ["Knowledge/a.md"],
            "source_bytes": 1, "bundle_bytes": 2, "classification": "bundle_only_semantic",
            "mapping_status": "mapped", "recommended_action": "block_generation_and_migrate_or_classify",
            "resolution_status": "unresolved",
            "candidate_source_paths": ["Knowledge/candidate.md"],
            "bundle_only_excerpt_or_ref": [{"path": "Knowledge/a.md", "excerpt": "extra"}],
            "source_only_excerpt_or_ref": [],
        }],
    })
    for field in ("Source paths", "Source bytes", "Bundle bytes", "Classification", "Mapping status", "Recommended action", "Bundle-only excerpt", "Source-only excerpt"):
        assert field in report


def test_candidate_sources_exclude_bundles_and_archives(tmp_path: Path) -> None:
    (tmp_path / "Knowledge").mkdir()
    (tmp_path / "Knowledge_Bundles").mkdir()
    (tmp_path / "archive").mkdir()
    phrase = "This is a unique canonical source sentence for matching."
    (tmp_path / "Knowledge" / "candidate.md").write_text(phrase, encoding="utf-8")
    (tmp_path / "Knowledge_Bundles" / "copy.md").write_text(phrase, encoding="utf-8")
    (tmp_path / "archive" / "old.md").write_text(phrase, encoding="utf-8")
    assert AUDIT.candidate_source_paths(tmp_path, [{"path": "x", "excerpt": phrase}]) == ["Knowledge/candidate.md"]
