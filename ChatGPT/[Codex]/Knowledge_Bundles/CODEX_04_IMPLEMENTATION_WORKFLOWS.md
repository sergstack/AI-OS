# [Codex] — Implementation Workflows

## Purpose

Compact upload artifact for [Codex] covering implementation workflows.

## Source files

- `ChatGPT/[Codex]/Knowledge/BUGFIX_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/REFACTORING_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/DATA_PIPELINE_IMPLEMENTATION_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/ANALYTICAL_MEMO_AUTOMATION_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/ANALYTICAL_TECHNIQUES_FOR_CODEX.md`
- `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`
- `EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`

# Analytical Memo Factory via Codex APP
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
`[Codex]` is the task package design layer. Codex APP is the executor layer.

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
Improve structure without changing behavior.
## Existing working scripts
When Sergey asks to clean, simplify, modularize, or refactor an existing working script or pipeline, use `Existing Script Controlled Refactor Standard` from the repo root.
Preserve behavior first:
```text
baseline current behavior
-> define output contract
-> add safety tests
-> cleanup/refactor
-> compare before/after output
-> acceptance
```
Do not remove code or restructure internals before baseline, output contract, and safety checks exist. Do not use this standard for all Codex tasks; use it for existing working scripts/pipelines where behavior preservation matters.
## Steps
1. Identify current behavior.
2. Identify files and scope.
3. Define the output contract.
4. Add or locate regression/golden-output safety tests.
5. Refactor minimally.
6. Run tests.
7. Compare before/after outputs.
8. Report changed files and preservation evidence.
## Acceptance
- behavior preserved;
- baseline captured;
- output contract explicit;
- before/after output compared;
- tests pass;
- no output contract changes;
- no broad unrelated edits.


## From: `EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`

# Existing Script Controlled Refactor Standard
Engineering / Codex standard for cleaning or refactoring an existing working script or pipeline without losing useful behavior.
Use when an existing script, CLI, notebook-exported script, or pipeline already runs or has known useful output and Sergey asks for cleanup, controlled refactor, modularization, simplification, or removal of obsolete internal code.
Do not use for greenfield implementation, bug recovery, Analytics methodology, business definition work, output-contract changes without acceptance, production deploys, migrations, source mutation, or real provider/API execution without separate approval.
Core rule:
```text
baseline current behavior
-> define output contract
-> add safety tests
-> remove dead/obsolete code
-> refactor structure without behavior change
-> compare before/after output
-> acceptance
```
Codex must not start cleanup or restructuring until current behavior is captured, the output contract is explicit, and a safety test or comparison path exists.
For large or risky refactors, use `Parent / Child Issue Gate Standard` from `PARENT_CHILD_ISSUE_GATE_STANDARD.md` by reference.


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
