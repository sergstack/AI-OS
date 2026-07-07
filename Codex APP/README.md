# Codex APP

## Purpose

This folder contains local operating settings, templates and checklists for using Codex App / Codex Web / Codex CLI / IDE extension in Sergey’s AI OS ecosystem.

## Important separation

`[Codex]` = ChatGPT Project for preparing implementation task packages.

`Codex APP` = local/app configuration pack for the actual Codex application and coding-agent workflow.

Do not mix these folders.

## Goal Mode boundary

Sergey may start in ChatGPT with a broad goal.

Goal Mode is build-first. `ChatGPT/[Codex]`, `[LLM]`, or a Goal Mode GitHub issue should help Codex inspect relevant files, infer bounded safe scope, create or use a non-main branch, implement the smallest useful working version, run checks, fix in-scope failures when safe, and report evidence for human review.

`Codex APP` is the executor layer. It should receive or safely infer an executor-ready package before editing, but soft uncertainty should not become a planning-only response.

Do not require Sergey to manually write atomic task fields. Goal Mode removes user-facing bureaucracy, not execution safety.

## Default workflow

```text
Inspect → Scope → Implement → Test → Review → Report
```

For long tasks, use:

```text
Intake gate → Decompose → Batch execute → Checkpoint → Validate → Safe retry once → Report
```

## Use this folder for

- Codex App setup;
- Codex CLI / IDE usage rules;
- GitHub branch and PR workflow;
- AGENTS.md templates;
- task templates;
- review checklists;
- acceptance / rollback templates;
- ultra-long local run protocol and checkpoint discipline.

## Core files

- `CODEX_APP_SETUP.md` — safe setup defaults.
- `CODEX_APP_OPERATING_MODES.md` — execution modes and stop conditions.
- `CODEX_APP_USAGE_POLICY.md` — cost, time, scope and autonomy rules.
- `CODEX_APP_TASK_PACKAGE_CONTRACT.md` — receiving contract for implementation tasks prepared in `ChatGPT/[Codex]`.
- `CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md` — protocol for multi-batch long-running work.
- `CODEX_CONFIG_PROFILES.md` — non-secret execution profiles.
- `CODEX_APP_AGENTS_TEMPLATE.md` — reusable root `AGENTS.md` template for real repos.
- `templates/ULTRA_LONG_TASK_PACKAGE.md` — task package template for long multi-batch execution.

## Do not use this folder for

- ChatGPT Project instructions;
- AI OS governed KB;
- raw transcripts;
- analytics marts;
- secrets;
- production runtime artifacts.
