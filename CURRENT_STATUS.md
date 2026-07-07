# Current Status — AI OS

- repo_version: v05
- project: AI-OS repository
- last_checked: 2026-07-07
- production_promotion: no
- project_instructions_path: ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md
- knowledge_path: ChatGPT/[AI OS]/Knowledge/
- default_upload_mode: Knowledge_Bundles
- default_upload_list: ChatGPT/[AI OS]/Knowledge_Bundles/UPLOAD_LIST.md
- smoke_qa_status: pass
- runtime_smoke_status: candidate
- realistic_pilot_status: not_run
- acceptance_status: candidate / ready for human review
- smoke_qa_evidence: SMOKE_QA_RESULTS.md; CROSS_PROJECT_SMOKE_QA_RESULTS.md
- validation_gates: see `MASTER_STATUS.md` — "Validation Gates" and "Operational Gates" (canonical lists; do not copy them here)
- blocked_items:
  - embeddings
  - semantic search
  - vector DB
  - web UI
  - agentic workflows
  - autonomous retrieval

## Current state

The repository contains ChatGPT project packages, compact Knowledge bundles,
Codex APP execution contracts, routing docs, StreamDeck candidate artifacts, and
repository governance checks.

`PROJECT_INSTRUCTIONS.md` files must stay compact. Supporting policies, examples, templates, checklists, and detailed workflows belong in `Knowledge/`.

Recent verified state:

- Goal Mode is the default; strict task packages are reserved for high-risk,
  already-scoped, ultra-long, or explicitly requested work.
- ChatGPT Project upload mode is compact `Knowledge_Bundles` by default.
- `SMOKE_QA_RESULTS.md` and `CROSS_PROJECT_SMOKE_QA_RESULTS.md` record
  2026-07-06 smoke QA evidence. Smoke QA does not equal production readiness.
- `PILOT_CASES.md` remains backlog/unsupported until pilot result evidence is
  recorded.
- StreamDeck v2.7 remains active; v2.8 remains candidate/manual-only.

## Next action

Run repository validation before PR review: use the canonical command set from `AGENTS.md` ("Validation" section) or `python3 scripts/sync_aios.py`, plus `python3 -m pytest tests/ -q`.

Then complete operational verification:

- `CHATGPT_PROJECT_SYNC_CHECKLIST.md`
- execute and record pilot results from `PILOT_CASES.md`
- keep production promotion blocked until accepted pilot evidence exists
