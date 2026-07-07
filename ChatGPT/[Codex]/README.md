# [Codex] Project Setup

## Что это

`[Codex]` — engineering command center для Codex / Claude Code: task packages, coding workflows, tests, smoke QA, acceptance, release и rollback.

## Что копировать в Project Instructions

Скопируй содержимое:

```text
ChatGPT/[Codex]/PROJECT_INSTRUCTIONS.md
```

## Что загружать в Knowledge

Default mode: upload the compact bundles listed in:

```text
ChatGPT/[Codex]/Knowledge_Bundles/UPLOAD_LIST.md
```

Do not upload granular `Knowledge/` files together with bundles unless debugging a sync issue.

## Active granular Knowledge sources

- `ACCEPTANCE_CRITERIA.md`
- `AGENTS.md`
- `AI_OS_REFERENCE.md`
- `ANALYTICAL_MEMO_AUTOMATION_WORKFLOW.md`
- `ANALYTICAL_TECHNIQUES_FOR_CODEX.md`
- `BUGFIX_WORKFLOW.md`
- `CLAUDE_CODE_HANDOFF.md`
- `CODEX_HANDOFF_WORKFLOW.md`
- `DATA_PIPELINE_IMPLEMENTATION_WORKFLOW.md`
- `DONE_DEFINITION.md`
- `FAILURE_MODES.md`
- `PROJECT_CONTEXT.md`
- `PROMPT_LIBRARY_CODEX.md`
- `REFACTORING_WORKFLOW.md`
- `RELEASE_CHECKLIST.md`
- `REVIEW_CHECKLIST.md`
- `SMOKE_QA_CHECKLIST.md`
- `SUBAGENT_DECOMPOSITION.md`
- `TASK_TEMPLATE.md`
- `TESTING_WORKFLOW.md`

## Reference-only / not uploaded by default

- `CLAUDE.md` — legacy/reference only; `AGENTS.md` is canonical.
- `KESTRA_AUTOMATION_STANDARD_REFERENCE.md` — reference only; Kestra is not an active runtime standard.

## What not to upload to ChatGPT Project Knowledge

Do not upload:

- top-level `../../Codex APP/` executor-layer files
- reference-only granular Knowledge files unless explicitly debugging
- `.gitkeep`
- secrets / `.env` / credentials
- raw transcripts
- source cards
- chunks
- temp files
- logs
- embeddings
- vector DB
- web UI artifacts

## Codex APP compatibility

Task packages produced in this ChatGPT Project should be executable by `Codex APP`.
Use `../../Codex APP/CODEX_APP_TASK_PACKAGE_CONTRACT.md` and `../../Codex APP/CODEX_APP_INTAKE_GATE.md` as the receiving-side contract.

## Что не делать

Не давать Codex размытые задачи. Не разрешать изменения без scope, tests и acceptance criteria.
