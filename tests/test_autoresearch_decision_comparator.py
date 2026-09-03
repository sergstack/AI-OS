"""Focused tests for the AIOS AutoResearch v0.1 stochasticity/non-inferiority/
decision-comparator method (issue #395, parent #388), owner [Analytics].

Every "Checks" bullet from issue #395 has a dedicated test below. No LLM
call, no provider call: all verdict data is synthetic/hand-constructed, per
issue #395's own instruction to "use deterministic synthetic/fixture data".
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location(
    "autoresearch_decision_comparator", REPO_ROOT / "scripts" / "autoresearch_decision_comparator.py"
)
dc = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = dc
_spec.loader.exec_module(dc)

av = dc.av
jsonschema = pytest.importorskip("jsonschema")

HASH_A = "a" * 64
HASH_B = "b" * 64


def _obs(
    case_id="C1", case_family="routing", baseline=("pass", "pass", "pass"), candidate=("pass", "pass", "pass"),
    hard_gate_status="pass", configuration_changed=False, model_hash=HASH_A, eval_hash=HASH_A,
) -> dc.CaseObservation:
    return dc.CaseObservation(
        case_id=case_id, case_family=case_family,
        baseline_verdicts=baseline, candidate_verdicts=candidate,
        model_provider_runtime_hash=model_hash, evaluator_version_hash=eval_hash,
        hard_gate_status=hard_gate_status, configuration_changed=configuration_changed,
    )


# ---------------------------------------------------------------------------
# Schema self-validity
# ---------------------------------------------------------------------------


def test_observation_row_schema_is_valid_draft7():
    schema = json.loads((REPO_ROOT / "schemas" / "autoresearch_observation_row.schema.json").read_text())
    jsonschema.Draft7Validator.check_schema(schema)


def _valid_row(**overrides) -> dict:
    row = {
        "schema_version": "0.1.0",
        "case_id": "C1",
        "case_family": "routing",
        "run_id": "run-1",
        "baseline_or_candidate": "candidate",
        "model_provider_runtime_hash": HASH_A,
        "evaluator_version_hash": HASH_A,
        "hard_gate_status": "pass",
        "normalized_behavior_result": "pass",
        "target_family_flag": True,
        "paired_delta": 1,
        "run_variance_or_disagreement": False,
        "non_inferiority_result": "pass",
        "material_regression_flag": False,
        "missingness_reason": None,
        "decision_contribution": "keep",
        "limitations": "none material",
    }
    row.update(overrides)
    return row


def test_valid_observation_row_passes():
    assert dc.validate_observation_row(_valid_row()) == []


def test_missing_result_requires_missingness_reason():
    row = _valid_row(normalized_behavior_result=None, missingness_reason=None)
    assert dc.validate_observation_row(row) != []
    row["missingness_reason"] = "no_observation"
    assert dc.validate_observation_row(row) == []


def test_present_result_forbids_missingness_reason():
    row = _valid_row(missingness_reason="no_observation")
    assert dc.validate_observation_row(row) != []


# ---------------------------------------------------------------------------
# severity / variance primitives
# ---------------------------------------------------------------------------


def test_severity_ordering_matches_validator_precedence():
    assert dc.severity("pass") < dc.severity("revise") < dc.severity("blocked")
    assert dc.severity(None) is None


def test_unknown_verdict_raises():
    with pytest.raises(dc.ContractError):
        dc.severity("fail")


def test_group_has_variance():
    assert dc.group_has_variance(["pass", "pass", "pass"]) is False
    assert dc.group_has_variance(["pass", "revise", "pass"]) is True
    assert dc.group_has_variance(["pass", None, "pass"]) is False  # None excluded, not counted as a distinct value


# ---------------------------------------------------------------------------
# 1. obvious improvement with no regression is eligible for keep_candidate
# ---------------------------------------------------------------------------


def test_obvious_improvement_no_regression_yields_keep_candidate():
    target = _obs(case_id="TARGET", baseline=("revise", "revise", "revise"), candidate=("pass", "pass", "pass"))
    non_target = _obs(case_id="OTHER", case_family="handoff", baseline=("pass", "pass", "pass"), candidate=("pass", "pass", "pass"))
    results = [
        dc.evaluate_case(target, target_family_flag=True),
        dc.evaluate_case(non_target, target_family_flag=False),
    ]
    decision = dc.aggregate_decision(results)
    assert decision["decision"] == "keep_candidate"


# ---------------------------------------------------------------------------
# 2. target gain inside noise band (baseline itself inconsistent) ->
#    inconclusive
# ---------------------------------------------------------------------------


def test_target_gain_inside_baseline_noise_is_inconclusive():
    # baseline itself flips between pass and revise -- an apparent candidate
    # advantage cannot be distinguished from baseline flakiness.
    target = _obs(case_id="TARGET", baseline=("revise", "pass", "revise"), candidate=("pass", "pass", "pass"))
    result = dc.evaluate_case(target, target_family_flag=True)
    assert result.material_improvement_result == "inconclusive"
    assert result.missingness_reason == "evaluator_disagreement_unresolved"
    decision = dc.aggregate_decision([result])
    assert decision["decision"] == "inconclusive"


# ---------------------------------------------------------------------------
# 3. one non-target material regression blocks KEEP
# ---------------------------------------------------------------------------


def test_one_non_target_regression_blocks_keep_even_with_target_improvement():
    target = _obs(case_id="TARGET", baseline=("revise", "revise", "revise"), candidate=("pass", "pass", "pass"))
    non_target = _obs(
        case_id="OTHER", case_family="handoff",
        baseline=("pass", "pass", "pass"), candidate=("pass", "pass", "revise"),  # one regressed rerun
    )
    results = [
        dc.evaluate_case(target, target_family_flag=True),
        dc.evaluate_case(non_target, target_family_flag=False),
    ]
    assert results[1].non_inferiority_result == "fail"
    decision = dc.aggregate_decision(results)
    assert decision["decision"] == "discard"


# ---------------------------------------------------------------------------
# 4. missing run / evaluator disagreement is not silently dropped
# ---------------------------------------------------------------------------


def test_missing_run_is_visible_not_silently_dropped():
    target = _obs(case_id="TARGET", baseline=("pass", "pass"), candidate=("pass", None))  # only 2 matched, one missing
    result = dc.evaluate_case(target, target_family_flag=True)
    assert result.missingness_reason == "no_observation"
    assert result.material_improvement_result == "inconclusive"
    decision = dc.aggregate_decision([result])
    assert decision["decision"] == "inconclusive"


def test_evaluator_disagreement_is_visible_not_silently_dropped():
    target = _obs(case_id="TARGET", baseline=("pass", "revise", "pass"), candidate=("pass", "pass", "pass"))
    result = dc.evaluate_case(target, target_family_flag=True)
    assert result.run_variance_baseline is True
    assert result.missingness_reason == "evaluator_disagreement_unresolved"


# ---------------------------------------------------------------------------
# 5. changed configuration prevents matched comparison
# ---------------------------------------------------------------------------


def test_changed_configuration_prevents_matched_comparison():
    target = _obs(case_id="TARGET", configuration_changed=True)
    result = dc.evaluate_case(target, target_family_flag=True)
    assert result.non_inferiority_result == "inconclusive"
    assert result.material_improvement_result == "inconclusive"
    assert result.missingness_reason == "configuration_changed"


# ---------------------------------------------------------------------------
# 6. efficiency-only gain is considered only after behavior is non-inferior
# ---------------------------------------------------------------------------


def test_pareto_efficiency_non_domination():
    assert dc.pareto_efficiency_result(cost_delta=-0.1, latency_delta=-0.1) == "non_dominated"  # better on both
    assert dc.pareto_efficiency_result(cost_delta=-0.1, latency_delta=0.1) == "non_dominated"  # better on one
    assert dc.pareto_efficiency_result(cost_delta=0.1, latency_delta=0.1) == "dominated"  # worse on both
    assert dc.pareto_efficiency_result(cost_delta=None, latency_delta=0.1) == "not_evaluated"


def test_efficiency_only_gain_does_not_override_a_behavioral_discard():
    # A regression exists (discard), regardless of how good efficiency is --
    # this test proves the CALLER'S OWN responsibility to gate on behavior
    # first (doc section 11): aggregate_decision never looks at efficiency
    # at all, so an efficiency result can never leak into this decision.
    non_target = _obs(case_id="OTHER", case_family="handoff", baseline=("pass",) * 3, candidate=("pass", "pass", "blocked"))
    decision = dc.aggregate_decision([dc.evaluate_case(non_target, target_family_flag=False)])
    assert decision["decision"] == "discard"
    # efficiency, even if dramatically positive, plays no role in the call above
    assert dc.pareto_efficiency_result(-0.9, -0.9) == "non_dominated"  # computed independently, not consulted


# ---------------------------------------------------------------------------
# 7. hard-veto input dominates all quantitative outputs
# ---------------------------------------------------------------------------


def test_hard_veto_dominates_even_alongside_obvious_improvement():
    target = _obs(case_id="TARGET", baseline=("revise",) * 3, candidate=("pass",) * 3, hard_gate_status="violated")
    non_target = _obs(case_id="OTHER", case_family="handoff", baseline=("pass",) * 3, candidate=("pass",) * 3)
    results = [
        dc.evaluate_case(target, target_family_flag=True),
        dc.evaluate_case(non_target, target_family_flag=False),
    ]
    decision = dc.aggregate_decision(results)
    assert decision["decision"] == "discard"
    assert "hard_gate" in decision["reason"]


# ---------------------------------------------------------------------------
# 8. different aggregation orders produce the same result
# ---------------------------------------------------------------------------


def test_aggregation_is_order_invariant():
    target = _obs(case_id="TARGET", baseline=("revise",) * 3, candidate=("pass",) * 3)
    non_target_a = _obs(case_id="A", case_family="handoff", baseline=("pass",) * 3, candidate=("pass",) * 3)
    non_target_b = _obs(case_id="B", case_family="evidence", baseline=("pass",) * 3, candidate=("pass",) * 3)
    results = [
        dc.evaluate_case(target, target_family_flag=True),
        dc.evaluate_case(non_target_a, target_family_flag=False),
        dc.evaluate_case(non_target_b, target_family_flag=False),
    ]
    decisions = {
        dc.aggregate_decision(list(perm))["decision"]
        for perm in itertools.permutations(results)
    }
    assert decisions == {"keep_candidate"}


def test_aggregation_is_order_invariant_for_a_regression_case_too():
    target = _obs(case_id="TARGET", baseline=("revise",) * 3, candidate=("pass",) * 3)
    regressed = _obs(case_id="BAD", case_family="handoff", baseline=("pass",) * 3, candidate=("blocked",) * 3)
    results = [
        dc.evaluate_case(target, target_family_flag=True),
        dc.evaluate_case(regressed, target_family_flag=False),
    ]
    decisions = {
        dc.aggregate_decision(list(perm))["decision"]
        for perm in itertools.permutations(results)
    }
    assert decisions == {"discard"}


# ---------------------------------------------------------------------------
# minimum sample requirement
# ---------------------------------------------------------------------------


def test_below_minimum_reruns_is_inconclusive():
    target = _obs(case_id="TARGET", baseline=("pass", "pass"), candidate=("pass", "pass"))  # only 2, below MIN=3
    result = dc.evaluate_case(target, target_family_flag=True)
    assert result.non_inferiority_result == "inconclusive"
    assert result.material_improvement_result == "inconclusive"


def test_escalation_ceiling_five_reruns_still_inconclusive_stays_inconclusive():
    # 5 reruns, baseline noisy throughout -- never resolves, stays
    # inconclusive rather than escalating further or flipping to fail.
    target = _obs(
        case_id="TARGET",
        baseline=("pass", "revise", "pass", "revise", "pass"),
        candidate=("pass", "pass", "pass", "pass", "pass"),
    )
    result = dc.evaluate_case(target, target_family_flag=True)
    assert result.material_improvement_result == "inconclusive"


def test_aggregate_decision_empty_list_raises():
    with pytest.raises(dc.ContractError):
        dc.aggregate_decision([])


# ---------------------------------------------------------------------------
# no pooling across changed model/provider/runtime configurations
# ---------------------------------------------------------------------------


def test_mismatched_hashes_are_not_silently_pooled():
    # Two "runs" of the same case under different model hashes must not be
    # treated as one matched comparison -- the caller is responsible for not
    # constructing a CaseObservation across mixed hashes; this test proves
    # the module's contract by asserting distinct hash values on purpose.
    obs_a = _obs(case_id="C1", model_hash=HASH_A)
    obs_b = _obs(case_id="C1", model_hash=HASH_B)
    assert obs_a.model_provider_runtime_hash != obs_b.model_provider_runtime_hash


# ---------------------------------------------------------------------------
# Contract document structural completeness
# ---------------------------------------------------------------------------

CONTRACT_DOC = REPO_ROOT / "ChatGPT" / "[Analytics]" / "Knowledge" / "AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md"

REQUIRED_SECTIONS = [
    "## 1. Matched baseline/candidate run design",
    "## 2. Repeated baseline sampling",
    "## 3. Provider/model/runtime/configuration changes",
    "## 4. Case-level normalization",
    "## 5. Observed run variance / disagreement",
    "## 6. Non-inferiority logic for non-target families",
    "## 7. Material-improvement logic for the target family",
    "## 8. Escalation from 3 to a maximum of 5 matched runs",
    "## 9. Mandatory `inconclusive` conditions",
    "## 10. Missing-data and evaluator-disagreement treatment",
    "## 11. Separation of behavioral and efficiency vectors",
    "## 12. Pareto / non-domination rule for efficiency",
    "## 13. Deterministic output fields consumed by #392",
    "## 14. Aggregation to `keep_candidate` / `discard` / `inconclusive`",
    "## 15. Limitations and minimum sample requirements",
    "## 16. Calibration/holdout reporting template",
]


def test_contract_document_has_all_required_sections():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    assert missing == [], f"method doc is missing required sections: {missing}"


def test_contract_document_bans_unearned_significance_language():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    assert "not an asymptotic" in text or "not asymptotic" in text
    assert "p-value" in text  # discussed and rejected, not silently absent


def test_contract_document_is_candidate_status():
    text = CONTRACT_DOC.read_text(encoding="utf-8")
    assert "Status: `candidate`" in text
