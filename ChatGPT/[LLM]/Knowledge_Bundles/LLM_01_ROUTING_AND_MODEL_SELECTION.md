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

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:062e3e26fce6c17cab1ba3647d812baf6d3fb22a73862f3d2229d767545bae85

---

# Content

## From: `ChatGPT/[LLM]/Knowledge/LLM_ROUTING.md`

# LLM Routing
## Task types
| Choose model | model routing |
## Routing rule
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
## Rule
Model routing is guidance, not a factual claim about current model capabilities. For current prices, limits, API details or release status, verify with fresh sources.
Route by model class rather than permanent model name.
## Primary gates
1. task type;
2. risk / error cost;
3. privacy;
4. verification path.
Use reasoning need, context length, latency, cost, and tool access as secondary factors or tie-breakers. Do not require a numerical scoring matrix.
```text
task type
-> can deterministic/tool verification solve or constrain it?
-> risk / error cost
-> privacy constraint
-> required verification path
-> cheapest suitable model class
-> Judge/escalation when required
```
Routing ownership remains:
- deterministic calculation -> `[Analytics]`;
- implementation and tests -> `[Codex]`;
- AI KB evidence and canonical governance -> `[AI OS]`;
- prompt, context, model-routing, and workflow eval -> `[LLM]`.
## Selection checklist
- task type;
- risk / error cost;
- privacy;
- verification path;
- reasoning need;
- context length;
- latency and cost;
- tool access and quality gate.


## From: `ChatGPT/[LLM]/Knowledge/ROUTING_AND_HANDOFF.md`

# Routing and Handoff
## Project routing
```text
AI-концепция / supported KB pattern → [AI OS]
Стратегия / решение / риски → [Thinking]
Расчёты / данные / marts → [Analytics]
Prompts / model routing / LLM quality → [LLM]
Код / implementation / tests / release → [Codex]
```
## Standard handoff format
```text
# Handoff

From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected outputs:
Acceptance criteria:
Risks:
Evidence / confidence:
Open questions:
```
## Thinking → Analytics
- question;
- metrics;
- period;
- assumptions;
- options to test;
- expected analytical output.
## Analytics → LLM
- curated facts;
- tables or marts;
- reconciled metrics;
- limitations;
- tone and output format.
## LLM → Codex
- prompt spec;
- input/output contract;
- files to inspect;
- forbidden actions;
- tests;
- acceptance criteria.
## Codex → QA / Release
- changed files;
- tests run;
- smoke QA;
- acceptance status;
- residual risks;
- rollback notes.
