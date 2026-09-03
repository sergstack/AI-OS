# Smoke QA Result — Analytics

Date: 2026-08-21 (sections 1-9); coverage note added 2026-09-03
Scope: `analytics-live-response-optimization`
Source checklist: `Knowledge/SMOKE_QA_FOR_ANALYTICS.md`

## Result

```text
smoke_qa_status: partial_pass — sections 1-9 pass; sections 10-11 not_run
failed_questions: none (of the sections actually run)
residual_risks:
- Smoke QA checks documentation behavior only; it is not production readiness.
- The focused live rerun used a small supplied fixture, not an owner data source.
- A real source-backed pilot is still required before production readiness.
- Section 10 (Quantitative sanity gate) and section 11 (Analytical Judge gate) were
  added to the checklist 2026-09-01/02, after this run, and have not been exercised
  against the live ChatGPT project. This file's "pass" previously read as full
  coverage; corrected 2026-09-03 to make the gap explicit rather than implied.
next_step: run a bounded real-data pilot while keeping production status NOT AUTHORIZED; separately, run sections 10-11 against the live project and record their result here
```

## Question checks

- [x] Scope/routing question passes.
- [x] Main files question passes.
- [x] Compact/full question passes.
- [x] Charts question passes.
- [x] Memo question passes.
- [x] Stop conditions question passes.
- [x] Acceptance question passes.
- [x] Short-task / anti-bloat question passes.
- [x] Missing-data compact fast path passes.
- [ ] Quantitative sanity gate question — NOT RUN (checklist section added after this smoke QA record).
- [ ] Analytical Judge gate question — NOT RUN (checklist section added after this smoke QA record).

## Evidence

- In-project analytics capability is defined in `PROJECT_INSTRUCTIONS.md` and `Knowledge/IN_PROJECT_ANALYSIS_MODE.md`.
- Handoff is limited by `Knowledge/ROUTING_AND_HANDOFF.md` and `Knowledge/CODEX_TASK_PACKETS.md`.
- Main file rules are defined in `Knowledge/MAIN_FILES_STANDARD.md`, `Knowledge/ANALYTICS_WORKFLOW.md`, and `Knowledge/MARTS_DESIGN.md`.
- QA and acceptance are defined in `Knowledge/QA_CHECKLIST.md` and `Knowledge/ACCEPTANCE_CRITERIA.md`.
- External `[ANALYTICS]` instructions were updated and verified after reload at 7,703 characters.
- Refreshed `ANALYTICS_05_QA_GOVERNANCE_ROUTING.md` was uploaded; the prior same-name source remains visible pending an explicit deletion decision. **Unresolved as of 2026-09-03** (flagged by `docs/evidence/PROJECT_WIDE_REVISION_REVIEW_2026-09-03.md` as a dangling note with no owner/date): this describes external ChatGPT Project Sources state that cannot be verified or resolved from the repository. Resolve by manually deleting the duplicate-named source in the live ChatGPT UI, then update this line.
- The same no-data prompt decreased from 1,850 to 1,034 visible characters (44.1%), removed the placeholder Top-3 table, and retained `NOT CALCULABLE`, confidence, minimum input, and next action.
- The supplied-data regression case retained ranking, the zero-denominator guard, the root-cause boundary, QA/limitations, and the `[Analytics]` → `[Codex]` handoff boundary.
- Targeted repository validation: 38 tests passed; Local Developer Worker test parse `RUN-7f1bcfa5e1e24979` independently recorded `run_status: passed` with observed exit code `0`.
