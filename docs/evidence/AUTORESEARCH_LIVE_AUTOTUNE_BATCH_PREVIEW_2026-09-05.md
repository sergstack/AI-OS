# AIOS AutoResearch — Live Autotune Program Preview (L1 + L2) — 2026-09-05

Status: **PREVIEW ONLY. This document is not a live-call authorization.**
Numbers below must be explicitly reviewed and accepted, envelope by envelope,
before any external call. Nothing in this document has been executed.

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409). Decision:
[#435](https://github.com/sergstack/AI-OS/issues/435). Implementation PR:
[#436](https://github.com/sergstack/AI-OS/pull/436).

## Reconciliation (2026-09-05) — PR #436 merge status correction

A prior execution report from this work stream stated PR #436 was **not
merged**. That was incorrect. Verified directly against the GitHub API in
this session:

- PR #436: `state: MERGED`.
- `mergedBy`: GitHub user **`sergstack`** (`is_bot: false`) — the repo
  owner's own account. No bot or automation identity is attributed to the
  merge by the API.
- Merge commit: `281585ddde18010238ff7fb22a21a2a528391d18`, single parent
  `3b81126cb754a3b4021fa16666b418e62eda5c90` (a squash/rebase-style merge,
  not a two-parent merge commit).
- Commit author on `281585d`: `sergstack <SStegancev@mail.ru>`.
- Commit timestamp: `2026-09-05T02:02:29+03:00` (`2026-09-04T23:02:29Z`).
- `281585d` is confirmed to be the current tip of `origin/main`.

Not observable from the API or git metadata, and therefore not claimed:
*how* the merge was performed (web UI vs. `gh`/CLI vs. some other client).
Only the account and commit facts above are asserted.

This corrects the acceptance-criteria state: **"PR #436 merge: owner-only"
is now met** — merged by the owner, `sergstack`. The live-autotune batch
preview acceptance gate remains separately pending (unchanged by the PR
merge; per the authority matrix, `live_call_authority` and
`usage_budget_authority` are granted per-envelope, not inherited from a
merge decision).

## Pinned identity for this preview

| Field | Value |
|---|---|
| Runtime revision | `281585ddde18010238ff7fb22a21a2a528391d18` (confirmed tip of `origin/main`; supersedes the prior "to be pinned at execution time" placeholder) |
| Evidence directory | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/`, with one subdirectory per stage/case run: `l1_c1r1_smoke/` and `l2_<control_name>/` (`l2_beneficial/`, `l2_harmful/`, `l2_noop/`, `l2_mixed/`). Fixed now as the naming convention; individual run subfolders are created only at actual execution time, never in advance of a real call. |
| Authority reference | (1) Owner decision on issue [#435](https://github.com/sergstack/AI-OS/issues/435) (2026-09-05) — design authority for MD-2 Option A + subject-content Option 2, already implemented and merged. (2) PR [#436](https://github.com/sergstack/AI-OS/pull/436) merge by `sergstack` at `281585d` — implementation-acceptance authority, now satisfied (see Reconciliation above). (3) This task's own instruction (session of 2026-09-05) — authorizes *preparing* this two-stage L1/L2 program document and correcting the record; does **not** authorize any live call. Per `docs/standards/autoresearch_v02_authority_matrix.json`, `live_call_authority` and `usage_budget_authority` are both `owner_only` and are granted per-envelope — neither has been granted for any envelope in this document. |

## Cost-ceiling validity check against the current live contract

The previous version of this document proposed `max_cost_amount: 0` /
`max_cost_currency: USD`. Checked against
`docs/standards/AUTORESEARCH_V02_LIVE_CONTRACT.md` §6 and its validator
(`scripts/autoresearch_v02_live_contract_validator.py`):

**`0` is not a valid `max_cost_amount` for any batch that is actually
authorized to run.** The validator's `UNBUDGETED_AUTHORIZATION` rule
requires `max_cost_amount` to be a **strictly positive number** whenever
`authority_status` or `transport_authority_status` is `"authorized"` — this
is enforced unconditionally in code (`scripts/autoresearch_v02_live_contract_validator.py:74`,
`if not (isinstance(doc["max_cost_amount"], (int, float)) and doc["max_cost_amount"] > 0)`),
with a dedicated regression test proving zero is rejected:
`tests/test_autoresearch_v02_live_contract.py::test_authorized_with_zero_cost_amount_rejected`.
The schema field description states this directly: *"REQUIRED to be a
positive number before transport_authority_status/authority_status may be
'authorized' for a usage_billed transport."*

The contract's prose (§6) frames the positive-cost requirement as applying
to transports it classifies as "potentially usage-billed," and separately
notes a browser-session transport (`playwright_mcp`) has no
*AutoResearch-side* per-call cost today. But the validator code draws no
such exemption by `credential_source_class` — it requires a positive
`max_cost_amount` for **any** authorized batch, and the accompanying test
suite confirms this unconditionally. Code and tests, not the prose gloss,
are what actually gate a batch config as valid.

**Conclusion: the `0 USD` ceiling is invalid as written and cannot be
carried into a live batch config that sets `authority_status: authorized`
or `transport_authority_status: authorized`.** A revised, strictly-positive
`max_cost_amount` (even a small one) must be owner-set before any envelope
below can pass the contract's own validator. Setting that number is a
`usage_budget_authority` decision — `owner_only` — and is not proposed here;
it is flagged as a required input to the authorization this document is
building toward.

## Program structure: two gated stages before any real autotune batch

Per this task's instruction, live execution is split into two stages, run
in order, each with its own acceptance check. **Stage L2 may not start
before Stage L1 passes its acceptance check. A separate, bounded,
real instruction-autotune batch may not start before all of Stage L1 and
all four Stage L2 controls pass.** No candidate is ever auto-promoted at
any stage — adoption stays a separate owner decision, unconditionally.

### Stage L1 — C1-R1 live smoke

Re-run the same, already-vetted C1-R1 candidate through the corrected
pipeline (directional Judge + bounded mutable-surface excerpt). Unchanged
from the prior version of this document except for the pinned runtime
revision and evidence path above:

| Field | Value |
|---|---|
| Candidate ID | `C1-R1` (`candidate_patch_hash: 9e7d0a1ea07f4b626b7be9a5bbd42b3df950b3481016fddf43d86d26bc45509c`) |
| Mutable surface | `MUT-ROUTING-TIEBREAK` (only) |
| Case ID / family | `c1-routing-tiebreak-coding-task-prep` / `routing` |
| Baseline revision | `0b1ce29386342ef4e1884d8a58b574445572575e` |
| Runtime revision | `281585ddde18010238ff7fb22a21a2a528391d18` (pinned) |
| Model / transport | `playwright_mcp`, dedicated persistent Playwright profile (owner-authenticated, interactive sign-in only); model identity `ui_observed` only |
| Rerun policy | exactly 3 matched reruns (`adc.MIN_MATCHED_RERUNS`); 3→5 escalation path stays blocked |
| Subject calls | 6 (2 conditions × 3 reruns) |
| Judge calls | 6 base (2 orders × 3 reruns), `retry_limit: 1` per order-attempt |
| **Worst-case external calls** | **18** = 6 subject + up to 12 Judge |
| Evidence subdirectory | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l1_c1r1_smoke/` |

**L1 acceptance check**: terminates in exactly one of
`reject \| inconclusive \| candidate_for_owner_review`; ledger hash-chain
verifies; a real, order-consistent `subject` attribution (`A`/`B`/`both`)
is present on every retained finding (proves the directional fix actually
functions live, not only under fixtures); Judge output format-failure rate
does not exhaust the retry ceiling on more than half the order-slots. A
result of `inconclusive` is an acceptable pass for L1 (it was C1-R1's own
prior live result, and its mutation is near-cosmetic) — L1's bar is that
the *mechanism* worked correctly and observably, not that this specific
candidate shows an improvement.

### Stage L2 — live four-control calibration

The same deterministic four-control shape already proven with fake-Judge
fixtures in `tests/test_autoresearch_md2_calibration.py` (beneficial,
harmful, no-op, mixed), re-run through the **real** live Judge, so that
directional attribution and regression-veto handling are demonstrated with
actual model outputs — this is the explicit purpose of L2, since a
fixture-based pass proves the comparator's arithmetic but not that a real
Judge produces the signal the comparator needs.

| Control | Predeclared expected decision | Purpose |
|---|---|---|
| Beneficial | `keep_candidate` or `candidate_for_owner_review` | proves a real, order-consistent improvement signal reaches `aggregate_decision` |
| Harmful | `discard` or `reject` | proves a real regression signal is caught, not smoothed over |
| No-op | `inconclusive` | proves a genuinely indistinguishable case does not get forced into a false positive/negative |
| Mixed | `reject` (regression veto wins) | proves the regression veto dominates over a simultaneous partial-improvement signal, live |

Each control needs its own case: a real baseline/candidate pair on one of
the four declared mutable surfaces (`MUT-ROUTING-TIEBREAK`,
`MUT-AIOS-CONTEXT-PRIORITY`, `MUT-AIOS-HANDOFF-WORDING`,
`MUT-HANDOFF-PROJECT-ADDITIONS`), constructed and frozen (patch-hashed,
non-sealed-holdout) so its expected direction is known *before* the live
run — the same rigor C1-R1 itself went through before being used as a
live case.

**Open prerequisite, not yet done, flagged rather than assumed**: the four
L2 control cases' concrete baseline/candidate content does not exist yet.
The only four-control artifact that exists today is the deterministic
Python fixture set in `tests/test_autoresearch_md2_calibration.py`, which
directly injects synthetic Judge findings and therefore cannot be "run
live" as-is — it validates the comparator's arithmetic, not a real Judge's
behavior. Authoring and freezing four real, small, low-risk mutations
(one per control, ideally spread across the four declared mutable
surfaces for coverage) is a prerequisite deliverable for L2 that has not
been produced. This document does not fabricate placeholder case content
to fill that gap.

| Field | Value (per control; ×4 controls) |
|---|---|
| Rerun policy | same as L1: 3 matched reruns, no escalation |
| Subject calls | 6 per control (2 conditions × 3 reruns) |
| Judge calls | 6 base per control (2 orders × 3 reruns), `retry_limit: 1` per order-attempt |
| **Worst-case external calls per control** | **18** |
| **Worst-case external calls, all 4 L2 controls** | **72** |
| Evidence subdirectory | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_<beneficial\|harmful\|noop\|mixed>/` |

**L2 acceptance check**: each of the four controls independently
terminates in its predeclared expected decision (table above); each
retained finding across all four controls carries a real, order-consistent
`subject` attribution; no control's Judge format-failure rate exhausts the
retry ceiling on more than half its order-slots. **All four must pass** —
a partial pass (e.g. 3 of 4) does not satisfy the gate to proceed to a real
autotune batch.

### Gate to a separate, bounded, real instruction-autotune batch

Only if L1's acceptance check passes **and** all four L2 controls
independently pass their acceptance checks may execution proceed to a
separate, later-authorized, bounded real instruction-autotune batch. That
batch is out of scope for this document and requires its own envelope and
its own owner authorization — this document does not propose one.

## Revised combined call/budget envelope (L1 + L2 only)

| Field | Value |
|---|---|
| Scope | Stage L1 (1 case) + Stage L2 (4 cases) = 5 case-runs total. Does **not** include any real autotune batch. |
| Runtime revision | `281585ddde18010238ff7fb22a21a2a528391d18` (pinned), verified unchanged immediately before each case-run |
| `call_timeout_seconds` | 180 (all case-runs) |
| Rerun policy | 3 matched reruns per case, fixed; no 3→5 escalation, any stage |
| `retry_limit` | 1 per Judge order-attempt, any stage |
| Worst-case subject calls | 6 (L1) + 6×4 = 24 (L2) = **30 total** |
| Worst-case Judge calls | up to 12 (L1) + up to 12×4 = 48 (L2) = **up to 60 total** |
| **Worst-case total external calls, L1+L2 combined** | **90** (18 per case-run × 5 case-runs) |
| `max_provider_calls` (per case-run budget) | 18 — set independently on each case-run's subject-side and Judge-side `BudgetState` (existing wiring keeps these two pools independent per case-run, per the standing budget-wiring note below; this is *not* a single shared pool across all 5 case-runs) |
| `max_cost_amount` / `max_cost_currency` | **not yet valid as proposed** — see Cost-ceiling validity check above. Must be a strictly positive number, owner-set, before any case-run's config may declare `authority_status: authorized`. No amount is proposed here; that is a `usage_budget_authority` decision. |
| Program-level stop condition (new, since nothing in the existing wiring aggregates across case-runs) | hard-stop the entire L1+L2 program, do not start the next case-run, if the running total of actually-consumed external calls across already-completed case-runs plus this case-run's worst case would exceed **90** |
| Per-case-run stop conditions (unchanged from the prior single-candidate version, applied to every one of the 5 case-runs) | a 19th external call would be needed by that case-run; that case-run's frozen patch/hash fails to verify unchanged immediately before running; context drift from the declared surface/excerpt; model/evaluator/transport identity drift from what is declared for that case-run; a captured response/hash cannot be preserved; anything requiring a change to `evaluate_case_non_inferiority`/`evaluate_case_material_improvement`/`aggregate_decision`; anything requiring active Project Instructions/routing changes; that case-run's Judge format-failure rate exhausts the retry ceiling on more than half its order-slots |
| Sequencing stop condition | do not start Stage L2 if Stage L1 does not pass its acceptance check; do not start any real autotune batch if Stage L1 or any of the four Stage L2 controls does not pass |
| Rollback | discard ephemeral shadow worktrees per case-run (automatic, `asr.remove_shadow_worktree`); no active Project, `main`, or committed artifact is touched by any case-run itself |
| Evidence directory (program root) | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/`, one subdirectory per case-run (see per-stage tables above) |

## Budget-wiring note (standing, unchanged from the prior version)

`autoresearch_coordinated_session.py`'s `build_live_controller` and
`Controller.run_experiment` each call `RoleBudget.as_shared_state()`
independently, so the subject-side and Judge-side call counts are tracked
as two independent `BudgetState` pools per case-run invocation, not one
shared pool. This does not change the per-case-run worst-case bound of 18
(subject only ever needs 6; Judge only ever needs up to 12 against the
same `max_provider_calls: 18` ceiling on each side). It does mean nothing
in the existing code aggregates consumption **across** the 5 case-runs in
this program — the new program-level stop condition above is an
operator/reporting discipline for this multi-case-run program, not an
enforced code-level guarantee, and must be tracked manually against the
evidence recorded after each case-run.

## Execution-strategy note (standing, unchanged from the prior version)

This session's tool architecture still cannot bind a live `mcp_call`
inside a single `Controller.run_experiment` process call. If any envelope
above is authorized, execution would use the same owner-authorized
disposable-bridge pattern already used for C1-R1: pure functions compute
exact payload text with no live call; the operator drives each real
submission by hand through the real browser tools; genuine captures are
fed into a thin, honestly-labeled transport satisfying the existing
`BrowserSessionTransport`/`JudgeModel` protocols (routing through the real
`lba.invoke()`) so budget accounting and `LiveTransportError` handling are
real; the real `Controller.run_experiment` then runs once over the
pre-captured data, per case-run. Not a new capability — the same pattern
already used and evidenced for C1-R1.

## What is not requested by this document

- No authorization to execute L1, L2, or any real autotune batch is
  requested here.
- No `max_cost_amount` figure is proposed — that positive number must be
  separately owner-set before any case-run config can pass the live
  contract's own validator.
- No L2 control case content (baseline/candidate mutations) is authored
  here — that is a separate prerequisite deliverable, not yet produced.
- No auto-promotion or adoption of any candidate at any stage — adoption
  is a separate owner decision at every gate, unconditionally.
