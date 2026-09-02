# Current Status — AI OS

- repo_version: v05
- project: AI-OS repository
- last_checked: 2026-09-02 (executable capability routing P0 audit for #350)
- production_promotion: no
- project_instructions_path: ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md
- knowledge_path: ChatGPT/[AI OS]/Knowledge/
- default_upload_mode: Knowledge_Bundles
- default_upload_list: ChatGPT/[AI OS]/Knowledge_Bundles/UPLOAD_LIST.md
- smoke_qa_status: pass
- runtime_smoke_status: candidate
- realistic_pilot_status: candidate (AI OS, Thinking, Analytics, and one cross-project routing/resume pilot passed; broader pilot set not run)
- durable_runtime_gap_status: not proven; Restate Phase 1 not authorized
- local_first_compute_status: candidate policy; production allowlist empty; owner review pending
- orchestration_primitives_p1_status: review complete; P1.3 partial gap; implementation owner review pending
- executable_capability_routing_status: resolved; P0 audit BLOCKED_FOR_NATIVE_DISPATCH; P1–P4 already owned by canonical contracts; no MVP implemented; owner accepted the audit and closed #350 as completed (2026-09-02)
- native_subagent_dispatch_status: STANDARDIZED BOUNDED (2026-09-02; owner-approved, Judge round-2 pass). Bounded, pilot-scoped: root -> bounded routed slice -> Plan child + isolation:"worktree" -> evidence/patch -> root -> validation/AES continuation. Plan child cannot use the native Agent tool; no write-capable child; root is sole router + writer; no child->child; one execution_id per user goal. Commissioning punch-list 4/4 closed — dispatch-evidence schema + blocking linter (scripts/check_subagent_dispatch_evidence.py in docs-safety), enforced telemetry contract, 18 hardened dispatches across 7 owners, guard-calibration proposal (thresholds unchanged), [AI OS] cost/latency owner. NOT a default/unrestricted standard; general promotion + guard thresholds remain separate owner decisions. Evidence: docs/evidence/NATIVE_SUBAGENT_DISPATCH_{PILOT,STANDARDIZATION,COMMISSIONING}_2026-09-02.md + subagent_dispatch_records_2026-09-02.json
- acceptance_status: candidate / ready for human review
- smoke_qa_evidence: docs/evidence/SMOKE_QA_RESULTS.md; docs/evidence/CROSS_PROJECT_SMOKE_QA_RESULTS.md
- validation_gates: see `MASTER_STATUS.md` — "Validation Gates" and "Operational Gates" (canonical lists; do not copy them here)
- blocked_items:
  - embeddings
  - semantic search
  - vector DB
  - web UI
  - agentic workflows  # one bounded exception: supervised AI-OS subagent dispatch (pilot), root-controlled, pilot-only — see AGENT_LOOP_PLAYBOOK.md
  - autonomous retrieval

## Current state

The repository contains ChatGPT project packages, compact Knowledge bundles,
Codex APP execution contracts, routing docs, StreamDeck candidate artifacts, and
repository governance checks.

Deterministic repository state:

- Baseline for the 2026-08-12 reconciliation is live `main` commit
  `21526a812e5ea4823c64815b84f6792f10b563dd`.
- `PROJECT_REGISTRY.md` identifies seven governed ChatGPT Projects, including
  `[Thinkers OS]`, and records AES applicability separately from execution
  evidence.
- AES rollout artifacts, the Analytics extension, pilot evidence fixtures, and
  Knowledge Bundle exposure are present in the repository. Their presence does
  not prove external execution or deployment.

Evidence-dependent or external state:

- ChatGPT Project UI sync, actual smoke/pilot execution, owner acceptance, PR
  review, merge, production authorization, and deploy require separate observed
  evidence.
- No new external evidence was observed during the 2026-08-12 repository
  reconciliation. Existing dated evidence and `not_verified` / `not_run`
  statuses remain unchanged.

Observed external pilot evidence — 2026-08-27:

- `PILOT-AIOS-001` completed one live `[AI OS]` response and is recorded as
  `candidate` with `medium` confidence in `docs/evidence/PILOT_RESULTS_2026-08-27_AIOS.md`.
- The response named its KB sources, separated facts from hypotheses, retained
  the promotion gate for embeddings, semantic search, and vector DB, and
  routed the next step to bounded governance evidence collection.
- This is one bounded pilot result, not owner acceptance, a full pilot set,
  or production authorization. All blocked items and `production_promotion: no`
  remain unchanged.

- `PILOT-THINKING-001` completed one live decision memo and is recorded as
  `candidate` with `medium` confidence in
  `docs/evidence/PILOT_RESULTS_2026-08-27_THINKING.md`.
- The memo compared four reversible options, separated facts, assumptions, and
  unknowns, identified risks, set a `recommended` decision status and revisit
  triggers, and handed the next stage back to `[AI OS]`.
- It recommends further diverse live pilots before a retrieval investigation,
  architecture change, owner acceptance, or any promotion decision. This is
  decision-support evidence only; it does not authorize any of those actions.

- `PILOT-ANALYTICS-001` completed one live quick-analysis response on an
  artificial three-row dataset and is recorded as `candidate` with `medium`
  confidence in `docs/evidence/PILOT_RESULTS_2026-08-27_ANALYTICS.md`.
- The response defined grain, period, units, formulas, `RAW → stage → mart`,
  reconciliation checks, and limitations. It handled the zero-plan row without
  inventing a percentage and made no causal claim beyond the supplied data.
- This is bounded analytical behavior evidence only; no user data, files,
  implementation, promotion, or production action was involved.

- `PILOT-CROSS-001` completed one live `[AI OS] → [Thinking] → [AI OS]`
  routing/resume case and is recorded as `candidate` with `medium` confidence
  in `docs/evidence/PILOT_RESULTS_2026-08-27_CROSS.md`.
- The route preserved the original goal, constraints, owner boundaries, and
  return path; no scope drift or role confusion was observed. This is limited
  evidence from one route, not proof of general cross-project reliability,
  owner acceptance, or production authorization.

Repository evidence refresh — 2026-08-27:

- PR #298 restored the generated Knowledge Bundle and provenance-audit
  artifacts that had drifted from their tracked sources.
- The repository bundle check and provenance-audit check completed
  successfully; the focused provenance/bundle test set reported 11 passing
  tests.
- The PR's `docs-safety` and `merge-gate` checks were observed successful
  before merge.
- This refresh verifies repository evidence only. It does not add external
  ChatGPT UI sync evidence, a new smoke run, pilot results, owner acceptance,
  or production authorization. Accordingly, the smoke, pilot, acceptance, and
  production-promotion statuses above are unchanged.

`PROJECT_INSTRUCTIONS.md` files must stay compact. Supporting policies, examples, templates, checklists, and detailed workflows belong in `Knowledge/`.

Recent verified state:

- Goal Mode is the default; strict task packages are reserved for high-risk,
  already-scoped, ultra-long, or explicitly requested work.
- ChatGPT Project upload mode is compact `Knowledge_Bundles` by default.
- `docs/evidence/SMOKE_QA_RESULTS.md` and
  `docs/evidence/CROSS_PROJECT_SMOKE_QA_RESULTS.md` record
  2026-07-06 smoke QA evidence. Smoke QA does not equal production readiness.
- `PILOT-AIOS-001`, `PILOT-THINKING-001`, `PILOT-ANALYTICS-001`, and
  `PILOT-CROSS-001` have recorded candidate results; all other pilots remain
  backlog/unsupported until their own result evidence is recorded.
- StreamDeck v2.7 remains active; v2.8 remains candidate/manual-only.

## Dual Surface operational acceptance

Recorded on 2026-08-18 from three real Live Tests:

| Live Test | Route | Manual orchestration |
|---|---|---:|
| `#1` | `[Analytics]` | 0 |
| `#2` | `[Thinking] -> [Analytics] -> [Codex]` | 0 |
| `#3` | `[Thinking] -> [LLM] -> [Codex]` | 0 |

Scoped verdict:

- Dual Surface Phase 1: operationally accepted;
- single-project routing: pass;
- cross-project routing: pass;
- cross-project continuity: pass;
- manual orchestration: 0 in the tested cases;
- `broad_phase_2: NOT REQUIRED` by current evidence.

This is operational evidence from three tested cases, not proof of universal or
technically deterministic routing and not evidence of a production-grade
orchestration engine. General correctness beyond the tested cases remains
monitored.

Revisit Phase 2 only if observed evidence shows a recurring material gap: manual
routing becomes necessary, material context is lost during handoff, repeated
canonical entrypoint exclusion affects correctness, ownership boundaries break,
recurring AI-OS-owned execution friction appears, or QA/acceptance exposes a
systematic defect.

Operating mode:

```text
use
-> observe
-> record material friction
-> fix only recurring evidenced gaps
```

Ordinary work uses the current merged Dual Surface without a special Live Test
protocol unless an eval is explicitly requested.

## Durable runtime gap review

Issue #342 Phase 0 reviewed the recorded Dual Surface/AES live evidence and the
provider rate-limit, inaccessible-chat, and handoff-identity cases. The review
did not find an observed material gap that requires durable runtime mechanics:
existing routing/continuity cases passed, and the remaining friction has viable
smaller controls or sits outside an authorized machine-callable boundary.

Phase 0 verdict: `blocked`; Restate Phase 1/2: `not authorized`; implementation
path: `not_planned`. Evidence and revisit conditions are recorded in
`docs/evidence/DURABLE_RUNTIME_GAP_PHASE0_2026-08-31.md`.

## Local-first compute policy

Issue #345 defines the AI-OS policy/LDW mechanics boundary, a machine-readable
task-class registry, progressive-disclosure and loss-aware compaction rules,
promotion evidence, provenance, fallback, and rollback. P0 found current
progressive disclosure, adaptive routing, and deterministic verification
already sufficient; compaction, local offload, and promotion telemetry have
partial evidence gaps.

The production `local_first` allowlist remains empty. Synthetic evidence does
not authorize task-class promotion, automated policy-assisted routing, owner
authority, merge/deploy, or production use. See
`docs/evidence/LOCAL_FIRST_COMPUTE_P0_AUDIT_2026-08-31.md`.

## Orchestration primitives P1 gap review

Issue #344 reviewed four framework-neutral P1 primitives against the current
AES, continuation, external-action, validation, and live evidence contracts.
P1.1 execution journal is `not needed`; P1.2 WAIT/RESUME and P1.4 control/effect
separation are `already sufficient`; P1.3 side-effect idempotency is a
`partial gap` because replay and duplicate-commit semantics are not explicit.

This finding does not authorize a contract implementation. A bounded P1.3
follow-up requires `[AI OS]` owner review. P2 remains `not_planned`, P3 remains
`blocked`, and no framework, runtime, dependency, merge, deploy, or production
promotion is authorized. Evidence and the exact future file/test scope are in
`docs/evidence/ORCHESTRATION_PRIMITIVES_P1_GAP_REVIEW_2026-08-31.md`.

## Executable capability routing MVP — P0 audit

Issue #350 asked for an executable capability-routing MVP (one broad goal →
dynamic canonical routing → bounded specialized executor → central return → AES
continuation). P0 finding: `BLOCKED_FOR_NATIVE_DISPATCH`. The canonical target
runtime (ChatGPT Project / Codex prompt surface) has no native executor
creation, executor identity, per-executor tool restriction, timeout/cancel, or
nested delegation; `Invoke AI-OS` is prompt-level orchestration by contract, not
a runtime service. Simulating an executor via a prompt switch is disallowed by
the issue and by AES §17 / `AGENT_LOOP_PLAYBOOK.md`.

