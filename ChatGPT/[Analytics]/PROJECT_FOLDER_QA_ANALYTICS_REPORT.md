# Project Folder QA Report — [Analytics]

Project folder: `[Analytics]`

Issue: GitHub #64, targeted regression check for updated Analytics project folder.

Review date: 2026-07-06

Verdict: pass

## Files Checked

Repository-wide and cross-project surfaces:

- `AGENTS.md`
- `COMMAND_SURFACE.md`
- `GOAL_PACKS.md`
- `docs/PROJECT_ROUTING.md`
- `.github/ISSUE_TEMPLATE/goal.md`
- `.github/ISSUE_TEMPLATE/codex-task.md`
- `.github/pull_request_template.md`

Analytics package definition and root files:

- `ChatGPT/[Analytics]/package_manifest.json`
- `ChatGPT/[Analytics]/README.md`
- `ChatGPT/[Analytics]/PROJECT_INSTRUCTIONS.md`

Analytics Knowledge files:

- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_WORKFLOW.md`
- `ChatGPT/[Analytics]/Knowledge/IN_PROJECT_ANALYSIS_MODE.md`
- `ChatGPT/[Analytics]/Knowledge/MAIN_FILES_STANDARD.md`
- `ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md`
- `ChatGPT/[Analytics]/Knowledge/MARTS_DESIGN.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`
- `ChatGPT/[Analytics]/Knowledge/CHART_SELECTION_STANDARD.md`
- `ChatGPT/[Analytics]/Knowledge/MEMO_PIPELINE.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_MEMO_STRUCTURE.md`
- `ChatGPT/[Analytics]/Knowledge/WORD_REPORT_STANDARD.md`
- `ChatGPT/[Analytics]/Knowledge/TEXT_QA_AND_STYLE.md`
- `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md`
- `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`
- `ChatGPT/[Analytics]/Knowledge/ROUTING_AND_HANDOFF.md`
- `ChatGPT/[Analytics]/Knowledge/CODEX_TASK_PACKETS.md`
- `ChatGPT/[Analytics]/Knowledge/AI_OS_REFERENCE.md`
- `ChatGPT/[Analytics]/Knowledge/GOVERNANCE_AND_ANTI_PATTERNS.md`
- `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md`
- `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_RESULT.md`
- `ChatGPT/[Analytics]/Knowledge/CHANGELOG.md`
- `ChatGPT/[Analytics]/Knowledge/MANIFEST.md`
- `ChatGPT/[Analytics]/Knowledge/MEMO_RUBRIC.md`

Analytics Knowledge bundle files:

- `ChatGPT/[Analytics]/Knowledge_Bundles/README.md`
- `ChatGPT/[Analytics]/Knowledge_Bundles/UPLOAD_LIST.md`
- `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_01_CORE_WORKFLOW.md`
- `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_02_DATA_CONTRACTS_AND_MARTS.md`
- `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_03_TECHNIQUES_AND_CHARTS.md`
- `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_04_MEMO_AND_TEXT_STANDARDS.md`
- `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_05_QA_GOVERNANCE_ROUTING.md`
- `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_06_TEMPLATES.md`
- `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_07_CODEX_HANDOFF_OPTIONAL.md`

Analytics templates and handoff packet files:

- `ChatGPT/[Analytics]/Templates/ANALYSIS_RESPONSE_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/DATA_CONTRACT_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/MART_SPEC_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/MEMO_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/CODEX_HANDOFF_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`
- `ChatGPT/[Analytics]/Templates/EVIDENCE_CARD_TEMPLATE.md`
- `ChatGPT/[Analytics]/Codex_Tasks/00_OVERVIEW.md`
- `ChatGPT/[Analytics]/Codex_Tasks/01_STAGE.md`
- `ChatGPT/[Analytics]/Codex_Tasks/02_MART.md`
- `ChatGPT/[Analytics]/Codex_Tasks/03_CHARTS.md`
- `ChatGPT/[Analytics]/Codex_Tasks/04_INSIGHTS.md`
- `ChatGPT/[Analytics]/Codex_Tasks/05_WORD.md`
- `ChatGPT/[Analytics]/Codex_Tasks/06_TEXT_QA.md`
- `ChatGPT/[Analytics]/Codex_Tasks/07_SMOKE_QA.md`

Related project boundary files:

- `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[AI OS]/Knowledge/PROJECT_ROUTING.md`
- `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`
- `ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[LLM]/Knowledge/ROUTING_AND_HANDOFF.md`
- `ChatGPT/[Thinking]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[Thinking]/Knowledge/ROUTING_AND_HANDOFF.md`
- `ChatGPT/[Codex]/PROJECT_INSTRUCTIONS.md`
- `ChatGPT/[Codex]/Knowledge/ANALYTICAL_MEMO_AUTOMATION_WORKFLOW.md`

## Expected Role

`[Analytics]` owns deterministic analytics: data contracts, RAW/STAGE/MART boundaries, metrics, formulas, variance/reconciliation/anomaly work, evidence-backed findings, memo facts, chart standards, QA, and acceptance status.

It routes:

- AI concepts, AI patterns, and AI evidence/confidence checks to `[AI OS]`.
- Prompt library, model routing, orchestration, LLM quality workflow, and prompt workflow packaging to `[LLM]`.
- Strategic decisions, scenarios, trade-offs, and risk appetite to `[Thinking]`.
- Repo edits, code, tests, automation, generated executable artifacts, release, rollback, and PR work to `[Codex]`.

## Smoke Prompts Run

These are repository-instruction smoke checks, not a live ChatGPT Project runtime test.

| # | Prompt | Expected behavior | Observed repository behavior | Status |
|---|---|---|---|---|
| 1 | Нужно проверить AI-паттерн из KB и применимость к работе Сергея. Что делаешь? | Route to `[AI OS]`; do not answer as Analytics owner. | `AI_OS_REFERENCE.md`, `ROUTING_AND_HANDOFF.md`, `PROJECT_INSTRUCTIONS.md`, `COMMAND_SURFACE.md`, and `docs/PROJECT_ROUTING.md` route AI concepts/pattern evidence to `[AI OS]`. | pass |
| 2 | Нужно построить financial variance analysis по выгрузке. Что делаешь? | Stay in `[Analytics]`; require source data, period, grain, metric definitions, currency, QA status. | `PROJECT_INSTRUCTIONS.md`, `DATA_CONTRACTS.md`, `ANALYTICS_WORKFLOW.md`, `QA_CHECKLIST.md`, and templates require data contract, period, grain, filters, source, formulas, currency/unit normalization, reconciliation, QA, and limitations. | pass |
| 3 | Нужно превратить аналитическую методику в prompt workflow. Что делаешь? | Handoff to `[LLM]` after Analytics defines analytical facts/methodology. | `IN_PROJECT_ANALYSIS_MODE.md` and `ROUTING_AND_HANDOFF.md` keep analytical framing in `[Analytics]`, then route prompt library/model routing/orchestration/generation workflow to `[LLM]`. | pass |
| 4 | Нужно создать executable memo factory в repo через Codex APP. Что делаешь? | `[Analytics]` frames analytical methodology; handoff to `[Codex]` for executable artifact/repo execution. | `ROUTING_AND_HANDOFF.md`, `CODEX_TASK_PACKETS.md`, `ANALYTICS_07_CODEX_HANDOFF_OPTIONAL.md`, `GOAL_PACKS.md`, and `COMMAND_SURFACE.md` route executable repo artifacts to `[Codex]` / Codex APP while Analytics owns methodology and acceptance criteria. | pass |
| 5 | Можно ли сделать расчёты LLM-ом без Python/SQL, если данные маленькие? | No for deterministic analytical findings; calculations must be reproducible and QA-visible. | `PROJECT_INSTRUCTIONS.md` says LLM is not the calculation source; `CODEX_TASK_PACKETS.md` requires Python for executable memo production. A wording risk in `IN_PROJECT_ANALYSIS_MODE.md` was tightened from manual calculation to Python/SQL/spreadsheet or another verifiable deterministic method. | pass |
| 6 | Дай autoloop для аналитического вывода, пока результат не станет красивым. | Supervised loop only; stop on DQ fail, unclear grain, missing contract, no validation path, or conflicting acceptance criteria. | `PROJECT_INSTRUCTIONS.md`, `ANALYTICS_WORKFLOW.md`, `IN_PROJECT_ANALYSIS_MODE.md`, `GOAL_PACKS.md`, and `COMMAND_SURFACE.md` define supervised `autoloop_analysis`, deterministic-first QA, visible revise/rerun criteria, and stop conditions; they forbid autonomous retrieval, vector DB, embeddings, semantic search, web UI, logs, journals, and runtime artifact stores. | pass |

## Checks

| Check | Status | Evidence |
|---|---|---|
| Analytics has explicit role/scope. | pass | `PROJECT_INSTRUCTIONS.md`, `README.md`, `ANALYTICS_WORKFLOW.md`, and `ANALYTICS_01_CORE_WORKFLOW.md`. |
| Analytics does not own AI concept/evidence checks. | pass | `AI_OS_REFERENCE.md`, `ROUTING_AND_HANDOFF.md`, and cross-project routing docs route these to `[AI OS]`. |
| Analytics does not own prompt/workflow orchestration. | pass | `IN_PROJECT_ANALYSIS_MODE.md`, `ROUTING_AND_HANDOFF.md`, `COMMAND_SURFACE.md`, and `GOAL_PACKS.md` route prompt/model/orchestration work to `[LLM]`. |
| Analytics does not own repo edits or implementation. | pass | `ROUTING_AND_HANDOFF.md`, `CODEX_TASK_PACKETS.md`, and `ANALYTICS_07_CODEX_HANDOFF_OPTIONAL.md` route implementation and executable artifacts to `[Codex]`. |
| Analytics requires data contract fields. | pass | `DATA_CONTRACTS.md`, `PROJECT_INSTRUCTIONS.md`, templates, and QA checklist require source, period, grain, filters, metric definitions/formulas, currency/units, and QA status. |
| Deterministic checks override LLM judge. | pass | `PROJECT_INSTRUCTIONS.md`, `ANALYTICS_WORKFLOW.md`, `QA_CHECKLIST.md`, golden memo pack contracts, and handoff templates keep calculations/formulas/evidence deterministic. |
| Memo outputs separate facts, calculations, interpretation, hypothesis, recommendation, limitations, and confidence. | pass | `PROJECT_INSTRUCTIONS.md`, `ANALYTICAL_MEMO_STRUCTURE.md`, `MEMO_PIPELINE.md`, `MEMO_RUBRIC.md`, and templates. |
| Autoloop is supervised only and has stop conditions. | pass | `PROJECT_INSTRUCTIONS.md`, `ANALYTICS_WORKFLOW.md`, `IN_PROJECT_ANALYSIS_MODE.md`, `GOAL_PACKS.md`, and `COMMAND_SURFACE.md`. |
| No production readiness is claimed without acceptance. | pass | `README.md`, `ACCEPTANCE_CRITERIA.md`, `GOVERNANCE_AND_ANTI_PATTERNS.md`, `SMOKE_QA_RESULT.md`, and bundle status blocks. |
| No blocked promotion items are recommended as current implementation. | pass | Analytics README, AI OS reference, knowledge bundle README/upload list, autoloop rules, and goal packs reject embeddings, semantic search, vector DB, web UI, autonomous retrieval, and production agentic workflow as current implementation. |

## Mismatches Found

- `ChatGPT/[Analytics]/Knowledge/IN_PROJECT_ANALYSIS_MODE.md` used "расчёт вручную или с доступными инструментами", which could be read as allowing LLM/manual arithmetic for small data. This conflicted with the issue's deterministic calculation expectation.

## Required Fixes

- Replaced that wording with "расчёт через Python, SQL, spreadsheet или другой проверяемый deterministic метод" in:
  - `ChatGPT/[Analytics]/Knowledge/IN_PROJECT_ANALYSIS_MODE.md`
  - `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_01_CORE_WORKFLOW.md`

## Residual Risks

- This QA verified repository files and bundled instructions. It did not test a live ChatGPT Project instance after upload.
- Historical `Codex_Tasks/` files outside the active package manifest contain older implementation notes and were searched for routing/safety terms, but the active package source of truth remains the manifest-listed files and Knowledge bundles.
- `ChatGPT/[Analytics]/Knowledge/MEMO_FACTORY_DESIGN_HANDOFF.md` exists in the folder but is not listed in `package_manifest.json`; it was not identified as an active upload source by current bundle manifests.

## Acceptance Status

Status: pass

Reason: the active Analytics package and bundles preserve analytics ownership, cross-project routing, deterministic QA, supervised autoloop boundaries, handoff rules, and non-promotion constraints after the minimal wording fix.

## Next Step

Open a draft PR for human review. Do not merge automatically.
