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

For large or risky refactors, use `Parent / Child Issue Gate Standard` from `PARENT_CHILD_ISSUE_GATE_STANDARD.md`.

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
