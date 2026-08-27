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
- source_fingerprint: sha256:d64b02fe74d4ec0f15fb063c5b0c880dd1bce8be874477c2fe00e5af5cf59767
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
