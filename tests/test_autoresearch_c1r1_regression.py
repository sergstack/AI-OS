"""Regression tests surfaced by the C1-R1 live run (2026-09-04) and the
subsequent MD-2 / subject-content decision-package preflight (2026-09-05,
issue #409 parent, PR #434 runtime). These document CURRENT behavior only:

- Judge malformed-output fixtures reproduce the exact shapes the live Judge
  actually returned in C1-R1 (unescaped quotes inside a JSON string value;
  `evidence` supplied as an object instead of the required string) and
  assert the existing fail-closed parsing/validation correctly rejects
  them -- never a crash, never a fabricated pass.
- The MD-2 `_contributes_to_pair` -> `evaluate_case_material_improvement`
  composition is asserted to be structurally incapable of returning "keep"
  under the current wiring. This test is EXPECTED to start failing the
  moment a directional-mapping decision (see
  docs/evidence/AUTORESEARCH_MD2_DECISION_PACKAGE_2026-09-05.md) is
  implemented -- that is the intended trigger to update or remove it, not
  a bug in the test.
- The subject-content-propagation gap (`_case_payload` never includes the
  literal mutated text) is asserted as current behavior for the same
  reason -- see
  docs/evidence/AUTORESEARCH_SUBJECT_CONTENT_PROPAGATION_MEMO_2026-09-05.md.

No live/network/model call anywhere in this file.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def _load(name: str, relpath: str):
    path = REPO_ROOT / relpath
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


lba = _load("autoresearch_live_browser_adapter", "scripts/autoresearch_live_browser_adapter.py")
lj = _load("autoresearch_live_judge", "scripts/autoresearch_live_judge.py")
adc = _load("autoresearch_decision_comparator", "scripts/autoresearch_decision_comparator.py")
cli = _load("autoresearch_cli", "scripts/autoresearch_cli.py")
cpc = _load("autoresearch_context_pack_compiler", "scripts/autoresearch_context_pack_compiler.py")

jsonschema = pytest.importorskip("jsonschema")

FINDING_SCHEMA_PATH = REPO_ROOT / "schemas" / "autoresearch_live_semantic_finding.schema.json"


def _schema() -> dict:
    return json.loads(FINDING_SCHEMA_PATH.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Judge malformed-output regression fixtures (exact shapes from C1-R1)
# ---------------------------------------------------------------------------


def test_c1r1_unescaped_quote_json_is_rejected_not_crashed():
    """C1-R1 rerun 0, order 0: the live Judge emitted a JSON array whose
    "evidence" string contained literal, unescaped double quotes. This must
    parse-fail cleanly (None), never raise, never be treated as valid."""
    raw = (
        '[\n{\n"schema_version": "0.2.0", "case_id": "x", "case_family": "routing",\n'
        '"finding": "f", "evidence": "A states "Destination: [Codex]" and more",\n'
        '"severity": "low", "affected_invariant_or_metric": "routing_correctness",\n'
        '"verdict": "pass", "confidence": "high", "limitations": "none"\n}\n]'
    )
    assert lj.parse_judge_findings(raw) is None


def test_c1r1_evidence_as_object_fails_schema_not_silently_coerced():
    """C1-R1 rerun 2, order 0: the live Judge emitted schema-VALID JSON (it
    parses) but with "evidence" as an object instead of the required
    string. validate_live_finding must reject it, not silently str()-coerce
    the object into an accepted record."""
    finding = {
        "finding": "A and B are materially equivalent.",
        "evidence": {"A": "some text", "B": "some other text"},
        "severity": "none",
        "affected_invariant_or_metric": "routing_correctness",
        "verdict": "pass",
        "confidence": "strong",
        "limitations": "none",
    }
    rec, errs = lj.validate_live_finding(
        finding, schema=_schema(), case_id="c1r1-case", invocation_id="exp:c1r1-case:0",
        evaluator_version_hash="a" * 64, presentation_order_hash="b" * 64,
        response_hash="c" * 64,
    )
    assert rec is None
    assert errs


def test_c1r1_wrong_shape_verdict_tie_fails_schema():
    """C1-R1 rerun 2, order 1: the live Judge invented a "verdict": "tie"
    outside the frozen {pass, revise, blocked} vocabulary, with a different
    field set entirely (criterion/observation instead of
    finding/evidence/affected_invariant_or_metric). Must fail schema
    validation, not be coerced to a default verdict."""
    finding = {
        "schema_version": "0.2.0",
        "case_id": "c1r1-case",
        "criterion": "routing_correctness",
        "verdict": "tie",
        "severity": "none",
        "observation": "A and B are equivalent.",
    }
    rec, errs = lj.validate_live_finding(
        finding, schema=_schema(), case_id="c1r1-case", invocation_id="exp:c1r1-case:0",
        evaluator_version_hash="a" * 64, presentation_order_hash="b" * 64,
        response_hash="c" * 64,
    )
    assert rec is None
    assert errs


# ---------------------------------------------------------------------------
# Retry-exhaustion / accounting regression (the graceful-degradation path
# the C1-R1 manual bridge relied on)
# ---------------------------------------------------------------------------


class _OneShotThenExhaustedJudge:
    """Reproduces the exact C1-R1 bridge situation: exactly one real
    (malformed) capture is available per order; a bounded retry finds
    nothing and must degrade to a Judge-failure result, never crash, never
    consume an undeclared extra call by fabricating a second capture.

    Contract note (found while writing this test): `run_blind_ab` calls
    `judge.evaluate(...)` directly and does NOT catch an exception from
    it -- only the real `BrowserJudgeModel.evaluate()` is safe to let a
    transport-level failure propagate through, because it routes via
    `lba.invoke()`, which internally catches `LiveTransportError` and
    converts it to a `termination_status` result. Any other `JudgeModel`
    implementation (this fixture included, and `FakeJudgeModel`) MUST
    return a non-"completed" `RawJudgeCapture` on failure, never raise --
    confirmed empirically below: raising here crashes `run_blind_ab`
    instead of degrading gracefully."""

    independence_level = "limited_same_model_class"

    def __init__(self, malformed_text: str):
        self._malformed = malformed_text
        self.calls = 0

    def evaluate(self, prompt_text, *, invocation_id: str) -> "lj.RawJudgeCapture":
        self.calls += 1
        if self.calls == 1:
            return lj.RawJudgeCapture(
                response_text=self._malformed, invocation_id=invocation_id,
                response_hash=lba.sha256_hex(self._malformed.encode()),
                termination_status="completed", model_identity_status="ui_observed",
                model="gpt-5-6-thinking",
            )
        return lj.RawJudgeCapture(
            response_text="", invocation_id=invocation_id, response_hash=None,
            termination_status="validation_error", model_identity_status="not_observable",
            model="not_observable",
        )


def test_retry_exhaustion_degrades_to_inconclusive_never_pass():
    evaluator_config = lj.EvaluatorConfig.load(
        REPO_ROOT / "docs" / "standards" / "autoresearch_v02_evaluator_config.json"
    )
    judge = _OneShotThenExhaustedJudge('{"not": "a valid array"}')
    result = lj.run_blind_ab(
        case={"case_id": "c1r1-case", "case_family": "routing", "input": "x"},
        baseline_output="baseline says X", candidate_output="candidate says Y",
        evaluator_config=evaluator_config, judge=judge,
        finding_schema=_schema(), experiment_id="exp", seed=0,
        deterministic_precheck="none", retry_limit=1,
    )
    assert result.contributes == "inconclusive"
    assert result.consistency in ("judge_disagreement",)
    # Exactly 2 evaluate() calls: the one real attempt + the one bounded
    # retry -- never a silent third call, never a fabricated pass.
    assert judge.calls == 2


def test_first_order_failure_short_circuits_second_order():
    """Documents the real control-flow fact the C1-R1 bridge run depended
    on: run_blind_ab returns as soon as the FIRST order exhausts its
    retry, without ever invoking the second order. A caller that
    pre-provisions a capture for the second order must not assume it will
    be consumed."""
    evaluator_config = lj.EvaluatorConfig.load(
        REPO_ROOT / "docs" / "standards" / "autoresearch_v02_evaluator_config.json"
    )
    judge = _OneShotThenExhaustedJudge("not json at all")
    lj.run_blind_ab(
        case={"case_id": "c1r1-case", "case_family": "routing", "input": "x"},
        baseline_output="baseline says X", candidate_output="candidate says Y",
        evaluator_config=evaluator_config, judge=judge,
        finding_schema=_schema(), experiment_id="exp", seed=0,
        deterministic_precheck="none", retry_limit=1,
    )
    # Only 2 calls total (both spent on the FIRST order's attempt+retry);
    # the second order was never reached.
    assert judge.calls == 2


# ---------------------------------------------------------------------------
# MD-2 structural regression (see AUTORESEARCH_MD2_DECISION_PACKAGE_2026-09-05.md)
# ---------------------------------------------------------------------------


def test_md2_mapping_can_never_yield_material_improvement():
    """Structural proof, not a probabilistic sample: _contributes_to_pair
    only ever emits (pass, pass) or (None, None), and
    evaluate_case_material_improvement requires severity(candidate) <
    severity(baseline) in every matched pair. Equal severities can never
    satisfy a strict '<'. This test is EXPECTED to fail once a directional
    mapping (MD-2 decision package, Option A/B/C) is implemented -- update
    or remove it then, don't silently skip it."""
    # Every possible contributes value, mapped through the current MD-2 rule.
    pairs = [cli._contributes_to_pair(c) for c in ("pass", "revise", "blocked", "inconclusive")]
    assert pairs == [("pass", "pass"), (None, None), (None, None), (None, None)]

    # Even in the best case (3 matched "pass" reruns, baseline consistent),
    # the comparator cannot return "keep".
    obs = adc.CaseObservation(
        case_id="c1r1-case", case_family="routing",
        baseline_verdicts=("pass", "pass", "pass"),
        candidate_verdicts=("pass", "pass", "pass"),
        model_provider_runtime_hash="a" * 16, evaluator_version_hash="b" * 16,
    )
    result, reason = adc.evaluate_case_material_improvement(obs)
    assert result == "inconclusive"


