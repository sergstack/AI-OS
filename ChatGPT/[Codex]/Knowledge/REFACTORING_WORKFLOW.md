# Refactoring Workflow

## Goal

Improve structure without changing behavior.

## Existing working scripts

When Sergey asks to clean, simplify, modularize, or refactor an existing working script or pipeline, use `Existing Script Controlled Refactor Standard` from the repo root.

Preserve behavior first:

```text
baseline current behavior
-> define output contract
-> add safety tests
-> cleanup/refactor
-> compare before/after output
-> acceptance
```

Do not remove code or restructure internals before baseline, output contract, and safety checks exist. Do not use this standard for all Codex tasks; use it for existing working scripts/pipelines where behavior preservation matters.

## Steps

1. Identify current behavior.
2. Identify files and scope.
3. Define the output contract.
4. Add or locate regression/golden-output safety tests.
5. Refactor minimally.
6. Run tests.
7. Compare before/after outputs.
8. Report changed files and preservation evidence.

## Acceptance

- behavior preserved;
- baseline captured;
- output contract explicit;
- before/after output compared;
- tests pass;
- no output contract changes;
- no broad unrelated edits.
