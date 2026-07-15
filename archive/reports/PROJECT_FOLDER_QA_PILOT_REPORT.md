# Project Folder QA Pilot Report

Review date: 2026-07-07

Issue: GitHub #66

Method: repository-file based QA. Inspected active project folders, upload bundle lists, routing surfaces, issue templates, PR template, pilot-related Markdown files, and repo validation scripts. Universal smoke prompts were checked against repository instructions and bundled source files, not against a live ChatGPT Project runtime.

Limitations: this review does not prove live ChatGPT Project behavior after manual Project Instructions sync and Knowledge upload. Live smoke QA evidence exists from 2026-07-06, but fresh realistic pilot execution remains separately tracked in pilot result files.

## 2026-07-07 Refresh

This refresh updates inventory and pilot-file coverage after later Goal Mode,
Knowledge bundle, StreamDeck, and pilot-result changes. It is still a
repository-file QA pass, not a fresh live ChatGPT Project pilot run.

## Project folder inventory

| Project/surface | Files found | Active source of truth | Upload bundle | Status |
|---|---:|---|---|---|
| `ChatGPT/[AI OS]` | 29 | `PROJECT_INSTRUCTIONS.md`; `Knowledge/`; `Knowledge_Bundles/UPLOAD_LIST.md` | 6 required / 0 optional | pass |
| `ChatGPT/[Thinking]` | 22 | `PROJECT_INSTRUCTIONS.md`; `Knowledge/`; `Knowledge_Bundles/UPLOAD_LIST.md` | 3 required / 0 optional | pass |
| `ChatGPT/[Analytics]` | 76 | `PROJECT_INSTRUCTIONS.md`; `package_manifest.json`; `Knowledge/`; `Knowledge_Bundles/UPLOAD_LIST.md` | 6 required / 1 optional | pass |
| `ChatGPT/[LLM]` | 33 | `PROJECT_INSTRUCTIONS.md`; `Knowledge/`; `Knowledge_Bundles/UPLOAD_LIST.md` | 6 required / 0 optional | pass after fixes |
| `ChatGPT/[Codex]` | 42 | `PROJECT_INSTRUCTIONS.md`; `Knowledge/`; `Knowledge_Bundles/UPLOAD_LIST.md` | 6 required / 0 optional | pass |
| `ChatGPT/[Inbox Router]` | 19 | `PROJECT_INSTRUCTIONS.md`; `Knowledge/`; `Knowledge_Bundles/UPLOAD_LIST.md` | 2 required / 0 optional | pass |
| `Codex APP` | 19 | `README.md`; `CODEX_APP_*`; `templates/` | not a ChatGPT Project upload bundle | pass |
| `StreamDeck` | 214 | `README.md`; v2.7 active setup/map files; v2.8 candidate setup/map/icon/MCP files | not a ChatGPT Project upload bundle | pass |
| `COMMAND_SURFACE.md` | 1 | root command map | not upload bundle | pass |
| `GOAL_PACKS.md` | 1 | root goal-pack registry | not upload bundle | pass |
| `docs/PROJECT_ROUTING.md` | 1 | root routing table | not upload bundle | pass |
| `.github/ISSUE_TEMPLATE/**` and `.github/pull_request_template.md` | 3 | issue/PR workflow templates | not upload bundle | pass |
| `AGENTS.md` | 1 | repository operating rules | not upload bundle | pass |

## Project folder QA matrix

| Project/surface | Expected role | Smoke prompts checked | Verdict | Mismatches | Required fixes | Residual risks |
|---|---|---:|---|---|---|---|
| `[AI OS]` | AI concepts, trends, patterns, evidence/confidence, governance, use-case interpretation, owner-project routing. | 6 | pass | none found | none | Live project sync not verified. |
| `[Thinking]` | Decisions, assumptions, scenarios, trade-offs, downside, reversibility, revisit triggers. | 6 | pass | none found | none | Live project sync not verified. |
| `[Analytics]` | Deterministic analytics, data contracts, marts, metrics, formulas, variance, reconciliation, anomaly QA, memo facts. | 6 | pass | none found on `main`; issue #64 wording fix is not in `main` yet. | none in this branch | Live project sync not verified; issue #64 PR may further tighten wording. |
| `[LLM]` | Prompt design, context packs, workflow orchestration, model routing, judge/revisor flow, narrative from approved facts. | 6 | pass after fixes | `OLLAMA_OPENWEBUI_PILOT.md` lacked explicit owner/status metadata. | Added owner/status/manifest/residual-risk metadata to source and bundle excerpt. | Live local tool pilot still not recorded. |
| `[Codex]` | Repo edits, implementation, scripts, tests, checks, branches, PRs, rollback, release package; no auto-merge. | 6 | pass | none found | none | Live project sync not verified. |
| `[Inbox Router]` | Classify and route requests quickly without solving owner-project work. | 6 | pass | none found | none | Live project sync not verified. |
| StreamDeck / command surface | Short, routable commands aligned with goal packs; no hidden production automation. | 6 | pass | none found | none | Actual Stream Deck device behavior not tested. |
| Codex APP | Accept broad goals; infer internal scope/checks/rollback/acceptance; branch/checks/PR workflow. | 6 | pass | none found | none | Local Codex APP runtime behavior not tested in this QA. |

