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

## Material-Evidence Integration Gate

For every material or high-risk conclusion or recommendation, the Judge must
check more than whether sources are present:

1. identify the material facts, contradictions, and new evidence found;
2. determine whether any of them changes or qualifies the decision boundary;
3. verify that the conclusion and recommendation incorporate those
   consequences; and
4. return `revise` or `blocked` when a recommendation remains contradicted or
   materially qualified without an explicit limitation or corresponding
   change.

Source presence alone is not sufficient evidence integration.

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

## Bias and reference regression coverage

For material judge workflows, rerun the four manual golden cases in
`GOLDEN_EVAL_CASES.md` when judge class, rubric, prompt, supported language,
or reference-check availability changes:

- self-preference: hidden or changed author/model identity must not change a
  verdict without an evidence-bearing reason;
- language parity: semantically equivalent supported-language inputs must
  surface material verdict drift rather than silently treating it as quality;
- ambiguity calibration: low-agreement cases must preserve uncertainty as
  `revise` or `blocked`, not inflate confidence to `pass`;
- reference available: a deterministic/reference-based result takes precedence
  over unconstrained holistic preference.

These are bounded regression cases, not a claim of universal vendor behavior
or a substitute for owner acceptance.

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
