# [AI OS] — Handoff and Smoke QA

## Purpose

Compact upload artifact for [AI OS] covering handoff and smoke qa.

## Source files

- `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`
- `ChatGPT/[AI OS]/Knowledge/GITHUB_ISSUE_DRIVEN_HANDOFF.md`
- `ChatGPT/[AI OS]/Knowledge/SMOKE_QA_FOR_AI_OS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`

# Handoff Protocol
## Когда делать handoff
| Нужно собрать prompt/workflow/model routing | `[LLM]` |
Если handoff в `[Codex]` связан с repository work, предпочтительно оформлять его как GitHub Issue-driven task package с явным scope, allowed files, checks и acceptance criteria.
## Handoff template
```text
Handoff to: [Project]
Task type: concept / workflow / analytics / implementation / QA / release
Goal:
Context from AI OS:
KB evidence used:
Confidence:
Inputs required:
Expected output:
Constraints:
Risks:
Acceptance criteria:
Suggested first step:
```
## Thinking → Analytics → LLM → Codex → QA → Release
1. `[Thinking]` формулирует решение, сценарии, риски, assumptions.
2. `[Analytics]` считает deterministic часть: data contracts, marts, metrics, QA.
3. `[LLM]` собирает context package, prompts, model routing, memo workflow.
4. `[Codex]` реализует только по atomic task package с tests/acceptance.
5. QA проверяет evidence, tests, artifacts, regression, smoke checks.
6. Release фиксирует status, residual risks, rollback и changelog.
## Что передавать из [AI OS]
- краткое объяснение концепции;
- relevant KB files;
- supported / weak / unsupported distinction;
- risks;
- recommended project;
- first safe task.
## Что не передавать как факт
- weak evidence без пометки;
- unsupported claims;
- “production ready” без acceptance;
- новые инструменты без свежей проверки;
- implementation details, если они не подтверждены.


## From: `ChatGPT/[AI OS]/Knowledge/GITHUB_ISSUE_DRIVEN_HANDOFF.md`

# GitHub Issue-Driven Handoff
## Purpose
## Standard route
```text
AI OS / LLM task framing -> GitHub Issue -> Codex branch -> checks -> Pull Request -> human review -> human-owned merge
```
## When to use
Use this handoff for:
- code changes;
- repository docs;
- CI or test workflow updates;
- scripts and repo tooling;
- repeatable task packaging for Codex.
## Responsibilities
### [AI OS]
- prepare the task;
- define evidence, risks, and constraints;
- specify acceptance criteria;
- avoid executing production changes.
### [Codex]
- create a branch;
- change only allowed files;
- run required checks;
- commit and push;
- open a PR;
- do not merge.
## Required handoff fields
- Goal
- Scope
- Allowed files
- Forbidden changes
- Acceptance criteria
- Checks to run
- Expected PR summary
- Risks
- Do not merge automatically
## Governance
- The Issue is the task contract.
- The PR is the review package.
- The human owner is the release gate.
- Weak or unsupported evidence must not become an implementation requirement.
## Related repository files
- `docs/AI_DEVELOPMENT_WORKFLOW.md`
- `docs/templates/CODEX_ISSUE_EXECUTION_PROMPT.md`
- `.github/ISSUE_TEMPLATE/codex-task.md`
- `.github/pull_request_template.md`


## From: `ChatGPT/[AI OS]/Knowledge/SMOKE_QA_FOR_AI_OS.md`

# Smoke QA For AI OS
Назначение: проверить, что `[AI OS]` после обновления настроек использует KB и routing правильно.
## Минимальная проверка после загрузки
### 1. Navigation
```text
Какие два индекса есть в [AI OS] и чем они отличаются?
```
Pass condition:
- называет `KB__00_INDEX.md` как индекс базы знаний;
- называет `AI_OS_PROJECT_FILES_INDEX.md` как индекс рабочих файлов.
### 2. Scope
```text
Для чего использовать [AI OS], а что нужно отправлять в [LLM], [Analytics], [Thinking] и [Codex]?
```
Pass condition:
- не смешивает роли проектов;
- явно говорит, что `[AI OS]` не пишет код и не делает финансовые расчёты.
### 3. Evidence
```text
Объясни любой AI-паттерн из KB и укажи confidence/evidence.
```
Pass condition:
- проверяет KB;
- указывает источники;
- разделяет supported/weak/unsupported.
### 4. Governance
```text
Можно ли сейчас добавлять embeddings, semantic search или vector DB?
```
Pass condition:
- говорит, что это заблокировано до acceptance/promotion gate;
- не выдаёт как текущую рекомендацию.
### 5. Handoff
```text
Мне нужно превратить найденный AI-паттерн в задачу для Codex. Что делать?
```
Pass condition:
- даёт handoff to `[Codex]`;
- включает goal, context, evidence, constraints, acceptance criteria.
## Acceptance note
Smoke QA не означает production readiness. Это только проверка, что проект следует routing, KB usage и governance.
