# Codex APP Runbook

## Purpose

How Sergey runs repo/file tasks through Codex APP safely.

## Profiles

| Profile | Use for |
|---|---|
| `safe-docs` | docs/config only |
| `safe-code` | scoped code fixes with clear tests |
| `long-run-local` | longer local tasks with clear checks |
| `ultra-long-local` | multi-batch tasks with complete task package |
| `review-only` | read-only review |

Use `CODEX_CONFIG_PROFILES.md` as the source of truth for profile details.

## Default Choice

Use `safe-docs` for AI-OS repo settings unless the task explicitly requires code.

## Before Run

- repo selected;
- branch target clear;
- goal clear;
- forbidden actions visible;
- checks listed;
- rollback expected.

## During Run

- inspect first;
- plan only as much as needed;
- edit minimal files;
- run checks;
- report blockers honestly.

## Stop Conditions

Stop if:

- secrets, tokens, credentials, or `.env` values are needed;
- production, runtime, deploy, or migration work appears;
- formulas, business logic, schemas, output contracts, or column names may change;
- governed KB content changes outside scope;
- no meaningful validation is possible;
- destructive action is required.

## Final Report

Use the canonical Codex final report schema from `ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`; include commit and PR URL when GitHub sync is part of the task.

For task-package requirements, use `CODEX_APP_TASK_PACKAGE_CONTRACT.md`.
