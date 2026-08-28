# ChatGPT + Codex APP Operating Guide

## Purpose

Daily shortcut for choosing between ChatGPT Projects and Codex APP.

## When To Use ChatGPT Projects

| Project | Use for |
|---|---|
| `[AI OS]` | AI concepts, KB, evidence, governance, use cases |
| `[Thinking]` | decisions, options, risks, scenarios |
| `[Analytics]` | data, calculations, marts, QA, memo |
| `[LLM]` | prompts, workflow, model routing, judge/revise |
| `[Codex]` | implementation task prep, scope check, handoff |
| `[Inbox Router]` | classify incoming tasks and choose a route |

## When To Use Codex APP

Use Codex APP when the task needs:

- repo file changes;
- branch / commit / PR workflow;
- checks or smoke tests;
- docs, config, or code execution;
- long-run or ultra-long local work.

## Main Difference

`ChatGPT/[Codex]` prepares, checks, and packages implementation work.

Codex APP executes repo/local file work on a branch and reports checks, risks, rollback, and acceptance status.

## Default Route

| Need | Route |
|---|---|
| Simple question | ChatGPT Project |
| Repo/file change | Codex APP |
| Unclear routing | `[Inbox Router]` |
| AI evidence or governance | `[AI OS]` |
| Data or calculation | `[Analytics]` |
| Prompt or workflow | `[LLM]` |
| Implementation | Codex APP via `[Codex]` or direct Goal Mode |
| Clean/refactor an existing working script without behavior loss | Codex APP via `Existing Script Controlled Refactor Standard` |

## Existing Working Script Cleanup

If Sergey asks to clean, simplify, modularize, or refactor a working script or pipeline, preserve behavior first.

Use `Existing Script Controlled Refactor Standard`:

```text
baseline current behavior -> define output contract -> add safety tests -> refactor -> compare before/after output -> acceptance
```

This is engineering/Codex guidance, not Analytics methodology. Do not use it to change business definitions, formulas, metrics, schemas, or output contracts without separate acceptance.

## Minimal Daily Workflow

1. Write the goal.
2. Choose the ChatGPT Project or Codex APP.
3. Paste a compact goal or context pack.
4. Let the system infer scope, checks, rollback, and acceptance.
5. Review the final report.
6. Merge only after human approval.
