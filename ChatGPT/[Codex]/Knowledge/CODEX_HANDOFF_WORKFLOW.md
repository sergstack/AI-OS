# Codex Handoff Workflow

## Purpose

Turn work from Thinking / Analytics / LLM into an implementation-ready task.

## Required fields

```markdown
# Codex Task

## Context
## Objective
## Autonomy mode
## Inputs
## Files to inspect
## Files allowed to modify
## Forbidden actions
## Expected outputs
## Acceptance criteria
## Tests / smoke checks
## Rollback plan
## Final response format
```

For Codex App, Codex Web, Codex CLI, or IDE execution, align the package with `../Codex_App/CODEX_APP_TASK_PACKAGE_CONTRACT.md`.

## Handoff quality

A good handoff is:
- atomic;
- testable;
- file-specific;
- clear about forbidden actions;
- clear about acceptance.
- explicit about autonomy mode and hard blockers.

## Bad handoff

- “Improve everything”
- “Refactor project”
- “Make it production-ready”
- “Use AI to automate this”
- no tests;
- no files;
- no acceptance criteria.
