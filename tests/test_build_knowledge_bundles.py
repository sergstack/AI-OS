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
