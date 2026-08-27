from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("bundle_builder", ROOT / "scripts/build_knowledge_bundles.py")
assert SPEC and SPEC.loader
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)


def test_render_is_deterministic_and_includes_provenance(tmp_path: Path) -> None:
    (tmp_path / "Knowledge").mkdir()
    (tmp_path / "Knowledge/a.md").write_text("# A\n\nText\n", encoding="utf-8")
    item = {"output": "out.md", "sources": ["Knowledge/a.md"]}
    first = BUILDER.render(tmp_path, item)
    assert first == BUILDER.render(tmp_path, item)
    assert "source_fingerprint: sha256:" in first
    assert "## From: `Knowledge/a.md`" in first


def test_render_rejects_forbidden_source(tmp_path: Path) -> None:
    (tmp_path / "logs").mkdir()
    (tmp_path / "logs/a.md").write_text("x", encoding="utf-8")
    try:
        BUILDER.render(tmp_path, {"output": "out.md", "sources": ["logs/a.md"]})
    except ValueError as exc:
        assert "forbidden" in str(exc)
    else:
        raise AssertionError("forbidden input was accepted")


def test_render_preserves_declarative_upload_contract(tmp_path: Path) -> None:
    (tmp_path / "Knowledge").mkdir()
    (tmp_path / "Knowledge/a.md").write_text("# A\nText\n", encoding="utf-8")
    item = {
        "output": "out.md",
        "sources": ["Knowledge/a.md"],
        "contract": {
            "title": "Project — Bundle",
            "purpose": "Compact upload artifact.",
            "upload_target": "ChatGPT Project Sources / Knowledge for `[Test]`.",
            "status_lines": ["production_promotion: no"],
        },
    }
    rendered = BUILDER.render(tmp_path, item)
    assert rendered.startswith("# Project — Bundle\n\n## Purpose\n\nCompact upload artifact.")
    assert "## Source files\n\n- `Knowledge/a.md`" in rendered
    assert "- production_promotion: no" in rendered


def test_check_distinguishes_provenance_and_stale_content(tmp_path: Path) -> None:
    (tmp_path / "Knowledge").mkdir()
    (tmp_path / "Knowledge/a.md").write_text("# A\nText\n", encoding="utf-8")
    item = {"output": "out.md", "sources": ["Knowledge/a.md"]}
    expected = BUILDER.render(tmp_path, item)
    (tmp_path / "out.md").write_text(expected.replace("Text", "Changed"), encoding="utf-8")
    assert BUILDER.check(tmp_path, {"bundles": [item]}) == ["STALE_BUNDLE: out.md"]
    (tmp_path / "out.md").write_text(expected.replace("source_fingerprint: sha256:", "source_fingerprint: sha256:0"), encoding="utf-8")
    assert BUILDER.check(tmp_path, {"bundles": [item]}) == ["HASH_PROVENANCE_MISMATCH: out.md"]
