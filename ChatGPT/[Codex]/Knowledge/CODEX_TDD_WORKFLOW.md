# Codex TDD Workflow

## Purpose

Keep AI coding tasks testable and reviewable without turning docs-only work into heavy process.

## Use TDD For

- code changes;
- scripts;
- data pipeline logic;
- parsers, converters, validators;
- bugfixes with reproducible behavior;
- output contract changes explicitly approved by the user.

## Test-first Loop

```text
understand expected behavior
-> inspect existing tests and entrypoints
-> write or identify the smallest failing test
-> run it and observe the failure
-> implement the smallest fix
-> run the focused test
-> run the smallest relevant regression/smoke check
-> review diff
-> report checks, risks, rollback, acceptance
```

## When Existing Tests Are Enough

If a suitable test already exists, run it before editing and again after editing. Do not add duplicate tests just to satisfy ceremony.

## Docs-only Tasks

Docs/config tasks do not need TDD. Use lightweight smoke checks instead:

- affected file search;
- `git diff --check`;
- repo consistency scripts;
- bundle/source consistency checks when Knowledge bundles change.

## Data And Analytics

For numeric, financial, or analytical logic, Python or SQL performs calculations. LLM may explain results but must not compute totals, ratios, variances, or reconciliations mentally.

## Stop Conditions

Stop or ask for approval if the task may change formulas, schemas, metric definitions, column names, output contracts, production behavior, or deployment.
