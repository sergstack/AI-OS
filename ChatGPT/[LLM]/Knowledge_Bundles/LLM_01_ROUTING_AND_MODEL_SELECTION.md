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
- source_fingerprint: sha256:cd52ea369a2fefddc0e79389b09ab0068b137e6d85fc88a6a17dca1d464d9690

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
## Selection checklist
- latency;
- cost;
- context length;
- reasoning need;
- privacy;
- tool access;
- quality gate.


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
