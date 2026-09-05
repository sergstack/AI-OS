# AIOS AutoResearch — Live Authorization Packet — L1 + L2 — 2026-09-05

Status: **this is the one consolidated document this program needs the
owner to accept before any live call. Nothing in this document has been
executed. No candidate is authorized, accepted, or promoted by it.**

Supersedes, by consolidating, the per-stage tables already in
`AUTORESEARCH_LIVE_AUTOTUNE_BATCH_PREVIEW_2026-09-05.md` (L1 shape) and
`AUTORESEARCH_L2_CONTROLS_FREEZE_2026-09-05.md` (the four L2 controls,
frozen and gate-verified) — both remain the detailed backing evidence;
this document is the single envelope to say **AUTHORIZED** or **not yet**
against.

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409). Decision:
[#435](https://github.com/sergstack/AI-OS/issues/435). Implementation:
[#436](https://github.com/sergstack/AI-OS/pull/436) (merged). Preparation:
[#438](https://github.com/sergstack/AI-OS/pull/438).

## Authority reference

1. Owner decision on issue [#435](https://github.com/sergstack/AI-OS/issues/435) (2026-09-05): MD-2 Option A + subject-content Option 2 — design authority, implemented and merged.
2. PR [#436](https://github.com/sergstack/AI-OS/pull/436) merged by GitHub user `sergstack` (`is_bot: false`), merge commit `281585ddde18010238ff7fb22a21a2a528391d18` onto `main`@`3b81126` — implementation-acceptance authority, satisfied.
3. This session's owner instruction (2026-09-05, chat turn): explicitly authorizes *preparing* this packet, freezing the four L2 controls, and bringing PR #438 to review-ready — does **not** itself grant `live_call_authority` or `usage_budget_authority` for the envelope below.
4. Per `docs/standards/autoresearch_v02_authority_matrix.json`: `live_call_authority` and `usage_budget_authority` are both `owner_only`, granted per-envelope, with no implicit conversion from (1)-(3) above. **Granting them for the exact envelope in this document is the one remaining gate.**

The owner's own acceptance of this document — a single explicit
`AUTHORIZED`, or a revision of the numbers below — is the only additional
authority this program needs before Stage L1 begins.

## Runtime and baseline identity (all 5 case-runs)

| Field | Value |
|---|---|
| Pipeline runtime revision | `281585ddde18010238ff7fb22a21a2a528391d18` (current tip of `origin/main`) |
| Shared baseline revision | `0b1ce29386342ef4e1884d8a58b574445572575e` — verified byte-identical to `281585d` for every file any of the 5 candidates touches; held constant across all 5 case-runs per manifest invariant INV-09 |
| Evaluator identity | `evaluator_contract_version 0.3.0`, `evaluator_version_hash 960e1408c58e97d9fab1aa19c62147dbfa20de2839f90e86a7f0236ad8bdb853` — re-verified this session via `EvaluatorConfig.load(...).frozen_hash()`, no drift |
| Transport | `playwright_mcp`, dedicated persistent Playwright profile, owner-authenticated interactive sign-in only, never automated credentials |

## The 5 candidate/case identities

Two different kinds of "evidence directory" apply here, kept distinct
rather than conflated: the **identity/freeze directory** (each candidate's
patch, hashes, and spec — already committed, immutable, append-only) and
the **run-output directory** — where `Controller.run_experiment`'s own
`evidence_dir` argument actually writes.

**Run-output directory is shared across all 5 case-runs, deliberately,
not split per control**: `autoresearch_cli.py`'s `run_experiment` names its
per-case artifacts by `spec.experiment_id`
(`{experiment_id}_evidence.json`, `{experiment_id}_record.json` — no
collision risk, all 5 experiment_ids are already distinct) but appends
every completed run's record to one single file,
`evidence_dir/autoresearch_manual_evaluations.jsonl`, verified as one
hash chain by `av.verify_ledger` (confirmed against the real code, not
assumed — this is exactly the mechanism
`test_all_four_controls_ledger_hash_chain_verifies` already proves for 4
runs into one shared `tmp_path`). Pointing all 5 case-runs at the same
`evidence_dir` therefore gives this program **one continuous, verifiable,
append-only ledger across L1 and all 4 L2 controls**, instead of 5
disconnected ledgers that would each only prove their own single entry.
This corrects an earlier draft of this packet, which would have given
each control its own separate run-output directory — caught and fixed
before authorization, not left as a live-time surprise.

**Shared run-output directory for the whole program**:
`docs/evidence/autoresearch_live_l1_l2_2026-09-05/` (the program's own
root — created already, holding the L2 controls' identity subfolders
below; the ledger and per-experiment evidence/record files land directly
in this root at execution time).

| # | Stage | Candidate ID | Surface | Case ID(s) | Patch SHA-256 | Identity/freeze directory (exists now) |
|---|---|---|---|---|---|---|
| 1 | L1 | `C1-R1` | `MUT-ROUTING-TIEBREAK` | `c1-routing-tiebreak-coding-task-prep` | `9e7d0a1ea07f4b626b7be9a5bbd42b3df950b3481016fddf43d86d26bc45509c` | `docs/evidence/autoresearch_c1r1_freeze/` (unchanged, not moved — already an accepted append-only record of the 2026-09-04 run) |
| 2 | L2 beneficial | `L2-BEN-1` | `MUT-ROUTING-TIEBREAK` | `l2-ben-1-rollout-tiebreak` | `7941ec48800b5ebb751b491bd9154a344d1ba1e5b5e766ebdfa7bc4e024f0506` | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_beneficial/` |
| 3 | L2 harmful | `L2-HARM-1` | `MUT-AIOS-HANDOFF-WORDING` | `l2-harm-1-codex-handoff-fields` | `ea0084bfe80c25f56fd4b2c952e941ad022e61d6c67a130bd5e78e7e02834a9c` | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_harmful/` |
| 4 | L2 no-op | `L2-NOOP-1` | `MUT-HANDOFF-PROJECT-ADDITIONS` | `l2-noop-1-codex-fields-list` | `3132ecf427996be18987b5a9261e68d45805d61a0f32bafd256a8e3d4c7a1586` | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_noop/` |
| 5 | L2 mixed | `L2-MIXED-1` | `MUT-AIOS-CONTEXT-PRIORITY` | `l2-mixed-1-conflict-priority` (target), `l2-mixed-1-checklist-completeness` (non-target) | `c88596959994f4aeca3a079156080475c28d40ed10b6fc05bbf31a69d37d4976` | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_mixed/` |

Candidates #2–#5 were built and gate-verified against the real repository
code this session (patch scope, context equivalence, literal
subject-content propagation, schema validation, evaluator hash — see
`AUTORESEARCH_L2_CONTROLS_FREEZE_2026-09-05.md` for the full gate log per
control). Candidate #1 is unchanged from its own prior freeze — not moved,
per this contract's own append-only rule for prior records — only re-run
under the pinned current runtime revision, with its new run's own output
appended to the shared program ledger above rather than overwriting the
2026-09-04 record.

## Call/budget envelope

| Field | Value |
|---|---|
| Rerun policy | exactly 3 matched reruns per case (`adc.MIN_MATCHED_RERUNS`), fixed, for every one of the 5 case-runs; the §8 3→5 escalation path stays blocked |
| Retry policy | `retry_limit: 1` per Judge order-attempt, every case-run |
| `call_timeout_seconds` | `180`, every case-run |
| Subject calls | 6 per case-run × 5 = **30 total** |
| Judge calls (worst case) | up to 12 per case-run × 5 = **up to 60 total** |
| **Total external-call ceiling** | **90** (18 worst-case per case-run × 5 case-runs) |
| `max_provider_calls` | `18`, set on each case-run's own subject-side and Judge-side `BudgetState` independently (existing wiring keeps these two pools independent per case-run invocation — documented in the batch-preview doc's own "budget-wiring note," unchanged) |
| **`max_cost_amount`** | **`1.00`** |
| **`max_cost_currency`** | **`USD`** |

### Why `$1.00`, not `$0` — and not left to the previous document's `$0` proposal

The prior version of this program's preview proposed `$0`, matching Phase
0's own precedent (#417, "$0 / plan-included only"). Checking that number
against this repo's own code this session surfaced a real, previously
undocumented split between two enforcement points, reported here rather
than silently resolved one way:

- `scripts/autoresearch_v02_live_contract_validator.py`'s
  `UNBUDGETED_AUTHORIZATION` rule — tested, standalone, but **not called
  anywhere in the actual execution path** (`autoresearch_cli.py` only
  checks that the live-contract *document* exists, never calls
  `validate_batch_config`) — requires `max_cost_amount` to be **strictly
  positive** once a batch is `authorized`, confirmed by
  `test_authorized_with_zero_cost_amount_rejected`.
- `scripts/autoresearch_live_browser_adapter.py`'s `BudgetState.authorization_ok()`
  — the function actually wired into the real call path (`lba.invoke`,
  what Phase 0 really ran through) — explicitly treats `max_cost_amount:
  0.0` plus a set currency as a valid, authorized budget; its own code
  comment cites Phase 0's `$0` grant as exactly the case this is meant to
  accept.

**What could actually be tariffed**: today, nothing, for this specific
transport. `TransportPolicy.incremental_paid_cost` defaults to `False` and
is never set `True` anywhere in this codebase for `playwright_mcp`
(confirmed by search) — so the cost-ceiling check in `lba.invoke`
(`if policy.incremental_paid_cost and (budget.max_cost_amount or 0.0) <= 0.0: ...`)
never actually fires for this program's calls regardless of the number
declared here. The transport rides the owner's own existing, flat-rate
ChatGPT account (§6/§10 of the live contract: browser-session transports
have no AutoResearch-side per-call fee). The only ways a real charge could
occur are drift scenarios this program already treats as hard stops: (a) a
future code change flips `incremental_paid_cost` to `True` for this
transport, or (b) the actual transport silently becomes the metered
`api_openai_sdk` path instead of the browser session — both are
"transport/model/context/evaluator identity drift," already a declared
stop condition below.

**What happens at the limit**: honestly, under the code as it stands
today, hitting `max_cost_amount` triggers nothing automatically for this
transport — the operative ceiling that actually bounds real exposure for
this program is `max_provider_calls` (18 per case-run, 90 total), not
`max_cost_amount`. `max_cost_amount: 1.00 / USD` therefore functions as a
governance trip-wire and a contract-compliance value, not as an active
runtime meter: it satisfies the standalone validator's positive-number
requirement (confirmed empirically this session:
`validate_batch_config` on a copy of each frozen batch config with
`authority_status: authorized` and `max_cost_amount: 0` returns
`UNBUDGETED_AUTHORIZATION`; the same copy with `1.0` returns no findings),
it is negligible relative to any plausible real cost even if a drift
scenario above did occur, and it does not authorize or imply any
expectation of actual spend.

**Recommendation, not yet done, flagged as a real gap**: run every one of
the 5 case-runs' final batch configs through
`autoresearch_v02_live_contract_validator.validate_batch_config()`
explicitly before its first call, since this program has just shown that
check is not automatic. This is a one-line call per case-run, cheap
insurance against exactly the class of contract-vs-runtime drift found
here — recorded as an explicit step in the sequencing rules below, not
left implicit.

## Stop conditions

**Per case-run** (all 5, unchanged from the batch-preview doc): a 19th
external call would be needed by that case-run; that case-run's frozen
patch/hash fails to verify unchanged immediately before running; context
drift from the declared surface/excerpt; model/evaluator/transport
identity drift from what is declared for that case-run; a captured
response/hash cannot be preserved; anything requiring a change to
`evaluate_case_non_inferiority` / `evaluate_case_material_improvement` /
`aggregate_decision`; anything requiring active Project Instructions/
routing changes; that case-run's Judge format-failure rate exhausts the
retry ceiling on more than half its order-slots; `autoresearch_v02_live_contract_validator.validate_batch_config()`
returns any finding for that case-run's final batch config once it flips
to `authorized`.

**Program-level**: hard-stop the whole L1+L2 program, do not start the
next case-run, if the running total of actually-consumed external calls
across completed case-runs plus the next case-run's worst case would
exceed **90**. Consumption *counting* is an operator/reporting discipline,
not an automatically-enforced code guarantee — `RoleBudget.as_shared_state()`
gives each case-run invocation an independent call-budget pool (documented
in the batch-preview doc's budget-wiring note), so nothing in the existing
code sums call consumption across case-runs; it must be tracked against
each case-run's recorded evidence as the program proceeds. Ledger
*integrity*, separately, is verified for real by code, not just tracked by
hand: `av.verify_ledger()` on the shared
`docs/evidence/autoresearch_live_l1_l2_2026-09-05/autoresearch_manual_evaluations.jsonl`
after every case-run must return no findings before the next case-run
starts — a hash-chain break on any entry stops the program immediately, per
manifest invariant INV-04.

## Sequencing rules

1. Run L1 (`C1-R1`) first. Do not start any L2 control before L1's own
   acceptance check completes (§ "L1 acceptance check" in the batch-preview
   doc: terminates in `reject | inconclusive | candidate_for_owner_review`;
   ledger hash-chain verifies; real order-consistent `subject` attribution
   present; Judge format-failure rate does not exhaust the retry ceiling on
   more than half the order-slots).
2. Run the four L2 controls in the order beneficial → harmful → no-op →
   mixed. Each control's batch config passes
   `autoresearch_v02_live_contract_validator.validate_batch_config()`
   cleanly immediately before that control's first call.
3. **All four L2 controls must independently reach their predeclared
   expected decision** (beneficial: `keep_candidate`/`candidate_for_owner_review`;
   harmful: `discard`/`reject`; no-op: `inconclusive`; mixed: `discard`/`reject`
   with the reason citing regression, not the local gain) for the gate to
   a real autotune batch to open. A partial pass (e.g. 3 of 4, or a control
   landing on a decision other than its predeclared one) does **not**
   satisfy the gate — report it honestly as a finding against this
   program's own design or the pipeline, whichever it actually is, and
   stop for a fresh owner decision rather than improvising past it.
4. Only after 1–3 all pass may execution proceed to a separate, later,
   bounded real instruction-autotune batch. That batch is out of scope for
   this packet and needs its own envelope and its own owner authorization.
5. No candidate is ever auto-promoted at any point in this sequence.
   `keep_candidate` / `candidate_for_owner_review` is exactly that —
   evidence for a separate owner review — never accepted, active,
   merge-ready, or production-authorized by this program itself (manifest
   invariant INV-08, unchanged).

## Rollback

Per case-run: discard the ephemeral shadow worktree (automatic,
`asr.remove_shadow_worktree`) — no active Project, `main`, or committed
artifact is touched by any case-run itself. Nothing in this program
requires any other rollback mechanism: no active configuration, merge
state, or production state is ever a mutation target (manifest
`rollback_ownership`, unchanged).

## What this document does not do

- Does not authorize any live call by itself.
- Does not propose a `max_cost_amount` casually — the number above is
  reasoned from the actual code path that would run, not copied forward
  from Phase 0 or picked arbitrarily.
- Does not start Stage L1, any L2 control, or any real autotune batch.
- Does not change `adc.py`'s comparator functions, the evaluator contract,
  or any schema.

**The one remaining ask**: the owner's explicit `AUTHORIZED` against this
exact envelope (or a revision of any number in it) is the single gate this
program is waiting on. On receiving it, execution proceeds through the
sequencing rules above without further intermediate confirmation, subject
to the stop conditions and the fail-closed rules already established by
this program's own contract (no `inconclusive` becomes a pass; no
candidate is auto-promoted; any protected-contract blocker stops the
program and is reported, not improvised around).
