#!/usr/bin/env python3
"""Final Judge role: compare immutable raw baseline and candidate results."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    baseline = _load(args.baseline)
    candidate = _load(args.candidate)
    base_eval = baseline["evaluation"]
    candidate_eval = candidate["evaluation"]
    definition = _load(Path(__file__).with_name("benchmark_definition.json"))
    same_benchmark = base_eval["benchmark_hash"] == candidate_eval["benchmark_hash"]
    improvement = round(candidate_eval["score"] - base_eval["score"], 6)
    regressions_pass = all(item["passed"] for item in candidate_eval["results"] if item["case_set"] == "regression")
    verdict = "pass" if (
        same_benchmark
        and candidate["mandatory_checks_pass"]
        and not candidate_eval["hard_failures"]
        and candidate_eval["floors_met"]
        and regressions_pass
        and improvement >= definition["minimal_meaningful_improvement"]
    ) else "revise"
    result = {
        "role": "Final Judge",
        "verdict": verdict,
        "evidence_level": "A",
        "source_baseline_commit": definition["source_baseline_commit"],
        "benchmark_hash": candidate_eval["benchmark_hash"],
        "evaluator_hash": candidate_eval["evaluator_hash"],
        "baseline_commit": baseline["repo_commit"],
        "candidate_commit": candidate["repo_commit"],
        "baseline_score": base_eval["score"],
        "candidate_score": candidate_eval["score"],
        "improvement": improvement,
        "baseline_hard_failures": base_eval["hard_failures"],
        "candidate_hard_failures": candidate_eval["hard_failures"],
        "critical_floors_met": candidate_eval["floors_met"],
        "regression_pass": regressions_pass,
        "mandatory_checks_pass": candidate["mandatory_checks_pass"],
        "benchmark_unchanged": same_benchmark,
        "baseline_raw_sha256": _sha(args.baseline),
        "candidate_raw_sha256": _sha(args.candidate),
        "independent_evaluation": "UNVERIFIED",
        "residual_risk": "self-evaluation bias",
        "external_behavior": "UNVERIFIED",
        "statement": "Best configuration observed within the fixed benchmark, tested scope and available execution capabilities." if verdict == "pass" else "Configuration improvement is not proven within the fixed benchmark."
    }
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
