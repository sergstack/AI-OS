# ChatGPT Project Sync Checklist

## Purpose

Track manual synchronization from repository source files into ChatGPT Projects.

Repository validation does not prove ChatGPT UI sync. Use `not_verified` until there is explicit human evidence.

For compact Sources sync, use each project's `Knowledge_Bundles/UPLOAD_LIST.md`. Upload bundle files OR granular Knowledge files, not both, unless debugging.

For analytical memo production, verify that the uploaded bundles include the `Analytical Memo Factory via Codex APP` workflow before running a memo pilot.

Allowed sync status values: `not_verified`, `pending`, `partial`, `done`, `not_applicable`, `blocked`.
Allowed confidence values: `strong`, `medium`, `weak`, `unsupported`.
Allowed acceptance status values: `draft`, `candidate`, `accepted`, `blocked`, `not_applicable`.

| Project | Repo project path | PROJECT_INSTRUCTIONS.md path | Project Instructions pasted to ChatGPT | Project Instructions pasted date | Knowledge files expected | Knowledge files uploaded to ChatGPT | Knowledge upload date | Smoke QA run | Smoke QA date | Pilot case defined | Pilot case completed | Acceptance status | Confidence | Owner | Blockers | Next step | Evidence link / notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `[AI OS]` | `ChatGPT/[AI OS]` | `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md` | done | 2026-07-06 | `ChatGPT/[AI OS]/Knowledge_Bundles/UPLOAD_LIST.md` | done | 2026-07-06 | done | 2026-07-06 | done | not_verified | candidate | medium | Sergey | Pilot `PILOT-AIOS-001` not completed; production promotion remains blocked | Execute pilot `PILOT-AIOS-001` and record result evidence | `SMOKE_QA_RESULTS.md`; Codex browser observed Project Instructions field and expected `[AI OS]` Sources in ChatGPT UI |
| `[Thinking]` | `ChatGPT/[Thinking]` | `ChatGPT/[Thinking]/PROJECT_INSTRUCTIONS.md` | not_verified | not_verified | `ChatGPT/[Thinking]/Knowledge/` | not_verified | not_verified | not_verified | not_verified | done | not_verified | draft | unsupported | Sergey | ChatGPT UI sync not evidenced | Manually paste instructions, upload expected Knowledge, run smoke QA, then run pilot `PILOT-THINKING-001` | none |
| `[Analytics]` | `ChatGPT/[Analytics]` | `ChatGPT/[Analytics]/PROJECT_INSTRUCTIONS.md` | not_verified | not_verified | `ChatGPT/[Analytics]/Knowledge/` | not_verified | not_verified | not_verified | not_verified | done | not_verified | draft | unsupported | Sergey | ChatGPT UI sync not evidenced | Manually paste instructions, upload expected Knowledge, run smoke QA, then run pilot `PILOT-ANALYTICS-001` | none |
| `[LLM]` | `ChatGPT/[LLM]` | `ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md` | not_verified | not_verified | `ChatGPT/[LLM]/Knowledge/` | not_verified | not_verified | not_verified | not_verified | done | not_verified | draft | unsupported | Sergey | ChatGPT UI sync not evidenced | Manually paste instructions, upload expected Knowledge, run smoke QA, then run pilot `PILOT-LLM-001` | none |
| `[Codex]` | `ChatGPT/[Codex]` | `ChatGPT/[Codex]/PROJECT_INSTRUCTIONS.md` | not_verified | not_verified | `ChatGPT/[Codex]/Knowledge/` | not_verified | not_verified | not_verified | not_verified | done | not_verified | draft | unsupported | Sergey | ChatGPT UI sync not evidenced | Manually paste instructions, upload expected Knowledge, run smoke QA, then run pilot `PILOT-CODEX-001` | none |
| `[Inbox Router]` | `ChatGPT/[Inbox Router]` | `ChatGPT/[Inbox Router]/PROJECT_INSTRUCTIONS.md` | not_verified | not_verified | `ChatGPT/[Inbox Router]/Knowledge/` | not_verified | not_verified | not_verified | not_verified | done | not_verified | draft | unsupported | Sergey | ChatGPT UI sync not evidenced | Manually paste instructions, upload expected Knowledge, run smoke QA, then run pilot `PILOT-INBOX-001` | none |
| Codex APP | `Codex APP` | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | done | not_verified | not_applicable | unsupported | Sergey | Local executor, not a ChatGPT Project | Run local task package pilot `PILOT-CODEXAPP-001` | not a ChatGPT Project |
