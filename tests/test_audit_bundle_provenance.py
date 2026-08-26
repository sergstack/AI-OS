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
