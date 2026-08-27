# Intermediate-State Assertions

## Purpose

Add deterministic QA checkpoints to the existing analytical flow:

```text
RAW → STAGE assertions → MART assertions → EVIDENCE assertions → artifact QA
```

This is a cross-project governance pattern. `[Analytics]` remains the owner of
metrics, formulas, thresholds, and business meaning; `[Codex]` may implement
only accepted contracts.

## Assertion record

```text
assertion_id:
owner_project:
pipeline_layer: raw | stage | mart | evidence | output
contract_ref:
check_type:
expected:
actual:
severity:
status: pass | fail | not_run
```

`NOT RUN` is evidence, not a pass. Do not invent a threshold, metric, or
business rule: use an explicit Analytics contract or report the check as not
applicable/not run.

## Applicable deterministic checks

- schema and required columns;
- key uniqueness and join cardinality;
- contract-defined row-count ranges and null rates;
- allowed values, sign, unit, currency, and period consistency;
- reconciliation totals and evidence-table completeness.

## Smoke example

`ASSERT-001`: a stage join duplicates a declared unique key. The STAGE
cardinality assertion fails before MART/EVIDENCE/final memo output; the result
is `fail`, not a plausible final artifact.

## Boundaries

No LLM arithmetic, autonomous assertion generation, source-data mutation,
production deployment, or expanded authority is introduced. Rollback is the
existing revert/manual-review path for an approved implementation.
