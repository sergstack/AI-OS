# Task Template for Codex

````markdown
# Codex Task

## Context

<What project/repo/feature this task belongs to.>

## Objective

<One clear outcome.>

## Autonomy mode

long-run / normal / inspect-only

Default:
Codex may continue on safe reversible assumptions and must stop only on canonical hard blockers from `AUTONOMY_POLICY.md`.

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

Use the canonical final report schema from `EXECUTION_REPORTING_RULES.md`. Mode-specific reports may be shorter but must include status, evidence, risks, blockers, rollback/next step, and no-auto-merge/PR fields when GitHub is involved.
````
