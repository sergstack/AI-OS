# Judge Calibration

## Purpose

Define how AI-OS uses LLM-as-a-Judge without treating judge output as objective truth.

## Core Rules

- Judge is a reviewer, not truth.
- Deterministic checks override LLM judge for calculations, tests, schemas, output contracts, source traceability, formulas, metric definitions, column names, and business logic.
- Judge must use explicit rubric.
- Judge output must include `pass`, `revise`, or `blocked`.
- High-risk outputs require human review.
- Unsupported claims must be listed, not silently fixed.
- Revision must be traceable to judge findings.

## Judge Volatility

Judge model behavior may change across model versions, prompts, context windows, or temperature/settings.

When judge model class changes:

- rerun golden eval cases;
- compare verdict drift;
- record risk if verdicts change;
- do not silently promote new judge behavior.

## Model Naming Rule

Do not hardcode permanent model names as governance truth.

Use model classes:

- `fast`;
- `reasoning`;
- `high-reasoning`;
- `local`;
- `judge`.

## Calibration Sample

Every important judge workflow should have:

- one pass example;
- one revise example;
- one blocked example;
- known failure modes;
- owner project.

## Verdict Discipline

Use:

```text
pass
revise
blocked
```

`pass` means ready for human review or adoption decision, not production-ready by default.

`revise` means the issue is local, clear, and bounded.

`blocked` means missing evidence, no validation path, unsafe scope, secrets, production/runtime/deploy risk, autonomous retrieval, or unapproved formula/schema/contract/business logic changes.

## Override Rule

If tests fail, data QA fails, schema checks fail, source traceability fails, or contracts are missing, the eval status cannot be `pass` even if the judge likes the text.
