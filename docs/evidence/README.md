# Verification Evidence

This directory contains observed smoke-QA and pilot-result evidence. Evidence
records describe what was checked; they do not grant owner acceptance,
production authorization, or a change in the repository's current status.

Start with [`MASTER_STATUS.md`](../../MASTER_STATUS.md) for gates and
[`CURRENT_STATUS.md`](../../CURRENT_STATUS.md) for the current state.

Current decision evidence:

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
