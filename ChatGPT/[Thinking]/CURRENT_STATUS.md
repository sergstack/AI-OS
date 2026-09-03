# [Thinking] Current Status

Status: active
Owner: Sergey / Thinking Lead
Last updated: 2026-09-03
Last smoke QA: 2026-07-31 — repository contract pass; external behavior pass after 2 targeted reruns
Last pilot: `PILOT-THINKING-001` (2026-08-27) — one live decision memo, recorded `candidate` / `medium` confidence in root `docs/evidence/PILOT_RESULTS_2026-08-27_THINKING.md`; next step is owner review, then a further bounded pilot (see root `docs/operations/PILOT_CASES.md`)
- status_scope: ChatGPT/[Thinking]
- status_verified_revision: cddceb1f738191e67d03459e73dfa6c6a99db559

## Active canonical files

| File | Status | Purpose |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | active | core project instructions |
| `README.md` | active | project setup and loading guidance |
| `CURRENT_STATUS.md` | active | live status tracking |
| `SMOKE_QA_RESULTS.md` | active | smoke QA record |
| `DECISION_LOG.md` | active | reusable decision record |
| `Knowledge/INDEX.md` | active | canonical file index |
| `Knowledge/REVISOR_REWRITE.md` | active | rewrite standard |
| `Knowledge/DECISION_STATUS_AND_REVISIT.md` | active | decision status standard |
| `Knowledge/THINKERS_LENS_ROUTER.md` | active | bounded lens selection for real decisions |
| `Knowledge/THINKERS_CONFLICT_MAP.md` | active | provisional cross-author conflict boundaries |
| `Knowledge/THINKERS_SYNTHESIS_PATTERNS.md` | active | five active provisional synthesis patterns mirrored from Thinkers OS |
| `Knowledge/THINKERS_APPLICATION_LOG.md` | active | empty append-only real-case logging schema |

## Candidate files

| File | Status | Why candidate |
|---|---|---|
| `Knowledge/THINKING_WORKFLOW.md` | candidate | workflow reference, not status source |
| `Knowledge/DECISION_MEMO_TEMPLATE.md` | candidate | template, not policy |
| `Knowledge/RISK_REVIEW.md` | candidate | supporting review guidance |
| `Knowledge/JUDGE_REVIEW.md` | candidate | supporting review guidance |
| `Knowledge/STRATEGY_OPTIONS_TEMPLATE.md` | candidate | supporting template |
| `Knowledge/ROUTING_AND_HANDOFF.md` | candidate | routing reference |
| `Knowledge/AI_OS_REFERENCE.md` | candidate | external reference |

## Deprecated / do not load as core

| File | Reason |
|---|---|
| none | no deprecated core files identified |

## Recently resolved gaps

- Dedicated decision log added.
- Smoke QA results file added.
- Explicit status/revisit standard added in a standalone canonical file.
- README now points to the canonical index file.
- Scenario analysis template exists and is covered by `THINKING_03_ROUTING_AND_TEMPLATES.md` (moved here 2026-09-03 — was miscategorized under "Current gaps" despite reading as already resolved).

## Current gaps

- Smoke QA remains documentation-level and does not replace a pilot case.
- Root path decision remains canonicalized to `ChatGPT/[Thinking]`.
- External ChatGPT sync is complete for Project Instructions and all four authoritative bundles.
- External behavioral smoke initially found two missing explicit fields; the Project Instructions gate was clarified and both targeted reruns passed.
- One prospective `[Thinking]` application pilot ran 2026-08-27 (`PILOT-THINKING-001`, see "Last pilot" above) with `candidate`/`medium`-confidence result; broader application effectiveness beyond this one pilot remains unverified.

## Thinkers synthesis status

- repository bundle: synchronized to external `[Thinking]`; follow-up instruction fix verified
- pattern count: 5 active provisional read-only mirrors
- isolated patterns excluded: Drucker, Boyd, Munger, Ohno, Simon, Goldratt, Rumelt, Rogers, Norman (corrected 2026-09-03 to match `[Thinkers OS]`'s current portfolio — Rumelt/Rogers/Norman were added there 2026-08-21 and this list had not been updated; see `docs/evidence/PROJECT_WIDE_REVISION_REVIEW_2026-09-03.md`)
- pilot candidate revisions: excluded pending separate Judge authorization
- owner acceptance: pending
- production status: NOT AUTHORIZED

## Next review trigger

- new project instructions change;
- routing conflict;
- judge/revisor failure;
- decision status missing in important outputs;
- handoff confusion;
- smoke QA fail.
