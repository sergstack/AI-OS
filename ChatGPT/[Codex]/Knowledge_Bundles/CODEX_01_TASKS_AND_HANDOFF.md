# [Codex] — Tasks and Handoff

## Purpose

Compact upload artifact for [Codex] covering tasks and handoff.

## Source files

- `ChatGPT/[Codex]/Knowledge/TASK_TEMPLATE.md`
- `ChatGPT/[Codex]/Knowledge/CODEX_HANDOFF_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/AI_OS_REFERENCE.md`
- `ChatGPT/[Codex]/Knowledge/LOCAL_GITHUB_SYNC_WORKFLOW.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

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

## Inputs

- <input files/data/context>

## Files to inspect

- `<path>`
```bash
```

## Rollback plan

<How to revert safely.>

## Final response format

Use the canonical final report schema from `EXECUTION_REPORTING_RULES.md`. Mode-specific reports may be shorter but must include status, evidence, risks, blockers, rollback/next step, and no-auto-merge/PR fields when GitHub is involved.
````


## From: `ChatGPT/[Codex]/Knowledge/CODEX_HANDOFF_WORKFLOW.md`

# Codex Handoff Workflow
## Purpose
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
For real working repositories, start root agent instructions from `../../../Codex APP/CODEX_APP_AGENTS_TEMPLATE.md`.
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
- понять новую AI-концепцию;
- найти supported pattern;
- проверить confidence / evidence;
- связать AI-тренд с работой Сергея;
- найти governance rule;
- отличить supported / weak / unsupported claim.
## Не копировать
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
```bash
git switch <branch>
git rebase main
```
## Before editing
```bash
git status --short --branch
```
## After editing
```bash
git status --short --branch
git diff --stat
git diff --check
git diff -- <allowed_paths>
```
## Commit
```bash
git add <allowed_paths>
git commit -m "<type>: <summary>"
```
## Push and PR
```bash
git push -u origin <branch>
```
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
```bash
git push origin --delete <branch>
```
## Rollback
```bash
git restore <allowed_paths>
```
```bash
git reset --hard HEAD~1
```
```bash
git revert <commit_or_merge_sha>
```
## Hard blockers
These are local GitHub sync blockers in addition to the canonical hard blockers in `AUTONOMY_POLICY.md`.
- remote does not match expected repo;
- local branch has unrelated dirty files;
- pull requires non-fast-forward merge;
- branch contains unrelated commits;
- PR would include files outside allowed scope.
