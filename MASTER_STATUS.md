# Master Status

## Repository Governance

- status: governance-validation-added
- last_checked: 2026-07-07
- production_promotion: no

## Validation Gates

- Project instructions length: <= 8000 chars
- Public safety scan: required
- No raw absolute local paths: required
- Manifest/path consistency: required
- Knowledge bundle consistency: required
- Knowledge index coverage: required
- Codex Goal Mode default scan: required
- Pytest validation script regression tests: required
- Smoke QA: required
- Pilot case: required before production promotion

## Operational Gates

- ChatGPT Project sync checklist: required
- Knowledge_Bundles upload layer: required for compact Sources sync
- Smoke QA refresh after sync: candidate evidence recorded on 2026-07-06
- One pilot case per project: required before production promotion
- Production promotion remains no until pilots pass

## Canonical Workflow Patterns

- Analytical Memo Factory via Codex APP: active
- Route: Analyst -> `[Analytics]` -> `[Codex]` -> Codex APP -> Python -> LLM -> Judge/QA -> Human
- Goal Mode: default for broad repo/workflow goals; strict task packages remain
  available for high-risk, already-scoped, ultra-long, or explicitly requested work.
- ChatGPT Project Knowledge upload: compact `Knowledge_Bundles` by default.
- StreamDeck: v2.7 active; v2.8 candidate/manual-only until human migration and acceptance.

## Evidence Pointers

- `SMOKE_QA_RESULTS.md` — `[AI OS]` smoke QA evidence from 2026-07-06.
- `CROSS_PROJECT_SMOKE_QA_RESULTS.md` — cross-project smoke QA evidence from 2026-07-06.
- `CHATGPT_PROJECT_SYNC_CHECKLIST.md` — manual sync status.
- `PILOT_CASES.md` — pilot backlog; pilot completion still requires result evidence.
- `StreamDeck/README.md` — StreamDeck active/candidate status.

## Project Instructions Rule

`PROJECT_INSTRUCTIONS.md` is the compact behavior kernel for each ChatGPT Project.

Use `Knowledge/` for supporting policies, templates, examples, checklists, and detailed workflows.

If `PROJECT_INSTRUCTIONS.md` exceeds 8000 characters, do not paste it into ChatGPT Project Settings. Split supporting content into `Knowledge/` and keep only routing, scope, evidence, output, and critical safety rules in Project Instructions.
