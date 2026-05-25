# Codex Handoff Workflow

## Purpose

Turn work from Thinking / Analytics / LLM into an implementation-ready task.

## Required fields

```markdown
# Codex Task

## Context
## Objective
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

## Handoff quality

A good handoff is:
- atomic;
- testable;
- file-specific;
- clear about forbidden actions;
- clear about acceptance.

## Bad handoff

- “Improve everything”
- “Refactor project”
- “Make it production-ready”
- “Use AI to automate this”
- no tests;
- no files;
- no acceptance criteria.
