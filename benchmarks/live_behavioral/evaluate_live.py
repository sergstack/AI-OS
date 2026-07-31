#!/usr/bin/env python3
"""Validate and aggregate frozen live benchmark captures and annotations."""

from __future__ import annotations

import argparse
import hashlib
import json
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--captures", required=True, type=Path)
    parser.add_argument("--annotations", required=True, type=Path)
    parser.add_argument("--phase", required=True, choices=["baseline", "candidate", "holdout"])
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    spec = load_json(HERE / "benchmark_spec.json")
    rubric = load_json(HERE / "rubric.json")
    cases = {item["case_id"]: item for item in load_json(HERE / "cases.json")}
    captures = load_jsonl(args.captures)
    annotations = load_jsonl(args.annotations)
    annotation_by_key = {(item["case_id"], item["run"]): item for item in annotations}
    expected_runs = 1 if args.phase == "holdout" else spec["runs_per_case"]
    if args.phase != "holdout":
        expected_keys = {(case_id, run) for case_id in cases for run in range(1, expected_runs + 1)}
        actual_keys = {(item["case_id"], item["run"]) for item in captures}
        if actual_keys != expected_keys:
            raise SystemExit(f"capture coverage mismatch: missing={sorted(expected_keys-actual_keys)} extra={sorted(actual_keys-expected_keys)}")
    criterion_names = {category: list(data["criteria"]) for category, data in rubric["categories"].items()}
    run_results = []
    for capture in captures:
        key = (capture["case_id"], capture["run"])
        annotation = annotation_by_key.get(key)
        if annotation is None:
            raise SystemExit(f"missing annotation for {key}")
        if capture["prompt_sha256"] != sha256_text(capture["prompt"]):
            raise SystemExit(f"prompt hash mismatch for {key}")
        if capture["response_sha256"] != sha256_text(capture["response"]):
            raise SystemExit(f"response hash mismatch for {key}")
        category_scores = {}
        for category, names in criterion_names.items():
            values = annotation["criteria"][category]
            if set(values) != set(names) or any(not 0 <= score <= 4 for score in values.values()):
                raise SystemExit(f"invalid rubric scores for {key} {category}")
            category_scores[category] = sum(values.values()) / (4 * len(names)) * 100
        aggregate = sum(category_scores[name] * weight / 100 for name, weight in spec["category_weights"].items())
        hard_failures = annotation.get("hard_failures", [])
        unknown_hard_failures = set(hard_failures) - set(spec["hard_fail_rules"])
        if unknown_hard_failures:
            raise SystemExit(f"unknown hard failures for {key}: {sorted(unknown_hard_failures)}")
        run_results.append({"case_id": capture["case_id"], "run": capture["run"], "categories": category_scores, "aggregate": aggregate, "hard_failures": hard_failures})

    aggregates = [item["aggregate"] for item in run_results]
    categories = {}
    for category in spec["category_weights"]:
        values = [item["categories"][category] for item in run_results]
        categories[category] = {"median": statistics.median(values), "minimum": min(values), "maximum": max(values), "range": max(values)-min(values)}
    hard_failure_count = sum(len(item["hard_failures"]) for item in run_results)
    result = {
        "phase": args.phase,
        "benchmark_version": spec["benchmark_version"],
        "capture_count": len(captures),
        "aggregate": {"median": statistics.median(aggregates), "minimum": min(aggregates), "maximum": max(aggregates), "range": max(aggregates)-min(aggregates)},
        "categories": categories,
        "hard_failure_count": hard_failure_count,
        "hard_failures": sorted({failure for item in run_results for failure in item["hard_failures"]}),
        "captures_sha256": hashlib.sha256(args.captures.read_bytes()).hexdigest(),
        "annotations_sha256": hashlib.sha256(args.annotations.read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
