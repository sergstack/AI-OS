from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AES = ROOT / "AUTONOMOUS_EXECUTION_STANDARD.md"
FAILURE_REGISTRY = ROOT / "ChatGPT/[AI OS]/Knowledge/FAILURE_REGISTRY.md"
GOLDEN_CASES = ROOT / "ChatGPT/[AI OS]/Knowledge/GOLDEN_EVAL_CASES.md"


def test_harness_repair_requires_trace_grounded_attribution():
    aes = AES.read_text(encoding="utf-8")
    registry = FAILURE_REGISTRY.read_text(encoding="utf-8")
    golden_cases = GOLDEN_CASES.read_text(encoding="utf-8")

    assert "A failed execution is evidence of an observed defect" in aes
    assert "harness/workflow repair eligible: true" in aes
    assert "do not select a convenient repair" in aes
    assert "no autonomous diagnosis, self-modification" in aes
    assert "attribution_status: attributable | uncertain | ineligible" in registry

    for case_id in (
        "TRACE-ATTRIBUTION-EXTERNAL-INPUT",
        "TRACE-ATTRIBUTION-LOCALIZED-TARGET",
        "TRACE-ATTRIBUTION-AMBIGUOUS",
        "TRACE-ATTRIBUTION-HARD-REGRESSION",
    ):
        assert case_id in golden_cases

    assert "hard regression is rejected" in aes
