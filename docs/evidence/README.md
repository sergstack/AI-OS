# Verification Evidence

This directory contains observed smoke-QA and pilot-result evidence. Evidence
records describe what was checked; they do not grant owner acceptance,
production authorization, or a change in the repository's current status.

Start with [`MASTER_STATUS.md`](../../MASTER_STATUS.md) for gates and
[`CURRENT_STATUS.md`](../../CURRENT_STATUS.md) for the current state.

Current decision evidence:

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
