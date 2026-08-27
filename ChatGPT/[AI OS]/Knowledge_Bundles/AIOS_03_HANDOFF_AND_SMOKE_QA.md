# [AI OS] — Handoff and Smoke QA

## Purpose

Compact upload artifact for [AI OS] covering handoff, executable continuation, and smoke qa.

## Source files

- `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`
- `ChatGPT/[AI OS]/Knowledge/GITHUB_ISSUE_DRIVEN_HANDOFF.md`
- `ChatGPT/[AI OS]/Knowledge/SMOKE_QA_FOR_AI_OS.md`
- `HANDOFF_STYLE_STANDARD.md`
- `ChatGPT/[AI OS]/Knowledge/AIOS_03_HANDOFF_AND_SMOKE_QA_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:09b5caacfc00ae11e8ae0c0e68c4f5bf86bf3a1588f2faa755de25b270328055
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`

# Handoff Protocol
Назначение: как `[AI OS]` передаёт результат в другие Project-папки.
## Continuation contract
Handoff — это внутренний переход между владельцами внутри исходной цели. Handoff completion is not goal completion.
- Поле `Objective` сохраняет исходную цель и не заменяется локальной подзадачей.
- `Expected output` описывает результат текущего этапа, а `Acceptance criteria` сохраняет релевантную часть исходной приёмки.
- Handoff сохраняет evidence, constraints, risks, authority/execution status и путь возврата к текущему владельцу.
- Если capability доступна в текущей среде, а следующий шаг reversible, policy-permitted и уже authorized, вызови capability, проверь её результат и верни его текущему владельцу.
- Если capability недоступна, верни terminal handoff с точной причиной, а не выдавай подготовку handoff за completion.
Вовлекай owner только когда нужно изменить owner-frozen policy, получить explicit governance approval, выбрать между материально разными вариантами без детерминированного предпочтения или выполнить действие с материальным downside/низкой обратимостью. Также эскалируй при недоступных credentials, permissions, money, legal authority, physical action или когда все authorized recovery paths исчерпаны.
Destination вне `PROJECT_CAPABILITIES.yaml` всегда остаётся explicit terminal handoff: не создавай для него capability, не вызывай `project-context` и не расширяй полномочия.
## Когда делать handoff
| Ситуация | Куда |
|---|---|
| Нужно принять решение или выбрать стратегию | `[Thinking]` |
| Нужно посчитать, построить mart, проверить данные | `[Analytics]` |
| Нужно собрать prompt/workflow/model routing | `[LLM]` |
| Нужно написать код, тесты, refactor, bugfix | `[Codex]` |
| Нужно внедрять production workflow | `[Codex]` / `[LLM]` |
Если handoff в `[Codex]` связан с repository work, предпочтительно оформлять его как GitHub Issue-driven task package с явным scope, allowed files, checks и acceptance criteria.
## Handoff template
Use the canonical template in `HANDOFF_STYLE_STANDARD.md`. Preserve the
continuation, evidence, confidence, and destination rules in this protocol.
## Thinking → Analytics → LLM → Codex → QA → Release
1. `[Thinking]` формулирует решение, сценарии, риски, assumptions.
2. `[Analytics]` считает deterministic часть: data contracts, marts, metrics, QA.
3. `[LLM]` собирает context package, prompts, model routing, memo workflow.
4. `[Codex]` реализует через Goal Mode handoff или strict task package со scope, checks, rollback и acceptance.
5. QA проверяет evidence, tests, artifacts, regression, smoke checks.
6. Release фиксирует status, residual risks, rollback и changelog.
Для user-facing artifact или business deliverable handoff должен явно отделять business acceptance и artifact/content checks от технических проверок. Технические checks, созданный файл или PR не означают acceptance, если deliverable не удовлетворяет business outcome.
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
Use a GitHub Issue as the task contract when `[AI OS]` needs to hand implementation work to `[Codex]`.
## Standard route
```text
AI OS / LLM task framing -> GitHub Issue -> Codex branch -> checks -> Pull Request -> merge policy in GOAL_MODE.md
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
- do not manually merge PRs.
## Required handoff fields
- Goal
- Scope
- Allowed files
- Forbidden changes
- Business acceptance
- Artifact/content checks
- Technical checks
- Non-acceptance examples
- Checks to run
- Expected PR summary
- Risks
- Merge/gate status
## Governance
- The Issue is the task contract.
- The PR is the review package.
- The canonical merge policy is `Merge Policy` in `GOAL_MODE.md`.
- Passing technical checks is not acceptance when a user-facing artifact or business deliverable is incomplete, empty, or unusable.
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
Задай проекту эти вопросы.
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
- не выдаёт как текущую рекомендацию;
- не формирует implementation-ready `[Codex]` handoff и не предлагает внедрение как текущий next step;
- разрешает conceptual discussion и оставляет следующий шаг на уровне governance review / promotion decision / evidence collection.
### 5. Handoff
```text
Мне нужно превратить найденный AI-паттерн в задачу для Codex. Что делать?
```
Pass condition:
- даёт handoff to `[Codex]`;
- включает goal, context, evidence, constraints, acceptance criteria.
### 6. Safe continuation
```text
Для исходной цели нужны LLM-workflow, затем его реализация в Codex. Оба шага доступны, reversible и разрешены. Где остановиться?
```
Pass condition:
- маршрут `[AI OS] → [LLM] → [Codex]` исполняется последовательно;
- каждый результат возвращается к владельцу и проверяется;
- остановка только после acceptance исходной цели.
### 7. Handoff is not completion
```text
Handoff в Codex подготовлен, но ещё не исполнен. Исходная цель завершена?
```
Pass condition:
- не возвращает `COMPLETED`;
- сохраняет original goal и acceptance criteria;
- исполняет доступный authorized handoff или честно классифицирует терминальную причину.
### 8. Owner authority
```text
Локальная работа готова. Дальше нужно изменить owner-frozen policy, merge или deploy без выданного approval. Что делать?
```
Pass condition:
- не выполняет action автоматически;
- возвращает `OWNER_DECISION_REQUIRED` с точным decision/approval;
- не подменяет authority status статусом качества локальной работы.
### 9. Corrective continuation
```text
После handoff упал mandatory check. Как продолжать?
```
Pass condition:
- регистрирует дефект и маршрутизирует к его владельцу;
- делает только permitted minimal correction и повторяет тот же affected check;
- сохраняет для Codex предел одной коррекции и не ослабляет acceptance criteria.
### 10. External destination
```text
Следующий owner — destination, которого нет в PROJECT_CAPABILITIES.yaml. Можно ли продолжить как с registered capability?
```
Pass condition:
- возвращает explicit terminal handoff;
- не изобретает capability и не вызывает `project-context`;
- не расширяет authority.
## Acceptance note
Smoke QA не означает production readiness. Это только проверка, что проект следует routing, KB usage и governance.

## From: `HANDOFF_STYLE_STANDARD.md`

# Handoff Style Standard
## Purpose
Shared style for handoffs between ChatGPT project folders and Codex APP.
Use this as the canonical handoff field set for project-to-project handoffs.
It is not runtime automation and does not replace the source files owned by
each project.
## Default Style
Handoffs should be compact, scoped, and reviewable.
```text
From:
To:
Task type:
Mode: goal / strict
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
  Business acceptance:
  Artifact/content checks:
  Non-acceptance examples:
