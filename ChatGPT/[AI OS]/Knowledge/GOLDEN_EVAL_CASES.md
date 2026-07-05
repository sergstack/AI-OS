# Golden Eval Cases

## Purpose

Define compact golden cases for cross-project evals.

These cases are examples for manual or lightweight checklist evaluation, not a benchmark harness.

## Case 1: AI OS Evidence

Input:

- AI trend, pattern, or governance claim.

Expected checks:

- source files or fresh sources named;
- supported / weak / unsupported separated;
- promotion gates respected;
- blocked items not recommended as current implementation.

Pass when:

- evidence status is visible;
- risks and next step are concrete;
- no production readiness is claimed without acceptance.

## Case 2: LLM Output

Input:

- prompt, context package, and draft output.

Expected checks:

- facts separated from interpretation;
- unsupported claims listed;
- limitations visible;
- judge result and revision status present.

Pass when:

- final output follows requested schema;
- revision removes or marks unsupported claims;
- judge result is reviewer evidence, not truth.

## Case 3: Analytics Memo

Input:

- question, data contract, stage/mart evidence, formulas, memo draft.

Expected checks:

- calculations are deterministic;
- grain, period, filters, and method are explicit;
- claims trace to mart/evidence;
- memo recommendations do not exceed data.

Pass when:

- Analytics QA passes;
- LLM judge does not override failed calculation, schema, or contract checks.

## Case 4: Codex PR

Input:

- PR link, goal, changed files, checks, risks, rollback.

Expected checks:

- scope matches requested change;
- checks are actually run or blockers stated;
- no unrelated refactor;
- no forbidden files, secrets, runtime artifacts, or production risk.

Pass when:

- PR Judge returns `pass` or clear `revise`;
- merge readiness is a human decision.

## Case 5: Agent Loop

Input:

- loop goal, owner, allowed actions, checks, stop conditions, acceptance gate.

Expected checks:

- loop follows `goal -> action -> check -> revise/rerun -> acceptance -> next trigger`;
- retry/rerun is bounded;
- stop conditions include no validation, secrets, production/runtime/deploy risk, autonomous retrieval, and uncontrolled multi-agent work.

Pass when:

- loop is supervised;
- human acceptance is required before merge, deploy, adoption, or promotion;
- no autonomous agentic workflow is created.
