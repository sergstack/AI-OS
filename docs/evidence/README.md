# Verification Evidence

This directory contains observed smoke-QA and pilot-result evidence. Evidence
records describe what was checked; they do not grant owner acceptance,
production authorization, or a change in the repository's current status.

Start with [`MASTER_STATUS.md`](../../MASTER_STATUS.md) for gates and
[`CURRENT_STATUS.md`](../../CURRENT_STATUS.md) for the current state.

Current decision evidence:

- [`AUTORESEARCH_V02_LIVE_LOOP_WIRING_2026-09-04.md`](AUTORESEARCH_V02_LIVE_LOOP_WIRING_2026-09-04.md)
  records Issue #433 (follow-up to #416): the transport-binding seam that lets
  the committed harness run a bounded live `manual_candidate_evaluation`.
  **Implementation only — no live call.** Adds `Controller.run_experiment` (a
  sequencer over the frozen #392–#395/#412–#415 components, no new decision
  logic), `scripts/autoresearch_coordinated_session.py` (the one `mcp_call`
  injection point), and 14 fakes-only tests; full suite **606 passed**. A bare
  shell `experiment` stays `EXIT_BLOCKED`; a live run happens only through the
  coordinated session. Outcome vocabulary is `reject | inconclusive |
  candidate_for_owner_review` — never `keep_candidate`. A formal method
  review of MD-1..4 found MD-2/MD-3 `blocked` and MD-1 `revise`; a
  subsequent **owner scoping ruling narrowed the harness to a
  minimal-for-C1 pilot** (MD-1/MD-2 resolved narrowly, not as general
  reusable semantics; full #395 §8 escalation and a directional per-side
  Judge extension deferred to a follow-up) — see the "Owner scoping ruling:
  minimal-for-C1" section in this same doc. New batch identity fixes
  `call_timeout_seconds = 180` and does not inherit the Phase 0 authorization.
  No admission/comparator/evaluator/schema semantics change; no Phase 1; no
  active-config change. A live run of C1 still requires a separate, fresh
  owner authorization.
- [`AUTORESEARCH_V02_PHASE0_LIVE_2026-09-04.md`](AUTORESEARCH_V02_PHASE0_LIVE_2026-09-04.md)
  records the Issue #417 Phase 0 live calibration & discovery gate for Issue
  #409, executed in a coordinated live session (owner signed in to the
  dedicated Playwright MCP profile). **12 real `gpt-5-6-thinking` calls**
  (10 subject, 2 blind A/B Judge, 0 Researcher), $0 / plan-included, 0
  retries/timeouts/invalid outputs. Part A: a harmful shadow tie-break
  mutation regressed the routing outcome from `blocked` to `[Codex]` as
  designed (CAL-2b vs baseline CAL-4b); the live blind Judge flagged the
  harmful output `revise` and the baseline `pass` **order-consistently** in
  both A/B orders; deterministic hard-gate dominance is proven in code (0
  Judge calls on a `discard` precheck). Part B: all 6 behavioral families
  answered correctly on a single run each. **`measurement_verdict: pass`**;
  **`failure_discovery_result: no_failure_found`** → **#418 (Phase 1) remains
  `blocked`** (no reproducible, attribution-eligible baseline failure; a fake
  failure must not be manufactured). Machine-readable per-call records in
  `autoresearch_v02_phase0_records_2026-09-04.json`. No candidate generated or
  applied; no active configuration touched.
- [`AUTORESEARCH_V02_CLI_CONTROLLER_2026-09-04.md`](AUTORESEARCH_V02_CLI_CONTROLLER_2026-09-04.md)
  records Issue #416 (integrate matched live runs, hard gates, ledger, stable
  CLI) for Issue #409. One documented 9-verb command surface
  (`scripts/autoresearch_cli.py`, `autoresearch_cli 0.2.0`; guide
  `docs/guides/AUTORESEARCH_CLI.md`) integrating the v0.1 validator / shadow
  runner / comparator / ledger and the v0.2 #412–#415 components through real
  import points. Every external-calling verb has a no-network `--dry-run`;
  `doctor` fails (exit 3) before any call when authority / budget / context /
  evaluator identity is missing; a real run without a wired transport reports
  `blocked` (exit 4). `RunManifest` (additive schema) is the durable
  bounded-resume state; `cleanup` removes only registered ephemeral
  worktrees. Runs no Phase 0/1 batch; changes no active configuration.
