# AGENTS.md

## Project purpose

<Tell coding agents what this repository does.>

## Architecture

<Key folders, entrypoints, data flow.>

## Allowed actions

- Read repo.
- Edit files allowed by task.
- Run listed tests.
- Add focused tests if useful.

## Task package source

Prefer tasks prepared by `ChatGPT/[Codex]`.
Before implementation, verify that the task contains objective, context, repo, files to inspect, files allowed to modify, forbidden actions, expected outputs, acceptance criteria, tests/smoke checks and rollback plan.

If the task package is incomplete, stop and return a blocker instead of guessing.

## Forbidden actions

- Do not touch `.env`, secrets, credentials, tokens.
- Do not change business logic without explicit approval.
- Do not change schemas or output contracts without explicit approval.
- Do not remove validation or tests.
- Do not add unrelated dependencies.
- Do not deploy.
- Do not add semantic search, vector DB, web UI, autonomous retrieval, or agentic workflows without explicit approval.

## Test commands

```bash
<insert project-specific test commands>
```

## Acceptance

A task is accepted only if:

- objective is met;
- scope stayed within allowed files;
- checks are reported;
- risks are stated;
- rollback is clear.
