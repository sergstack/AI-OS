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
| `[AI OS]` | `ChatGPT/[AI OS]` | `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md` | done | 2026-08-12 | `ChatGPT/[AI OS]/Knowledge_Bundles/UPLOAD_LIST.md` | done | 2026-08-12 | done | 2026-08-12 | done | not_verified | candidate | strong | Sergey | none within bounded LPV v1 scope | Owner review of governed MVP evidence | `SYNC_VERIFIED`; all six required bundle fingerprints exact. `LIVE-AIOS-SMOKE-002`: deterministic PASS, independent Judge PASS, final PASS. Governed record below. |
| `[Thinking]` | `ChatGPT/[Thinking]` | `ChatGPT/[Thinking]/PROJECT_INSTRUCTIONS.md` | done | 2026-07-06 | `ChatGPT/[Thinking]/Knowledge_Bundles/UPLOAD_LIST.md` | done | 2026-07-06 | done | 2026-07-06 | done | not_verified | candidate | medium | Sergey | Pilot `PILOT-THINKING-001` not completed; production promotion remains blocked | Execute pilot `PILOT-THINKING-001` and record result evidence | `CROSS_PROJECT_SMOKE_QA_RESULTS.md`; Codex browser observed Project Instructions field, expected `[Thinking]` Sources, and smoke QA answer |
| `[Analytics]` | `ChatGPT/[Analytics]` | `ChatGPT/[Analytics]/PROJECT_INSTRUCTIONS.md` | done | 2026-08-12 | `ChatGPT/[Analytics]/Knowledge_Bundles/UPLOAD_LIST.md` | done | 2026-08-12 | done | 2026-08-12 | done | not_verified | candidate | strong | Sergey | none within bounded LPV v1 scope | Owner review of governed MVP evidence | `SYNC_VERIFIED_FOR_MVP` using affected-scope verification. Instructions normalized-content PASS: repo raw SHA-256 `3e567ad75baa316d780dc0e7e7dbf3143899e8040ded0c35f7de1dd194042537`, live raw SHA-256 `aba2c40012a75f90ed7a01b40650c8b3cc649804a938b27b61182ba63ede092b`; sole difference is one terminal LF removed by ChatGPT UI. All six required unchanged bundles presence PASS. `LIVE-ANALYTICS-SMOKE-001`: deterministic PASS, independent Judge PASS, final PASS. Governed record below. |
| `[LLM]` | `ChatGPT/[LLM]` | `ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md` | done | 2026-08-12 | `ChatGPT/[LLM]/Knowledge_Bundles/UPLOAD_LIST.md` | done | 2026-08-12 | done | 2026-08-12 | done | not_verified | candidate | strong | Sergey | none within bounded LPV v1 scope | Owner review of governed MVP evidence | `SYNC_VERIFIED_FOR_MVP` using affected-scope verification. Instructions normalized-content PASS: repo raw SHA-256 `e7165b25650406f64b61a2ac40de2b871e3157dceb1ead37fe86ed1196552db2`, live raw SHA-256 `443c323f2ac751f0dc17cc9ce4d59bdf389444e96a49771dca56b63c16b17307`; sole difference is one terminal LF removed by ChatGPT UI. Exact fingerprints PASS for changed `LLM_02/03`; unchanged `LLM_01/04/05/06` presence PASS. `LIVE-LLM-SMOKE-001`: deterministic PASS, independent Judge PASS, final PASS. Governed record below. |
| `[Codex]` | `ChatGPT/[Codex]` | `ChatGPT/[Codex]/PROJECT_INSTRUCTIONS.md` | done | 2026-07-06 | `ChatGPT/[Codex]/Knowledge_Bundles/UPLOAD_LIST.md` | done | 2026-07-06 | done | 2026-07-06 | done | not_verified | candidate | medium | Sergey | Pilot `PILOT-CODEX-001` not completed; production promotion remains blocked | Execute pilot `PILOT-CODEX-001` and record result evidence | `CROSS_PROJECT_SMOKE_QA_RESULTS.md`; Codex browser observed updated Project Instructions field, expected `[Codex]` Sources, and passing smoke QA rerun |
| `[Inbox Router]` | `ChatGPT/[Inbox Router]` | `ChatGPT/[Inbox Router]/PROJECT_INSTRUCTIONS.md` | done | 2026-07-06 | `ChatGPT/[Inbox Router]/Knowledge_Bundles/UPLOAD_LIST.md` | done | 2026-07-06 | done | 2026-07-06 | done | not_verified | candidate | medium | Sergey | Pilot `PILOT-INBOX-001` not completed; production promotion remains blocked | Execute pilot `PILOT-INBOX-001` and record result evidence | `CROSS_PROJECT_SMOKE_QA_RESULTS.md`; Codex browser observed updated Project Instructions field, expected `[Inbox Router]` Sources, and passing smoke QA rerun |
| `[Thinkers OS]` | `ChatGPT/[Thinkers OS]` | `ChatGPT/[Thinkers OS]/PROJECT_INSTRUCTIONS.md` | not_verified | not_verified | `ChatGPT/[Thinkers OS]/Knowledge_Bundles/UPLOAD_LIST.md` | not_verified | not_verified | not_verified | not_verified | done | not_verified | candidate | unsupported | Sergey | External Project creation, Sources sync, smoke QA, and pilot execution are not verified; production remains unauthorized | Perform owner-led manual sync, execute the defined smoke QA, then run `PILOT-THINKERS-001` | `ChatGPT/[Thinkers OS]/CURRENT_STATUS.md`; definition coverage only, no observed external evidence |
| Codex APP | `Codex APP` | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | not_applicable | done | not_verified | not_applicable | unsupported | Sergey | Local executor, not a ChatGPT Project | Run local task package pilot `PILOT-CODEXAPP-001` | not a ChatGPT Project |