- [`AUTORESEARCH_V02_RESEARCHER_SMOKE_2026-09-04.md`](AUTORESEARCH_V02_RESEARCHER_SMOKE_2026-09-04.md)
  records Issue #415 (real failure intake, attribution, bounded Researcher
  proposal flow) for Issue #409. `scripts/autoresearch_failure_intake.py` +
  additive `schemas/autoresearch_failure_record.schema.json` /
  `autoresearch_researcher_proposal.schema.json` (no v0.1 schema modified) +
  frozen `docs/standards/autoresearch_v02_researcher_contract.json`.
  Observation / reproduction / attribution / eligibility are separate
  machine-checkable states; a field observation is never `reproduced` on
  intake; reproduced-without-causal-evidence stays `uncertain`; `rejected`
  attribution blocks any mutation proposal. `deterministic_preflight` reuses
  the v0.1 shadow-runner machinery unchanged and does not decide the
  candidate is good. In the 2026-09-04 live Phase 0 (#417) no failure
  candidate arose to route through this intake. Authorizes no candidate
  acceptance, active Project edit, merge, or production.
- [`AUTORESEARCH_V02_PARENT_FINAL_QA_2026-09-04.md`](AUTORESEARCH_V02_PARENT_FINAL_QA_2026-09-04.md)
  records the Issue #419 parent final-QA gate for Issue #409 (AIOS
  AutoResearch v0.2 — live behavioral autotuning loop), re-run after the
  live session. Children #410–#417 are delivered (PRs #420–#428) and #417's
  Phase 0 was executed live: `measurement_verdict: pass`,
  `failure_discovery_result: no_failure_found`. #418 (Phase 1) is `blocked`
  by that result — no reproducible, attribution-eligible baseline failure —
  so finalist/holdout evaluation is `not_applicable` (Branch B). **Parent
  gate `pass`**: the v0.2 live loop was built, calibrated against real model
  output (live transport + blind order-consistent Judge + deterministic-gate
  dominance), and correctly declined to promote anything under insufficient
  evidence — mirroring v0.1's #398. Recommendation: keep the harness
  available and re-engage only when a genuine field-observed failure exists;
  do not run Phase 1; manual bounded review remains sufficient. 0 finalists,
  0 candidates; promotes nothing; authorizes no merge or production. #409 may
  close on owner review.
- [`AUTORESEARCH_V02_LIVE_JUDGE_CALIBRATION_2026-09-04.md`](AUTORESEARCH_V02_LIVE_JUDGE_CALIBRATION_2026-09-04.md)
  records Issue #414 (live blind A/B semantic Judge + de-blinding boundary)
  for Issue #409. Implementation and 19 focused tests are complete
  (`scripts/autoresearch_live_judge.py`; additive
  `schemas/autoresearch_live_semantic_finding.schema.json` — the frozen #394
  schema is not modified; frozen
  `docs/standards/autoresearch_v02_evaluator_config.json` with a
  self-consistent `evaluator_version_hash`). Blinding reuses
  `alternation_order` unchanged; the reversed second pass is mandatory;
  de-blinding happens only after both orders yield schema-valid findings and
  only in the evidence layer; material order disagreement contributes
  `inconclusive` (never averaged); a `discard`-consequence deterministic
  precheck bypasses the Judge entirely. Each Judge call routes through the
  #413 transport and consumes the shared budget. The **live calibration proof
  is `blocked`** pending the coordinated live session (obvious + ambiguous +
  reversed + deterministic-hard-fail pairs with real Judge calls). Authorizes
  no candidate acceptance, merge, or production.
