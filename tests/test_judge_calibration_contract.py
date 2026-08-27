from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CALIBRATION = ROOT / "ChatGPT/[AI OS]/Knowledge/JUDGE_CALIBRATION.md"
GOLDEN_CASES = ROOT / "ChatGPT/[AI OS]/Knowledge/GOLDEN_EVAL_CASES.md"


def test_judge_bias_regression_cases_are_small_and_reusable():
    calibration = CALIBRATION.read_text(encoding="utf-8")
    golden_cases = GOLDEN_CASES.read_text(encoding="utf-8")

    for case_id in (
        "JUDGE-SELF-PREFERENCE",
        "JUDGE-LANGUAGE-PARITY",
        "JUDGE-AMBIGUITY-CALIBRATION",
        "JUDGE-REFERENCE-AVAILABLE",
    ):
        assert case_id in golden_cases

    assert "Deterministic checks override LLM judge" in calibration
    assert "not a claim of universal vendor behavior" in calibration
    assert "owner acceptance" in calibration