## LPV v1 post-sync governed evidence

Repository revision: `0631205033203c49774e719b2bf21435510e74b7`

Verification scope: affected-scope MVP verification, not exhaustive full-project fingerprint verification. Exact artifact verification covered AI OS required bundles and materially changed LLM bundles `LLM_02` and `LLM_03`. Presence-based verification covered unchanged LLM bundles `LLM_01/04/05/06` and all unchanged required Analytics bundles. Project Instructions used normalized text comparison that ignores exactly one terminal LF removed by the ChatGPT UI; both raw hashes remain recorded above.

### `LIVE-AIOS-SMOKE-002`

- run_id: `LPV-LIVE-AIOS-SMOKE-002-7e3be6e0704a`
- project: `[AI OS]`
- sync_state: `SYNC_VERIFIED` (Instructions exact; all six required bundles exact)
- transport: `CONTROLLED_BROWSER_TRANSPORT`; completed
- response_sha256: `7e3be6e0704aa00695fd6403cc7b07140839ebb03a1d3d6ca7e3ccb18da23c00`
- response_hash_scope: bounded semantic excerpt from actual full response
- run_reference: `https://chatgpt.com/g/g-p-6a0512a228c88191afcc953866789dad-ai-os/c/6a7cc907-2fcc-83eb-a4a8-40bb9b9ee284`
- bounded_excerpt: `Нет — сейчас добавлять в AI OS как текущую реализацию embeddings, semantic search или vector DB нельзя. Они находятся за explicit acceptance/promotion gate. GATE: blocked для implementation.`
- deterministic: `PASS`
- independent_judge: `PASS`
- final_verdict: `PASS`
- limitation: exact transport start timestamp was not exposed; full response remains local.

### `LIVE-LLM-SMOKE-001`

- run_id: `LPV-LIVE-LLM-SMOKE-001-21e862d6f51d`
- project: `[LLM]`
- sync_state: `SYNC_VERIFIED_FOR_MVP` (normalized Instructions exact; changed bundles exact; unchanged bundles presence-based)
- transport: `CONTROLLED_BROWSER_TRANSPORT`; completed
- response_sha256: `21e862d6f51d92bdee537702a1c90a60ea4d5c1b295cb135aea1673d0526f5a7`
- response_hash_scope: bounded semantic excerpt from actual full response
- run_reference: `https://chatgpt.com/g/g-p-69e9f1058440819181beb1f41cfd672c-llm/c/6a7cc98c-d6d8-83eb-b825-937e2cef478e`
- bounded_excerpt: `prompt_id: evidence_aware_synthesis. input_requirements: objective, curated_context. output_schema: objective, facts, interpretation, unsupported_claims, risks, recommendation, limitations. model_class: reasoning. quality_gate: pass, revise, blocked.`
- deterministic: `PASS`
- independent_judge: `PASS`
- final_verdict: `PASS`
- limitation: exact transport start timestamp was not exposed; full response remains local.

### `LIVE-ANALYTICS-SMOKE-001`

- run_id: `LPV-LIVE-ANALYTICS-SMOKE-001-0c8850d7c4d2`
- project: `[Analytics]`
- sync_state: `SYNC_VERIFIED_FOR_MVP` (normalized Instructions exact; unchanged bundles presence-based)
- transport: `CONTROLLED_BROWSER_TRANSPORT`; completed
- response_sha256: `0c8850d7c4d237b5290481e1c50f7012c93713ded18259748f9f9bca2623b848`
- response_hash_scope: bounded semantic excerpt from actual full response
- run_reference: `https://chatgpt.com/g/g-p-69e9f058f22481918c854fffa86335ec-analytics/c/6a7cc7c6-b474-83eb-9b4a-dec25a99b82a?tab=chats`
- bounded_excerpt: `Data contract: period — один отчётный месяц; grain: period × cfo_id × expense_category_id. stage_main_full очищает и типизирует исходные строки без бизнес-метрик. mart_main_full содержит детерминированные показатели и QA/evidence поля.`
- deterministic: `PASS`
- independent_judge: `PASS`
- final_verdict: `PASS`
- limitation: no input dataset was supplied, so the response correctly remained at design scope; full response remains local.

Requirements: `LPV-022 PASS`; `LPV-023 PASS`; `LPV-024 PASS`.

## AES Closure Review repository rollout — 2026-08-24

All seven registered project bundle surfaces were reviewed and updated with a
thin Closure Review exposure. Repository bundle validation is PASS; this does
not change any live Project Instructions/Sources status or prove a UI sync.
Each project requires owner-led source replacement and project-specific smoke
QA before its affected live scope can be marked verified. `[Thinkers OS]`
remains `not_verified` for live sync.
