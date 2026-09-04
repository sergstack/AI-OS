# AIOS AutoResearch — First Live Autotune Batch Preview — 2026-09-05

Status: **PREVIEW ONLY. This document is not a live-call authorization.**
Per the owner's own instruction, this preview is "the only remaining owner
gate before live autotune" — numbers must be reviewed and accepted before
any external call. Nothing in this document has been executed.

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409). Decision:
[#435](https://github.com/sergstack/AI-OS/issues/435). Implementation:
branch `codex/issue-435-md2-directional-observation`, deterministic tests
+ four-control calibration passing (see
`AUTORESEARCH_MD2_IMPLEMENTATION_CLOSURE_REVIEW_2026-09-05.md`).

## Why this candidate, this batch

Per the owner's instruction to "start with a small representative set, not
repository-wide optimization," this preview proposes re-running the
**exact same candidate as C1-R1** — not a new one — under the now-fixed
pipeline (directional Judge, bounded mutable-surface excerpt). This is a
deliberate methodological choice: C1-R1 is already fully vetted (frozen,
patch-hash-verified, previously run and evidenced), and re-running it lets
the result be read against a known prior baseline (`inconclusive`, produced
by a pipeline that could structurally never do otherwise) rather than
introducing a brand-new, unvetted candidate at the same time as a pipeline
change.

## Batch envelope

| Field | Value |
|---|---|
| Candidate ID | `C1-R1` (unchanged; `candidate_patch_hash: 9e7d0a1ea07f4b626b7be9a5bbd42b3df950b3481016fddf43d86d26bc45509c`) |
| Mutable surface | `MUT-ROUTING-TIEBREAK` (only) |
| Case ID / family | `c1-routing-tiebreak-coding-task-prep` / `routing` (same case as C1-R1, for direct comparability) |
| Baseline revision | `0b1ce29386342ef4e1884d8a58b574445572575e` |
| Runtime revision | this branch's tip once merged, or the branch itself if run pre-merge under explicit owner sign-off — to be pinned exactly at execution time |
| Model / transport | `playwright_mcp`, dedicated persistent Playwright profile (owner-authenticated, interactive sign-in only — never automated); model identity `ui_observed` only, never predetermined (prior runs observed `gpt-5-6-thinking`, not pinned as a requirement) |
| Rerun policy | exactly `adc.MIN_MATCHED_RERUNS` = 3 matched reruns, fixed; the §8 3→5 escalation path remains explicitly blocked by `Controller.run_experiment`'s `run_count` guard (unchanged) — a case that would need escalation stays `inconclusive`, never silently escalated |
| Planned subject calls | 6 (2 conditions × 3 reruns), no retry mechanism at this layer |
| Planned Judge calls | 6 (2 presentation orders × 3 reruns), `retry_limit: 1` per order-attempt |
| Retry ceiling | 1 bounded retry per Judge order-call (existing rule, unchanged) |
| **Worst-case total external calls** | **18** = 6 subject + up to 12 Judge (6 order-slots × up to 2 attempts each if every retry is needed) |
| `call_timeout_seconds` | 180 |
| `max_provider_calls` | **18** on each of the subject-side and Judge-side budgets — see budget-wiring note below; this is the value both must be set to |
| `max_cost_amount` / `max_cost_currency` | `0` / `USD` — plan-included only; abort any call that would require paid overage |
| Stop conditions | any of: a 19th external call would be needed; C1-R1's patch/hash fails to verify unchanged immediately before the run; context drift (`equivalence_report.differences` != `["ROUTING_RULES.md"]`, or `mutable_surface_excerpt` identity mismatch); model/evaluator/transport identity drift from what's declared here; a captured response/hash cannot be preserved; anything requiring a change to `evaluate_case_non_inferiority`/`evaluate_case_material_improvement`/`aggregate_decision`; anything requiring active Project Instructions/routing changes; a Judge output format-failure rate that exhausts the retry ceiling on more than half the order-slots (a reliability signal to stop and report, not to improvise around) |
| Rollback | discard the ephemeral shadow worktrees (automatic, `asr.remove_shadow_worktree`); no active Project, `main`, or committed artifact is touched by the run itself |
| Evidence path | a fresh `evidence_dir` under `docs/evidence/` (e.g. `docs/evidence/autoresearch_md2_live_batch_2026-09-05/`), containing the schema-valid `manual_candidate_evaluation` record, the evidence package JSON, and the hash-chained ledger — exact path to be fixed at execution time and recorded in the resulting evidence doc |

## Budget-wiring note (found during implementation, not changed by it)

`autoresearch_coordinated_session.py`'s `build_live_controller` constructs
the Judge's `BudgetState` via one call to `RoleBudget.as_shared_state()`,
and `Controller.run_experiment` separately calls
`budget.as_shared_state()` again internally for the subject side —
`RoleBudget.as_shared_state()` returns a **new** `BudgetState` object each
time it is called, so in this exact wiring the subject-side and Judge-side
call counts are tracked **independently**, each against the same
`max_provider_calls` value, not a single shared pool of 18. This is
pre-existing behavior, not touched by the MD-2/subject-content
implementation. Practically: setting `max_provider_calls: 18` cannot be
exceeded by either side alone (subject only ever needs 6; Judge only ever
needs up to 12), so the stated worst-case ceiling of 18 real external calls
holds regardless of this wiring detail — flagged here for transparency,
not because it changes the bound.

## Execution-strategy note (standing, not new)

This session's tool architecture still cannot bind a live `mcp_call` inside
a single `Controller.run_experiment` process call (no way to interleave
live `mcp__playwright__browser_*` tool calls into a running Python
subprocess). If this preview is authorized, execution would use the same
owner-authorized disposable-bridge pattern as the C1-R1 run: pure functions
compute exact payload text with no live call; the operator drives each real
submission by hand through the real browser tools; genuine captures are fed
into a thin, honestly-labeled transport satisfying the existing
`BrowserSessionTransport`/`JudgeModel` protocols (routing through the real
`lba.invoke()` for both subject and Judge calls, matching production
wiring exactly) so budget accounting and `LiveTransportError` handling are
real; then the real `Controller.run_experiment` runs once over the
pre-captured data. This is not a new capability being requested — it is
the same one-off pattern already used and evidenced.

## What is different from C1-R1's own run, if this executes

- The subject will now receive the literal excerpted `## Tie-break rules`
  table text (via `mutable_surface_excerpt`), not just a byte-count
  difference — the manifest-only gap that made C1-R1's subject responses
  uninformative about the mutation is closed.
- The Judge's findings will carry a `subject` attribution (`A`/`B`/`both`),
  letting a real, order-consistent directional signal reach the comparator
  — the symmetric-mapping gap that made `material_improvement_result:
  "keep"` structurally unreachable is closed.
- The comparator itself (`evaluate_case_material_improvement`,
  `aggregate_decision`) is unchanged — the same strict-improvement rule
  applies.
- Given C1-R1's mutation is a near-cosmetic wording clarification, `inconclusive`
  remains a plausible, honest, and acceptable outcome even with both gaps
  closed — closing the gaps makes an improvement/regression signal
  *reachable*, not *guaranteed* for this specific candidate.

## Not requested by this document

No authorization to execute is requested here. This is the artifact the
owner asked to review before deciding whether to grant one.
