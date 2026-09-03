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

- `../../docs/standards/EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md` — shared engineering/Codex standard for controlled cleanup/refactor of existing working scripts.
- `ACCEPTANCE_CRITERIA.md`
- `AGENTS.md`
- `AI_OS_REFERENCE.md`
- `ANALYTICAL_MEMO_AUTOMATION_WORKFLOW.md`
- `ANALYTICAL_TECHNIQUES_FOR_CODEX.md`
- `AUTONOMY_POLICY.md`
- `BUGFIX_WORKFLOW.md`
- `CLAUDE_CODE_HANDOFF.md`
- `CODEX_HANDOFF_WORKFLOW.md`
- `CODEX_LONG_RUN_PLAYBOOK.md`
- `CODEX_TASK_EXAMPLES.md`
- `CODEX_TDD_WORKFLOW.md`
- `DATA_PIPELINE_IMPLEMENTATION_WORKFLOW.md`
- `DONE_DEFINITION.md`
- `EVALS_FOR_CODEX_WORKFLOW.md`
- `EXECUTION_REPORTING_RULES.md`
- `FAILURE_MODES.md`
- `LOCAL_GITHUB_SYNC_WORKFLOW.md`
- `PROJECT_CONTEXT.md`
- `PROMPT_LIBRARY_CODEX.md`
- `PR_JUDGE_CHECKLIST.md`
- `REFACTORING_WORKFLOW.md`
- `RELEASE_CHECKLIST.md`
- `REVIEW_CHECKLIST.md`
- `SMOKE_QA_CHECKLIST.md`
- `SUBAGENT_DECOMPOSITION.md`
- `TASK_TEMPLATE.md`
- `TESTING_WORKFLOW.md`
- `WORKTREE_AND_PARALLEL_AGENT_POLICY.md`

## Bundle semantic migration sources

- `CODEX_01_TASKS_AND_HANDOFF_BUNDLE_SEMANTICS.md`
- `CODEX_02_EXECUTION_AUTONOMY_REPORTING_BUNDLE_SEMANTICS.md`
- `CODEX_04_IMPLEMENTATION_WORKFLOWS_BUNDLE_SEMANTICS.md`
- `CODEX_06_AI_CODING_DISCIPLINE_BUNDLE_SEMANTICS.md`

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

For complex/high-risk GitHub issue sequences, cite `../../docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md` as the parent/child dependency gate reference. Do not use it to make child issues mandatory for simple Goal Mode tasks.

For existing working script or pipeline cleanup/refactor, cite `../../docs/standards/EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`; `[Codex]` applies it operationally after current behavior, output contract, and safety tests are pinned down.

## Что не делать

Не давать Codex размытые задачи. Не разрешать изменения без scope, tests и acceptance criteria.
