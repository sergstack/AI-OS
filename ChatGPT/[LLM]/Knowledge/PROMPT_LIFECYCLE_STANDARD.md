# Prompt Lifecycle Standard

## Purpose

Define the minimum lifecycle for reusable prompt and workflow assets in `[LLM]`.

This standard is a thin implementation adapter. `[AI OS]` remains the owner of canonical evidence semantics, Judge doctrine, and generic promotion governance.

## Lifecycle states

Use exactly these lifecycle states:

```text
draft
candidate
active
superseded
retired
```

- `draft`: working version; not allowed as a governed reusable asset.
- `candidate`: version prepared for possible reuse; it must pass risk-appropriate checks before promotion.
- `active`: current version allowed for reuse. Active does not itself mean universally reliable, fully calibrated, or production-proven. Reliability is established by eval evidence and acceptance metadata.
- `superseded`: replaced by a newer active version; do not use by default for new runs.
- `retired`: must no longer be used.

`evaluated`, `accepted`, `revised`, `failed`, and `passed` are not lifecycle states. They describe an evaluation result, acceptance decision, or transition event.

## Version transition

For a material change to an active asset:

```text
active v1
-> candidate v2
-> risk-appropriate eval
-> acceptance
-> active v2
-> v1 superseded
```

A material change creates a new identifiable candidate version. Do not overwrite an active definition in a way that loses its lineage. A simple version identifier and a `supersedes` reference are sufficient; this standard does not require semantic versioning.

## Lifecycle metadata

Keep the existing Prompt Registry fields and add this baseline metadata:

| Field | Meaning |
|---|---|
| `version` | Version identifier. `unversioned` is an honest migration marker for a legacy entry whose historical version was not recorded. |
| `eval_status` | Workflow evaluation result or state, such as `not_recorded`, `pending`, `pass`, `revise`, or `fail`. |
| `acceptance_status` | Owner decision, such as `not_recorded`, `pending`, `accepted`, or `rejected`. |
| `eval_refs` | References to existing eval records or evidence; use `not_recorded` when none is available. |
| `supersedes` | Prior version replaced by this version; use `not_recorded` when lineage is unavailable. |

Optional fields may include `last_evaluated`, `accepted_by`, and `acceptance_date` when the information exists and is useful. Do not fabricate historical evidence or make every optional field mandatory for every asset class.

Legacy `active` entries remain active during metadata migration unless an owner makes a different governance decision. `eval_status: not_recorded` or `acceptance_status: not_recorded` makes the evidence gap visible; it does not retroactively prove or revoke acceptance.

## Promotion gate

Promotion from `candidate` to `active` requires:

1. compliance with the input/output contract;
2. risk-appropriate evaluation under `LLM_EVAL_STANDARD.md`;
3. no unresolved material failure;
4. owner acceptance;
5. version and traceability metadata.

Evaluation depth follows risk. A large eval suite is not a blanket requirement for every reusable prompt.

## Corrections and change impact

A minor editorial correction does not change the contract or expected behavior. It may be recorded without automatically invoking a heavyweight lifecycle process.

A material behavior change requires a new candidate version, relevant regression/evaluation, acceptance, and promotion. Material changes include:

- output schema changes;
- evidence discipline changes;
- routing or Judge logic changes;
- correction of a historical failure mode;
- other substantive instructions that affect behavior.

## Boundaries

- Use the existing Prompt Registry; do not create another registry.
- Use canonical `[AI OS]` evidence, Judge, and promotion governance rather than copying it here.
- Follow existing Context Engineering rules for curated context, facts versus assumptions, forbidden secrets, Context Pack/CTC selection, and quality gates.
- This standard does not define autonomous execution or runtime automation.
