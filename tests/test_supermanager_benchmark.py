import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmarks" / "supermanager"


def _load_evaluator():
    spec = importlib.util.spec_from_file_location("supermanager_evaluator", BENCHMARK / "evaluator.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_case_ids_are_unique_and_cover_required_minimums() -> None:
    evaluator = _load_evaluator()
    definition = json.loads((BENCHMARK / "benchmark_definition.json").read_text(encoding="utf-8"))
    ids = evaluator.case_ids(definition)
    assert len(ids) == len(set(ids))
    for project in definition["projects"]:
        slug = project.lower().replace(" ", "_")
        assert len([case_id for case_id in ids if case_id.startswith(f"project_{slug}_")]) >= 3
    for route in definition["routes"]:
        route_ids = [case_id for case_id in ids if case_id.startswith(f"route_{route['id']}_")]
        assert len([case_id for case_id in route_ids if "positive" in case_id]) >= 2
        assert len([case_id for case_id in route_ids if "negative" in case_id]) >= 1


def test_each_hard_fail_class_has_an_adversarial_case() -> None:
    evaluator = _load_evaluator()
    definition = json.loads((BENCHMARK / "benchmark_definition.json").read_text(encoding="utf-8"))
    ids = evaluator.case_ids(definition)
    hard_fail_classes = {
        "fabricated_fact", "unsupported_execution_claim", "incorrect_route", "hidden_blocker",
        "lost_material_constraint", "unauthorized_mutation", "direct_main_write",
        "benchmark_manipulation", "holdout_disclosure", "false_external_validation",
        "secret_exposure", "status_or_source_change",
    }
    assert {case_id.removeprefix("adversarial_") for case_id in ids if case_id.startswith("adversarial_")} == hard_fail_classes


def test_weights_total_100_and_evaluator_is_complete() -> None:
    evaluator = _load_evaluator()
    definition = json.loads((BENCHMARK / "benchmark_definition.json").read_text(encoding="utf-8"))
    assert sum(definition["category_weights"].values()) == 100
    result = evaluator.evaluate(ROOT)
    assert result["case_count"] == len(evaluator.case_ids(definition))
    result_by_id = {item["case_id"]: item for item in result["results"]}
    assert all(result_by_id[f"project_{project.lower().replace(' ', '_')}_registry"]["passed"] for project in definition["projects"])
    assert result_by_id["adversarial_unauthorized_mutation"]["passed"]
