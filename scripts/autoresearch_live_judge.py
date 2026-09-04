#!/usr/bin/env python3
"""Live blind A/B semantic Judge integration for AIOS AutoResearch v0.2
(issue #414, parent #409).

Turns the accepted #394 frozen semantic-evaluator contract
(`ChatGPT/[LLM]/Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md`) into a
real, bounded live Judge that:

- runs only AFTER the deterministic precheck (a `discard`-consequence hard
  finding bypasses the Judge entirely and stays controlling -- #394 §3);
- receives two outputs as anonymised `A`/`B` with NO baseline/candidate label,
  NO mutation/patch/target clause, NO Researcher hypothesis/rationale, NO
  expected winner, NO prior decision, NO owner preference, NO authority state
  (#414 "The Judge must never receive");
- executes the reversed A/B presentation order (#394 §4, mandatory for any
  material finding);
- validates every finding against
  `schemas/autoresearch_live_semantic_finding.schema.json` (additive to the
  frozen #394 schema, which is not modified);
- preserves order disagreement as explicit `inconclusive` evidence, never an
  average (#414 "Disagreement policy");
- de-blinds A/B back to baseline/candidate ONLY after both findings validate,
  and only in the privileged evidence layer -- never in the Judge prompt or
  the finding object;
- returns evidence only: it gains no candidate, owner, merge, or production
  authority (the finding schema has no field capable of carrying any).

Each live Judge call is an ordinary live model call routed through the #413
transport (`scripts/autoresearch_live_browser_adapter.invoke`) and consumes
the SAME shared `BudgetState` as subject calls (#411: "Every call, including
retries and Judge calls, consumes budget").

No real browser / network / model call happens in this module's own code
paths; `FakeJudgeModel` is deterministic and does no I/O.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Protocol

import sys

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import autoresearch_live_browser_adapter as lba  # noqa: E402
import autoresearch_shadow_runner as asr  # noqa: E402  (reuse alternation_order, unchanged)


CASE_FAMILIES = frozenset(
    {"routing", "scope_execution", "evidence", "authority", "handoff", "adversarial"}
)

#: Substrings that must never appear in a Judge prompt (candidate identity /
#: Researcher intent / decision leakage). Checked fail-closed before any call.
_LEAKAGE_TOKENS = (
    "baseline",
    "candidate",
    "hypothesis",
    "research_surface",
    "researcher rationale",
    "expected winner",
    "expected outcome",
    "preferred result",
    "prior decision",
    "owner preference",
    "authority_status",
    "merge_status",
    "production_status",
    "keep_candidate",
)

CONSISTENCY_VALUES = frozenset(
    {"order_consistent", "judge_disagreement", "deterministic_bypass"}
)

CONTRIBUTION_VALUES = frozenset({"pass", "revise", "blocked", "inconclusive"})

INDEPENDENCE_VALUES = frozenset(
    {"independent_model", "limited_same_model_class", "unknown"}
)

_VERDICT_PRECEDENCE = {"pass": 0, "revise": 1, "blocked": 2}


class LiveJudgeError(RuntimeError):
    """A Judge-integration invariant break that must not be silently absorbed
    (e.g. de-blinding attempted before both findings validated)."""


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# Frozen evaluator identity (#414 "Frozen evaluator identity" / #394 §10)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class EvaluatorConfig:
    evaluator_contract_version: str
    prompt_family_text: str
    rubric_blocks: dict  # case_family -> rubric block text
    finding_schema_version: str
    model_class_pin: str  # e.g. "judge"
    sampling_configuration: dict
    blinding_impl_version: str
    order_schedule_rule: str  # e.g. "alternation_order(experiment_id, seed); reversed second pass"
    context_construction_version: str
    evaluator_model_identity: str = "not_observable"

    def frozen_hash(self) -> str:
        """sha256 over {prompt_family_text, rubric_blocks_by_case_family,
        model_class_pin, finding_schema_version} -- exactly #394 §10's
        content-hash contract, not a second mechanism."""
        payload = json.dumps(
            {
                "prompt_family_text": self.prompt_family_text,
                "rubric_blocks": {k: self.rubric_blocks[k] for k in sorted(self.rubric_blocks)},
                "model_class_pin": self.model_class_pin,
                "finding_schema_version": self.finding_schema_version,
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        return sha256_hex(payload.encode("utf-8"))

    def identity_manifest(self) -> dict:
        """The full frozen-identity record (#414 'Before the first live call,
        freeze and hash')."""
        return {
            "evaluator_contract_version": self.evaluator_contract_version,
            "prompt_family_hash": sha256_hex(self.prompt_family_text.encode("utf-8")),
            "rubric_blocks_hash": sha256_hex(
                json.dumps({k: self.rubric_blocks[k] for k in sorted(self.rubric_blocks)}, sort_keys=True).encode("utf-8")
            ),
            "finding_schema_version": self.finding_schema_version,
            "model_class_pin": self.model_class_pin,
            "evaluator_model_identity": self.evaluator_model_identity,
            "sampling_configuration": self.sampling_configuration,
            "context_construction_version": self.context_construction_version,
            "blinding_impl_version": self.blinding_impl_version,
            "order_schedule_rule": self.order_schedule_rule,
            "evaluator_version_hash": self.frozen_hash(),
        }

    @classmethod
    def load(cls, path: Path) -> "EvaluatorConfig":
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        cfg = cls(
            evaluator_contract_version=raw["evaluator_contract_version"],
            prompt_family_text=raw["prompt_family_text"],
            rubric_blocks=raw["rubric_blocks"],
            finding_schema_version=raw["finding_schema_version"],
            model_class_pin=raw["model_class_pin"],
            sampling_configuration=raw.get("sampling_configuration", {}),
            blinding_impl_version=raw["blinding_impl_version"],
            order_schedule_rule=raw["order_schedule_rule"],
            context_construction_version=raw["context_construction_version"],
            evaluator_model_identity=raw.get("evaluator_model_identity", "not_observable"),
        )
        declared = raw.get("evaluator_version_hash")
        if declared and declared != cfg.frozen_hash():
            raise LiveJudgeError(
                f"evaluator config drift: declared evaluator_version_hash {declared} "
                f"!= computed {cfg.frozen_hash()}"
            )
        return cfg


# ---------------------------------------------------------------------------
# Blinding / order schedule
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AbAssignment:
    """Which side of the A/B pair each condition occupies, for one order pass.
    `a_is` / `b_is` are 'baseline'|'candidate' -- used ONLY by the privileged
    de-blinding step after evaluation, never in the prompt."""

    a_is: str
    b_is: str
    order_index: int  # 0 = primary, 1 = reversed

    def presentation_order_hash(self, experiment_id: str, case_id: str) -> str:
        return sha256_hex(f"{experiment_id}:{case_id}:{self.order_index}:{self.a_is}:{self.b_is}".encode("utf-8"))


def primary_assignment(experiment_id: str, seed: int = 0) -> AbAssignment:
    """Reuses `autoresearch_shadow_runner.alternation_order` (issue #393) --
    the same deterministic seeded schedule the shadow runner already computes,
    not a second randomisation mechanism."""
    order = asr.alternation_order(experiment_id, seed)  # shuffled ["baseline","candidate"]
    return AbAssignment(a_is=order[0], b_is=order[1], order_index=0)


def reversed_assignment(primary: AbAssignment) -> AbAssignment:
    return AbAssignment(a_is=primary.b_is, b_is=primary.a_is, order_index=1)


# ---------------------------------------------------------------------------
# Prompt construction + leakage guard
# ---------------------------------------------------------------------------


def assert_no_leakage(injected_text: str) -> list[str]:
    """Names of every forbidden token found in the *pipeline/case-injected*
    portion of a Judge prompt (frozen_input + applicable_deterministic_findings).

    Deliberately NOT run over the frozen prompt-family boilerplate or the
    rubric: those legitimately *name* the forbidden concepts ("you receive no
    ... hypothesis ... expected outcome") in order to instruct the Judge to
    ignore them. It is also not run over the two subject outputs, which are
    anonymised positionally (`A:`/`B:`) with no identity wrapper and may
    themselves discuss any topic. A non-empty list means the prompt must NOT
    be sent."""
    low = injected_text.lower()
    return [tok for tok in _LEAKAGE_TOKENS if tok in low]


def build_judge_prompt(
    *,
    evaluator_config: EvaluatorConfig,
    case: dict,
    output_a: str,
    output_b: str,
    applicable_deterministic_findings: str = "none",
) -> str:
    case_family = case["case_family"]
    if case_family not in CASE_FAMILIES:
        raise LiveJudgeError(f"unknown case_family {case_family!r}")
    rubric = evaluator_config.rubric_blocks.get(case_family)
    if not rubric:
        raise LiveJudgeError(f"no frozen rubric block for case_family {case_family!r}")
    frozen_input = case.get("input")
    if frozen_input is None:
        frozen_input = "[holdout — not disclosed]"

    # Fail-closed: the case/pipeline-injected text must not smuggle in
    # candidate identity, Researcher intent, or a decision (#414 "The Judge
    # must never receive"). The frozen boilerplate/rubric are exempt (§ docstring).
    leaks = assert_no_leakage(f"{frozen_input}\n{applicable_deterministic_findings}")
    if leaks:
        raise LiveJudgeError(
            f"refusing to build a Judge prompt: case-injected text contains forbidden token(s): {leaks}"
        )

    prompt = (
        f"{evaluator_config.prompt_family_text}\n\n"
        f"CASE CONTEXT:\n"
        f"case_id: {case['case_id']}\n"
        f"case_family: {case_family}\n"
        f"frozen_input: {frozen_input}\n"
        f"rubric: {rubric}\n"
        f"applicable_deterministic_findings: {applicable_deterministic_findings}\n\n"
        f"OUTPUTS:\nA: {output_a}\nB: {output_b}\n\n"
        f"TASK:\nCompare A and B strictly against the rubric. Emit one finding "
        f"object per material observation, matching finding schema "
        f"{evaluator_config.finding_schema_version}. Return ONLY a JSON array "
        f"of finding objects, no prose outside it."
    )
    return prompt


# ---------------------------------------------------------------------------
# Judge model: protocol + fake + browser-backed
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RawJudgeCapture:
    response_text: str
    invocation_id: str
    response_hash: Optional[str]
    termination_status: str
    model_identity_status: str
    model: str


class JudgeModel(Protocol):
    independence_level: str

    def evaluate(self, prompt_text: str, *, invocation_id: str) -> RawJudgeCapture: ...


class FakeJudgeModel:
    """Deterministic, no I/O. `scripted` maps an order_index (0/1) -> a JSON
    array string of finding objects. Used only by automated tests; its output
    is never labelled `live`."""

    independence_level = "limited_same_model_class"

    def __init__(self, scripted: dict[int, str], *, model: str = "fake-judge") -> None:
        self._scripted = scripted
        self._model = model
        self.calls = 0

    def evaluate(self, prompt_text: str, *, invocation_id: str) -> RawJudgeCapture:
        self.calls += 1
        order_index = 1 if invocation_id.endswith(":rev") else 0
        text = self._scripted.get(order_index, "[]")
        return RawJudgeCapture(
            response_text=text,
            invocation_id=invocation_id,
            response_hash=sha256_hex(lba.normalize_response(text).encode("utf-8")) if text.strip() else None,
            termination_status="completed" if text.strip() else "empty_response",
            model_identity_status="not_observable",
            model=self._model,
        )


class BrowserJudgeModel:
    """Routes each Judge call through the #413 live transport
    (`lba.invoke`) as an ordinary live model call, sharing the batch
    `BudgetState`. The Judge prompt is the payload; the captured answer text
    is parsed downstream into findings."""

    def __init__(
        self,
        *,
        policy: "lba.TransportPolicy",
        budget: "lba.BudgetState",
        transport: "lba.BrowserSessionTransport",
        judge_context_id: str,
        judge_context_hash: str,
        authority_evidence_ref: str,
        independence_level: str = "limited_same_model_class",
    ) -> None:
        self._policy = policy
        self._budget = budget
        self._transport = transport
        self._ctx_id = judge_context_id
        self._ctx_hash = judge_context_hash
        self._auth_ref = authority_evidence_ref
        self.independence_level = independence_level

    def evaluate(self, prompt_text: str, *, invocation_id: str) -> RawJudgeCapture:
        request = lba.LiveInvocationRequest(
            invocation_id=invocation_id,
            experiment_id=invocation_id.split(":")[0],
            condition="baseline",  # structural only; the Judge is not a subject condition
            case_id=invocation_id.split(":")[1] if ":" in invocation_id else "judge",
            context_id=self._ctx_id,
            context_hash=self._ctx_hash,
            payload_text=prompt_text,
            authority_evidence_ref=self._auth_ref,
            external_action_preview_ref=f"judge-preview:{invocation_id}",
        )
        result = lba.invoke(request, self._policy, self._budget, self._transport)
        return RawJudgeCapture(
            response_text=result.response_text_or_ref or "",
            invocation_id=invocation_id,
            response_hash=result.response_hash,
            termination_status=result.termination_status,
            model_identity_status=result.model_identity_status,
            model=result.model,
        )


# ---------------------------------------------------------------------------
# Finding parsing + validation
# ---------------------------------------------------------------------------

_JSON_ARRAY_RE = re.compile(r"\[.*\]", re.DOTALL)


def parse_judge_findings(response_text: str) -> Optional[list[dict]]:
    """Extract the JSON array of finding objects from a Judge response.
    Returns None on anything not parseable as a non-empty list of objects --
    the caller maps that to a bounded retry / Judge failure, never a PASS."""
    if not response_text or not response_text.strip():
        return None
    candidate = response_text.strip()
    if not candidate.startswith("["):
        m = _JSON_ARRAY_RE.search(candidate)
        if not m:
            return None
        candidate = m.group(0)
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        return None
    if not isinstance(parsed, list) or not parsed or not all(isinstance(x, dict) for x in parsed):
        return None
    return parsed


def _forbidden_fields(finding: dict) -> list[str]:
    forbidden = {
        "authority_status",
        "merge_status",
        "production_status",
        "candidate_identity",
        "which_is_candidate",
        "expected_winner",
        "researcher_rationale",
        "aggregate_score",
        "numeric_score",
    }
    return sorted(forbidden.intersection(finding.keys()))


def validate_live_finding(
    finding: dict,
    *,
    schema: dict,
    case_id: str,
    invocation_id: str,
    evaluator_version_hash: str,
    presentation_order_hash: str,
    response_hash: Optional[str],
) -> tuple[Optional[dict], list[str]]:
    """Returns (normalised_record | None, errors). A record is produced only
    when it is schema-valid AND carries no forbidden authority/identity/score
    field."""
    import jsonschema  # local import: optional dep, mirrors repo test style

    errors: list[str] = []
    bad = _forbidden_fields(finding)
    if bad:
        errors.append(f"forbidden field(s) in Judge finding: {bad}")

    record = {
        "schema_version": "0.2.0",
        "finding_id": finding.get("finding_id") or f"{invocation_id}:{sha256_hex(json.dumps(finding, sort_keys=True).encode()) [:12]}",
        "case_id": case_id,
        "case_family": finding.get("case_family", ""),
        "invocation_id": invocation_id,
        "evaluator_version_hash": evaluator_version_hash,
        "presentation_order_hash": presentation_order_hash,
        "finding": finding.get("finding", ""),
        "evidence": finding.get("evidence", ""),
        "severity": finding.get("severity", ""),
        "affected_invariant_or_metric": finding.get("affected_invariant_or_metric", ""),
        "verdict": finding.get("verdict", ""),
        "confidence": finding.get("confidence", ""),
        "limitations": finding.get("limitations") or "none material",
        "response_hash": response_hash,
        "validation_status": "pending",
    }
    validator = jsonschema.Draft7Validator(schema)
    schema_errors = sorted(validator.iter_errors(record), key=lambda e: e.path)
    for err in schema_errors:
        errors.append(f"schema: {err.message}")

    record["validation_status"] = "valid" if not errors else "invalid"
    return (record if not errors else None), errors


# ---------------------------------------------------------------------------
# Case-level blind A/B evaluation
# ---------------------------------------------------------------------------


@dataclass
class CaseSemanticEvidence:
    case_id: str
    evaluator_version_hash: str
    consistency: str
    aggregate_verdict: Optional[str]
    contributes: str
    order_findings: list = field(default_factory=list)  # [order0_records, order1_records]
    judge_invocation_ids: list = field(default_factory=list)
    independence_level: str = "unknown"
    deblinding: dict = field(default_factory=dict)
    limitations: str = "none material"
    retries_used: int = 0


def _worst_verdict(records: list[dict]) -> Optional[str]:
    verdicts = [r["verdict"] for r in records if r.get("verdict") in _VERDICT_PRECEDENCE]
    if not verdicts:
        return None
    return max(verdicts, key=lambda v: _VERDICT_PRECEDENCE[v])


def _material(records: list[dict]) -> tuple[Optional[str], Optional[str]]:
    """(worst_verdict, worst_severity) across a pass's records."""
    sev_rank = {"low": 0, "medium": 1, "high": 2, "critical": 3}
    wv = _worst_verdict(records)
    sevs = [r["severity"] for r in records if r.get("severity") in sev_rank]
    ws = max(sevs, key=lambda s: sev_rank[s]) if sevs else None
    return wv, ws


def run_blind_ab(
    *,
    case: dict,
    baseline_output: str,
    candidate_output: str,
    evaluator_config: EvaluatorConfig,
    judge: JudgeModel,
    finding_schema: dict,
    experiment_id: str,
    seed: int = 0,
    deterministic_precheck: str = "none",  # "none" | "discard" | "pass"
    retry_limit: int = 1,
) -> CaseSemanticEvidence:
    """The #414 required evaluation sequence. A `discard`-consequence
    deterministic precheck bypasses the Judge entirely (#394 §3)."""
    evh = evaluator_config.frozen_hash()

    if deterministic_precheck == "discard":
        return CaseSemanticEvidence(
            case_id=case["case_id"],
            evaluator_version_hash=evh,
            consistency="deterministic_bypass",
            aggregate_verdict="blocked",
            contributes="blocked",
            independence_level=getattr(judge, "independence_level", "unknown"),
            limitations="deterministic discard finding is controlling; Judge not invoked (#394 §3).",
        )

    prim = primary_assignment(experiment_id, seed)
    rev = reversed_assignment(prim)
    by_condition = {"baseline": baseline_output, "candidate": candidate_output}

    order_records: list[list[dict]] = []
    invocation_ids: list[str] = []
    retries_used = 0
    limitations: list[str] = []

    for assignment, suffix in ((prim, ""), (rev, ":rev")):
        out_a = by_condition[assignment.a_is]
        out_b = by_condition[assignment.b_is]
        prompt = build_judge_prompt(
            evaluator_config=evaluator_config, case=case, output_a=out_a, output_b=out_b
        )
        poh = assignment.presentation_order_hash(experiment_id, case["case_id"])
        records: Optional[list[dict]] = None
        attempts = 0
        while records is None and attempts <= retry_limit:
            inv_id = f"{experiment_id}:{case['case_id']}:{attempts}{suffix}"
            invocation_ids.append(inv_id)
            capture = judge.evaluate(prompt, invocation_id=inv_id)
            if attempts > 0:
                retries_used += 1
            if capture.termination_status != "completed":
                attempts += 1
                limitations.append(f"order {assignment.order_index}: judge call {capture.termination_status}")
                continue
            parsed = parse_judge_findings(capture.response_text)
            if parsed is None:
                attempts += 1
                limitations.append(f"order {assignment.order_index}: unparseable/empty Judge output")
                continue
            validated: list[dict] = []
            ok = True
            for f in parsed:
                rec, errs = validate_live_finding(
                    f,
                    schema=finding_schema,
                    case_id=case["case_id"],
                    invocation_id=inv_id,
                    evaluator_version_hash=evh,
                    presentation_order_hash=poh,
                    response_hash=capture.response_hash,
                )
                if rec is None:
                    ok = False
                    limitations.append(f"order {assignment.order_index}: invalid finding ({errs[:1]})")
                    break
                validated.append(rec)
            if ok:
                records = validated
            else:
                attempts += 1
        if records is None:
            # repeated invalidity is a Judge failure, not a subject failure
            return CaseSemanticEvidence(
                case_id=case["case_id"],
                evaluator_version_hash=evh,
                consistency="judge_disagreement",
                aggregate_verdict="blocked",
                contributes="inconclusive",
                order_findings=order_records,
                judge_invocation_ids=invocation_ids,
                independence_level=getattr(judge, "independence_level", "unknown"),
                limitations="Judge failure: no valid findings after bounded retry. " + " | ".join(limitations[:4]),
                retries_used=retries_used,
            )
        order_records.append(records)

    # --- both orders produced valid findings: compare, then de-blind ---
    v0, s0 = _material(order_records[0])
    v1, s1 = _material(order_records[1])
    consistent = (v0 == v1) and (s0 == s1)
    consistency = "order_consistent" if consistent else "judge_disagreement"
    aggregate = _worst_verdict(order_records[0] + order_records[1])
    if consistency == "judge_disagreement":
        contributes = "inconclusive"
        limitations.append(
            f"material order disagreement: order0=({v0},{s0}) order1=({v1},{s1}); contributes inconclusive, not averaged."
        )
    else:
        contributes = aggregate if aggregate in CONTRIBUTION_VALUES else "inconclusive"

    deblinding = {
        "order0": {"A_was": prim.a_is, "B_was": prim.b_is},
        "order1": {"A_was": rev.a_is, "B_was": rev.b_is},
        "deblinded_after": "both order findings validated",
    }

    return CaseSemanticEvidence(
        case_id=case["case_id"],
        evaluator_version_hash=evh,
        consistency=consistency,
        aggregate_verdict=aggregate,
        contributes=contributes,
        order_findings=order_records,
        judge_invocation_ids=invocation_ids,
        independence_level=getattr(judge, "independence_level", "unknown"),
        deblinding=deblinding,
        limitations="; ".join(limitations) if limitations else "none material",
        retries_used=retries_used,
    )
