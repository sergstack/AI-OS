import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmarks" / "live_behavioral"


def load(name):
    return json.loads((BENCHMARK / name).read_text(encoding="utf-8"))


def test_fixed_case_catalog_has_required_sets_and_counts():
    cases = load("cases.json")
    assert len(cases) == 45
    assert len({case["case_id"] for case in cases}) == 45
    assert Counter(case["set"] for case in cases) == {
        "routing": 21,
        "response_quality": 5,
        "readability": 10,
        "adversarial": 9,
    }


def test_each_project_has_three_core_cases_and_each_route_has_two_positive_one_negative():
    cases = load("cases.json")
    spec = load("benchmark_spec.json")
    for project in spec["tested_projects"]:
        core = [case for case in cases if case["project"] == project and "core" in case["tags"]]
        assert len(core) >= 3
        assert len([case for case in core if "positive" in case["tags"]]) >= 2
        assert len([case for case in core if "negative" in case["tags"]]) >= 1


def test_cross_project_readability_and_hard_fail_coverage():
    cases = load("cases.json")
    spec = load("benchmark_spec.json")
    assert len([case for case in cases if "cross_project" in case["tags"]]) >= 5
    assert len([case for case in cases if case["set"] == "readability" and case["complexity"] == "simple"]) >= 5
    assert len([case for case in cases if case["set"] == "readability" and case["complexity"] == "material"]) >= 5
    tags = {tag for case in cases for tag in case["tags"]}
    assert set(spec["hard_fail_rules"]) <= tags


def test_scoring_contract_is_complete_and_totals_100():
    spec = load("benchmark_spec.json")
    rubric = load("rubric.json")
    assert sum(spec["category_weights"].values()) == 100
    assert spec["category_weights"] == {name: data["weight"] for name, data in rubric["categories"].items()}
    assert all(data["criteria"] for data in rubric["categories"].values())


def test_evaluator_module_loads():
    module_spec = importlib.util.spec_from_file_location("evaluate_live", BENCHMARK / "evaluate_live.py")
    module = importlib.util.module_from_spec(module_spec)
    assert module_spec.loader is not None
    module_spec.loader.exec_module(module)
