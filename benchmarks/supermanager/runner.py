#!/usr/bin/env python3
"""Frozen-input runner for baseline and candidate repository snapshots."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path

from evaluator import evaluate_case, load_cases


HERE = Path(__file__).resolve().parent
DEFINITION_FILES = ("cases.json", "evaluator.py", "runner.py")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def benchmark_hash() -> str:
    digest = hashlib.sha256()
    for name in DEFINITION_FILES:
        digest.update((HERE / name).read_bytes())
    return digest.hexdigest()


def git_value(repo_root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=repo_root, text=True, capture_output=True, check=False
    )
    return completed.stdout.strip() if completed.returncode == 0 else "UNVERIFIED"


def summarize(results: list[dict], weights: dict[str, float]) -> dict:
    by_category: dict[str, list[int]] = defaultdict(list)
    for result in results:
        by_category[result["category"]].append(result["score"])
    category_scores = {
        category: sum(scores) / len(scores) for category, scores in sorted(by_category.items())
    }
    aggregate = sum(category_scores[name] * weight for name, weight in weights.items())
    return {
        "aggregate_score": round(aggregate, 3),
        "category_scores": {key: round(value, 3) for key, value in category_scores.items()},
        "passed": sum(result["passed"] for result in results),
        "failed": sum(not result["passed"] for result in results),
        "failed_case_ids": [result["id"] for result in results if not result["passed"]],
        "failed_hard_fail_classes": [
            result["hard_fail_class"]
            for result in results
            if not result["passed"] and result["hard_fail_class"]
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--role", choices=("baseline", "candidate", "final"), required=True)
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    specification = json.loads((HERE / "specification.json").read_text(encoding="utf-8"))
    results = [evaluate_case(case, repo_root) for case in load_cases(HERE / "cases.json")]
    payload = {
        "benchmark_version": specification["benchmark_version"],
        "benchmark_hash": benchmark_hash(),
        "evaluator_hash": sha256_file(HERE / "evaluator.py"),
        "role": args.role,
        "repository_commit": git_value(repo_root, "rev-parse", "HEAD"),
        "repository_status": git_value(repo_root, "status", "--short"),
        "summary": summarize(results, specification["category_weights"]),
        "results": results,
        "independent_evaluation": "UNVERIFIED",
        "residual_risk": "self-evaluation bias",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0 if payload["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
