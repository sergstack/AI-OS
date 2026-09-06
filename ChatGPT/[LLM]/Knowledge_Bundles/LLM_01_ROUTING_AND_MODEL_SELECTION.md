# [LLM] — Routing and Model Selection

## Purpose

Compact upload artifact for [LLM] covering routing and model selection.

## Source files

- `ChatGPT/[LLM]/Knowledge/LLM_ROUTING.md`
- `ChatGPT/[LLM]/Knowledge/MODEL_ROUTING.md`
- `ChatGPT/[LLM]/Knowledge/ROUTING_AND_HANDOFF.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:13f527f0e1bb8cee2cfb08b001961abc61ec8a759a035b904d79cf69d8e118a1
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[LLM]/Knowledge/LLM_ROUTING.md`

# LLM Routing
## Task types
| Need | Route |
|---|---|
| Draft text | draft workflow |
| Critique | judge workflow |
| Improve | revise workflow |
| Summarize | summarize workflow |
| Extract structured facts | extraction workflow |
| Build memo | memo generation workflow |
| Choose model | model routing |
| Check output | quality gates |
## Routing rule
Before prompting, decide:
1. task type;
2. input context;
3. output format;
4. quality gate;
5. handoff target.
## Do not use LLM for
- source-of-truth calculations;
- secrets handling;
- unsupported factual claims;
- production implementation without Codex.

## From: `ChatGPT/[LLM]/Knowledge/MODEL_ROUTING.md`

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

## From: `ChatGPT/[LLM]/Knowledge/ROUTING_AND_HANDOFF.md`

# Routing and Handoff
Canonical destination routing is defined in repo-root `ROUTING_RULES.md`.
Use the canonical handoff fields in `HANDOFF_STYLE_STANDARD.md`.
## Thinking → Analytics
Используй, когда decision или scenario требует расчётов.
Передать:
- question;
- metrics;
- period;
- assumptions;
- options to test;
- expected analytical output.
## Analytics → LLM
Используй, когда verified numbers нужно превратить в memo, summary или narrative.
Передать:
- curated facts;
- tables or marts;
- reconciled metrics;
- limitations;
- tone and output format.
## LLM → Codex
Используй, когда нужен код для автоматизации prompt/memo/report workflow.
Передать:
- prompt spec;
- input/output contract;
- files to inspect;
- forbidden actions;
- tests;
- acceptance criteria.
## Codex → QA / Release
Передать:
- changed files;
- tests run;
- smoke QA;
- acceptance status;
- residual risks;
- rollback notes.
