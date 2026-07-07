# Codex SPEC — Repo AI Context Contract

## Status

ready_for_codex

## Mode

documentation / repo context contract / minimal diff

---

## 1. Objective

Add a minimal AI Context Contract to the repository without changing business logic.

The goal is to make the repo understandable and safe for ChatGPT/Codex workflows by adding:

- `AGENTS.md`
- `docs/ai/PROJECT_BRIEF.md`
- `docs/ai/PROJECT_INDEX.md`
- `docs/ai/ARCHITECTURE.md`
- `docs/ai/RUNBOOK.md`
- `docs/ai/QUALITY_GATES.md`

This task is documentation/context-contract only.

---

## 2. Context

The repository should follow a repo-first AI workflow:

```text
GitHub repo
→ ChatGPT analysis
→ Codex implementation
→ AGENTS.md + docs/ai/*
→ tests / lint / smoke QA
→ PR review
```

The key principle is not to create a “super-agent”, but to make the repo clear for any AI implementation agent:

- where the entrypoints are;
- where the code is;
- where the tests are;
- what must not be touched;
- how to validate changes;
- how to rollback safely.

---

## 3. Scope

### In scope

Create or update minimal AI-readable documentation:

- repo-level operating rules;
- project brief;
- project index;
- architecture overview;
- runbook;
- quality gates.

### Out of scope

- business logic changes;
- schema changes;
- dependency changes;
- generated artifact changes;
- MCP/RAG/vector DB implementation;
- new services;
- new automation architecture;
- production runtime changes.

---

## 4. Files to inspect before editing

Inspect the actual repository before creating documentation.

Recommended files/directories to inspect:

- `README.md`, if present;
- project root tree;
- source directories:
  - `src/`
  - `app/`
  - or equivalent;
- test directories:
  - `tests/`
  - or equivalent;
- package/runtime files:
  - `pyproject.toml`
  - `requirements.txt`
  - `package.json`
  - `Makefile`
  - `Dockerfile`
  - or equivalent;
- existing docs:
  - `docs/`
  - `RUNBOOK.md`
  - `SPEC.md`
  - `AGENTS.md`
  - or equivalent;
- config examples:
  - `.env.example`
  - config templates only;
- generated/artifact/log directories to mark as forbidden or sensitive.

Do not read or print secrets.

---

## 5. Files allowed to create or modify

### Required

- `AGENTS.md`
- `docs/ai/PROJECT_BRIEF.md`
- `docs/ai/PROJECT_INDEX.md`
- `docs/ai/ARCHITECTURE.md`
- `docs/ai/RUNBOOK.md`
- `docs/ai/QUALITY_GATES.md`

### Optional only if clearly needed

- `README.md`

Use `README.md` only for a short pointer to:

- `AGENTS.md`
- `docs/ai/`

Do not make broad README rewrites.

---

## 6. Forbidden actions

- Do not modify source/business logic.
- Do not change schemas.
- Do not change output contracts.
- Do not add dependencies.
- Do not add MCP.
- Do not add RAG.
- Do not add vector DB.
- Do not add new services.
- Do not add agentic workflows.
- Do not run destructive commands.
- Do not commit or push unless explicitly instructed.
- Do not read, print, modify, or commit secrets.
- Do not modify:
  - `.env`
  - credentials
  - tokens
  - private dumps
  - raw logs
  - production configs
- Do not edit generated artifacts unless explicitly required for documentation.
- Do not invent commands, modules, architecture, or tests.

---

## 7. Documentation rules

Each created file must describe the actual repository, not an imagined future state.

Use compact, factual documentation.

If something is unknown, mark it as:

```text
TBD
```

Do not guess.

Each file should be operational and useful for future Codex tasks.

Required documentation principles:

- separate facts from assumptions;
- mark unknown commands as `TBD`;
- avoid unsupported claims;
- avoid excessive prose;
- include forbidden areas;
- include quality gates;
- include rollback expectations;
- keep the diff minimal.

---

## 8. Required file content

### 8.1 `AGENTS.md`

Must include:

- project goal;
- what the project is not;
- tech stack;
- repository map;
- required reading before changes;
- install/run/test/lint/build commands or `TBD`;
- working rules;
- forbidden areas;
- definition of done;
- final response format.

Minimal required structure:

