# LLM Eval Standard

## Purpose

Define minimum, risk-proportional evaluation for reusable `[LLM]` prompt and workflow assets. Evaluation must be sufficient for the cost of error without turning `[LLM]` into an MLOps platform.

## Risk classification

Choose the evaluation level from four primary considerations:

- error cost;
- evidence sensitivity;
- reversibility;
- verification path.

Downstream consequence may also raise the level. Do not use a mandatory numerical risk formula.

## Evaluation levels

### LIGHT

Use for low-risk, reversible workflows whose output is easy to verify, such as formatting, simple rewriting, structure transformation, or low-risk extraction with easy manual verification.

Minimum:

- schema or smoke check;
- 1-3 representative cases;
- owner check.

LIGHT does not require a full regression suite or heavyweight eval suite.

### CONTROLLED

Use for reusable workflows where an error may affect downstream analysis, decision support, or a repeated process.

Minimum:

- representative cases;
- negative and boundary cases;
- materially relevant historical failures;
- regression protection;
- Judge/revise where appropriate;
- owner acceptance.

### HIGH-RISK

Use for evidence-sensitive or consequential workflows.

Minimum:

- extended representative set;
- boundary and adversarial cases;
- historical failure cases;
- workflow-specific Judge fixtures;
- deterministic verification where applicable;
- explicit human acceptance;
- visible limitations.

HIGH-RISK does not authorize an LLM to perform deterministic calculations. Route `[Analytics]` calculations and analytical work to `[Analytics]`.

## Evaluation types

### Pre-promotion / offline eval

Checks a candidate before promotion and governed reuse.

### Regression eval

Checks that a material change has not reintroduced known failure modes. Regression cases should primarily come from materially relevant historical failures or corrections; not every comment needs to become a regression test.

### Runtime/output QA

Checks a specific output produced during workflow use. Runtime QA does not by itself prove the quality of the reusable asset.

## Deterministic before Judge

If a criterion can be checked deterministically, perform that check before relying on an LLM Judge. Examples include:

- required sections and schema fields;
- enum and exact status values;
- file presence;
- routing owner;
- forbidden field detection;
- simple contract validation.

Use Judge evaluation for semantic or evidence-sensitive criteria. A Judge is not absolute truth.

## Ownership boundary

`[AI OS]` owns:

- canonical Judge doctrine;
- evaluator governance and calibration principles;
- generic evidence/confidence semantics;
- generic promotion governance.

`[LLM]` owns:

- workflow-specific rubrics;
- domain, negative, and boundary cases;
- expected outcomes;
- historical regression fixtures.

`[LLM]` provides workflow-specific test fixtures for the canonical Judge mechanism. It does not own a separate generic Judge calibration standard.

## Evidence, evaluation, and acceptance

Keep these operational concepts separate:

```text
evidence_status -> follows canonical [AI OS] semantics
workflow_eval -> result for a specific LLM asset or workflow
acceptance_status -> owner or human-gate decision
```

Do not introduce model confidence, Judge confidence, a workflow-confidence score, or a multi-level confidence architecture. Self-reported LLM confidence is not a governance metric or a calibrated probability. Model uncertainty may be recorded as a textual limitation.

## Failure to regression

When a failure materially affected output, can recur, and belongs to reusable behavior, consider its case as a candidate regression fixture. Keep the reference in existing eval records; do not create a separate Failure Registry.

## Local AI boundary

Existing `LOCAL_AI_EXPERIMENT_PLAYBOOK.md`, `LOCAL_AI_SECURITY_BOUNDARY.md`, and local pilot rules remain authoritative:

- local output is draft/candidate evidence;
- local retrieval is not final truth;
- only curated context is allowed;
- limitations are required;
- production truth is prohibited without appropriate QA.

Risk-aware use:

- low risk: a local result may be sufficient after deterministic/schema verification passes;
- controlled: use a local draft with stronger or Judge verification where needed;
- high-risk or evidence-sensitive: local processing may prepare a draft, but consequential conclusions require stronger verification and a human gate.

This is an operational interpretation, not a separate permanent escalation architecture.

## Context boundary

Follow the existing Context Engineering standards for curated context, facts versus assumptions, forbidden secrets, Context Pack/CTC selection, and quality gates. Do not duplicate the Context Pack schema here.
