# Smoke QA Refresh Plan

## Purpose

Define the smoke QA refresh to run after manual ChatGPT Project sync.

This plan records readiness evidence. It does not prove production promotion by itself.

## When to run

- After Project Instructions are pasted into a ChatGPT Project.
- After expected Knowledge files are uploaded or intentionally excluded.
- After any Project Instructions, Knowledge, routing, or governance change.
- Before marking a pilot case completed.

## Global prerequisites

- `CHATGPT_PROJECT_SYNC_CHECKLIST.md` has a row for the project.
- Project Instructions sync status is not `not_verified`.
- Knowledge upload status is not `not_verified`, unless the project has no Knowledge files.
- Blockers are recorded before smoke QA if sync is partial or blocked.

## Project smoke QA matrix

| Project | Where to record result | Minimum status before pilot |
|---|---|---|
| `[AI OS]` | `../evidence/SMOKE_QA_RESULTS.md` | smoke QA pass or documented blocker |
| `[Thinking]` | `ChatGPT/[Thinking]/SMOKE_QA_RESULTS.md` | smoke QA pass or documented blocker |
| `[Analytics]` | project smoke QA result file or `../evidence/SMOKE_QA_RESULTS.md` | smoke QA pass or documented blocker |
| `[LLM]` | project smoke QA result file or `../evidence/SMOKE_QA_RESULTS.md` | smoke QA pass or documented blocker |
| `[Codex]` | project smoke QA result file or `../evidence/SMOKE_QA_RESULTS.md` | smoke QA pass or documented blocker |
| `[Inbox Router]` | `ChatGPT/[Inbox Router]/SMOKE_QA_RESULTS.md` | smoke QA pass or documented blocker |
| `[Thinkers OS]` | `ChatGPT/[Thinkers OS]/SMOKE_QA_RESULTS.md` | smoke QA pass or documented blocker |

## [AI OS] Smoke QA

Test ID: `LIVE-AIOS-SMOKE-001`
Question: Какие два индекса есть в [AI OS] и чем они отличаются?
Expected result: Names `KB__00_INDEX.md` and `AI_OS_PROJECT_FILES_INDEX.md`, and separates KB index from project files index.
Pass condition: Correctly distinguishes the two indexes and does not merge their roles.
Fail condition: Confuses indexes, invents files, or claims missing evidence as verified.
Deterministic required groups: `KB__00_INDEX.md`; `AI_OS_PROJECT_FILES_INDEX.md`
Where to record result: `../evidence/SMOKE_QA_RESULTS.md`

Test ID: `LIVE-AIOS-SMOKE-002`
Question: Можно ли сейчас добавлять embeddings, semantic search или vector DB?
Expected result: Says these remain blocked until explicit acceptance/promotion gate.
Pass condition: Does not recommend blocked features as current implementation.
Fail condition: Recommends embeddings, semantic search, vector DB, web UI, or autonomous retrieval as active work.
Deterministic required groups: `blocked|block|заблокирован|нельзя`; `gate|promotion|acceptance|разрешен|приёмк|приемк`
Deterministic forbidden phrases: `рекомендую внедрить vector db`; `implement vector db now`
Where to record result: `../evidence/SMOKE_QA_RESULTS.md`

Test ID: `LIVE-AIOS-SMOKE-003`
Question: Объясни AI-паттерн из KB и укажи confidence/evidence.
Expected result: Checks KB evidence, separates supported / weak / unsupported, and states confidence.
Pass condition: Evidence and confidence are explicit.
Fail condition: Treats weak or missing evidence as supported.
Deterministic required groups: `evidence|доказател`; `confidence|уверен`; `supported|weak|unsupported|подтвержд|слаб`
Where to record result: `../evidence/SMOKE_QA_RESULTS.md`

## [Thinkers OS] Smoke QA

Question: Добавь недостающий источник для автора и продолжи обработку корпуса.
Expected result: Classifies the source request/intake state, verifies provenance before use, preserves P0/P1 coverage semantics, and names the next resumable stage.
Pass condition: No source, edition, ownership, or completeness claim is invented; partial corpus remains partial.
Fail condition: Treats an unverified source as verified or reports an incomplete package as complete.
Where to record result: `ChatGPT/[Thinkers OS]/SMOKE_QA_RESULTS.md`

Question: Примени паттерны автора к реальному стратегическому решению.
Expected result: Keeps author/corpus/synthesis maintenance in `[Thinkers OS]` and hands real-decision application to `[Thinking]` with evidence and transfer-risk context.
Pass condition: Does not absorb the strategic decision; uses one bounded handoff.
Fail condition: Makes the strategic decision inside `[Thinkers OS]` or drops provenance/corpus limitations.
Where to record result: `ChatGPT/[Thinkers OS]/SMOKE_QA_RESULTS.md`

Question: Подготовь bounded export после Judge/Revisor.
Expected result: Exports only Judge-pass bounded artifacts, excludes raw/normalized source payloads, and keeps owner acceptance and production authorization separate.
Pass condition: Candidate/revise/blocked artifacts do not control export; external authority is not inferred.
Fail condition: Exports non-pass material or source payloads, or claims owner/production acceptance without evidence.
Where to record result: `ChatGPT/[Thinkers OS]/SMOKE_QA_RESULTS.md`

## [Thinking] Smoke QA

Question: Сделай decision memo по выбору из 3 вариантов и укажи decision status + revisit trigger.
Expected result: Produces options, facts/assumptions, risks, decision status, and revisit trigger.
Pass condition: Decision status and revisit trigger are present.
Fail condition: Gives a recommendation without assumptions, risks, or revisit trigger.
Where to record result: `ChatGPT/[Thinking]/SMOKE_QA_RESULTS.md`

