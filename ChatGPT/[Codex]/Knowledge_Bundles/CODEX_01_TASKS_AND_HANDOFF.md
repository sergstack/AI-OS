# [Codex] — Tasks and Handoff

## Purpose

Compact upload artifact for [Codex] covering tasks and handoff.

## Source files

- `ChatGPT/[Codex]/Knowledge/TASK_TEMPLATE.md`
- `ChatGPT/[Codex]/Knowledge/CODEX_HANDOFF_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/AI_OS_REFERENCE.md`
- `ChatGPT/[Codex]/Knowledge/LOCAL_GITHUB_SYNC_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/CODEX_01_TASKS_AND_HANDOFF_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:1e7a7e748b3faa02b8df668eb65690e45ae8b26987820ecd0bb3eb8e723a8b51
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Codex]/Knowledge/TASK_TEMPLATE.md`

# Task Template for Codex
````markdown
# Codex Task
## Context
<What project/repo/feature this task belongs to.>
## Objective
<One clear outcome.>
## Autonomy mode
long-run / normal / inspect-only
Default:
Codex may continue on safe reversible assumptions and must stop only on canonical hard blockers from `AUTONOMY_POLICY.md`.
For normal bounded repo work, the task may say `Use Goal Mode Contract` instead of repeating the full autonomy, execution, forbidden-action, reporting, PR/merge-gate posture, and no-deletion-without-quarantine rules.
## Inputs
- <input files/data/context>
## Files to inspect
- `<path>`
## Files allowed to modify
- `<path>`
## Forbidden actions
- Do not modify secrets or `.env`.
- Do not change business logic unless explicitly stated.
- Do not remove validation/QA checks.
- Do not change output schemas unless explicitly stated.
- Do not add unrelated dependencies.
## Expected outputs
- <files/artifacts/behavior>
## Acceptance criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
## Tests / smoke checks
```bash
<commands>
```
## Rollback plan
<How to revert safely.>
## Final response format
Use the canonical final report schema from `EXECUTION_REPORTING_RULES.md`. Mode-specific reports may be shorter but must include status, evidence, risks, blockers, rollback/next step, and PR/merge-gate fields when GitHub is involved.
````

## From: `ChatGPT/[Codex]/Knowledge/CODEX_HANDOFF_WORKFLOW.md`

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

## From: `ChatGPT/[Codex]/Knowledge/AI_OS_REFERENCE.md`

# AI OS Reference
## Purpose
Этот проект не содержит полную AI OS KB. `[AI OS]` уже существует и хранит governed knowledge base.
Используй `[AI OS]`, когда нужно:
- понять новую AI-концепцию;
- найти supported pattern;
- проверить confidence / evidence;
- связать AI-тренд с работой Сергея;
- найти governance rule;
- отличить supported / weak / unsupported claim.
## Не копировать
Не копировать в этот проект:
- весь compact KB package;
- raw transcripts;
- source cards;
- chunks;
- temp files;
- logs;
- embeddings;
- vector DB;
- web UI artifacts.
## Как ссылаться
Когда нужен KB-backed вывод, формулируй handoff в `[AI OS]` так:
```text
Используй AI OS KB. Найди supported/weak/unsupported evidence по теме:
<topic>
Верни:
- найдено в KB: да/нет/частично
- sources
- confidence
- supported claims
- weak/unsupported claims
- practical use for Sergey
```
## Rule
AI OS даёт evidence и patterns. Текущий проект применяет их в своей области, не смешивая роли.

## From: `ChatGPT/[Codex]/Knowledge/LOCAL_GITHUB_SYNC_WORKFLOW.md`

# Local GitHub Sync Workflow
## Purpose
Keep local repo, branch, commit, pushed branch, and PR aligned.
## Preconditions
- local path is known;
- remote is correct;
- working tree is clean or dirty files are understood;
- task package defines allowed files;
- branch name is defined.
## Standard flow
```bash
cd "<LOCAL_REPO>"
git remote -v
git status --short --branch
git fetch origin
git switch main
git pull --ff-only origin main
git switch -c <branch>
```
If branch exists:
```bash
git switch <branch>
git rebase main
```
## Before editing
```bash
git status --short --branch
```
Stop if dirty files are outside allowed scope.
## After editing
```bash
git status --short --branch
git diff --stat
git diff --check
git diff -- <allowed_paths>
```
Run task-specific tests/checks.
## Commit
```bash
git add <allowed_paths>
git commit -m "<type>: <summary>"
```
## Push and PR
```bash
git push -u origin <branch>
```
Create PR with:
- summary;
- changed files;
- checks run;
- assumptions;
- risks;
- rollback;
- acceptance status.
## After merge
```bash
git switch main
git pull --ff-only origin main
git branch -d <branch>
```
If remote branch remains:
```bash
git push origin --delete <branch>
```
## Rollback
Before any rollback:
```bash
git status
```
For local file restoration before commit:
```bash
git restore --source=HEAD -- <allowed_paths>
```
For pushed commits or merged PRs:
```bash
git revert <commit_or_merge_sha>
```
Do not use destructive rollback commands as the default. Commands such as
`git reset --hard` require explicit human confirmation and a clean
understanding of what uncommitted work would be lost.
## Hard blockers
These are local GitHub sync blockers in addition to the canonical hard blockers in `AUTONOMY_POLICY.md`. Stop if:
- remote does not match expected repo;
- local branch has unrelated dirty files;
- pull requires non-fast-forward merge;
- branch contains unrelated commits;
- PR would include files outside allowed scope.

## From: `ChatGPT/[Codex]/Knowledge/CODEX_01_TASKS_AND_HANDOFF_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Codex]/Knowledge_Bundles/CODEX_01_TASKS_AND_HANDOFF.md`.
## Legacy section: `ChatGPT/[Codex]/Knowledge/LOCAL_GITHUB_SYNC_WORKFLOW.md`
Do not use destructive rollback commands as the default. Commands such as `git reset --hard` require explicit human confirmation and a clean understanding of what uncommitted work would be lost.
These are local GitHub sync blockers in addition to the canonical hard blockers in `AUTONOMY_POLICY.md`.
