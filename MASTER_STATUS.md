# Master Status

## Repository Governance

- status: governance-validation-added
- last_checked: 2026-08-12
- production_promotion: no

## Validation Gates

Canonical list. Other documents (including `CURRENT_STATUS.md`) must reference this section instead of copying it; the canonical check-command set lives in `AGENTS.md` ("Validation").

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
- StreamDeck: v3.0 Dual Deck repo candidate; v2.7 remains the physical rollback baseline until owner migration, device QA, export/import, and acceptance.

## Evidence Pointers

- `docs/evidence/SMOKE_QA_RESULTS.md` — `[AI OS]` smoke QA evidence from 2026-07-06.
- `docs/evidence/CROSS_PROJECT_SMOKE_QA_RESULTS.md` — cross-project smoke QA evidence from 2026-07-06.
- `docs/evidence/EXECUTABLE_CAPABILITY_ROUTING_P0_AUDIT_2026-09-02.md` — Issue #350 P0 audit: `BLOCKED_FOR_NATIVE_DISPATCH`; P1–P4 already owned by canonical contracts; no MVP implemented. See `docs/evidence/README.md` for the other decision-evidence records (#342, #344, #345).
- `docs/operations/CHATGPT_PROJECT_SYNC_CHECKLIST.md` — manual sync status.
- `docs/operations/PILOT_CASES.md` — pilot backlog; pilot completion still requires result evidence.
- `StreamDeck/README.md` — StreamDeck active/candidate status.

## Repository State Reconciliation

Deterministic state at the 2026-08-12 baseline (`main`
`21526a812e5ea4823c64815b84f6792f10b563dd`):

- `PROJECT_REGISTRY.md` is the canonical topology owner for seven governed
  ChatGPT Projects and the AES applicability matrix.
- AES phase artifacts and bundle rollout are repository-present; the historical
  adoption plan remains historical and now points to current repository state.
- Local repository checks can establish file, schema, bundle, index, routing,
  and test state only.

External state remains evidence-dependent. ChatGPT Project UI sync, observed
smoke/pilot execution, owner acceptance, PR review, merge, production
authorization, and deploy must not be inferred from repository definitions or
artifact presence.

## Project Instructions Rule

`PROJECT_INSTRUCTIONS.md` is the compact behavior kernel for each ChatGPT Project.

Use `Knowledge/` for supporting policies, templates, examples, checklists, and detailed workflows.

If `PROJECT_INSTRUCTIONS.md` exceeds 8000 characters, do not paste it into ChatGPT Project Settings. Split supporting content into `Knowledge/` and keep only routing, scope, evidence, output, and critical safety rules in Project Instructions.
