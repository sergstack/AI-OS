# Codex APP

## Purpose

This folder contains local operating settings, templates and checklists for using Codex App / Codex Web / Codex CLI / IDE extension in Sergey’s AI OS ecosystem.

## Important separation

`[Codex]` = ChatGPT Project for preparing implementation task packages.

`Codex APP` = local/app configuration pack for the actual Codex application and coding-agent workflow.

Do not mix these folders.

## Default workflow

```text
Inspect → Plan → Implement → Test → Review → Report
```

## Use this folder for

- Codex App setup;
- Codex CLI / IDE usage rules;
- GitHub branch and PR workflow;
- AGENTS.md templates;
- task templates;
- review checklists;
- acceptance / rollback templates.

## Task package contract

Use `CODEX_APP_TASK_PACKAGE_CONTRACT.md` as the receiving contract for implementation tasks prepared in `ChatGPT/[Codex]`.

## Do not use this folder for

- ChatGPT Project instructions;
- AI OS governed KB;
- raw transcripts;
- analytics marts;
- secrets;
- production runtime artifacts.