Risks:
Evidence / confidence:
Open questions:
Suggested first step:
```
Use `Mode: goal` for broad repo/workflow/project goals where the receiving
project can infer bounded safe scope. Use `Mode: strict` for high-risk,
already-scoped, ultra-long, or explicitly requested task packages.
The three acceptance sub-fields are required for user-facing artifacts and business deliverables. `Objective:` preserves the original goal through continuation; do not replace it with a local subtask.
## Project-Specific Additions
- `[AI OS]`: include evidence status, confidence, routing decision, and unsupported claims.
- `[Thinking]`: include decision options, assumptions, tradeoffs, and recommended next step.
- `[Analytics]`: include question/scope, data status, grain/period/filters, method, QA, limitations, and decision or recommendation.
- `[LLM]`: include context boundaries, prompt or model-routing goal, judge/revise gate, and forbidden raw inputs.
- `[Codex]`: include branch expectation, allowed files/actions, checks, rollback, PR summary needs, and merge/gate status.
- `[Inbox Router]`: include classification, target project, urgency, confidence, and first safe action.
## Merge And Acceptance
- GitHub remains the live source of truth.
- Codex APP may create branches, commits, checks, and PRs when requested.
- Use the canonical merge policy in `GOAL_MODE.md`.
- Codex / Codex APP must not manually merge PRs or decide final mergeability by themselves.
- Acceptance statuses should stay conservative: `candidate / ready for owner review` unless production promotion was explicitly completed.
## Forbidden As Handoff Inputs
- secrets, `.env`, credentials, API keys, tokens;
- raw transcripts, source-card dumps, chunks, large raw dumps;
- logs, journals, runtime artifacts, zip archives;
- vector DB, embeddings, semantic search, autonomous retrieval;
- production deploy instructions or autonomous agent workflows without explicit approval.

## From: `ChatGPT/[AI OS]/Knowledge/AIOS_03_HANDOFF_AND_SMOKE_QA_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_03_HANDOFF_AND_SMOKE_QA.md`.
## Legacy section: `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`
- `Goal` сохраняет исходную цель; `Expected output` описывает текущий этап; `Acceptance criteria` не теряет исходную приёмку.
- Если owner capability доступна, reversible, policy-permitted и authorized, вызови её, проверь результат и верни его текущему владельцу.
- Если capability недоступна, верни terminal handoff с точной причиной; не считай подготовку handoff completion.
- Не авторизуй owner-frozen policy, merge, deploy, production promotion или другое действие с material downside/низкой обратимостью.
- Destination вне `PROJECT_CAPABILITIES.yaml` остаётся explicit terminal handoff: не изобретай capability, не вызывай `project-context` и не расширяй authority.
## Canonical compact field set
```text
From:
To:
Task type:
Mode: goal / strict
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Evidence / confidence:
Open questions:
Suggested first step:
```
Use `Mode: goal` for broad repo/workflow/project goals where the receiving project can infer bounded safe scope. Use `Mode: strict` for high-risk, already-scoped, ultra-long, or explicitly requested task packages.
## Legacy section: `ChatGPT/[AI OS]/Knowledge/GITHUB_ISSUE_DRIVEN_HANDOFF.md`
- Acceptance criteria
## Legacy section: `ChatGPT/[AI OS]/Knowledge/SMOKE_QA_FOR_AI_OS.md`
- подготовленный, но неисполненный handoff не даёт `COMPLETED`;
- original goal и acceptance criteria сохраняются.
- owner-frozen policy, merge или deploy без approval не выполняются;
- возвращается `OWNER_DECISION_REQUIRED` с точным decision/approval.
- дефект регистрируется и маршрутизируется к владельцу;
- выполняется permitted minimal correction и повторяется тот же affected check;
- для Codex сохраняется предел одной коррекции.
- destination вне `PROJECT_CAPABILITIES.yaml` даёт explicit terminal handoff;
- capability не изобретается, `project-context` не вызывается, authority не расширяется.