# ---------------------------------------------------------------------------
# Subject-content-propagation regression (see
# AUTORESEARCH_SUBJECT_CONTENT_PROPAGATION_MEMO_2026-09-05.md)
# ---------------------------------------------------------------------------


def test_case_payload_does_not_currently_include_mutated_row_text():
    """Documents CURRENT (manifest-only) behavior: the literal changed text
    of a mutable surface never reaches _case_payload's output, only the
    containing file's name and byte count. This is expected to change once
    the subject-content memo's Option 2 (or an alternative) is accepted --
    update this test then, don't treat its current pass as evidence the gap
    is fine to leave forever."""
    spec = cli.ManualCandidateSpec(
        experiment_id="regression-test", baseline_revision="HEAD",
        project="ai_os", research_surface="MUT-ROUTING-TIEBREAK",
        target_file="ROUTING_RULES.md", patch_text="", candidate_patch_hash="a" * 64,
        cases=[{"case_id": "c", "case_family": "routing", "target_family_flag": True,
                "input": "irrelevant for this test"}],
    )
    fake_ctx = {
        "role": "subject_baseline", "project": "ai_os", "source_revision": "HEAD",
        "candidate_patch_hash": None, "context_id": "x", "context_hash": "y",
        "fidelity_mode": "repo_replay",
        "ordered_sources": [
            {"path": "ROUTING_RULES.md", "source_class": "canonical_routing", "bytes": 2596,
             "purpose": "canonical routing/tie-break rules"},
        ],
        "excluded_sources": [], "limitations": "test fixture",
    }
    payload = cli._case_payload(spec, "c", fake_ctx)
    assert "2596 bytes" in payload
    assert "a prompt or workflow deliverable" not in payload
    assert "a prompt/workflow deliverable" not in payload
