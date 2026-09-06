# Model Routing

## Routing criteria

| Need | Model style |
|---|---|
| Fast draft | fast model |
| Hard reasoning | reasoning model |
| Long context synthesis | long-context model |
| Local/private draft | local/Ollama |
| Critique | judge model |
| Rewrite | balanced model |
| Code implementation | route to Codex |

## Rule

Model routing is guidance, not a factual claim about current model capabilities. For current prices, limits, API details or release status, verify with fresh sources.

## Selection checklist

- latency;
- cost;
- context length;
- reasoning need;
- privacy;
- tool access;
- quality gate.

## Adaptive escalation

Do not default to the highest reasoning tier for every task. Start at the
model style the routing criteria above indicate for the task's declared need,
then escalate one step at a time only on an explicit trigger. This does not
replace the routing criteria table; it governs movement between rows when the
first choice proves insufficient.

Escalation ladder: `fast` → `reasoning` → `high-reasoning` → `human/owner
review or abstain`. Never skip a step and never escalate past `abstain` on
the executor's own authority.

Escalate one step when any of the following holds:

- the current model's output fails a quality-gate check (schema, evidence
  presence, internal consistency) and a minimal retry at the same tier does
  not resolve it;
- the task is flagged `material`, `complex`, or high-risk in the applicable
  execution/risk mode;
- confidence signals are low or contradictory (e.g. the model states
  uncertainty, gives materially different answers on rerun, or the Judge
  returns `revise`/`blocked` citing insufficient reasoning depth rather than
  a factual gap);
- the task requires long-context synthesis or multi-step planning beyond what
  the current tier's selection checklist supports.

Abstain (stop and hand to the owner or a human reviewer) instead of escalating
further when:

- `high-reasoning` has already been tried and the quality gate still fails;
- the remaining gap is a missing fact, a business-rule ambiguity, or an
  authority question — no model tier resolves this;
- escalating would require a schema, formula, metric, output-contract,
  business-logic, or provider/API change outside current approval.

Escalation and abstention never widen authority: a higher model tier still
cannot self-accept `accepted_risk`, override deterministic checks (see
`JUDGE_CALIBRATION.md`), or bypass the Judge/owner acceptance gate. Record
which tier produced the accepted output and why escalation stopped where it
did; this is evidence for the eval gate, not a new approval mechanism.
