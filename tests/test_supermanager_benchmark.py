import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmarks" / "supermanager"


def _load_evaluator():
    spec = importlib.util.spec_from_file_location("supermanager_evaluator", BENCHMARK / "evaluator.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class SupermanagerBenchmarkTests(unittest.TestCase):
    def test_case_ids_are_unique_and_categories_are_weighted(self):
        cases = json.loads((BENCHMARK / "cases.json").read_text(encoding="utf-8"))["cases"]
        specification = json.loads((BENCHMARK / "specification.json").read_text(encoding="utf-8"))
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual({case["category"] for case in cases}, set(specification["category_weights"]))
        self.assertAlmostEqual(sum(specification["category_weights"].values()), 1.0)

    def test_each_project_has_two_positive_and_one_negative_case(self):
        cases = json.loads((BENCHMARK / "cases.json").read_text(encoding="utf-8"))["cases"]
        projects = ["[AI OS]", "[Thinking]", "[Analytics]", "[LLM]", "[Codex]", "[Inbox Router]", "[Thinkers OS]"]
        for project in projects:
            positive = [case for case in cases if case["project"] == project and "-POS-" in case["id"]]
            negative = [case for case in cases if case["project"] == project and "-NEG-" in case["id"]]
            self.assertGreaterEqual(len(positive), 2, project)
            self.assertGreaterEqual(len(negative), 1, project)

    def test_registry_case_passes_for_current_repository(self):
        evaluator = _load_evaluator()
        case = {"id": "test", "set": "repository", "project": "repository", "route": "registry", "category": "regression_stability", "assertion": "registry_matches"}
        result = evaluator.evaluate_case(case, ROOT)
        self.assertTrue(result["passed"], result["evidence"])


if __name__ == "__main__":
    unittest.main()
