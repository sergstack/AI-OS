from __future__ import annotations

from pathlib import Path
import re

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT = REPO_ROOT / "ChatGPT/[Thinkers OS]"
UPLOAD_NAMES = [
    "THINKERS_OS_01_PORTFOLIO_AND_CORPUS.md",
    "THINKERS_OS_02_ARTIFACTS_AND_SYNTHESIS.md",
]


def read(relative: str) -> str:
    return (PROJECT / relative).read_text(encoding="utf-8")


def upload_files() -> list[str]:
    text = read("Knowledge_Bundles/UPLOAD_LIST.md")
    section = text.split("## Required upload files", 1)[1].split(
        "## Optional upload files", 1
    )[0]
    return re.findall(r"^- `([^`]+)`$", section, flags=re.MULTILINE)


def test_project_package_has_required_bundle_first_structure() -> None:
    expected = {
        "PROJECT_INSTRUCTIONS.md",
        "README.md",
        "CURRENT_STATUS.md",
        "SMOKE_QA_RESULTS.md",
        "Knowledge/INDEX.md",
        "Knowledge/THINKERS_OS_WORKFLOW.md",
        "Knowledge/CORPUS_AND_SOURCE_RULES.md",
        "Knowledge/ARTIFACT_CONTRACTS.md",
        "Knowledge/SYNTHESIS_AND_EXPORT.md",
        "Knowledge/ROUTING_AND_HANDOFF.md",
        "Knowledge_Bundles/README.md",
        "Knowledge_Bundles/UPLOAD_LIST.md",
        *(f"Knowledge_Bundles/{name}" for name in UPLOAD_NAMES),
    }

    assert all((PROJECT / relative).is_file() for relative in expected)


def test_upload_list_is_exact_and_authoritative() -> None:
    text = read("Knowledge_Bundles/UPLOAD_LIST.md")

    assert upload_files() == UPLOAD_NAMES
    assert "single authoritative manual upload list" in text
    assert "Optional: 0" in text
    assert "Total if all uploaded: 2" in text


def test_upload_list_excludes_granular_and_unsafe_payloads() -> None:
    listed = upload_files()

    assert all("/" not in name and "\\" not in name for name in listed)
    assert all(not name.lower().endswith((".pdf", ".epub", ".fb2", ".zip")) for name in listed)
    assert all("manifest" not in name.lower() and "log" not in name.lower() for name in listed)


def test_bundle_sources_are_only_bounded_repository_markdown() -> None:
    for name in UPLOAD_NAMES:
        text = read(f"Knowledge_Bundles/{name}")
        section = text.split("## Source files", 1)[1].split("## Upload target", 1)[0]
        sources = re.findall(r"- `([^`]+)`", section)

        assert sources
        assert all(source.startswith("ChatGPT/[Thinkers OS]/") for source in sources)
        assert all(source.endswith(".md") for source in sources)
        assert all("Knowledge_Bundles" not in source for source in sources)


def test_canonical_name_and_manual_external_boundary() -> None:
    texts = "\n".join(path.read_text(encoding="utf-8") for path in PROJECT.rglob("*.md"))

    assert "[Thinkers OS]" in texts
    assert "[Thinker OS]" not in texts
    assert "external_project_status: UPDATED" in texts
    assert "external_sources_sync_status: UPDATED WITH DISPLAY-NAME LIMITATION" in texts
    assert "external_full_suite: NOT RUN" in texts
    assert "production_status: NOT AUTHORIZED" in texts
    assert "owner_acceptance: pending" in texts


def test_source_gate_is_scope_based_and_compact() -> None:
    instructions = read("PROJECT_INSTRUCTIONS.md")
    source_rules = read("Knowledge/CORPUS_AND_SOURCE_RULES.md")
    workflow = read("Knowledge/THINKERS_OS_WORKFLOW.md")
    bundle = read("Knowledge_Bundles/THINKERS_OS_01_PORTFOLIO_AND_CORPUS.md")

    for text in (instructions, source_rules, workflow, bundle):
        assert "whole project" in text or "blanket project blocker" in text

    assert "scope | status | evidence | next action" in instructions
    assert "request closure" in source_rules
    assert "unaffected Judge-pass synthesis" in bundle


@pytest.mark.parametrize(
    ("scenario", "needle", "relative"),
    [
        ("missing book routes to source pipeline", "source request/intake", "Knowledge/ROUTING_AND_HANDOFF.md"),
        ("real decision routes to Thinking", "real decision", "Knowledge/ROUTING_AND_HANDOFF.md"),
        ("extraction prompt routes to LLM", "extraction prompt", "Knowledge/ROUTING_AND_HANDOFF.md"),
        ("source pipeline implementation routes to Codex", "repository implementation", "Knowledge/ROUTING_AND_HANDOFF.md"),
        ("quantitative validation routes to Analytics", "quantitative validation", "Knowledge/ROUTING_AND_HANDOFF.md"),
        ("missing verified source blocks claim", "no verified source", "PROJECT_INSTRUCTIONS.md"),
        ("partial corpus is not complete", "package is not complete", "Knowledge/CORPUS_AND_SOURCE_RULES.md"),
        ("preview is not a full work", "Preview, sample chapter", "Knowledge/CORPUS_AND_SOURCE_RULES.md"),
        ("raw and normalized source payloads are excluded", "Never export books, normalized text", "Knowledge/ARTIFACT_CONTRACTS.md"),
        ("non-pass artifacts cannot control synthesis", "cannot control active synthesis", "Knowledge/THINKERS_OS_WORKFLOW.md"),
        ("uploaded bundle is not live state", "never live repository evidence", "Knowledge_Bundles/THINKERS_OS_01_PORTFOLIO_AND_CORPUS.md"),
        ("handoff has one recipient and canonical fields", "Use one receiving project", "Knowledge/ROUTING_AND_HANDOFF.md"),
    ],
)
def test_smoke_contracts(scenario: str, needle: str, relative: str) -> None:
    assert needle in read(relative), scenario


def test_repository_routing_surfaces_discover_thinkers_os() -> None:
    registry = (REPO_ROOT / "PROJECT_REGISTRY.md").read_text(encoding="utf-8")
    repo_paths = (REPO_ROOT / "REPO_PATHS.md").read_text(encoding="utf-8")
    routing_rules = (REPO_ROOT / "ROUTING_RULES.md").read_text(encoding="utf-8")

    assert "ChatGPT/[Thinkers OS]" in registry
    assert "ChatGPT/[Thinkers OS]" in repo_paths
    assert "[Thinkers OS]" in routing_rules
    assert "Strategy, decision" in routing_rules
    assert "[Thinking]" in routing_rules
