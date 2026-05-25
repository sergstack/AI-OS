# Codex App Task Package Contract

## Purpose

Define the required interface between `ChatGPT/[Codex]` and `Codex APP`.

## Producer

`ChatGPT/[Codex]` prepares implementation task packages.

## Executor

`Codex APP` / `Codex Web` / `Codex CLI` / IDE executes only scoped tasks.

## Required input fields

- objective
- context
- repo
- files to inspect
- files allowed to modify
- forbidden actions
- expected outputs
- acceptance criteria
- tests / smoke checks
- rollback plan

## Refuse / block if

- scope is unclear
- allowed files are missing
- business logic changes without approval
- schemas/output contracts change without approval
- no test/smoke check is possible
- secrets or production credentials are needed

## Output format

- Summary
- Files changed
- Checks run
- Risks / limitations
- Rollback
- Acceptance status
- Next step

## Smoke test

Take one task package produced by `ChatGPT/[Codex]` and verify that `Codex APP` can classify mode, allowed files, forbidden actions, acceptance criteria, checks and rollback before implementation.
