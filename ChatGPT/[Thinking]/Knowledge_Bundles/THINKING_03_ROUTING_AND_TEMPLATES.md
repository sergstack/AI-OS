# [Thinking] — Routing and Templates

## Purpose

Compact upload artifact for [Thinking] covering routing and templates.

## Source files

- `ChatGPT/[Thinking]/Knowledge/ROUTING_AND_HANDOFF.md`
- `ChatGPT/[Thinking]/Knowledge/AI_OS_REFERENCE.md`
- `ChatGPT/[Thinking]/Knowledge/SCENARIO_ANALYSIS_TEMPLATE.md`
- `ChatGPT/[Thinking]/CURRENT_STATUS.md`
- `ChatGPT/[Thinking]/SMOKE_QA_RESULTS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Thinking]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:3420e67bc116807dfae9ad7f129154857a42fc4994e4ac393716a258070805fc

---

# Content

## From: `ChatGPT/[Thinking]/Knowledge/ROUTING_AND_HANDOFF.md`

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


## From: `ChatGPT/[Thinking]/Knowledge/AI_OS_REFERENCE.md`

# AI OS Reference
## Purpose
- понять новую AI-концепцию;
- найти supported pattern;
- проверить confidence / evidence;
- связать AI-тренд с работой Сергея;
- найти governance rule;
- отличить supported / weak / unsupported claim.
## Не копировать
- весь compact KB package;
- raw transcripts;
- source cards;
- chunks;
- temp files;
- logs;
- embeddings;
- vector DB;
- web UI artifacts.
## Как ссылаться
Когда нужен KB-backed вывод, формулируй handoff в `[AI OS]` так:
```text
Используй AI OS KB. Найди supported/weak/unsupported evidence по теме:
<topic>

Верни:
- найдено в KB: да/нет/частично
- sources
- confidence
- supported claims
- weak/unsupported claims
- practical use for Sergey
```
## Rule
AI OS даёт evidence и patterns. Текущий проект применяет их в своей области, не смешивая роли.


## From: `ChatGPT/[Thinking]/Knowledge/SCENARIO_ANALYSIS_TEMPLATE.md`

# Scenario Analysis Template
## Question
## Decision context
## Scenarios
| Scenario | What happens | Key assumptions | Trigger | Leading indicators | Downside | Reversibility | Decision implication |
|---|---|---|---|---|---|---|---|
| Base | | | | | | | |
| Optimistic | | | | | | | |
| Downside | | | | | | | |
## Cross-scenario risks
## What would change the decision
## Handoff required?
- Analytics:
- LLM:
- Codex:
- AI OS:
## Recommendation
## Confidence
## Next step


## From: `ChatGPT/[Thinking]/CURRENT_STATUS.md`

# [Thinking] Current Status
Status: active
Owner: Sergey / Thinking Lead
Last smoke QA: 2026-05-25
## Active canonical files
| File | Status | Purpose |
| `CURRENT_STATUS.md` | active | live status tracking |
| `SMOKE_QA_RESULTS.md` | active | smoke QA record |
| `Knowledge/DECISION_STATUS_AND_REVISIT.md` | active | decision status standard |
## Candidate files
| File | Status | Why candidate |
| `Knowledge/THINKING_WORKFLOW.md` | candidate | workflow reference, not status source |
| `Knowledge/DECISION_MEMO_TEMPLATE.md` | candidate | template, not policy |
| `Knowledge/STRATEGY_OPTIONS_TEMPLATE.md` | candidate | supporting template |
| `Knowledge/ROUTING_AND_HANDOFF.md` | candidate | routing reference |
## Deprecated / do not load as core
## Recently resolved gaps
- Dedicated decision log added.
- Smoke QA results file added.
- Explicit status/revisit standard added in a standalone canonical file.
- README now points to the canonical index file.
## Current gaps
- Scenario analysis template exists and is covered by `THINKING_03_ROUTING_AND_TEMPLATES.md`.
- Smoke QA remains documentation-level and does not replace a pilot case.
- Root path decision remains canonicalized to `ChatGPT/[Thinking]`.
## Next review trigger
- new project instructions change;
- routing conflict;
- judge/revisor failure;
- decision status missing in important outputs;
- handoff confusion;
- smoke QA fail.


## From: `ChatGPT/[Thinking]/SMOKE_QA_RESULTS.md`

# [Thinking] Smoke QA Results
Verdict: pass
| Test | Prompt / Input | Expected behavior | Actual behavior | Status | Fix required |
| Routing calculation to [Analytics] | Ask for deterministic calculation or metric math | Route to `[Analytics]`, not `[Thinking]` | Route rules and evidence guidance point to `[Analytics]` | pass | no |
| Routing code implementation to [Codex] | Ask for code changes, tests, or repo edits | Route to `[Codex]` | Handoff guidance points code work to `[Codex]` | pass | no |
| Unsupported claim flagged by `@judge` | Present weak claim with missing evidence | Mark unsupported claim and note evidence gap | Evidence rules require unsupported / blocker classification | pass | no |
| `@revisor` does not add new facts | Ask for rewrite of judged memo | Keep support status, no new facts | Revisor standard forbids new facts | pass | no |
| Scenario analysis uses 3 scenarios and does not invent numbers | Provide scenario template use case | Use base / optimistic / downside and avoid fabricated values | Scenario template added with empty numeric slots | pass | no |
| Decision memo includes status and revisit trigger | Create reusable decision record | Include status and revisit trigger | Decision status standard requires both | pass | no |
| AI OS evidence request is handed off, not copied into [Thinking] | Ask for KB-backed evidence | Hand off to `[AI OS]` instead of duplicating KB | Routing / handoff rules point to `[AI OS]` | pass | no |
## Issues found
- none
## Required fixes
- none
## Acceptance status
pass
