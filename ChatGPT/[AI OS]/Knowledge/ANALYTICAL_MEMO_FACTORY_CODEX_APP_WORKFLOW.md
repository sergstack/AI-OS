# Analytical Memo Factory via Codex APP

## Purpose

Canonical workflow for producing analytical memos as executable artifacts through Codex APP while keeping project roles separate.

Use this workflow when the user wants a memo, charts, QA, and final artifacts produced from data with deterministic calculations.

## Terminology

- Analyst: task owner / analytical requester.
- `[Analytics]`: analytical methodology and framing layer.
- `[Codex]`: task package design layer.
- Codex APP: executor layer.
- Python: calculation layer.
- LLM: narrative layer.
- Judge/QA: quality layer.
- Human: acceptance layer.

## End-to-end workflow

```text
Analyst defines the analytical task
-> [Analytics] structures analytical methodology
-> [Codex] prepares an ultra-long Codex APP task package
-> Codex APP executes the task package
-> Python calculates
-> LLM writes from evidence
-> Judge/QA checks
-> Human accepts the result
```

## 1. Analyst defines the task

The Analyst provides:

- business question;
- data sources;
- period;
- expected memo type;
- constraints;
- audience;
- acceptance expectations.

## 2. [Analytics] structures the analytical methodology

`[Analytics]` owns analytical framing and methodology. It should define:

- `RAW -> STAGE -> MART -> EVIDENCE -> MEMO -> QA`;
- `stage_main_full` requirement;
- `mart_main_full` requirement;
- `mart_main_tz` / compact requirement;
- chart and evidence requirements;
- limitations and QA criteria.

`[Analytics]` is not reduced to Codex routing. It remains the place for analytical reasoning, methodology, data contracts, assumptions, limitations, and acceptance criteria.

## 3. [Codex] prepares an ultra-long task package

`[Codex]` designs the task package for Codex APP. It is not the local executor in this workflow.

The task package should include:

- objective;
- inputs;
- files to inspect;
- files allowed to modify;
- forbidden actions;
- expected outputs;
- tests / smoke checks;
- acceptance criteria;
- rollback;
- final response format.

## 4. Codex APP executes

Codex APP executes the task package locally. It should:

- inspect repository and data;
- write Python;
- build stage, mart, evidence, and charts;
- generate memo artifacts;
- run QA / smoke checks;
- report acceptance status.

## 5. Python calculates

Python is the calculation layer for:

- metrics;
- deltas;
- shares;
- rankings;
- totals;
- charts;
- evidence tables.

LLM must not perform these calculations mentally.

## 6. LLM writes

LLM is the narrative layer. It writes:

- memo narrative only from Python outputs and evidence;
- no unsupported calculations;
- no invented facts;
- no hidden assumptions.

## 7. Judge/QA checks

Judge/QA checks:

- unsupported claims;
- evidence coverage;
- limitations;
- data contracts;
- chart captions;
- memo quality;
- acceptance criteria.

## 8. Human accepts

Human review accepts or rejects:

- final memo;
- residual risks;
- limitations;
- next actions.

## Modes

### Mode A - Interactive Analytics

Use when the user wants to reason, explore, discuss methodology, or manually inspect outputs.

```text
User <-> [Analytics]
```

### Mode B - Analytical Memo Factory via Codex APP

Use when the user wants the memo produced as an artifact/work package with Python calculations, charts, QA, and final report.

```text
User -> [Analytics] -> [Codex] -> Codex APP
```

## Routing rule

If the user asks to create an analytical memo as an executable artifact, the default route is:

```text
[Analytics] for analytical task framing
-> [Codex] for ultra-long Codex APP task package
-> Codex APP for execution
```

Do not force the user into a manual loop where `[Analytics]` asks for Python outputs back and forth, unless the user explicitly wants interactive analysis.

## Boundaries

- Do not change metric definitions without explicit analytical approval.
- Do not invent schemas, formulas, facts, or business rules.
- Do not let LLM narrative exceed Python/evidence outputs.
- Do not claim production readiness without human acceptance.
- Do not treat Codex APP execution as ChatGPT Project sync evidence.

## Status

- status: canonical workflow pattern
- production_promotion: no
- source_of_truth: this file plus the granular Analytics and Codex workflow files