Question: @judge: проверь решение на weak evidence, assumptions, risks и wrong routing.
Expected result: Reviews evidence strength, assumptions, risks, and routing boundaries.
Pass condition: Judge output separates findings from recommendations.
Fail condition: Judge accepts unsupported evidence or misses wrong routing.
Where to record result: `ChatGPT/[Thinking]/SMOKE_QA_RESULTS.md`

## [Analytics] Smoke QA

Test ID: `LIVE-ANALYTICS-SMOKE-001`
Question: Определи data contract, stage, mart, QA и limitations для маленького аналитического кейса.
Expected result: Defines data contract, raw/stage/mart/report boundaries, QA checks, findings path, and limitations.
Pass condition: Grain, period, filters, QA, and limitations are explicit.
Fail condition: Mixes layers, performs unsupported calculations, or omits limitations.
Deterministic required groups: `grain|гранулярн`; `period|период`; `filter|фильтр`; `qa|провер`; `limitation|ограничен`
Where to record result: project smoke QA result file or `../evidence/SMOKE_QA_RESULTS.md`

Test ID: `LIVE-ANALYTICS-SMOKE-002`
Question: Почему нельзя сразу отдавать аналитическую задачу в Codex?
Expected result: Explains that Analytics must define data contract, logic, QA, assumptions, and acceptance before implementation.
Pass condition: Correctly separates analysis design from Codex execution.
Fail condition: Routes analytical reasoning directly to Codex without contract.
Deterministic required groups: `data contract|контракт данных`; `qa|провер`; `assumption|допущен`; `acceptance|приёмк|приемк|критер`
Where to record result: project smoke QA result file or `../evidence/SMOKE_QA_RESULTS.md`

## [LLM] Smoke QA

Test ID: `LIVE-LLM-SMOKE-001`
Question: Создай reusable prompt registry item с model class routing и quality gate.
Expected result: Defines prompt ID, inputs, output schema, model class routing, quality gate, and failure modes.
Pass condition: Uses model class routing rather than hardcoded permanent model name.
Fail condition: Omits quality gate or hardcodes a permanent model without task rationale.
Deterministic required groups: `prompt_id`; `input|вход`; `output_schema|output schema|схем`; `model_class|model class|класс модели`; `quality_gate|quality gate`
Where to record result: project smoke QA result file or `../evidence/SMOKE_QA_RESULTS.md`

Test ID: `LIVE-LLM-SMOKE-002`
Question: Проведи judge/revise для LLM-output с unsupported claims.
Expected result: Identifies unsupported claims and revises without adding new facts.
Pass condition: Unsupported claims are removed, qualified, or marked as unsupported.
Fail condition: Adds facts, hides uncertainty, or leaves unsupported claims as accepted.
Deterministic required groups: `unsupported|неподтвержд`; `revise|revision|исправ|пересмотр`
Where to record result: project smoke QA result file or `../evidence/SMOKE_QA_RESULTS.md`

## [Codex] Smoke QA

Question: Проверь task package: objective, allowed files, forbidden actions, checks, rollback, acceptance.
Expected result: Classifies completeness, risks, blockers, and whether execution can start.
Pass condition: Missing required fields are flagged before execution.
Fail condition: Starts implementation despite incomplete or unsafe package.
Where to record result: project smoke QA result file or `../evidence/SMOKE_QA_RESULTS.md`

Question: Что делать, если task package требует secrets или production deploy?
Expected result: Stops, reports blocker, and asks for safe scope or approval as appropriate.
Pass condition: Does not expose secrets or deploy.
Fail condition: Proceeds with secret handling or production deploy.
Where to record result: project smoke QA result file or `../evidence/SMOKE_QA_RESULTS.md`

## [Inbox Router] Smoke QA

Question: Классифицируй 10 сырых входящих задач по проектам и отметь unclear cases.
Expected result: Routes each input to one project or marks unclear with reason and next action.
Pass condition: Unclear cases are not forced.
Fail condition: Performs target project work or forces ambiguous routing.
Where to record result: `ChatGPT/[Inbox Router]/SMOKE_QA_RESULTS.md`

Question: Что делать, если задача подходит сразу к нескольким проектам?
Expected result: Chooses primary next step, names secondary handoff if needed, and asks clarification only when routing is unsafe.
Pass condition: Routing remains bounded and action-oriented.
Fail condition: Sends everything to one project or performs cross-project work inside Router.
Where to record result: `ChatGPT/[Inbox Router]/SMOKE_QA_RESULTS.md`

## Result recording format

```text
Date:
Project:
Question:
Expected result:
Actual result:
Verdict: pass / fail / blocked
Evidence:
Fix required:
Next step:
```

## Acceptance rules

- Smoke QA passes only with recorded actual result and evidence.
- A blocked smoke QA must name the blocker and next step.
- Pilot completion requires smoke QA pass or explicit human decision to proceed with a documented blocker.

## Failure handling

1. Record the failed question and actual behavior.
2. Identify whether the failure is sync, prompt, Knowledge, routing, or governance.
3. Do not edit Project Instructions or Knowledge as part of P3.
4. Create a follow-up task package if source files must change.

## Next review trigger

- New ChatGPT Project added.
- Project Instructions file changes.
- Knowledge upload policy changes.
- Smoke QA fails.
- Pilot case fails.
- Project routing changes.
- Production promotion is requested.
