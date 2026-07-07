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

For Codex App, Codex Web, Codex CLI, or IDE execution, align the package with the repo-root file `Codex APP/CODEX_APP_TASK_PACKAGE_CONTRACT.md`.

For local + GitHub tasks, include branch, PR, and cleanup expectations from `LOCAL_GITHUB_SYNC_WORKFLOW.md`.

For real working repositories, start root agent instructions from the repo-root file `Codex APP/CODEX_APP_AGENTS_TEMPLATE.md`.

## Folder boundary

This file prepares handoff from ChatGPT `[Codex]` to the executor layer.

Executor-layer assets must be referenced from the top-level `Codex APP/` folder, not stored inside `ChatGPT/[Codex]`.

## Handoff quality

A good handoff is:
- atomic;
- testable;
- file-specific;
- clear about forbidden actions;
- clear about acceptance.
- explicit about autonomy mode and canonical hard blockers from `AUTONOMY_POLICY.md`.

## Bad handoff

- “Improve everything”
- “Refactor project”
- “Make it production-ready”
- “Use AI to automate this”
- no tests;
- no files;
- no acceptance criteria.
