# Baseline-vs-Candidate Regression Gate

## Purpose

Compare an accepted baseline with a candidate before owner acceptance. This
extends the existing Cross-Project Eval layer; it does not promote, roll back,
or change a configuration automatically.

## Contracts

```text
baseline_id:
configuration_ref:
source_revision:
eval_definition_ref:
accepted_by:
acceptance_status:

candidate_id:
baseline_id:
change_type:
change_summary:
affected_workflows:
source_revision:
```

An unknown baseline, uncommitted configuration, or missing acceptance reference
produces `blocked` rather than a regression verdict.

## Regression matrix

| Test | Baseline | Candidate | Delta | Severity | Verdict |
|---|---|---|---|---|---|
| required contract | pass | pass | unchanged | — | pass |
| confirmed failure case | fail | pass | improvement | medium | pass |
| hard contract | pass | fail | regression | high | blocked |
| non-critical case | fail | fail | unchanged | low | revise |

Allowed deltas: `improvement`, `unchanged`, `regression`, `inconclusive`.
Never replace this matrix with an aggregate score.

## Verdict rules

`pass` requires required cases, valid deterministic contracts, respected scope,
and no critical/high regression. `revise` covers repairable regression or an
incomplete/inconclusive comparison. `blocked` covers missing baseline or
validation, deterministic/hard-boundary regression, or unaccepted authority
expansion. Improvement never compensates for a hard regression.

When Judge/model class changes, list verdict drift explicitly and require owner
review for material drift. Deterministic checks always override a Judge.

## Boundaries

Confirmed material cases from `FAILURE_REGISTRY.md` may supply regression cases.
Human acceptance remains mandatory. This gate adds no unattended evaluation,
automatic rollback/promotion, retrieval system, or runtime database.

## Smoke scenario

`REGRESSION-001`: compare an accepted baseline and a candidate against one
required workflow contract and one confirmed-failure case. A hard-contract
regression must yield `blocked` even if another case improves.
