# Executable Capability Routing MVP — P0 Audit & Owner-Decision Package — 2026-09-02

- Issue: [#350](https://github.com/sergstack/AI-OS/issues/350)
- Baseline: `origin/main` at `49768ef` (Merge PR #349)
- Semantic owner: `[AI OS]`
- Implementation owner (if authorized): `[Codex]`
- Execution scope: P0 audit only (native executor, governance, duplication)
- Evidence status: repository evidence plus this session's observed checks; no
  production promotion, no owner acceptance

## P0 deliverable

```text
BLOCKED
```

Specifically `BLOCKED_FOR_NATIVE_DISPATCH` for the executable-dispatch core, and
`REVISE (duplication)` for P1–P4, which are already owned by current canonical
contracts. P1–P5 implementation is **not started** and is **not authorized** by
this audit.

Final verdict (issue's required vocabulary):

```text
BLOCKED
```

`PASS` is not permitted: the issue states `PASS` requires that "executable
multi-capability dispatch was actually run and observed". It was not, because
the canonical target runtime has no native executor-dispatch mechanism to run.

## 1. Native executor capability audit (P0.1)

The canonical target surfaces for `Invoke AI-OS` are the ChatGPT Project prompt
surface and the Codex prompt/repo surface. `.agents/skills/ai-os-orchestrator/SKILL.md`
defines `Invoke AI-OS` as "prompt-level orchestration over capabilities and
tools already available to the active agent, **not a runtime service, automatic
project-invocation platform, or expansion of authority**".

Each capability the issue asks about, classified against what that surface
actually provides:

| Executor capability (P0.1) | Canonical target surface | Finding |
| --- | --- | --- |
| Specialized subagent / executor creation | ChatGPT Project / Codex prompt | `unavailable` — no primitive that instantiates a separate executor process/identity; a "project" is a prompt/context selection, not a dispatchable executor. |
| Bounded instruction / context transfer | prompt | `partial (non-executable)` — `project-context` + AES handoff envelope transfer bounded context **to the same agent**, not to a distinct executor. |
| Result return to parent / controller | prompt | `partial (non-executable)` — AES §15 handoff persistence and §15.2 continuation handoff rule return evidence to the same AES record; there is no callee process returning a value. |
| Sequential / parallel invocation | prompt | `unavailable` — no mechanism to invoke a capability as a callable unit; sequencing is the single agent following steps. |
| Executor identity | prompt | `unavailable` — `from`/`to` in a handoff are role labels, not process/agent identities. |
| Tool / permission restriction per executor | prompt | `unavailable` — tools/permissions are the active agent's; they cannot be scoped down to a spawned executor because none is spawned. |
| Timeout / cancel | prompt | `unavailable` — no callable unit to time out or cancel; AES stop conditions govern the single execution. |
| Nested delegation | prompt | `unavailable` — no parent→child→parent call stack; `ai-os-orchestrator` is a single controller thread. |

Capabilities were **not** inferred from Temporal, LangGraph, CrewAI, AutoGen,
Mastra, or any external framework, per the issue's constraint.

Note on other surfaces: some coding-agent surfaces (e.g. a Task/subagent tool)
do expose real bounded dispatch. That is a **surface-specific** capability, not a
property of AI-OS or of the ChatGPT/Codex target the issue names. Building the
MVP around a surface-specific tool would add an executor mechanism the canonical
target does not have, and would make the MVP non-portable across the surfaces
`Invoke AI-OS` is contracted to run on. The issue explicitly forbids simulating
"a separate executor with a prompt switch while calling it executable dispatch".

**P0.1 result: `BLOCKED_FOR_NATIVE_DISPATCH`.**

## 2. Governance audit (P0.2)

| Governance surface | Statement | Effect on this MVP |
| --- | --- | --- |
| `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` §17 | Forbidden: "an agent orchestration platform; automatic project invocation". | An "executor mechanism" that invokes capabilities as callable units is a prohibited class. |
| `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md` | Supervised loops are "not … autonomous agents … uncontrolled multi-agent execution". Human acceptance required before "adding automation, retrieval, persistent memory, or new runtime tools". | New executor dispatch = new runtime tool → owner acceptance required. |
| `ChatGPT/[AI OS]/Knowledge/SKILLS_HOOKS_MCP_DECISION_MATRIX.md` | "Sub-agent" is a gated pattern: use only when "scope is isolated and final diff owner is clear", gate = "branch/file isolation"; "Human acceptance is required before enabling any … sub-agent pattern … as a standard workflow". | Standardizing executor dispatch needs explicit human acceptance. |
| `AGENTS.md` "Change Rules" | "Do not add blocked promotion items: … agentic workflows, autonomous agents". | Implementation without an owner decision would breach this rule. |
| `docs/evidence/DURABLE_RUNTIME_GAP_PHASE0_2026-08-31.md` (#342) | "do not add Restate code, configuration, deployment, or a competing state model"; durable-runtime gap `blocked`. | A dispatch/executor runtime is a competing state model class → currently barred. |

Classification (issue's taxonomy):

```text
C. currently prohibited      — for a new executor-dispatch runtime / mechanism
B. requires bounded governance clarification — for any narrower "executor" field
                               added to PROJECT_CAPABILITIES.yaml
A. policy-compatible          — only the parts already shipped (see §3)
```

The governance position is **not** silently weakened by this audit. An
owner-decision package is in §5.

## 3. Duplication audit (P0.3)

Every P1–P4 semantic the issue proposes is already owned by a current canonical
contract on `origin/main`. Verified by reading the files below.

| Issue ask | Existing canonical owner | Evidence |
| --- | --- | --- |
| P1 capability = domain ownership + canonical context | `PROJECT_CAPABILITIES.yaml` (`schema_version: 2`, `canonical_path`, `context_entrypoints`) | file read at baseline |
| P1 executor = verified mechanism (distinct concept) | not present, and **cannot** be truthfully populated — see §1. Adding `executor.type/id` with no verified backend would let "an executor without verified backend … report execution", which the issue's own P5 test forbids. | §1 |
| P1 input contract (`execution_id`, `handoff_id`, `from`, `to`, `objective`, `original_goal`, `requirement_ids`, `evidence_refs`, `authority_status`, `authority_provenance`, `acceptance_criteria`, `return_to`) | `HANDOFF_STYLE_STANDARD.md` + AES §15 (`handoff_id`, `execution_id`, `parent_execution_id`, `from`, `to`, `requirement_ids`, `open_defect_ids`, `evidence_refs`, `acceptance_snapshot`, `authority_status`, `authority_provenance`, `next_owner`) + AES §5.5 continuation envelope + §5.7 authority-provenance object | `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` §5.5, §5.7, §15, §15.1 |
| P1 output contract (`result`, `validation`, `limitations`, `open_questions`, `cross_domain_needs`, `acceptance_status`) | `HANDOFF_STYLE_STANDARD.md` "Default Style" + AES §15 `acceptance_snapshot`/`qa_status`/`judge_verdict` + reverse-handoff §15.1 | same |
| P1 "do not create a new `execution_id` during ordinary capability transitions" | AES §15 ("A new execution ID is permitted only with an explicit parent/child link") + §5.2 | AES §5.2, §15 |
| P2 `CAPABILITY EXECUTOR != CANONICAL ROUTER`; capability returns `cross_domain_need`, must not self-route | `ai-os-orchestrator/SKILL.md` §7 ("Add capabilities only by handoff … return it to the primary owner") + `AUTONOMOUS_EXECUTION_CONTINUATION_CONTROL_PLANE_CONTRACT.md` ("The controller routes, records, and terminates; it does not execute domain work … an executor does not make a material decision") + AES §2.1 | `.agents/skills/ai-os-orchestrator/SKILL.md`, control-plane contract |
| P2 centralized delegation (`orchestrator → owner → orchestrator`) | `ai-os-orchestrator/SKILL.md` "Canonical loop" + `ROUTING_RULES.md` ("single owner of destination selection") | same |
| P3 context isolation, record `included_context` / `excluded_context` / `reason` / `context_sufficiency` | `.agents/skills/project-context/SKILL.md` "Context pack" ("included files with selection reasons; excluded candidates with reasons; … context sufficiency") + orchestrator "Context boundary" | `.agents/skills/project-context/SKILL.md` |
| P3 path-traversal / symlink-escape rejection | `project-context/SKILL.md` step 2 + `ai-os-orchestrator/SKILL.md` "Validate paths" | same |
| P3 preserve `execution_id`, `original_goal`, `original_acceptance_criteria`, resolved owner, `resume_stage`, requirement/defect IDs, evidence refs, authority, source hashes across stages | AES §5.5 continuation envelope + §15.2 continuation handoff rule + §6 source-revision contract | AES §5.5, §6, §15.2 |
| P4 append-only route trace (`step_id`, `from`, `to`, `reason`, `requirement_ids`, `handoff_id`, `input_state_ref`, `result_state_ref`, `evidence_added`, `outcome`) | `schemas/autonomous_execution_record.schema.json` `continuation.route_trace[]` (`route_id`, `from_owner`, `to_owner`, `resume_stage`, `criteria_addressed`, `route_signature`, `evidence_delta`, `refusal_reason`, `outcome`) | schema lines ~631–650 |
| P4 loop invariant (same owner + same unresolved requirement + same input state + no new evidence ⇒ suspected loop; `A→B→A` allowed with material delta) | `AUTONOMOUS_EXECUTION_CONTINUATION_CONTROL_PLANE_CONTRACT.md` "Repeat routes and guards" (`evidence_delta` ∈ {`new_evidence`, `changed_assumption`, `failed_validation`, `changed_acceptance_interpretation`, `new_owner_instruction`, `implementation_feedback`}; else `repeat_route_refused_missing_evidence_delta`) | control-plane contract; schema `refusal_reason` enum |
| P4 loop ⇒ register orchestration/routing defect under AES, no widened retry limits | AES §9.2 (`governance` / `traceability` defect classes) + control-plane "Guards do not authorize extra corrections or weaken Codex's one-correction limit" + `stopped` / `continuation_no_progress_limit_reached` (schema line 79) | AES §9, schema |
| P4 four guards (hops, per-owner retries, no-progress, route-signature cycle) | schema `continuation.guards` (`max_continuation_hops`, `max_retries_per_owner`, `max_no_progress_hops`, `route_signature_history_window`, `tripped_guards`) | schema lines ~666–676 |
| "one AES execution / not a second state machine" | AES §0, §7 state machine; control-plane "without creating a parallel state machine" | AES, control-plane contract |

Predecessor decisions that already cover this ground:

- **#344** (`ORCHESTRATION_PRIMITIVES_P1_GAP_REVIEW_2026-08-31.md`): execution
  journal `not needed` (AES route trace already reconstructs the route);
  WAIT/RESUME `already sufficient`; control/effect separation `already
  sufficient`. Only side-effect idempotency (P1.3) is a partial gap and is
  `not_authorized`.
- **#342** (`DURABLE_RUNTIME_GAP_PHASE0_2026-08-31.md`): no observed
  crash/retry-state loss; competing state model / durable runtime `blocked`.
- **#345** (`LOCAL_FIRST_COMPUTE_P0_AUDIT_2026-08-31.md`): adaptive routing and
  deterministic verification `already sufficient`; no new worker/executor.

**P0.3 result: substantial duplication.** Implementing P1–P4 as new artifacts
would create a second routing/handoff/route-trace surface and hit the issue's
own non-acceptance list ("a framework is added without a demonstrated gap"; "a
second routing registry"; "a second state machine").

## 4. Acceptance-criteria pre-check (issue's 20 criteria)

The criteria split cleanly:

- **Already satisfied by current contracts (prompt-level):** 1, 2, 3, 4, 6, 7,
  8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20 — owned by `GOAL_MODE.md`,
  `ai-os-orchestrator/SKILL.md`, `ROUTING_RULES.md`, `PROJECT_CAPABILITIES.yaml`,
  `project-context/SKILL.md`, and the AES continuation/route-trace/closure
  contracts. Dual Surface live evidence (`CURRENT_STATUS.md`, three 2026-08-18
  Live Tests; `PILOT-CROSS-001`) shows criteria 1–3, 7–8, 17 observed in
  practice with zero manual orchestration.
- **Cannot be satisfied in the canonical target runtime:** **5** ("any claimed
  executable capability is actually executed by a verified executor mechanism")
  and, as a consequence, **14/15** only to the extent they presume an executor
  boundary distinct from the single controller. §1 shows no verified executor
  mechanism exists to satisfy criterion 5.

Because criterion 5 is unmet and unmeetable here, and the issue bars `PASS`
without observed executable dispatch, the verdict is `BLOCKED`.

## 5. Owner-decision package (governance classes B / C)

Not an implementation authorization. For `[AI OS]` owner decision.

### Decision 1 — Is any new "executor" concept wanted at all?

- **Option A (recommended): No new executor concept; close #350 as covered.**
  P1–P4 are already owned (§3). Keep `Invoke AI-OS` prompt-level. Downside: the
  issue's phrase "executable capability routing" stays aspirational on the
  ChatGPT/Codex surface; no behavioural change.
- **Option B: Add a documentation-only `dispatch_mode` note to
  `PROJECT_CAPABILITIES.yaml` per capability** with values limited to
  `prompt_context` (the only currently true value) and no `executor.id`/`type`
  until a verified backend exists. Bounded, reversible, adds no runtime.
  Governance class **B**. Downside: a field with one legal value is low value
  now; risk of future misuse as an "executor registry".
- **Option C: Authorize a surface-specific executable-dispatch pilot** (e.g. on
  a coding-agent surface that has a real bounded subagent tool), strictly
  outside the ChatGPT target, under a new strict issue with branch/file
  isolation, its own AES record, and the issue's P5 test set. Governance class
  **B→C**: needs an explicit owner grant against `AGENTS.md` "Change Rules" and
  the AES §17 "automatic project invocation" prohibition, plus a demonstrated
  recurring gap (none is recorded — see §6).

### Decision 2 — If Option C is ever taken, required guardrails

- one AES `execution_id` across the route; no new `execution_id` per hop
  (parent/child link only);
- executor receives only `project-context`-bounded context; `included` /
  `excluded` / `reason` / `context_sufficiency` recorded;
- control returns to `ai-os-orchestrator` after every slice; executor may emit
  `cross_domain_need` but never selects the next canonical owner;
- route trace + four guards from the existing continuation control plane, not a
  new table;
- merge / deploy / production / owner gates unchanged;
- rollback = `git revert` of the pilot PR; no runtime/data migration.

## 6. Revisit trigger

Reopen executable-dispatch evaluation only when a real `Invoke AI-OS` execution
records, with an `execution_id` and evidence refs, at least one of:

- manual orchestration became necessary because prompt-level routing could not
  carry a multi-hop goal;
- material context was lost across a handoff that the AES envelope should have
  preserved;
- a routing loop occurred that the existing `evidence_delta` / guard mechanism
  did not detect;
- a capability could not be executed at all on the target surface and this
  blocked goal completion, with the smallest non-dispatch alternative shown
  insufficient.

For that case also record: number of manual recovery actions, owner
interventions, elapsed recovery time, and an explicit map from the observed gap
to a specific verified executor primitive.

## 7. Files changed by this audit

- `docs/evidence/EXECUTABLE_CAPABILITY_ROUTING_P0_AUDIT_2026-09-02.md` (new; this file)
- `docs/evidence/README.md` (index pointer)
- `CURRENT_STATUS.md` (status line + section + `last_checked`)

No change to `GOAL_MODE.md`, `ai-os-orchestrator/SKILL.md`, `ROUTING_RULES.md`,
`PROJECT_CAPABILITIES.yaml`, `project-context/SKILL.md`,
`HANDOFF_STYLE_STANDARD.md`, the AES standard, the schema, validators, or any
gate. Docs-only, `risk_mode: lightweight`.

## 8. Commands run

Recorded in the PR body from this session's worktree at `origin/main` `49768ef`.

## 9. Gates and rollback

- P0 audit: candidate evidence, ready for owner review.
- P1–P5 implementation: `not started`, `not authorized`.
- Executable dispatch / executor runtime: `blocked` (`BLOCKED_FOR_NATIVE_DISPATCH`).
- Governance change: owner decision required (classes B / C).
- Merge: owner review pending (Merge Gate).
- Production: not authorized.
- Rollback: revert this PR / delete this record and its two index/status
  references. No runtime or canonical AES state requires rollback.

## 10. AES statuses (reported separately)

```yaml
execution_state: completed        # the P0 audit scope is complete
overall_delivery: partial         # audit delivered; requested MVP not delivered (blocked upstream)
qa_status: pass                    # repository validation checks run and observed (see PR body)
judge_verdict: not_run             # no independent Judge review performed
authority_status: owner_review_pending
merge_status: not_opened           # → open on PR
production_status: not_applicable
```

Terminal outcome for the issue's lifecycle: `BLOCKED` — reported as
`BLOCKED_FOR_NATIVE_DISPATCH`, with a duplication finding that P1–P4 are already
owned by current canonical contracts and an owner-decision package for any
governance change.
