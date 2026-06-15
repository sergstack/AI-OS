# [Codex] — Implementation Workflows

## Purpose

Compact upload artifact for [Codex] covering implementation workflows.

## Source files

- `ChatGPT/[Codex]/Knowledge/BUGFIX_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/REFACTORING_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/DATA_PIPELINE_IMPLEMENTATION_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/ANALYTICAL_MEMO_AUTOMATION_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/ANALYTICAL_TECHNIQUES_FOR_CODEX.md`
- `ChatGPT/[Codex]/Knowledge/KESTRA_AUTOMATION_STANDARD_REFERENCE.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Codex]/Knowledge/BUGFIX_WORKFLOW.md`

# Bugfix Workflow
## Steps
1. Reproduce bug or define failure.
2. Identify root cause.
3. Patch minimally.
4. Add regression test when possible.
5. Run checks.
6. Report fix and residual risk.
## Output
```text
Bug:
Root cause:
Fix:
Files changed:
Tests:
Residual risk:
```


## From: `ChatGPT/[Codex]/Knowledge/REFACTORING_WORKFLOW.md`

# Refactoring Workflow
## Goal
## Steps
1. Identify current behavior.
2. Identify files and scope.
3. Add or locate regression tests.
4. Refactor minimally.
5. Run tests.
6. Compare outputs.
7. Report changed files and preservation evidence.
## Acceptance
- behavior preserved;
- tests pass;
- no output contract changes;
- no broad unrelated edits.


## From: `ChatGPT/[Codex]/Knowledge/DATA_PIPELINE_IMPLEMENTATION_WORKFLOW.md`

# Data Pipeline Implementation Workflow
## Target shape
```text
RAW → STAGE → MARTS → ANALYSIS → LLM PACKAGE → REPORT → QA → ARCHIVE
```
## Steps
1. Inspect current entrypoints.
2. Identify input/output contracts.
3. Locate raw/stage/mart layers.
4. Preserve existing behavior.
5. Implement scoped change.
6. Add/adjust tests.
7. Run smoke QA.
8. Report acceptance.
## Forbidden
- changing metric definitions silently;
- changing output schema without approval;
- deleting validation;
- mixing generated artifacts with source code;
- adding infrastructure before governance approval.


## From: `ChatGPT/[Codex]/Knowledge/ANALYTICAL_MEMO_AUTOMATION_WORKFLOW.md`

# Analytical Memo Automation Workflow
## Pipeline
```text
data contracts
→ marts
→ insight cards
→ evidence cards
→ LLM context package
→ draft
→ judge
→ revise
→ final memo
```
## Codex responsibility
- data extraction;
- mart generation;
- evidence card creation;
- context package assembly;
- output validation;
- tests.
## Not Codex responsibility
- deciding business recommendation;
- inventing metric definitions;
- treating LLM text as data truth.


## From: `ChatGPT/[Codex]/Knowledge/ANALYTICAL_TECHNIQUES_FOR_CODEX.md`

# Analytical Techniques for Codex
Codex may implement analytical workflows, but must not invent business logic.
## Techniques to implement
- variance analysis;
- driver analysis;
- bridge tables;
- cohort summaries;
- anomaly flags;
- reconciliation totals;
- mart generation;
- evidence cards;
- memo context packages.
## Implementation rules
- formulas must be explicit;
- grain must be explicit;
- outputs must have tests;
- business definitions must come from Analytics task package;
- LLM narrative must be separate from deterministic calculation.


## From: `ChatGPT/[Codex]/Knowledge/KESTRA_AUTOMATION_STANDARD_REFERENCE.md`

# Kestra Automation Standard Reference
## Purpose
## Core model
```text
scripts / Python / Ollama / services → executors
Kestra → orchestration and run control
artifacts → evidence of execution
run_summary → audit trail
validation → quality gate
```
## Required production-like flow structure
```text
preflight
→ prepare_inputs
→ main_run
→ validation
→ save_artifacts
→ run_summary
→ error_handling
```
## Required metadata
* owner;
* purpose;
* environment;
* flow_type;
* input contract;
* output contract;
* validation rule;
* artifact policy;
* timeout policy;
* retry policy or no-retry decision;
* failure behavior.
## Flow types
* business;
* service;
* healthcheck;
* smoke_test;
* maintenance.
## Artifact policy
Every meaningful run should leave evidence:
* output;
* metrics / status;
* run_summary;
* execution logs available.
```text
artifacts/runs/<flow_id>/<execution_id>/
```
## Run summary minimum fields
* Flow;
* Namespace;
* Execution ID;
* Status;
* Validation result;
* Artifacts / evidence;
* Errors;
* Next action.
## Production checklist
* validation exists;
* run_summary exists;
* artifacts / evidence exist;
* execution logs are available;
* timeout policy exists;
* retry or no-retry decision exists;
* failure behavior exists;
* no temporary names like `_final`, `_new`, `_test2`.
## Open decisions
Do not create final YAML templates until these are known:
* artifact backend;
* actual task types;
* current flow YAML;
* storage layout;
* alerting policy;
* isolation strategy.
