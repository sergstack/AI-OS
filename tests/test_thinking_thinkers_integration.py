from __future__ import annotations

from pathlib import Path
import re

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
THINKING = REPO_ROOT / "ChatGPT/[Thinking]"
BUNDLE_NAME = "THINKING_04_THINKERS_SYNTHESIS.md"
PATTERN_IDS = [
    "SYN-001-REPEATED-FAILURE-DIAGNOSIS",
    "SYN-002-DECISION-UNDER-FRICTION",
    "SYN-003-OWNERSHIP-AND-SYSTEM-CHECK",
    "SYN-004-BIAS-AWARE-DECISION-REVIEW",
    "SYN-005-REVERSIBLE-INTERVENTION-GATE",
]


def read(relative: str) -> str:
    return (THINKING / relative).read_text(encoding="utf-8")


def listed_uploads() -> list[str]:
    text = read("Knowledge_Bundles/UPLOAD_LIST.md")
    section = text.split("## Required upload files", 1)[1].split(
        "## Optional upload files", 1
    )[0]
    return re.findall(r"^- `([^`]+)`", section, flags=re.MULTILINE)


def test_named_thinking_artifacts_exist_and_are_indexed() -> None:
    names = [
        "THINKERS_LENS_ROUTER.md",
        "THINKERS_CONFLICT_MAP.md",
        "THINKERS_SYNTHESIS_PATTERNS.md",
        "THINKERS_APPLICATION_LOG.md",
    ]
    index = read("Knowledge/INDEX.md")

    assert all((THINKING / "Knowledge" / name).is_file() for name in names)
    assert all(name in index for name in names)
    assert (THINKING / "Knowledge_Bundles" / BUNDLE_NAME).is_file()


def test_upload_list_adds_exact_thinking_synthesis_bundle() -> None:
    assert listed_uploads() == [
        "THINKING_01_WORKFLOW_AND_DECISIONS.md",
        "THINKING_02_JUDGE_REVISOR_RISK.md",
        "THINKING_03_ROUTING_AND_TEMPLATES.md",
        BUNDLE_NAME,
    ]
    assert "Required: 4" in read("Knowledge_Bundles/UPLOAD_LIST.md")
    assert "Total if all uploaded: 4" in read("Knowledge_Bundles/UPLOAD_LIST.md")


def test_bundle_uses_bounded_repository_markdown_sources() -> None:
    text = read(f"Knowledge_Bundles/{BUNDLE_NAME}")
    section = text.split("## Source files", 1)[1].split("## Upload target", 1)[0]
    sources = re.findall(r"- `([^`]+)`", section)

    assert sources == [
        "ChatGPT/[Thinkers OS]/Knowledge/SYNTHESIS_AND_EXPORT.md",
        "ChatGPT/[Thinking]/Knowledge/THINKERS_LENS_ROUTER.md",
        "ChatGPT/[Thinking]/Knowledge/THINKERS_CONFLICT_MAP.md",
        "ChatGPT/[Thinking]/Knowledge/THINKERS_SYNTHESIS_PATTERNS.md",
        "ChatGPT/[Thinking]/Knowledge/THINKERS_APPLICATION_LOG.md",
    ]
    assert all(source.endswith(".md") for source in sources)
    assert all((REPO_ROOT / source).is_file() for source in sources)


def test_bundle_contains_exactly_five_active_provisional_patterns() -> None:
    text = read(f"Knowledge_Bundles/{BUNDLE_NAME}")
    headings = re.findall(r"^### `([^`]+)`$", text, flags=re.MULTILINE)

    assert headings == PATTERN_IDS
    assert "All five remain `active_provisional`" in text
    assert "canonical_status: false" in text
    assert "owner_acceptance: pending" in text
    assert "production_status: NOT AUTHORIZED" in text


def test_isolated_and_unjudged_material_is_explicitly_excluded() -> None:
    text = read(f"Knowledge_Bundles/{BUNDLE_NAME}")

    assert "isolated Boyd, Drucker, Munger, and Ohno author patterns" in text
    assert "pilot candidate router/conflict revisions without separate Judge authorization" in text
    assert "candidate, revise, blocked, restricted, deprecated, rejected, or archival artifacts" in text


def test_application_log_is_empty_schema_not_imported_history() -> None:
    text = read("Knowledge/THINKERS_APPLICATION_LOG.md")

    assert "application_id:" in text
    assert "No entries recorded in the AI-OS repository at integration time" in text
    assert not re.search(r"^### APP-", text, flags=re.MULTILINE)
    assert "evidence_files:" not in text
    assert "application count never promotes" in text.lower()


def test_bundle_excludes_source_payloads_and_local_paths() -> None:
    text = read(f"Knowledge_Bundles/{BUNDLE_NAME}")
    lowered = text.lower()

    assert "/" + "Users/" not in text
    assert "/" + "home/" not in text
    assert "data/thinkers_os/" not in text
    assert not re.search(r"\.(pdf|epub|fb2|zip)\b", lowered)
    assert "### APP-" not in text
    assert "contains_raw_source_text: true" not in lowered


def test_thinking_applies_patterns_without_owning_corpus_or_status() -> None:
    instructions = read("PROJECT_INSTRUCTIONS.md")

    assert "`[Thinking]` \u043f\u0440\u0438\u043c\u0435\u043d\u044f\u0435\u0442 Judge-pass active provisional patterns" in instructions
    assert "`[Thinkers OS]` \u0443\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u0442 \u0430\u0432\u0442\u043e\u0440\u0430\u043c\u0438" in instructions
    assert "\u041d\u0435 \u0437\u0430\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0439 \u043a\u043d\u0438\u0433\u0438" in instructions


@pytest.mark.parametrize(
    ("scenario", "needle", "relative"),
    [
        ("problem is classified", "First classify one primary problem type", "Knowledge/THINKERS_LENS_ROUTER.md"),
        ("two to four lenses", "Never activate more than four lenses", "Knowledge/THINKERS_LENS_ROUTER.md"),
        ("Conflict Map is checked", "conflict_map_check", "Knowledge/THINKERS_LENS_ROUTER.md"),
        ("case evidence has precedence", "Case facts and direct evidence", "Knowledge/THINKERS_LENS_ROUTER.md"),
        ("irrelevant authors are not enumerated", "Do not enumerate unrelated authors", "Knowledge/THINKERS_LENS_ROUTER.md"),
        ("simple work is not overcomplicated", "simple, routine, reversible task", "Knowledge/THINKERS_LENS_ROUTER.md"),
        ("Analytics LLM Codex routing remains", "`[Analytics]`, `[LLM]`, or `[Codex]`", "Knowledge/THINKERS_LENS_ROUTER.md"),
    ],
)
def test_requested_smoke_contracts(scenario: str, needle: str, relative: str) -> None:
    assert needle in read(relative), scenario