## Pilot files inventory

| Project/surface | Pilot file | Status | Manifest/upload status | Verdict | Notes |
|---|---|---|---|---|---|
| Root operational verification | `PILOT_CASES.md` | backlog | Listed in `PROJECT_REGISTRY.md` and `REPO_PATHS.md` as an operational artifact; not a ChatGPT Project Knowledge upload bundle. | pass after fixes | Statuses changed from non-standard `draft` to allowed `backlog`. |
| Root operational verification | `PILOT_RESULTS_TEMPLATE.md` | template | Listed in `REPO_PATHS.md` as an operational artifact; not a ChatGPT Project Knowledge upload bundle. | pass after fixes | Added owner project, allowed pilot status, and manifest/upload status fields. |
| Root operational verification | `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md` | candidate evidence | Operational evidence file; not a ChatGPT Project Knowledge upload bundle. | pass | Records live ChatGPT runtime smoke context and local Ollama/Open WebUI checks from 2026-07-06. |
| Root operational verification | `PILOT_RESULTS_2026-07-07_PROJECT_FOLDER_PILOTS.md` | partial / not_run evidence | Operational evidence file; not a ChatGPT Project Knowledge upload bundle. | pass | Represents all six project pilots with honest fresh-live-pilot `not_run` blockers. |
| Root operational verification | `PROJECT_FOLDER_QA_PILOT_REPORT.md` | QA report | Operational report; not a ChatGPT Project Knowledge upload bundle. | pass | This consolidated project-folder and pilot Markdown QA report. |
| `[LLM]` | `ChatGPT/[LLM]/Knowledge/OLLAMA_OPENWEBUI_PILOT.md` | candidate | Source file for `ChatGPT/[LLM]/Knowledge_Bundles/LLM_06_LOCAL_AI_EXPERIMENTS.md`. | pass after fixes | Added explicit owner/status/manifest/residual-risk metadata. |
| `[AI OS]` | pilot-related Markdown | not found | not applicable | pass | No project-local pilot file found. |
| `[Thinking]` | pilot-related Markdown | not found | not applicable | pass | No project-local pilot file found. |
| `[Analytics]` | pilot-related Markdown | not found | not applicable | pass | No project-local pilot file found. |
| `[Codex]` | pilot-related Markdown | not found | not applicable | pass | No project-local pilot file found. |
| `[Inbox Router]` | pilot-related Markdown | not found | not applicable | pass | No project-local pilot file found. |
| Codex APP | pilot-related Markdown | not found | not applicable | pass | Pilot definition is in root `PILOT_CASES.md`. |
| StreamDeck | `StreamDeck/archive/v2.8/STREAMDECK_V2_8_MCP_ACTIONS_PILOT.md` | pilot passed / candidate-only | StreamDeck operational evidence; not a ChatGPT Project Knowledge upload bundle. | pass | Records supervised MCP execution of `AIOS_HOME_JUDGE` and `AIOS_HOME_REVISOR`; v2.8 remains candidate-only. |

## Pilot file QA matrix

| Pilot file | Owner project | Claimed status | Expected status | Mismatches | Required fixes | Residual risks |
|---|---|---|---|---|---|---|
| `PILOT_CASES.md` | Multiple: `[AI OS]`, `[Thinking]`, `[Analytics]`, `[LLM]`, `[Codex]`, `[Inbox Router]`, Codex APP, Cross-project. | `draft` before fix | `backlog` until result evidence exists | `draft` was outside allowed issue #66 status set. Manifest/upload status was implicit. | Marked definitions as backlog; added allowed statuses and non-upload operational status. | Pilot results are still not recorded. |
| `PILOT_RESULTS_TEMPLATE.md` | Filled per pilot result | template before fix | template with owner/status fields | Missing explicit owner project, pilot status, and manifest/upload status fields. | Added fields. | It remains a blank template until a real pilot result is recorded. |
| `ChatGPT/[LLM]/Knowledge/OLLAMA_OPENWEBUI_PILOT.md` | `[LLM]` after fix | implicit pilot | `candidate` | Owner project, pilot status, manifest/upload status, and residual risk were not explicit in source file. | Added metadata to source and `LLM_06_LOCAL_AI_EXPERIMENTS.md` bundle excerpt. | Actual Ollama/Open WebUI behavior not tested. |
| `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md` | `[AI OS]`, `[Thinking]`, `[Analytics]`, `[LLM]`, `[Codex]`, `[Inbox Router]`, `[LLM]` local AI | candidate evidence | runtime/smoke evidence, not production promotion | none found in this refresh | none | ChatGPT URLs are private browser state; future sync can drift. |
| `PILOT_RESULTS_2026-07-07_PROJECT_FOLDER_PILOTS.md` | All six ChatGPT projects | partial / not_run | honest fresh-pilot blocker report | none found | none | Live realistic pilots still need execution and captured output. |
| `StreamDeck/archive/v2.8/STREAMDECK_V2_8_MCP_ACTIONS_PILOT.md` | StreamDeck / command surface | pilot passed / candidate-only | candidate-only MCP action evidence | none found | none | Confirms only two MCP actions; full action set and physical device behavior still need broader QA. |

