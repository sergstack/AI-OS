# Current Status — AI OS

- repo_version: v05
- project: AI-OS repository
- last_checked: 2026-09-04 (AutoResearch v0.2 live behavioral autotuning loop — #409 closed completed)
- production_promotion: no
- project_instructions_path: ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md
- knowledge_path: ChatGPT/[AI OS]/Knowledge/
- default_upload_mode: Knowledge_Bundles
- default_upload_list: ChatGPT/[AI OS]/Knowledge_Bundles/UPLOAD_LIST.md
- smoke_qa_status: pass (as of 2026-07-06, `docs/evidence/SMOKE_QA_RESULTS.md`); that record predates ~15 Knowledge additions made 2026-08-25 through 2026-09-02 (including the eval-gate family and the subagent-dispatch pilot) which have not been re-verified against the live ChatGPT UI — see the coverage note added there 2026-09-03
- runtime_smoke_status: candidate
- realistic_pilot_status: candidate (AI OS, Thinking, Analytics, and one cross-project routing/resume pilot passed; broader pilot set not run)
- durable_runtime_gap_status: not proven; Restate Phase 1 not authorized
- local_first_compute_status: candidate policy; production allowlist empty; owner review pending
- orchestration_primitives_p1_status: review complete; P1.3 partial gap; implementation owner review pending
- executable_capability_routing_status: resolved; P0 audit BLOCKED_FOR_NATIVE_DISPATCH; P1–P4 already owned by canonical contracts; no MVP implemented; owner accepted the audit and closed #350 as completed (2026-09-02)
- native_subagent_dispatch_status: STANDARDIZED BOUNDED (2026-09-02; owner-approved, Judge round-2 pass). Bounded, pilot-scoped: root -> bounded routed slice -> Plan child + isolation:"worktree" -> evidence/patch -> root -> validation/AES continuation. Plan child cannot use the native Agent tool; no write-capable child; root is sole router + writer; no child->child; one execution_id per user goal. Commissioning punch-list 4/4 closed — dispatch-evidence schema + blocking linter (scripts/check_subagent_dispatch_evidence.py in docs-safety), enforced telemetry contract, 18 hardened dispatches across 7 owners, guard-calibration proposal (thresholds unchanged), [AI OS] cost/latency owner. NOT a default/unrestricted standard; general promotion + guard thresholds remain separate owner decisions. Evidence: docs/evidence/NATIVE_SUBAGENT_DISPATCH_{PILOT,STANDARDIZATION,COMMISSIONING}_2026-09-02.md + subagent_dispatch_records_2026-09-02.json
- autoresearch_v02_status: `pass` / harness available, Phase 1 deferred (2026-09-04; owner closed parent #409 as completed). AutoResearch v0.2 (live behavioral autotuning loop) children #410–#417 built and merged (PRs #420–#428): live browser transport (#413), live blind A/B semantic Judge (#414), failure intake + bounded Researcher proposal flow (#415), one documented CLI (#416). Phase 0 live calibration (#417) executed 2026-09-04 in a coordinated session (owner-authenticated dedicated Playwright MCP profile): 13 real `gpt-5-6-thinking` calls, $0 / plan-included, `measurement_verdict: pass` (a harmful shadow tie-break mutation regressed the routing outcome as designed; the live blind Judge flagged it order-consistently; deterministic hard gates dominate), `failure_discovery_result: no_failure_found` (all six behavioral families answered correctly). Phase 1 bounded autotuning pilot (#418) is `blocked` and was NOT run — no reproducible, attribution-eligible baseline failure exists and manufacturing one is forbidden. No candidate was generated or applied; no active Project Instructions / routing / `main` behaviour changed. `repo_replay` via a fresh non-Project chat is a lower-fidelity approximation of the real ChatGPT Project runtime — no UI-equivalence claim. Recommendation (mirrors v0.1 #398): keep the harness available and re-engage only when a genuine field-observed AI-OS failure appears; manual bounded regression review remains sufficient. Issues #417/#418/#419 left open by the owner as the re-engagement anchor. Evidence: docs/evidence/AUTORESEARCH_V02_PARENT_FINAL_QA_2026-09-04.md, AUTORESEARCH_V02_PHASE0_LIVE_2026-09-04.md (+ autoresearch_v02_phase0_records_2026-09-04.json), AUTORESEARCH_V02_LIVE_BROWSER_SMOKE_2026-09-04.md (§ "Update — 2026-09-04"; smoke facts recorded inline, no standalone JSON record), AUTORESEARCH_V02_LIVE_JUDGE_CALIBRATION_2026-09-04.md, AUTORESEARCH_V02_RESEARCHER_SMOKE_2026-09-04.md, AUTORESEARCH_V02_CLI_CONTROLLER_2026-09-04.md.
- project_wide_revision_review_status: reviewed 2026-09-03 via 7 parallel bounded subagent dispatches (one per `PROJECT_CAPABILITIES.yaml` capability); 40 findings (12 high / 11 medium / 17 low), no schema/business-logic issue, dominant pattern is stale status/evidence files across `[Thinking]`, `[AI OS]`, `[Analytics]`, `[Thinkers OS]`, `[Inbox Router]`. Review-and-plan record only; fixes tracked and applied separately. Evidence: docs/evidence/PROJECT_WIDE_REVISION_REVIEW_2026-09-03.md
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

## AutoResearch v0.2 — live behavioral autotuning loop

Issue #409 asked for a live behavioral autotuning loop over selected AI-OS
Project-Instructions / routing / handoff / context-loading wording: real
model outputs → observed/reproduced failure → causal attribution → one
minimal reversible shadow mutation → matched live runs → blind live Judge →
deterministic gates → `keep_candidate | discard | inconclusive` → immutable
evidence → separate owner promotion.

Delivered and merged (children #410–#417, PRs #420–#428):

- `#413` — one authorized Playwright MCP browser-session live transport
  (`scripts/autoresearch_live_browser_adapter.py`) with a transport-neutral
  `invoke()` that enforces authority / budget / context / target /
  model-selector gates before any submission; a transport smoke ran on
  2026-09-04 (1 real call, non-placeholder response hash).
- `#414` — live blind A/B semantic Judge (`scripts/autoresearch_live_judge.py`)
  built on #394's frozen contract: mandatory reversed second pass, de-blinding
  only after both orders validate, order disagreement → `inconclusive`.
- `#415` — failure intake + attribution + bounded Researcher proposal
  (`scripts/autoresearch_failure_intake.py`); observation / reproduction /
  attribution / eligibility are separate machine-checkable states; the
  deterministic preflight reuses the v0.1 shadow-runner machinery unchanged
  and never decides a candidate is good.
- `#416` — one documented CLI (`scripts/autoresearch_cli.py`,
  `docs/guides/AUTORESEARCH_CLI.md`) with a no-network `--dry-run`, bounded
  resume, and scoped cleanup; integrates the v0.1 validator / shadow runner /
  comparator / ledger and the v0.2 components through real import points.
- `#417` — Phase 0 live calibration, executed 2026-09-04.

Phase 0 result: **`measurement_verdict: pass`**, **`failure_discovery_result:
no_failure_found`**. 13 real `gpt-5-6-thinking` calls total (with the #413
smoke), $0 / plan-included, 0 retries / timeouts / invalid outputs. A harmful
shadow tie-break mutation changed the routing outcome from `blocked` to
`[Codex]` as designed; the live blind Judge flagged it `revise` and the
baseline `pass` order-consistently in both A/B orders; deterministic
hard-gate dominance is proven in code. All six behavioral families (routing,
scope/execution, evidence, authority, handoff, adversarial) answered
correctly on a single run each — no reproducible baseline failure.

Phase 1 bounded autotuning pilot (#418) is **`blocked` and was not run**: its
precondition is at least one reproducible, attribution-eligible Phase 0
failure, and none exists. Per #417's own rules a failure must not be
manufactured to proceed.

Parent gate (#419): **`pass`**. The v0.2 live loop is built and calibrated
against real model output and correctly declined to promote anything under
insufficient evidence — mirroring v0.1's #398 result. No candidate was
generated or applied; no active Project Instructions, routing, or `main`
behaviour was changed by any live run. `repo_replay` via a fresh non-Project
chat is a lower-fidelity approximation of the real ChatGPT Project runtime;
no UI-equivalence claim is made.

The owner closed #409 as `completed` on 2026-09-04 and left #417 / #418 /
#419 open as the re-engagement anchor. Recommendation: keep the harness
available and re-engage the loop only when a genuine field-observed AI-OS
failure appears; until then manual bounded regression review is sufficient.
`production_promotion: no` and all blocked items are unchanged. Evidence:
`docs/evidence/AUTORESEARCH_V02_PARENT_FINAL_QA_2026-09-04.md`,
`AUTORESEARCH_V02_PHASE0_LIVE_2026-09-04.md`,
`AUTORESEARCH_V02_LIVE_BROWSER_SMOKE_2026-09-04.md`,
`AUTORESEARCH_V02_LIVE_JUDGE_CALIBRATION_2026-09-04.md`,
`AUTORESEARCH_V02_RESEARCHER_SMOKE_2026-09-04.md`,
`AUTORESEARCH_V02_CLI_CONTROLLER_2026-09-04.md`.

## `[Analytics]` P0 adversarial audit — live validation

Follow-up to PR #440 (P0 semantic-reasoning contract strengthening, merged
`715f3ef`, closes #439): a paper-trace audit of 5 adversarial scenarios found
all 5 bounded, plus one real drafting gap ("Finding A" — §5 named the
population/denominator/scope self-report fields but, unlike §11–§13, stated
no consequence for a material "no"/unexplained answer).

Finding A has a bounded fix **implemented** in open PR #443 (`state: OPEN`,
not merged): one rule line + one sentence in §5 capping `claim_support <=
PARTIALLY_SUPPORTED` when population/denominator is materially unexplained.
No new `METHOD_ID`, no registry expansion, no P1 `RECONCILIATION_CONTRACT`
activation. Governance checks (`check_project_instructions_length`,
`check_manifest_paths`, `check_repo_public_safety`, `check_knowledge_bundles`,
`check_index_coverage`) pass on that branch;
`Knowledge_Bundles/ANALYTICS_03_TECHNIQUES_AND_CHARTS.md` was regenerated via
`scripts/build_knowledge_bundles.py --write`. PR #443 is **not** merged to
the repository, **not** synced/deployed to the live `[Analytics]` Project's
Knowledge Bundle, and **not** behaviorally revalidated live — canonical
closure of Finding A remains pending owner review and merge.

2 of the 5 audited scenarios (denominator drift; population/ЦФО
restructuring) were additionally run **live** against the real `[Analytics]`
ChatGPT Project on 2026-09-05, using synthetic data and a normal-analyst
framing (not flagged as a test). Both produced `GATE: revise` and rejected
the requested false/overstated CFO headline — consistent with the
paper-trace predictions; no contradiction found, no new finding raised. The
live Project had not yet ingested PR #443 at run time, so this run validates
the pre-existing §5 self-report + Judge fallback, not the Finding A fix
itself. `production_promotion: no`; no merge, method-catalog, or active
Project change was made. Evidence:
`docs/evidence/ANALYTICS_P0_ADVERSARIAL_LIVE_VALIDATION_2026-09-05.md`.

## Next action

Run repository validation before PR review: use the canonical command set from `AGENTS.md` ("Validation" section) or `python3 scripts/sync_aios.py`, plus `python3 -m pytest tests/ -q`.

Then complete operational verification:

- `docs/operations/CHATGPT_PROJECT_SYNC_CHECKLIST.md`
- obtain owner review for the four candidate pilots, then capture the next real
  failure-to-regression case from `docs/operations/PILOT_CASES.md`
- keep production promotion blocked until accepted pilot evidence exists
