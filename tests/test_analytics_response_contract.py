from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTRUCTIONS = ROOT / "ChatGPT/[Analytics]/PROJECT_INSTRUCTIONS.md"
SMOKE_QA = ROOT / "ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md"


def test_quick_mode_uses_evidence_bearing_compact_form() -> None:
    text = INSTRUCTIONS.read_text(encoding="utf-8")

    assert "at most one table with actual inputs or calculated rows" in text
    assert "one combined `QA / limitation / next` line" in text


def test_missing_data_fast_path_has_no_empty_ranking() -> None:
    text = INSTRUCTIONS.read_text(encoding="utf-8")

    assert "Missing-data fast path" in text
    assert "return `NOT CALCULABLE`" in text
    assert "No placeholder rankings, empty Top-N tables" in text
    assert "or repeated blocker" in text


def test_smoke_qa_covers_missing_data_response_contract() -> None:
    text = SMOKE_QA.read_text(encoding="utf-8")

    assert "## 9. Missing-data compact fast path" in text
    assert "no placeholder ranking or empty Top-N table" in text
    assert "same blocker is not repeated" in text
