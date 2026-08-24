# Project Registry

## ChatGPT Projects

| Project | Canonical path | Project Instructions rule |
|---|---|---|
| `[AI OS]` | `ChatGPT/[AI OS]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |
| `[Thinking]` | `ChatGPT/[Thinking]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |
| `[Analytics]` | `ChatGPT/[Analytics]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |
| `[LLM]` | `ChatGPT/[LLM]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |
| `[Codex]` | `ChatGPT/[Codex]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |
| `[Inbox Router]` | `ChatGPT/[Inbox Router]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |
| `[Thinkers OS]` | `ChatGPT/[Thinkers OS]` | `PROJECT_INSTRUCTIONS.md` <= 8000 chars |

## AES Applicability

`AUTONOMOUS_EXECUTION_STANDARD.md` is the single canonical AES semantic
owner. Each listed exposure includes the v1.1 Closure Review reference; this
table records applicability and deployment exposure; it does not
claim external execution, pilot completion, owner acceptance, merge, or
production authorization.

| Project | AES applicability | Canonical reference | Extension required | Extension | Bundle exposure | Execution evidence | Pilot evidence | Authority constraints |
|---|---|---|---|---|---|---|---|---|
| `[AI OS]` | applicable | `AUTONOMOUS_EXECUTION_STANDARD.md` | no | not_required | `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_02_GOVERNANCE_AND_EVIDENCE.md` | canonical_owner_repository_package | not_recorded | no_external_authority |
| `[Thinking]` | applicable | `AUTONOMOUS_EXECUTION_STANDARD.md` | no | not_required | `ChatGPT/[Thinking]/Knowledge_Bundles/THINKING_01_WORKFLOW_AND_DECISIONS.md` | `docs/autonomous_execution/examples/pilot_evidence/cross_project_handoff_pilot.json` | cross_project_pilot_only | no_external_authority |
| `[Analytics]` | applicable | `AUTONOMOUS_EXECUTION_STANDARD.md` | yes | `docs/autonomous_execution/extensions/ANALYTICS_EXTENSION.md` | `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_03_TECHNIQUES_AND_CHARTS.md` | `docs/autonomous_execution/examples/pilot_evidence/analytics_pilot.json` | synthetic_fixture_only | no_external_authority |
| `[LLM]` | applicable | `AUTONOMOUS_EXECUTION_STANDARD.md` | no | not_required | `ChatGPT/[LLM]/Knowledge_Bundles/LLM_03_QUALITY_GATES_AND_EVAL.md` | not_recorded | not_recorded | no_external_authority |
| `[Codex]` | applicable | `AUTONOMOUS_EXECUTION_STANDARD.md` | no | not_required | `ChatGPT/[Codex]/Knowledge_Bundles/CODEX_02_EXECUTION_AUTONOMY_REPORTING.md` | `docs/autonomous_execution/examples/pilot_evidence/codex_corrective_loop_pilot.json` | isolated_fixture_only | stricter_one_fix_policy; no_external_authority |
| `[Inbox Router]` | thin_applicability | `AUTONOMOUS_EXECUTION_STANDARD.md` | no | not_required | `ChatGPT/[Inbox Router]/Knowledge_Bundles/INBOX_02_HANDOFF_QA_ANTI_PATTERNS.md` | not_recorded | not_recorded | route_clarify_package_only; no_external_authority |
| `[Thinkers OS]` | applicable | `AUTONOMOUS_EXECUTION_STANDARD.md` | no | not_required | `ChatGPT/[Thinkers OS]/Knowledge_Bundles/THINKERS_OS_01_PORTFOLIO_AND_CORPUS.md` | not_recorded | not_recorded | no_external_authority |

## Executor Layer

| Package | Canonical path | Role |
|---|---|---|
| Codex APP | `Codex APP` | Execution/runtime layer for long-running Codex work; not a ChatGPT Project |

## Validation Gates

- Project instructions length: <= 8000 chars
- Public safety scan: required
- No raw absolute local paths: required
- Manifest/path consistency: required
- Knowledge bundle consistency: required
- Smoke QA: required
- Pilot case: required before production promotion

## Operational Artifacts

- `CHATGPT_PROJECT_SYNC_CHECKLIST.md`
- `PILOT_CASES.md`
- `SMOKE_QA_REFRESH_PLAN.md`
- `ChatGPT/[Project]/Knowledge_Bundles/`

## Canonical Workflows

- `Analytical Memo Factory via Codex APP`: `ChatGPT/[AI OS]/Knowledge/ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md`
