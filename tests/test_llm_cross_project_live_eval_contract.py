from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "ChatGPT/[LLM]/Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md"
AIOS_INSTRUCTIONS = ROOT / "ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md"
LLM_INSTRUCTIONS = ROOT / "ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md"
THINKING_INSTRUCTIONS = ROOT / "ChatGPT/[Thinking]/PROJECT_INSTRUCTIONS.md"


EXPECTED_CASES = {
    "CASE-AIOS-LLM-001",
    "CASE-THINKING-LLM-001",
    "CASE-ANALYTICS-LLM-001",
    "CASE-LLM-LLM-001",
    "CASE-CODEX-LLM-001",
    "CASE-INBOX-LLM-001",
    "CASE-THINKERS-LLM-001",
}


def test_matrix_is_versioned_and_covers_every_registered_chatgpt_project() -> None:
    text = MATRIX.read_text(encoding="utf-8")

    assert "matrix_id: `LLM-XPROJECT-LIVE-001`" in text
    assert "version: `1.0.0-candidate`" in text
    assert "owner_project: `[LLM]`" in text
    assert "production_status: `NOT AUTHORIZED`" in text
    assert {case for case in EXPECTED_CASES if f"### {case}" in text} == EXPECTED_CASES


def test_every_case_has_local_and_downstream_quality_gates() -> None:
    text = MATRIX.read_text(encoding="utf-8")

    case_definitions = text.split("## Cases", maxsplit=1)[1].split(
        "## Result record", maxsplit=1
    )[0]
    sections = case_definitions.split("### CASE-")[1:]
    assert len(sections) == len(EXPECTED_CASES)
    for section in sections:
        assert "- local_gate:" in section
        assert "- downstream_gate:" in section
        assert "- prompt:" in section
        assert "- expected:" in section


def test_partial_baseline_distinguishes_observed_and_blocked_cases() -> None:
    text = MATRIX.read_text(encoding="utf-8")

    assert "| CASE-INBOX-LLM-001 | `[Inbox Router]` | PASS | 9/10 |" in text
    assert "| CASE-AIOS-LLM-001 | `[AI OS]` | BLOCKED | 5/10 |" in text
    assert "| CASE-THINKING-LLM-001 | `[Thinking]` | BLOCKED | 4/10 |" in text
    assert "| CASE-LLM-LLM-001 | `[LLM]` | REVISE | 9/10 |" in text
    summary = text.split("## Baseline summary", maxsplit=1)[1].split(
        "## Observed results", maxsplit=1
    )[0]
    assert summary.count("| NOT RUN | - |") == len(EXPECTED_CASES) - 4
    assert "Overall baseline status: `PARTIAL`." in text
    assert "judge_verdict: NOT RUN" in text
    assert "rate-limit dialog" in text
    assert "record\n   the case as `NOT RUN`, not fail" in text


def test_ai_os_stops_after_handoff_for_llm_owned_deliverables() -> None:
    text = AIOS_INSTRUCTIONS.read_text(encoding="utf-8")

    assert "`[LLM]` ownership rule" in text
    assert "focused, executable handoff" in text
    assert "do not omit information needed to continue the work" in text
    assert "must not choose the model class, write the\nprompt or design the LLM workflow" in text


def test_llm_treats_an_explicit_length_limit_as_a_hard_cap() -> None:
    text = LLM_INSTRUCTIONS.read_text(encoding="utf-8")

    assert "An explicit user maximum is a hard cap" in text
    assert "including headings, tables and source labels" in text
    assert "keep a\nsmall buffer" in text


def test_thinking_stops_when_llm_owns_the_requested_deliverable() -> None:
    text = THINKING_INSTRUCTIONS.read_text(encoding="utf-8")

    assert "`[LLM]` ownership rule" in text
    assert "no strategic decision is requested" in text
    assert "focused, executable handoff" in text
    assert "do not\nomit information needed to continue the work" in text
    assert "Do not design the prompt, select\nthe model or expand the downstream workflow" in text