- [`AUTORESEARCH_V02_LIVE_BROWSER_SMOKE_2026-09-04.md`](AUTORESEARCH_V02_LIVE_BROWSER_SMOKE_2026-09-04.md)
  records Issue #413 (Playwright MCP browser-session live transport) for Issue
  #409. Implementation and 35 focused tests are complete
  (`scripts/autoresearch_live_browser_adapter.py`, additive
  `schemas/autoresearch_live_invocation.schema.json` — no v0.1 schema edited);
  the transport-neutral `invoke()` interface enforces the
  authority/budget/context/target/model-selector gates before any submission
  and maps timeout/session-loss/empty/secret-shaped captures to non-pass
  outcomes that never become a live PASS. One connection mode is implemented
  (owner-selected **dedicated persistent Playwright profile**); the concrete
  transport refuses to fabricate a response with no live `mcp_call` binding.
  The **live browser smoke was executed on 2026-09-04** (see that document's
  "Update — 2026-09-04" section): one real `gpt-5-6-thinking` call over the
  `playwright_mcp` transport, `response_hash b2539ec2…`, model `ui_observed`,
  `$0` / plan-included — a real browser answer with a non-placeholder hash in
  the pipeline. The pre-execution "blocked pending owner sign-in" body of the
  document is retained as a historical snapshot. Authorizes no candidate
  acceptance, merge, or production.
- [`AUTORESEARCH_V02_BASELINE_TRANSPORT_AUDIT_2026-09-03.md`](AUTORESEARCH_V02_BASELINE_TRANSPORT_AUDIT_2026-09-03.md)
  records the Issue #410 read-only baseline/transport-feasibility audit for
  Issue #409 (AIOS AutoResearch v0.2 — live behavioral autotuning loop): a
  full v0.1 reuse/extend/replace/protected matrix (nearly everything reuses
  unchanged), the exact blocker in `autoresearch_phase1_pilot.py` (every
  observation is hand-authored, no external call of any kind), and a
  transport-candidate matrix recommending **browser automation (Playwright
  MCP)** over an API transport, per an explicit, verbatim-recorded owner
  instruction received during the audit. Does not authorize any live call,
  credential use, or spending — that remains #411's and the owner's decision.
- [`AUTORESEARCH_PARENT_FINAL_QA_2026-09-03.md`](AUTORESEARCH_PARENT_FINAL_QA_2026-09-03.md)
  records the Issue #398 parent final QA closing Issue #388 (AIOS
  AutoResearch v0.1): all 10 children (#389-#398) reconciled against the
  original parent acceptance criteria; 0 finalists existed from #397, so
  finalist/holdout evaluation is `not_applicable` (not blocked — nothing to
  authorize); recommendation `simplify_to_manual_regression_suite` (the one
  falsification criterion that actually fired: manual review currently
  yields equivalent value at materially lower complexity, given no real
  evidence source exists yet); parent gate `pass` — the harness was
  responsibly built, calibrated, piloted, and correctly declined to promote
  anything under insufficient evidence. The harness remains available to
  re-engage once a live-Judge integration or a genuine field-observed
  failure exists.
- [`AUTORESEARCH_PHASE1_PILOT_2026-09-03.md`](AUTORESEARCH_PHASE1_PILOT_2026-09-03.md)
  records the Issue #397 Phase 1 bounded pilot for Issue #388 (AIOS
  AutoResearch v0.1): 4 of a maximum 10 shadow experiments (fewer explicitly
  permitted — no evidence-backed hypothesis was available beyond the two
  mandatory controls, a real-time protected-surface rejection test, and one
  bounded discriminating experiment) run against one immutable baseline
  revision. 0 `keep_candidate`, 1 `discard` (negative control correctly
  caught), 2 `inconclusive`, 1 rejected pre-application (protected-surface
  violation correctly caught by real anchor-scope enforcement against real
  file content). No live model call; explicitly scoped per owner
  authorization carried forward from #396. Does not justify Phase 2 — names
  that "the harness is ready; real evidence is not yet available" as the
  actual finding.