```md
# AGENTS.md

## Project goal

[TBD or actual project goal]

## What this project is not

- This project is not a place for secrets.
- This project is not a raw log archive.
- This project is not a sandbox for unrelated refactors.
- This project is not a place for MCP/RAG/vector DB experiments at the first stage.

## Tech stack

- Language:
- Runtime:
- Package manager:
- Main framework:
- Database / storage:
- External services:

## Repository map

- `src/` or `app/` — main source code.
- `tests/` — automated tests.
- `docs/ai/` — compact AI-readable project context.
- `artifacts/` — generated outputs; do not edit unless explicitly requested.
- `logs/` — runtime logs; do not use as source of truth.
- `.env` / secrets — never read, print, edit, or commit.

## Required reading before changes

Before editing, read:

1. `README.md`
2. `docs/ai/PROJECT_INDEX.md`
3. `docs/ai/ARCHITECTURE.md`
4. `docs/ai/RUNBOOK.md`
5. `docs/ai/QUALITY_GATES.md`

## Commands

### Install

```bash
TBD
```

### Run

```bash
TBD
```

### Test

```bash
TBD
```

### Lint / typecheck

```bash
TBD
```

### Build

```bash
TBD
```

## Working rules

- Start with a short plan.
- Identify affected files before editing.
- Prefer minimal diffs.
- Do not change schemas without a migration note.
- Do not edit generated files unless explicitly requested.
- Do not touch secrets, credentials, tokens, `.env`, raw logs, or private dumps.
- Do not introduce MCP/RAG/vector DB unless the task explicitly requests it.
- After changes, run available tests or explain why they were not run.

## Definition of done

A task is complete only when:

- changed files are listed;
- tests/checks are run or skipped with reason;
- risks are listed;
- rollback note is provided;
- generated files are not accidentally modified;
- no secrets are exposed;
- acceptance criteria are checked.
```

---

### 8.2 `docs/ai/PROJECT_BRIEF.md`

Must include:

- goal;
- primary users;
- business value;
- current priority;
- non-goals;
- critical risks;
- status.

Template:

```md
# Project Brief

## Goal

[TBD or actual goal]

## Primary users

- [TBD]

## Business value

[TBD]

## Current priority

[TBD]

## Non-goals

- [TBD]

## Critical risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| TBD | TBD | TBD |

## Status

- Current status: TBD
- Last reviewed: YYYY-MM-DD
- Owner: TBD
```

---

### 8.3 `docs/ai/PROJECT_INDEX.md`

Must include:

- entrypoints;
- core modules;
- data flow;
- important files;
- required reading;
- fragile areas.

Template:

```md
# Project Index

## Entry points

| Area | File / command | Purpose |
|---|---|---|
| Main run | TBD | TBD |
| Tests | TBD | TBD |
| Config | TBD | TBD |

## Core modules

| Module | Path | Responsibility |
|---|---|---|
| TBD | TBD | TBD |

## Data flow

```text
[input]
→ [processing]
→ [validation]
→ [output]
→ [QA]
```

## Important files

1. `TBD` — TBD
2. `TBD` — TBD
3. `TBD` — TBD

## Before changing anything

Read:

1. `AGENTS.md`
2. `README.md`
3. `docs/ai/ARCHITECTURE.md`
4. `docs/ai/QUALITY_GATES.md`

## Known fragile areas

| Area | Risk | Rule |
|---|---|---|
| TBD | TBD | TBD |
```

---

### 8.4 `docs/ai/ARCHITECTURE.md`

Must include:

- system overview;
- layers;
- main components;
- data contracts;
- invariants;
- architecture decisions.

Template:

```md
# Architecture

## System overview

[TBD or actual architecture overview]

## Layers

```text
Input
→ Parsing / ingestion
→ Processing
→ Validation
→ Output
→ QA / reporting
```

## Main components

| Component | Path | Responsibility | Depends on |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

## Data contracts

| Contract | Location | Notes |
|---|---|---|
| Input schema | TBD | TBD |
| Output schema | TBD | TBD |
| Config schema | TBD | TBD |

## Invariants

- TBD
- Do not change output contracts without explicit approval.
- Do not mix deterministic calculations with LLM narrative.

## Architecture decisions

| Date | Decision | Reason | Status |
|---|---|---|---|
| YYYY-MM-DD | TBD | TBD | active |
```

---

### 8.5 `docs/ai/RUNBOOK.md`

Must include:

- local setup;
- run command;
- test command;
- lint/typecheck command;
- expected outputs;
- common failures;
- safe rollback;
- release checklist.

Template:

```md
# Runbook

## Local setup

```bash
TBD
```

## Run project

```bash
TBD
```

## Run tests

```bash
TBD
```

## Run lint / typecheck

```bash
TBD
```

## Expected outputs

| Output | Path | How to validate |
|---|---|---|
| TBD | TBD | TBD |

## Common failures

| Symptom | Likely cause | Fix |
|---|---|---|
| TBD | TBD | TBD |

## Safe rollback

```bash
git restore AGENTS.md docs/ai/
```

If `README.md` was updated:

```bash
git restore README.md
```

## Release checklist

- [ ] tests pass;
- [ ] no secrets exposed;
- [ ] generated files reviewed;
- [ ] changed files listed;
- [ ] rollback note prepared.
```

---

### 8.6 `docs/ai/QUALITY_GATES.md`

Must include:

- required before PR;
- AI output QA;
- smoke checks;
- acceptance status block.

Template:

```md
# Quality Gates

## Required before PR

- [ ] install command works or is marked `TBD`;
- [ ] tests pass or skipped with reason;
- [ ] lint/typecheck pass or skipped with reason;
- [ ] no secrets touched;
- [ ] no raw logs added;
- [ ] no generated trash committed;
- [ ] no schema changes without migration note;
- [ ] changed files listed;
- [ ] rollback note provided.

## AI output QA

- [ ] Answer matches the task.
- [ ] Facts are separated from interpretation.
- [ ] Unsupported claims are marked.
- [ ] Limitations are visible.
- [ ] Output is actionable.
- [ ] Routing is correct.

## Smoke checks

```bash
TBD
```

## Acceptance status

```text
quality_status: pass / revise / blocked
reason:
unsupported_claims:
required_revision:
```
```