## Cross-project routing checks

| Scenario | Expected owner | Observed owner/routing | Verdict |
|---|---|---|---|
| AI concept / AI pattern / KB evidence applicability | `[AI OS]` | `PROJECT_INSTRUCTIONS.md`, `docs/PROJECT_ROUTING.md`, `COMMAND_SURFACE.md`, and `GOAL_PACKS.md` route AI concepts/evidence to `[AI OS]`. | pass |
| Finance calculation / data / mart / memo facts | `[Analytics]` then `[LLM]` for narrative if needed | Analytics owns deterministic data contract/calculation/QA; `finance_memo_factory` routes narrative after verified facts. | pass |
| Prompt workflow / model routing / context pack | `[LLM]` | LLM instructions, command surface, and goal packs route prompt/workflow/model routing to `[LLM]`. | pass |
| Repo file changes / implementation / tests / PR | `[Codex]` / Codex APP | Codex and Codex APP docs require branch/checks/PR/human review; AGENTS forbids direct main commits and auto-merge. | pass |
| Decision memo / strategic trade-off | `[Thinking]` | Thinking instructions and routing docs route options, risks, decisions, and revisit triggers to `[Thinking]`. | pass |
| Blocked promotion items: embeddings, semantic search, vector DB, web UI, autonomous retrieval | no current implementation owner; future backlog/hypothesis only | AGENTS, AI OS governance, LLM local AI docs, goal packs, and upload lists block these as current implementation without acceptance. | pass |

## Blocked / revise items

| Claim or behavior | Folder/file | Evidence | Risk | Required action | Owner project |
|---|---|---|---|---|---|
| Pilot status `draft` used for pilot definitions. | `PILOT_CASES.md` | Issue #66 allowed statuses exclude `draft`. | Pilot inventory could be ambiguous after QA. | Changed to `backlog`. | Root operational verification |
| Pilot result template lacked status and manifest/upload fields. | `PILOT_RESULTS_TEMPLATE.md` | Issue #66 requires each pilot file to expose owner/status/manifest or upload status. | Future results may omit required QA metadata. | Added fields. | Root operational verification |
| Ollama/Open WebUI pilot source lacked explicit owner/status metadata. | `ChatGPT/[LLM]/Knowledge/OLLAMA_OPENWEBUI_PILOT.md` | Source file had safe scope and stop rules, but no owner/status/manifest block. | Pilot could be read as current capability rather than candidate guidance. | Added metadata to source and upload bundle excerpt. | `[LLM]` |

## Fixes applied

| File | Change | Reason |
|---|---|---|
| `PILOT_CASES.md` | Replaced `draft` pilot statuses with `backlog`; added allowed status set and non-upload operational status. | Align pilot definitions with issue #66 allowed statuses and clarify manifest/upload role. |
| `PILOT_RESULTS_TEMPLATE.md` | Added owner project, pilot status, and manifest/upload status fields. | Ensure future pilot results capture required QA metadata. |
| `ChatGPT/[LLM]/Knowledge/OLLAMA_OPENWEBUI_PILOT.md` | Added owner project, candidate status, manifest/upload status, and residual risk. | Make pilot status explicit in source file. |
| `ChatGPT/[LLM]/Knowledge_Bundles/LLM_06_LOCAL_AI_EXPERIMENTS.md` | Mirrored Ollama/OpenWebUI pilot metadata in the upload bundle excerpt. | Keep source file and upload bundle consistent. |
| `PROJECT_FOLDER_QA_PILOT_REPORT.md` | Refreshed inventory for 2026-07-07 and listed new pilot evidence files. | Keep issue #66 report consistent with current repo contents. |

## Acceptance status

pass

The repository-file QA found only fixable pilot metadata/status mismatches. After
the minimal fixes and this refresh, project roles, routing, governance, output
boundaries, handoff behavior, pilot status clarity, blocked promotion
constraints, and Codex branch/checks/PR workflow are consistent in the inspected
files. Fresh realistic live pilot executions remain tracked as separate
`not_run` blockers where applicable.

## Next step

Open a draft PR for human review. Do not merge automatically. After merge and manual ChatGPT Project sync, run live smoke QA for each project folder and record real pilot results.
