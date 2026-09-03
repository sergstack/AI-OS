#!/usr/bin/env python3
"""Stochasticity, non-inferiority, and decision-comparator method for AIOS
AutoResearch v0.1 (issue #395, parent #388), owner [Analytics].

This is a deterministic, EXACT, rule-based method -- not inferential
statistics. Issue #389's baseline audit found no existing significance/
non-inferiority tooling in this repository, and issue #395 forbids inventing
a p-value, confidence interval, or significance claim "unless actually
computed under an explicit method and assumptions." At N=3-5 discrete,
non-independent Judge-verdict reruns, an asymptotic method would itself be
the dishonest claim this issue bans. See
ChatGPT/[Analytics]/Knowledge/AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md
for the full rationale and section-by-section specification this module
implements.

No LLM call, no provider call, no active instruction mutation, and no pilot
execution happens anywhere in this module -- it operates only on already-
collected verdict data (issue #391 semantic findings' verdicts, or raw
verdict lists for synthetic/fixture testing).
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import autoresearch_validator as av  # noqa: E402  (reuse Finding/VERDICT_PRECEDENCE, not reimplemented)

MIN_MATCHED_RERUNS = 3
MAX_MATCHED_RERUNS = 5

OBSERVATION_ROW_SCHEMA_PATH = av.SCHEMAS / "autoresearch_observation_row.schema.json"


class ContractError(av.ContractError):
    """Raised only for malformed inputs to this module (e.g. an unknown
    verdict string) -- never for an ordinary inconclusive/discard result."""


def severity(verdict: Optional[str]) -> Optional[int]:
    """None (missing) maps to None. An unknown non-None verdict is a caller
    bug, not a legitimate case outcome, and raises."""
    if verdict is None:
        return None
    if verdict not in av.VERDICT_PRECEDENCE:
        raise ContractError(f"unknown verdict {verdict!r}; expected one of {sorted(av.VERDICT_PRECEDENCE)}")
    return av.VERDICT_PRECEDENCE[verdict]


def group_has_variance(verdicts: list[Optional[str]]) -> bool:
    """Doc section 5: an exact set-cardinality check across a rerun group,
    not a variance formula -- appropriate to N<=5 discrete ordinal data."""
    observed = {v for v in verdicts if v is not None}
    return len(observed) > 1


def validate_observation_row(doc: dict) -> list[av.Finding]:
    return av._schema_findings(doc, OBSERVATION_ROW_SCHEMA_PATH, "observation_row")


@dataclass(frozen=True)
class CaseObservation:
    """Raw rerun data for one case. baseline_verdicts[i] pairs with
    candidate_verdicts[i] (same rerun index); use None for a missing
    rerun. This is the input a real runner integration (issue #392/#393
    territory, not this issue) would build from collected semantic
    findings; here it is also the direct input synthetic/fixture tests
    construct by hand."""

    case_id: str
    case_family: str
    baseline_verdicts: tuple[Optional[str], ...]
    candidate_verdicts: tuple[Optional[str], ...]
    model_provider_runtime_hash: str
    evaluator_version_hash: str
    hard_gate_status: str = "pass"
    configuration_changed: bool = False


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    case_family: str
    non_inferiority_result: str  # "pass" | "fail" | "inconclusive"
    material_regression_flag: bool
    material_improvement_result: str  # "keep" | "inconclusive" | "not_applicable" (non-target)
    missingness_reason: Optional[str]
    run_variance_baseline: bool
    run_variance_candidate: bool


def _matched_pairs(obs: CaseObservation, limit: int) -> list[tuple[str, str]]:
    pairs = list(zip(obs.baseline_verdicts[:limit], obs.candidate_verdicts[:limit]))
    return [(b, c) for b, c in pairs if b is not None and c is not None]


def evaluate_case_non_inferiority(obs: CaseObservation) -> tuple[str, bool, Optional[str]]:
    """Doc section 6, applied uniformly to every family (not just non-target
    ones): worst-case dominance. Returns (non_inferiority_result,
    material_regression_flag, missingness_reason)."""
    if obs.configuration_changed:
        return "inconclusive", False, "configuration_changed"
    if obs.hard_gate_status == "violated":
        return "inconclusive", True, "hard_gate_violated"

    matched = _matched_pairs(obs, MAX_MATCHED_RERUNS)
    if len(matched) < MIN_MATCHED_RERUNS:
        return "inconclusive", False, "no_observation"

    regressed = any(severity(c) > severity(b) for b, c in matched)
    if regressed:
        return "fail", True, None
    return "pass", False, None


def evaluate_case_material_improvement(obs: CaseObservation) -> tuple[str, Optional[str]]:
    """Doc sections 7-8: reproducible improvement across every matched
    rerun, escalating from 3 to a maximum of 5 reruns when the baseline
    itself is inconsistent. Returns ("keep" | "inconclusive",
    missingness_reason). Never returns a "fail": a target-family
    confirmed regression is caught separately by
    evaluate_case_non_inferiority (applied to every family uniformly)."""
    if obs.configuration_changed:
        return "inconclusive", "configuration_changed"
    if obs.hard_gate_status == "violated":
        return "inconclusive", "hard_gate_violated"

    matched = _matched_pairs(obs, MAX_MATCHED_RERUNS)
    if len(matched) < MIN_MATCHED_RERUNS:
        return "inconclusive", "no_observation"

    baseline_side = [b for b, _c in matched]
    if group_has_variance(baseline_side):
        # Baseline itself is noisy on this case: an apparent candidate
        # advantage cannot be distinguished from baseline flakiness at
        # this sample size (doc section 7, point 2).
        return "inconclusive", "evaluator_disagreement_unresolved"

    all_improved = all(severity(c) < severity(b) for b, c in matched)
    if all_improved:
        return "keep", None
    return "inconclusive", None


def evaluate_case(obs: CaseObservation, *, target_family_flag: bool) -> CaseResult:
    ni_result, regression_flag, ni_missing = evaluate_case_non_inferiority(obs)
    if target_family_flag:
        mi_result, mi_missing = evaluate_case_material_improvement(obs)
    else:
        mi_result, mi_missing = "not_applicable", None
    missingness = ni_missing or mi_missing
    return CaseResult(
        case_id=obs.case_id,
        case_family=obs.case_family,
        non_inferiority_result=ni_result,
        material_regression_flag=regression_flag,
        material_improvement_result=mi_result,
        missingness_reason=missingness,
        run_variance_baseline=group_has_variance(list(obs.baseline_verdicts)),
        run_variance_candidate=group_has_variance(list(obs.candidate_verdicts)),
    )


def pareto_efficiency_result(cost_delta: Optional[float], latency_delta: Optional[float]) -> str:
    """Doc section 12: non-domination, never a single weighted score.
    A negative delta means the candidate is cheaper/faster (improvement)."""
    if cost_delta is None or latency_delta is None:
        return "not_evaluated"
    worse_on_both = cost_delta > 0 and latency_delta > 0
    return "dominated" if worse_on_both else "non_dominated"


def aggregate_decision(case_results: list[CaseResult]) -> dict:
    """Doc section 14. Hard-veto-first, order-invariant (every step is
    any()/all() over the set of case_results, never a fold sensitive to
    input order -- permuting `case_results` before calling this function
    must never change the result)."""
    if not case_results:
        raise ContractError("aggregate_decision() called with no case results")

    any_hard_violation = any(r.missingness_reason == "hard_gate_violated" for r in case_results)
    if any_hard_violation:
        return {"decision": "discard", "reason": "hard_gate_violation_dominates"}

    any_regression = any(r.non_inferiority_result == "fail" for r in case_results)
    if any_regression:
        regressed_families = sorted({r.case_family for r in case_results if r.non_inferiority_result == "fail"})
        return {"decision": "discard", "reason": f"material regression in family/families: {regressed_families}"}

    target_results = [r for r in case_results if r.material_improvement_result != "not_applicable"]
    any_ni_inconclusive = any(r.non_inferiority_result == "inconclusive" for r in case_results)
    any_target_not_kept = any(r.material_improvement_result != "keep" for r in target_results)

    if not target_results:
        return {"decision": "inconclusive", "reason": "no target-family case observed"}

    if any_ni_inconclusive or any_target_not_kept:
        return {"decision": "inconclusive", "reason": "unresolved non-inferiority or unproven target-family improvement"}

    return {"decision": "keep_candidate", "reason": "all families non-inferior; target family shows reproducible material improvement"}