- [`AUTORESEARCH_PHASE0_CALIBRATION_2026-09-03.md`](AUTORESEARCH_PHASE0_CALIBRATION_2026-09-03.md)
  records the Issue #396 Phase 0 calibration for Issue #388 (AIOS
  AutoResearch v0.1): 23 cases across all 10 required calibration classes,
  verdict `pass`, exercising the real deterministic pipeline (#392/#393/
  #395) against calibration-owner-authored fixtures. Explicitly scoped: no
  live semantic Judge was invoked (`NOT_RUN`); does not authorize Phase 1
  (#397) on its own — two explicit owner decisions are named as required
  first.
- [`AUTORESEARCH_V01_BASELINE_AUDIT_2026-09-03.md`](AUTORESEARCH_V01_BASELINE_AUDIT_2026-09-03.md)
  records the Issue #389 read-only baseline/collision audit for Issue #388
  (AIOS AutoResearch v0.1): 27 inventoried artifacts, a reuse/extend/add/
  protected matrix, and 6 duplicate-or-conflicting-owner findings (most
  notably `PROMPT_QA_FACTORY.md`'s existing candidate lifecycle already
  governs Project-Instructions-wording changes, and `AI_EVAL_REGISTRY.md`
  must stay definitions-only, separate from any new experiment ledger). It
  does not implement the harness or authorize child #390 onward beyond
  starting.
- [`PROJECT_WIDE_REVISION_REVIEW_2026-09-03.md`](PROJECT_WIDE_REVISION_REVIEW_2026-09-03.md)
  records a 7-project revision review dispatched via the native subagent
  mechanism (one bounded `Plan` dispatch per `PROJECT_CAPABILITIES.yaml`
  capability): 34 findings (7 high / 13 medium / 14 low), no schema or
  business-logic issue, dominant pattern is stale status/evidence files. This
  is a review-and-plan record only; it does not itself apply any fix.
- [`NATIVE_SUBAGENT_DISPATCH_PILOT_2026-09-02.md`](NATIVE_SUBAGENT_DISPATCH_PILOT_2026-09-02.md)
  records the bounded native-subagent-dispatch MVP pilot on the Claude Code
  surface (follow-up to #350): 3 multi-owner executions, verdict `PASS`,
  recommended **pilot-only** pending a separate standardization decision. It
  does not authorize standardization, merge, or production.
- [`NATIVE_SUBAGENT_DISPATCH_STANDARDIZATION_2026-09-02.md`](NATIVE_SUBAGENT_DISPATCH_STANDARDIZATION_2026-09-02.md)
  records the standardization decision memo after 3 more bounded executions:
  blockers DEF-001 (workspace isolation) and native no-nesting closed
  structurally; recommendation **STANDARDIZE BOUNDED (conditional)** on a
  4-item punch-list. It does not authorize merge or production.
- [`NATIVE_SUBAGENT_DISPATCH_COMMISSIONING_2026-09-02.md`](NATIVE_SUBAGENT_DISPATCH_COMMISSIONING_2026-09-02.md)
  closes the commissioning punch-list 4/4 (dispatch-evidence schema + blocking
  linter, enforced telemetry contract, 18-dispatch sample across 7 owners with
  a guard-calibration proposal, `[AI OS]` cost/latency owner). Machine-checkable
  records in `subagent_dispatch_records_2026-09-02.json`. Judge round-2 `pass`
  → status is **`STANDARDIZED BOUNDED`** (bounded, pilot-scoped; not a
  default/unrestricted standard). It does not authorize merge or production.
- [`EXECUTABLE_CAPABILITY_ROUTING_P0_AUDIT_2026-09-02.md`](EXECUTABLE_CAPABILITY_ROUTING_P0_AUDIT_2026-09-02.md)
  records the Issue #350 P0 audit: `BLOCKED_FOR_NATIVE_DISPATCH` for executable
  dispatch, P1–P4 already owned by current canonical contracts, plus an
  owner-decision package. It does not authorize implementation.
- [`ORCHESTRATION_PRIMITIVES_P1_GAP_REVIEW_2026-08-31.md`](ORCHESTRATION_PRIMITIVES_P1_GAP_REVIEW_2026-08-31.md)
  records the Issue #344 P1.1–P1.4 classification and the bounded P1.3
  follow-up candidate; it does not authorize implementation.
- [`LOCAL_FIRST_COMPUTE_P0_AUDIT_2026-08-31.md`](LOCAL_FIRST_COMPUTE_P0_AUDIT_2026-08-31.md)
  records the Issue #345 capability/gap audit and why the initial production
  local-first allowlist remains empty.
- [`DURABLE_RUNTIME_GAP_PHASE0_2026-08-31.md`](DURABLE_RUNTIME_GAP_PHASE0_2026-08-31.md)
  records the Issue #342 Phase 0 gate and why no Restate fit test is authorized.
