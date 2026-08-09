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

`analytical_depth` and `output_mode` are independent. Apply the conditional reasoning depth and compact-path rules from `ANALYTICAL_REASONING_STANDARD.md`; a `quick` output does not become a full reasoning artifact unless a material trigger requires deeper analysis.

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
→ evidence challenge / calibration as required
→ management synthesis when material and management-facing
→ LLM context package
→ memo / report
→ judge / QA
→ revise or rerun
→ acceptance
→ next run trigger
```

## Parent / Child Issue Gate

For large or risky analytics tasks involving data contracts, stage/mart layers, workbook/report contracts, reconciliation, manual review, provider evidence, duplicate/anomaly candidates, or final QA, use `Parent / Child Issue Gate Standard` by reference.

Analytics should define parent scope, child issue sequence, source/output layers, grain, formulas, QA, limitations, and acceptance gates before Codex implementation. Do not use this pattern for simple one-step Goal Mode tasks.

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

Classify the active analytical intent and create the bounded `TASK_PROFILE` when the case is not eligible for the routine compact path. Use `ANALYTICAL_REASONING_STANDARD.md`; do not replace the existing data, calculation, memo, QA, or acceptance stages.

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

Select the deterministic-first minimum sufficient method set through the registry and intent mapping in `ANALYTICAL_TECHNIQUES.md`. Apply the prerequisite gate before execution. A blocked method is not an executed method and is not supporting evidence.

State method, metric, period, grain, data source and limitation.

After deterministic findings, apply the preliminary evidence check, explanation challenge, claim calibration, and final evidence sufficiency from `ANALYTICAL_REASONING_STANDARD.md` only to the depth required by the case. Preserve `driver != root cause` and do not silently reconcile material method disagreement.

## Step 10 — Charts

Charts must be sourced from `mart_main_full` or a documented slice derived from it.

## Step 11 — Memo

Memo uses verified analysis, not raw assumptions.

Important sentences must be backed by metric/table/mart/period/evidence or marked as interpretation.

For material or decision-critical management-facing output, compress verified findings into the smallest sufficient executive synthesis: supported business meaning, business effect versus data/control artefact where relevant, management implication and decision/action if any, material uncertainty, and what changes the view. Do not create evidence or infer controllability or persistence without support. Keep routine output compact; strategic choices remain with `[Thinking]`.

## Step 12 — QA and acceptance

Run the existing Data QA, Calculation QA, Analysis QA, Chart QA, Memo QA, Judge, and acceptance path before final conclusion. `manual_review_required = yes` blocks automatic final publication until the existing review path records a resolution.

## Default output

```text
Question / scope:
Data status:
Grain / period / filters:
Method:
Findings:
QA:
Limitations:
Management implication / decision or action if any:
Next step:
```