---

## 9. Suggested implementation steps

1. Inspect repo tree.
2. Identify project stack and commands.
3. Identify source, tests, configs, generated outputs, and sensitive areas.
4. Create `docs/ai/` directory.
5. Add `AGENTS.md`.
6. Add `docs/ai/PROJECT_BRIEF.md`.
7. Add `docs/ai/PROJECT_INDEX.md`.
8. Add `docs/ai/ARCHITECTURE.md`.
9. Add `docs/ai/RUNBOOK.md`.
10. Add `docs/ai/QUALITY_GATES.md`.
11. Optionally add a short README pointer.
12. Run available tests or static checks.
13. Review diff.
14. Report changed files, checks, risks, and rollback note.

---

## 10. Tests / smoke checks

Run the smallest safe checks available from the repository.

Prefer existing commands discovered from repo files.

Examples only:

```bash
pytest
npm test
npm run lint
python -m compileall .
```

Do not run heavy, destructive, production, or data-mutating commands.

If no reliable checks exist, run non-invasive static inspection only and explain why tests were skipped.

---

## 11. Acceptance criteria

- [ ] `AGENTS.md` exists at repo root.
- [ ] `docs/ai/PROJECT_BRIEF.md` exists.
- [ ] `docs/ai/PROJECT_INDEX.md` exists.
- [ ] `docs/ai/ARCHITECTURE.md` exists.
- [ ] `docs/ai/RUNBOOK.md` exists.
- [ ] `docs/ai/QUALITY_GATES.md` exists.
- [ ] Commands are documented or marked `TBD`.
- [ ] Entry points are documented or marked `TBD`.
- [ ] Forbidden areas are documented.
- [ ] Quality gates are documented.
- [ ] Rollback guidance is documented.
- [ ] No source/business logic changed.
- [ ] No schemas changed.
- [ ] No dependencies added.
- [ ] No secrets touched.
- [ ] No generated files accidentally changed.
- [ ] Tests/checks were run or skipped with explicit reason.
- [ ] Final response includes changed files, commands/checks, risks, rollback, and acceptance status.

---

## 12. Rollback plan

If documentation changes need to be reverted:

```bash
git restore AGENTS.md docs/ai/
```

If `README.md` was updated:

```bash
git restore README.md
```

---

## 13. Expected final report

Return:

```text
Summary:
Files changed:
Tests/checks run:
Assumptions:
Risks/limitations:
Rollback:
Acceptance status: pass / fail / blocked
Next step:
```

---

## 14. Quality gates

### Gate 1 — Structure

```text
pass: all required files exist
revise: files exist but are thin / generic
blocked: repo structure unclear or task touches forbidden areas
```

### Gate 2 — Evidence

```text
pass: docs describe actual repo files and commands
revise: some commands marked TBD
blocked: docs invent commands, modules, tests, or architecture
```

### Gate 3 — Safety

```text
pass: no secrets/logs/generated trash touched
revise: generated files changed but harmless and explained
blocked: secrets, .env, credentials, or private dumps touched
```

### Gate 4 — Codex usability

```text
pass: Codex can understand where to edit, how to test, what not to touch
revise: missing run/test/lint commands
blocked: no entry points, no test path, no forbidden areas
```

---

## 15. Failure modes to avoid

| Failure mode | Why it is dangerous | Control |
|---|---|---|
| Documentation is too large | Codex will drown in context | Keep templates compact |
| Commands are invented | False confidence | Unknown = `TBD` |
| No forbidden areas | Secrets/logs may be touched | Add explicit forbidden block |
| No quality gates | Pretty diff without validation | Add `QUALITY_GATES.md` |
| MCP/RAG/vector DB added too early | Premature architecture | Explicit non-goal |
| No rollback | Risky to merge | Rollback note required |
| Source code changed | Scope violation | Documentation-only task |
| Generated files edited | Dirty repo / unstable diffs | Mark generated areas as do-not-edit |

---

## 16. Handoff

```text
From: AI Operator
To: Codex

Task type:
documentation / repo context contract

Objective:
Implement AI Context Contract files in one concrete repo using this SPEC.

Inputs:
- this SPEC
- actual repository files
- existing README/docs/package files

Constraints:
- minimal diff
- no production code changes
- no secrets
- no raw logs
- no generated trash
- no MCP/RAG/vector DB at this stage

Expected outputs:
- created/updated context files
- final Codex report
- tests/checks result
- residual risks
- rollback note

Acceptance criteria:
- required files exist
- repo entrypoints documented
- commands documented or marked TBD
- quality gates visible
- Codex can propose future changes safely
```

---

## 17. Final instruction to Codex

Implement only the documentation/context-contract layer.

Do not improve the project broadly.

Do not refactor.

Do not change runtime behavior.

Make the repository easier and safer for future AI-assisted engineering work.
