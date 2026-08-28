from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EN_README = ROOT / "README.md"
RU_README = ROOT / "README_RU.md"
EN_DETAIL = ROOT / "docs/OPERATIONAL_RELIABILITY_EN.md"
RU_DETAIL = ROOT / "docs/OPERATIONAL_RELIABILITY.md"

LANGUAGE_SWITCH = "[English]({english}) | [Русский]({russian})"
CORRESPONDENCE_ROWS = (
    "| Жизненный цикл evidence | Evidence lifecycle ledger | Журнал жизненного цикла evidence |",
    "| Намерение запуска | Versioned run intent | Версионированное намерение запуска |",
    "| Наблюдаемость отказов | Typed fault telemetry | Типизированная телеметрия сбоев |",
    "| Превращение сбоя в проверку | Failure-to-regression harness | Контур «сбой → регрессия» |",
)
CONTRACT_NAMES = (
    "EvidenceUnit",
    "ACTIVE",
    "SUPERSEDED",
    "REVOKED",
    "Candidate Gate",
    "Human Gold",
    "fail-closed",
    "digest",
)


def test_operational_reliability_readmes_are_language_paired() -> None:
    english = EN_README.read_text(encoding="utf-8")
    russian = RU_README.read_text(encoding="utf-8")

    assert LANGUAGE_SWITCH.format(english="README.md", russian="README_RU.md") in english
    assert LANGUAGE_SWITCH.format(english="README.md", russian="README_RU.md") in russian
    assert "### Candidate operational reliability layer" in english
    assert "### Candidate operational reliability layer" in russian
    assert "docs/OPERATIONAL_RELIABILITY_EN.md" in english
    assert "docs/OPERATIONAL_RELIABILITY.md" in russian

    for row in CORRESPONDENCE_ROWS:
        assert row in english
        assert row in russian


def test_operational_reliability_detail_docs_preserve_contract_names() -> None:
    english = EN_DETAIL.read_text(encoding="utf-8")
    russian = RU_DETAIL.read_text(encoding="utf-8")

    assert LANGUAGE_SWITCH.format(
        english="OPERATIONAL_RELIABILITY_EN.md",
        russian="OPERATIONAL_RELIABILITY.md",
    ) in english
    assert LANGUAGE_SWITCH.format(
        english="OPERATIONAL_RELIABILITY_EN.md",
        russian="OPERATIONAL_RELIABILITY.md",
    ) in russian

    for text in (english, russian):
        assert "Status: `candidate`" in text or "Статус: `candidate`" in text
        assert "does not create" in text or "не создаёт" in text
        for name in CONTRACT_NAMES:
            assert name in text
