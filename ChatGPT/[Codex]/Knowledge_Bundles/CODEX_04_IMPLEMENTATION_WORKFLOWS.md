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
- `docs/standards/EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`
- `ChatGPT/[Codex]/Knowledge/CODEX_04_IMPLEMENTATION_WORKFLOWS_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:ec821c704f14e805cf1a5cb0fc28ef1da4d594e2813063d2c8b67cb0c349715a
- generator: scripts/build_knowledge_bundles.py

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
## Canonical route
Use the Analytical Memo Factory via Codex APP pattern:
```text
Analyst defines the task
-> [Analytics] structures methodology
-> [Codex] prepares an ultra-long Codex APP task package
-> Codex APP executes
-> Python calculates
-> LLM writes from evidence
-> Judge/QA checks
-> Human accepts
```
`[Codex]` is the task package design layer in this route. Codex APP is the executor layer.
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
Implement deterministic parts:
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

## From: `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`

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

## From: `docs/standards/EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`

# Existing Script Controlled Refactor Standard
## Purpose
Define a safe reusable workflow for cleaning or refactoring an existing working script or pipeline without losing useful behavior.
Use this standard when a script already produces valuable output but has messy internals, mixed responsibilities, obsolete code, debug fragments, local assumptions, old tests, or an unclear contract.
The standard is an engineering / Codex standard. It is not Analytics methodology and does not define business logic, metrics, formulas, or analytical conclusions.
## Use when
Use `Existing Script Controlled Refactor Standard` when all of these are true:
- an existing script, CLI, notebook-exported script, or pipeline already runs or has a known useful output;
- the user wants cleanup, controlled refactor, modularization, simplification, or removal of obsolete internal code;
- behavior preservation matters more than redesign;
- a baseline and at least one meaningful safety check can be created or identified;
- changes can be made locally and reviewed in a bounded PR.
## Do not use when
Do not use this standard when:
- the task is greenfield implementation;
- the script is not known to work and the goal is bugfix or recovery;
- the user explicitly requests behavior, schema, metric, formula, API, provider-routing, or output-contract changes;
- the task requires production deploy, migration, source data mutation, Safe Apply, or real provider/API execution without separate approval;
- there is no meaningful way to baseline current behavior or compare before/after output;
- the correct next step is Analytics framing, business definition work, or evidence review rather than engineering refactor.
## Core rule
Baseline, contract, and safety tests come before cleanup.
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
## Baseline requirements
Before refactor, capture the smallest useful baseline that makes behavior observable.
Include where applicable:
- current command or entrypoint;
- representative input fixture, sample, or dry-run path;
- current output files, stdout, stderr, and exit code behavior;
- output filenames and locations;
- schema, columns, ordering, formatting, row counts, and reconciliation totals;
- accepted warnings, known quirks, and intentional legacy behavior;
- current tests or smoke checks;
- before-refactor golden output or comparison artifact.
Do not commit generated runtime artifacts unless repo policy explicitly allows them as fixtures or golden files.
## Output contract
Define what must remain unchanged unless separately accepted.
The output contract should state:
- output filenames and locations;
- file formats;
- schema, column names, column order, and deterministic formatting;
- expected row counts or reconciliation totals where applicable;
- CLI arguments and defaults;
- exit codes;
- stdout / stderr behavior when relevant;
- generated artifact policy;
- accepted warning and error behavior;
- what counts as a behavior change.
Any change to the output contract requires separate explicit acceptance.
## Safety tests before cleanup
Before removing code or restructuring modules, add or identify the smallest meaningful safety checks.
Use one or more of:
- existing tests;
- focused regression tests;
- golden-output comparison;
- smoke run or dry-run;
- schema check;
- row-count or reconciliation-total check;
- CLI help / entrypoint check;
- artifact validation;
- `git diff --check`;
- repo-specific validation scripts.
If no safety check is possible, stop and report a blocker instead of refactoring by intuition.
## Allowed refactor
Allowed only after baseline, output contract, and safety checks exist:
- extract functions;
- split internal modules;
- rename internal helpers;
- isolate CLI parsing from business logic;
- isolate IO from transformation logic;
- isolate validation and reporting;
- remove truly dead, obsolete, or unreachable code;
- remove debug-only branches that are not part of the accepted behavior;
- replace duplicated internal logic with an equivalent helper;
- improve comments and docstrings that clarify the preserved contract;
- add focused tests around preserved behavior.
Keep the diff minimal and reversible.
## Forbidden without separate acceptance
Do not do any of the following without separate explicit acceptance:
- behavior changes;
- output contract changes;
- schema, column, file-format, or file-location changes;
- metric, formula, business-rule, or financial-control changes;
- dependency additions;
- provider/API behavior changes;
- real provider/API execution;
- migrations;
- production/runtime/deploy changes;
- broad rewrite;
- deleting tests, QA, validation, or safety checks;
- source data mutation;
- committing generated runtime artifacts outside accepted fixture policy;
- adding autonomous loops, embeddings, semantic search, vector DB, or web UI.
## Recommended module split
When useful, split the script into clear internal layers:
```text
cli / entrypoint
-> config
-> io
-> transform
-> validate
-> report
-> tests
-> fixtures / golden outputs, only where repo policy allows
```
This split is recommended, not mandatory. Use the smallest structure that makes behavior safer and clearer.
## Parent/child decomposition for large risky refactors
For large or risky refactors, use `Parent / Child Issue Gate Standard` from `docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md`.
Do not duplicate the full parent/child standard here.
A large refactor should usually be split into child issues such as:
1. baseline and output contract;
2. safety tests or golden checks;
3. dead-code cleanup;
4. module extraction;
5. final before/after comparison.
Do not start downstream cleanup/refactor child issues until the baseline and safety-test child issues are accepted or merged.
## Acceptance criteria
Pass only when:
- baseline behavior is captured;
- output contract is explicit;
- safety tests or comparison checks exist and run;
- cleanup stays inside the accepted scope;
- before/after output is compared;
- output contract is preserved unless separately accepted;
- no forbidden runtime, schema, business-logic, provider, dependency, or artifact changes are included;
- final report lists changed files, checks, risks, rollback, and acceptance status.
## Required final response
For tasks using this standard, Codex must report:
```text
Summary:
Branch:
Files inspected:
Files changed:
Baseline captured:
Output contract:
Safety tests:
Before/after comparison:
Behavior changes:
Checks run:
Risks:
Rollback:
PR:
Acceptance status:
```
If behavior changed, acceptance status cannot be `pass` unless the behavior change was separately accepted.
## Blockers
Stop and report a blocker when:
- current behavior cannot be run, inspected, or baselined;
- output contract cannot be inferred safely;
- no meaningful safety test or comparison path exists;
- required input data is missing and no safe fixture can be used;
- the task requires secrets, local absolute paths, production systems, real provider/API execution, or source data mutation;
- preserving behavior conflicts with requested cleanup;
- the requested change would alter schema, metrics, formulas, business rules, APIs, file formats, column order, or output locations without separate acceptance.
## Key principle
Do not clean a working script by memory, taste, or vibes. First pin down what it does, then make it safer to change, then refactor only what the baseline can protect.

## From: `ChatGPT/[Codex]/Knowledge/CODEX_04_IMPLEMENTATION_WORKFLOWS_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Codex]/Knowledge_Bundles/CODEX_04_IMPLEMENTATION_WORKFLOWS.md`.
## Legacy section: `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`
`[Codex]` is the task package design layer. Codex APP is the executor layer.
## Legacy section: `docs/standards/EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`
Engineering / Codex standard for cleaning or refactoring an existing working script or pipeline without losing useful behavior.
Use when an existing script, CLI, notebook-exported script, or pipeline already runs or has known useful output and Sergey asks for cleanup, controlled refactor, modularization, simplification, or removal of obsolete internal code.
Do not use for greenfield implementation, bug recovery, Analytics methodology, business definition work, output-contract changes without acceptance, production deploys, migrations, source mutation, or real provider/API execution without separate approval.
Core rule:
For large or risky refactors, use `Parent / Child Issue Gate Standard` from `docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md` by reference.