The P1–P4 semantics are already owned by current canonical contracts:
`PROJECT_CAPABILITIES.yaml`, `HANDOFF_STYLE_STANDARD.md`, AES §5.5/§5.7/§15,
`ai-os-orchestrator/SKILL.md`, `project-context/SKILL.md`, and
`AUTONOMOUS_EXECUTION_CONTINUATION_CONTROL_PLANE_CONTRACT.md` plus the schema's
`continuation.route_trace` and `guards`. Predecessors #342 (durable runtime
`blocked`) and #344 (execution journal `not needed`, WAIT/RESUME and
control/effect separation `already sufficient`) cover the same ground.

No MVP was implemented. The owner accepted the audit on 2026-09-02 (PRs #351 and
#352 merged) and closed #350 as `completed`: P1–P4 are treated as already
covered by the existing canonical contracts, and no new "executor" concept is
added. Merge and production authority are unchanged. Evidence and the
owner-decision package are in
`docs/evidence/EXECUTABLE_CAPABILITY_ROUTING_P0_AUDIT_2026-09-02.md`.

## Next action

Run repository validation before PR review: use the canonical command set from `AGENTS.md` ("Validation" section) or `python3 scripts/sync_aios.py`, plus `python3 -m pytest tests/ -q`.

Then complete operational verification:

- `docs/operations/CHATGPT_PROJECT_SYNC_CHECKLIST.md`
- obtain owner review for the four candidate pilots, then capture the next real
  failure-to-regression case from `docs/operations/PILOT_CASES.md`
- keep production promotion blocked until accepted pilot evidence exists
