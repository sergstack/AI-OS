# Analytics Workflow

## Purpose

Давать проверяемый аналитический результат: расчёт, data contract, stage, mart, analysis, charts, memo, QA или handoff.

## Step 0 — Output mode and artifact budget

Before running the full workflow, define:

```text
mode: quick / standard / full / autoloop_analysis
requested_output:
max_visible_metrics:
max_visible_columns:
max_sheets:
must_create_files: yes/no
evidence_depth: light / normal / full
```

If mode = `quick`, collapse the workflow:

```text
Question
→ minimal inputs
→ grain / period / filters
→ calculation or reasoning
→ compact result
→ QA note
→ limitation
```

Do not run full RAW/STAGE/MART/slices/charts/report workflow unless required by the task.

## Canonical workflow

```text
question / scope
→ inputs
→ data contract
→ RAW
→ stage_main_full
→ mart_main_full
→ compact mart
→ deterministic calculation
→ findings
→ LLM context package
→ memo / report
→ judge / QA
→ revise or rerun
→ acceptance
→ next run trigger
```

## `autoloop_analysis`

`autoloop_analysis` is a supervised analytical loop, not an autonomous agent. Backward-compatible alias: `autoloop`.

Rules:

- deterministic calculations first;
- judge/QA before final memo;
- revise or rerun only from visible QA findings;
- stop on blockers, missing data contract, failed DQ, unclear grain, or no validation path;
- do not add autonomous retrieval, vector DB, embeddings, semantic search, web UI, logs, journals, or runtime artifacts.

## Step 1 — Question / scope

Define:

- business question;
- decision context;
- audience;
- period;
- grain;
- metrics;
- filters;
- owner;
- expected output.

If scope is unclear, make a reasonable working assumption and mark it as `ASSUMPTION`.

## Step 2 — Inputs

Inventory:

- available files;
- missing files;
- compact/full JSON;
- source systems;
- refresh date;
- required joins;
- directories/mappings;
- known limitations.

## Step 3 — Data contract

No calculation without grain. No memo without method. No mart without expected output.

## Step 4 — RAW

RAW is original input. Do not add business logic here.

Allowed:

- file inventory;
- source metadata;
- raw totals;
- raw column list.

Forbidden:

- metric formulas;
- classifications;
- interpretations;
- memo conclusions.

## Step 5 — STAGE MAIN FULL

Create or define `stage_main_full` before any stage slices.

Purpose:

- cleaned;
- normalized;
- typed;
- joined only where needed for identity/mapping;
- no metrics and no classifiers.

## Step 6 — MART MAIN FULL

Create or define `mart_main_full` as the complete analysis-ready table.

It includes:

- business metrics;
- metric formulas;
- classification flags;
- risk fields;
- confidence fields;
- QA fields;
- evidence references;
- output eligibility fields.

## Step 7 — MART MAIN TZ / COMPACT

Create or define a shortened mart according to the task, audience, or executive memo.

It includes only:

- headline metrics;
- decision-relevant dimensions;
- material deviations;
- key flags;
- visible limitations.

## Step 8 — Slices

All analytical slices must derive from `mart_main_full`:

```text
mart_main_full
→ slice_for_executive
→ slice_by_period
→ slice_by_entity
→ slice_by_metric
→ slice_for_charts
→ slice_for_memo
```

## Step 9 — Analysis

Choose technique:

- variance analysis;
- driver analysis;
- bridge analysis;
- cohort analysis;
- anomaly detection;
- reconciliation;
- segmentation;
- trend analysis.

State method, metric, period, grain, data source and limitation.

## Step 10 — Charts

Charts must be sourced from `mart_main_full` or a documented slice derived from it.

## Step 11 — Memo

Memo uses verified analysis, not raw assumptions.

Important sentences must be backed by metric/table/mart/period/evidence or marked as interpretation.

## Step 12 — QA and acceptance

Run QA before final conclusion.

## Default output

```text
Question / scope:
Data status:
Grain / period / filters:
Method:
Findings:
QA:
Limitations:
Decision / recommendation:
Next step:
```
