# Task Template for Codex

````markdown
# Codex Task

## Context

<What project/repo/feature this task belongs to.>

## Objective

<One clear outcome.>

## Inputs

- <input files/data/context>

## Files to inspect

- `<path>`

## Files allowed to modify

- `<path>`

## Forbidden actions

- Do not modify secrets or `.env`.
- Do not change business logic unless explicitly stated.
- Do not remove validation/QA checks.
- Do not change output schemas unless explicitly stated.
- Do not add unrelated dependencies.

## Expected outputs

- <files/artifacts/behavior>

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Tests / smoke checks

```bash
<commands>
```

## Rollback plan

<How to revert safely.>

## Final response format

Summary:
Files changed:
Tests run:
Assumptions:
Risks:
Acceptance status:
Next step:
````
