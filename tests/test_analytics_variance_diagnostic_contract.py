import json
from decimal import Decimal
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "ChatGPT/[Analytics]/Knowledge/VARIANCE_DIAGNOSTIC_CONTRACT.md"
TECHNIQUES = ROOT / "ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md"
FIXTURE = ROOT / "tests/fixtures/analytics_variance_diagnostic_cases.json"


def load_cases():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def normalize(plan: Decimal, actual: Decimal, higher_is: str) -> Decimal:
    raw = actual - plan
    if higher_is == "adverse":
        return raw
    if higher_is == "favorable":
        return -raw
    raise ValueError("context-dependent direction requires an explicit business rule")


def test_p0_method_count_remains_22():
    text = TECHNIQUES.read_text(encoding="utf-8")
    registry = text.split("| METHOD_ID | PURPOSE", 1)[1].split("Mixed-component contract:", 1)[0]
    method_ids = re.findall(r"^\| `([^`]+)` \|", registry, flags=re.MULTILINE)
    assert len(method_ids) == 22
    assert len(set(method_ids)) == 22


def test_expense_and_revenue_normalization():
    cases = {case["id"]: case for case in load_cases()["cases"]}
    for case_id in ("A", "B"):
        case = cases[case_id]
        result = normalize(Decimal(case["plan"]), Decimal(case["actual"]), case["higher_is"])
        assert result == Decimal(case["expected_normalized"])
        assert result > 0


def test_historical_driver_discloses_favorable_offset_and_reconciles():
    fixture = load_cases()
    historical = fixture["historical_regression"]
    net = Decimal(historical["main_adverse_driver"]) + Decimal(historical["other_favorable_movements"])
    assert net == Decimal(historical["normalized_net_adverse"])
    assert Decimal(historical["main_adverse_driver"]) > net
    assert Decimal(historical["other_favorable_movements"]) < 0


def test_primary_attribution_and_gross_coverage_are_separate():
    cases = {case["id"]: case for case in load_cases()["cases"]}
    attribution = cases["I"]
    attributed = sum(
        Decimal(attribution[field])
        for field in ("economic_effect", "timing_effect", "data_mapping_effect", "unresolved_effect")
    )
    assert attributed == Decimal(attribution["expected_net"])

    coverage = cases["H"]
    denominator = Decimal(coverage["gross_adverse"]) + Decimal(coverage["gross_favorable_absolute"])
    result = Decimal(coverage["classified_gross_movement"]) / denominator
    assert denominator == Decimal(coverage["expected_denominator"])
    assert denominator != Decimal(coverage["net_variance"])
    assert result == Decimal(coverage["expected_coverage"])


def test_unknown_evidence_states_do_not_escalate():
    cases = {case["id"]: case for case in load_cases()["cases"]}
    assert cases["D"]["expected_controllability"] == "unknown"
    assert cases["F"]["expected_recurrence"] == "unknown"
    assert cases["J"]["expected_controllability"] == "unknown"
    assert cases["E"]["period_count"] == 1
    assert cases["E"]["generalization_evidence"] is None


def test_adjusted_view_reconciles_without_replacing_reported_view():
    case = next(case for case in load_cases()["cases"] if case["id"] == "K")
    adjusted = (
        Decimal(case["reported_management_variance"])
        + Decimal(case["adverse_increasing_adjustments"])
        - Decimal(case["adverse_reducing_adjustments"])
    )
    assert adjusted == Decimal(case["expected_adjusted_management_variance"])
    assert case["reported_view_must_remain_visible"] is True


def test_contract_contains_negative_regression_gates():
    text = CONTRACT.read_text(encoding="utf-8")
    required = [
        "raw mathematical variance != management direction",
        "Never mix raw and normalized signs inside one bridge.",
        "compensating favorable movement must be explicit",
        "Never use small net variance as the denominator for gross classification coverage.",
        "Secondary attributes must never be summed as independent causes",
        "controllability = unknown",
        "single-period evidence != systemic / non-systemic evidence",
        "management_owner != responsible_for_cause",
        "adjusted view is supplementary and never replaces the reported result",
        "No silent exclusion or ambiguous unsigned adjustment polarity is allowed.",
        "driver != root cause",
        "Routine cases must not instantiate the full structure.",
    ]
    for phrase in required:
        assert phrase in text
