# Judge Calibration

## Purpose

Keep LLM-as-a-Judge useful without treating it as deterministic truth.

## Core Rule

Judge is a reviewer, not truth.

Judge output can help find unsupported claims, missing checks, weak evidence, scope creep, and unclear next steps. It cannot validate calculations, tests, schemas, formulas, contracts, metric definitions, column names, or business logic by opinion.

## Volatility

Judge results can vary by:

- model class;
- prompt wording;
- context quality;
- missing evidence;
- output format;
- hidden assumptions;
- overly broad criteria.

For high-risk work, use the same rubric across revisions and compare only the material verdict and required fixes.

## Calibration Questions

Before accepting a judge verdict, ask:

- Is the task type clear?
- Was the same evidence available to the judge?
- Are deterministic checks present where needed?
- Did the judge identify specific unsupported claims?
- Did the judge confuse style preference with correctness?
- Did the judge recommend forbidden tooling or production promotion?

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

Deterministic evidence overrides judge opinion.

If tests fail, data QA fails, schema checks fail, or contracts are missing, the eval status cannot be `pass` even if the judge likes the text.
