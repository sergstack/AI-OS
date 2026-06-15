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
