---
name: ai-os-orchestrator
description: Default AI-OS entrypoint for a user goal. Route through canonical rules, resolve one owner capability, load bounded project context, and govern explicit handoffs, checks, acceptance, rollback, and reporting.
---

# AI-OS Orchestrator

Use this skill as the default front door when the user gives a goal that needs AI-OS methodology and does not manually provide a route. Simple local, reversible repository work with sufficient local instructions stays local and does not activate AI-OS.

This skill owns orchestration only. It does not own domain methodology, replace a capability, or create a second routing registry.

## Canonical sources

Before routing, verify and read:

1. the applicable `AGENTS.md` files;
2. `ROUTING_RULES.md` for front-door routing semantics and external destination classes;
3. `PROJECT_CAPABILITIES.yaml` for capability locations;
4. `.agents/skills/project-context/SKILL.md` for bounded context loading;
5. `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md` and `HANDOFF_STYLE_STANDARD.md` when a cross-project handoff is required;
6. `GOAL_MODE.md` and `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` when execution, correction, validation, or terminal reporting is required.

Treat those files as the semantic owners. Do not copy their routing tables, capability locations, project methodology, or merge policy into this skill.

## Invoke AI-OS continuation mode

`Invoke AI-OS` is the executable continuation mode of this orchestrator. It is prompt-level orchestration over capabilities and tools already available to the active agent, not a runtime service, automatic project-invocation platform, or expansion of authority.

Before the first route, preserve the `original_goal` and `original_acceptance_criteria`. When `Invoke AI-OS` begins, create or update the AES record's `continuation` envelope; it is the canonical durable state for this execution, not session context or a local cache. Keep it active across every stage and handoff.

Canonical loop:

```text
original goal -> route -> owner -> bounded handoff -> execution -> validation -> resume original goal
```

When the current owner identifies a concrete cross-domain need:

1. create the minimum sufficient handoff under the canonical handoff rules, preserving the original goal, acceptance criteria, evidence, constraints, execution state, and return path;
2. if the owning capability is available in the current environment and the next action is reversible, policy-permitted, and already authorized, invoke or follow that capability and obtain its result;
3. validate the returned result against the handoff acceptance criteria;
4. return the result to the current owner and reassess the original goal;
5. continue automatically while the original acceptance criteria remain unmet and an authorized path exists.

Handoff completion is not goal completion. A prepared contract, identified owner, passing intermediate check, generated artifact, completed slice, or ready-for-review state is only an intermediate milestone unless it satisfies the original goal.

### Native subagent dispatch (pilot)

Owner-approved bounded pilot, dated 2026-09-02, governed by
`ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md`
("Supervised AI-OS Subagent Dispatch"). It is not a standard workflow and
does not generalize. This subsection adds a dispatch mechanism to step 2 of the
canonical loop above; it does not add a second router, state machine, or
execution record.

Preconditions for one dispatched slice:

- routing has already resolved exactly one owner capability for this stage
  (Steps 2–4 of Procedure);
- that capability's `PROJECT_CAPABILITIES.yaml` entry has an `executor` block
  with `backend: claude_code_subagent`;
- the slice is reversible and policy-permitted, or its external action is
  already authorized; a `write_capable: false` executor may not perform repository writes.

Dispatch:

1. Spawn one subagent of `executor.agent_type`. Pass a bounded prompt only:
   the `original_goal`, the resolved capability id and `canonical_path`, the
   `context_entrypoints` to load through `executor.context_loader`
   (`project-context`), the single slice objective, the slice acceptance
   criteria, and the relevant `authority_provenance` claims. Do not pass the
   whole AES record, other projects, unrelated history, or secrets.
2. Instruct the child explicitly: return result, evidence references, and any
   `cross_domain_need`; do not choose or invoke the next owner; do not spawn
   sub-subagents (`child_dispatch: forbidden`).
3. The child runs in the same working tree. Treat shared filesystem as a risk:
   only a `write_capable: true` executor (currently `codex`) may be asked to
   modify files, and only when the slice genuinely requires it.

On return, the root (and only the root):

4. appends one `continuation.route_trace` entry — `from_owner:
   ai-os-orchestrator`, `to_owner: <capability>`, `resume_stage`,
   `criteria_addressed`, `route_signature`, `outcome` (`dispatched` →
   `completed` or `refused`), `evidence_refs`; the same `execution_id` is kept;
5. validates the child result against the slice acceptance criteria and folds
   its evidence into the AES record;
6. reassesses the `original_acceptance_criteria`;
7. selects the next route only through `ROUTING_RULES.md`, honoring the existing
   `continuation.guards` (`max_continuation_hops`, `max_retries_per_owner`,
   `max_no_progress_hops`, `route_signature_history_window`). A repeat route
   without a material `evidence_delta` is recorded as
   `repeat_route_refused_missing_evidence_delta` and not dispatched.

The after-child step is **mechanical, not discretionary** (preserves the AES
§2.1 resolved-owner boundary; a discretionary root becomes a standing
supervisor above the resolved owner and defeats warm resume). After a child
returns, the root performs only continuation-layer functions — record the
evidence delta, update progress against the original acceptance criteria,
evaluate the four guards — then restores the resolved owner and its
`resume_stage` and returns control to that owner. The root does not pick a new
owner on its own judgment and does not perform or redo domain work. The root
diverts from the resolved owner only on a closed trigger: (i) a cold-entry-level
change to the original goal, resolved owner, scope, authority, or canonical
routing state; (ii) an AES §2 `decide` trigger; (iii) a tripped continuation
guard; or (iv) all original acceptance criteria satisfied. Cross-domain routing
after a child return still originates from the resolved owner's identified
`cross_domain_need`.

Failure handling: a spawn error, missing result, denied tool, or unusable
output is registered as an AES defect (`classification: external_dependency`
for a runtime/tool failure, `implementation` for a bad result), not retried
silently or hidden. No subagent timeout primitive exists; rely on explicit
cancel and the guard limits. A dispatched slice is never terminal goal
completion — only Closure Review against the `original_goal` can close.

### Execution lifecycle and warm resume

Once `Invoke AI-OS` begins for an execution, this orchestration contract
governs that execution until the original acceptance criteria are satisfied,
the user materially changes the original goal, or it reaches
`OWNER_DECISION_REQUIRED` or `BLOCKED`. This is an execution lifecycle rule,
not a standing mode for a whole Codex session.

Simple local reversible work may execute without a new AI-OS routing pass. If
it is a stage of an active AI-OS execution, completing that local step does
not terminate orchestration: return its evidence to the active AES record,
validate it, and reassess the original acceptance criteria.

Use a **cold entry** (full Preflight, Classify, Resolve, and bounded context)
for a new execution or when the saved continuation envelope is absent, invalid,
stale, or has a material change to the original goal, resolved owner, scope,
authority, or canonical routing state. In all other cases use **warm resume**:

```text
read AES record_ref -> verify envelope freshness and hashes
-> restore resolved owner and resume_stage
-> load bounded current-owner context only if needed
-> continue from the next unresolved requirement or defect
```

An unchanged source revision alone never permits warm resume. A local ignored
pointer may cache only `execution_id` and `record_ref` after a behavioral test
shows it is needed; it is never canonical state and must not duplicate the
goal, acceptance criteria, requirements, defects, or authority state.

If validation fails, follow the corrective-loop and authority rules in
`docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`: register the defect, route
it to its owner, make only an eligible minimal correction, rerun the same
affected check, and keep `[Codex]`'s stricter one-correction limit. Never weaken acceptance criteria to terminate.

`Invoke AI-OS` does not expand authority. It must not auto-execute owner-frozen policy changes, merge, deploy, production promotion, destructive or low-reversibility actions, or actions requiring unavailable credentials, permissions, money, legal authority, or physical action.

Return exactly one user-facing terminal outcome while preserving the separate AES status fields:

- `COMPLETED`: the original goal and acceptance criteria are satisfied and read back or otherwise validated against current evidence;
- `OWNER_DECISION_REQUIRED`: only a genuine owner choice, approval, authority grant, or materially consequential low-reversibility decision remains; report the exact decision, viable options when applicable, recommendation, downside, and continuation after approval;
- `BLOCKED`: no authorized path can continue after available deterministic, reversible, and policy-permitted recovery routes have been exhausted; report the failing layer, operation, evidence, attempted recovery, preserved state, and minimum external action required.

## Procedure

1. **Preflight.** Confirm every required canonical source above exists. Preserve system, user, and applicable local repository constraints.
2. **Classify.** Apply the canonical front-door routing rules to the requested outcome. Require one canonical destination for the current stage. A raw or unclear intake may resolve to `[Inbox Router]` only when the canonical rules say so; it is not a fallback for conflicting owner candidates.
3. **Resolve.** Match the routed destination to registry-owned data without a hardcoded label map:
   - if routing returns a capability id, require an exact key match in `PROJECT_CAPABILITIES.yaml`;
   - if routing returns a project label, require its exact match to the final path component of exactly one registered `canonical_path`;
   - require exactly one match; zero or multiple registry matches are `blocked`;
   - then require one relative `canonical_path` and a non-empty `context_entrypoints` list whose first item is `PROJECT_INSTRUCTIONS.md`.
   The unique registered match is exactly one primary owner capability for the current stage.
   A canonical destination outside the registered AI-OS capabilities is not a registry failure. Respect the class from `ROUTING_RULES.md`: for `external`, report an explicit terminal handoff without inventing a capability; do not invoke `project-context`; for `internal_non_capability`, continue only through the named non-capability boundary; for `owner_escalation`, stop as `OWNER_DECISION_REQUIRED` and request the stated owner decision. Do not recast any of these classes as a registered project.
4. **Validate paths.** Resolve the canonical path inside the repository. Reject absolute paths, traversal, symlink escape, missing directories, missing entrypoints, and any entrypoint that escapes its canonical project.
5. **Load context.** Invoke or follow `project-context` only after Steps 2–4 pass. Read the owner instructions first, then only indexed or task-relevant references. Stop when context is sufficient.
6. **Execute within ownership.** Keep reasoning and methodology with the primary owner. For repository implementation, create a bounded handoff to local Codex execution with outcome, allowed scope, local constraints, checks, rollback, and acceptance criteria.
7. **Add capabilities only by handoff.** Use another capability only when the primary owner identifies a concrete cross-domain need. Record `From`, `To`, objective, inputs, constraints, expected output, acceptance, risks, evidence/confidence, and first step. Under `Invoke AI-OS`, invoke an available authorized owner capability, validate its result, and return it to the primary owner unless the user explicitly changes the requested outcome.
8. **Resume and validate.** After every intermediate result, compare current evidence with the original goal and acceptance criteria. If they are not satisfied, continue through the next authorized route. Apply only relevant project checks plus Goal Mode and AES acceptance, rollback, reporting, and merge gates. A passing check or Judge verdict does not authorize merge or production promotion.

## Fail-closed rules

Stop with status `blocked` and report the exact missing or conflicting evidence when:

- canonical routing does not yield exactly one destination for the current stage;
- a capability id or project label has zero or multiple registry matches;
- a required canonical source, registry entry, canonical path, or context entrypoint is absent;
- a registry or entrypoint path is absolute, escapes its canonical boundary, or cannot be verified;
- owner instructions conflict and precedence does not resolve them;
- a required handoff has no explicit owner, scope, checks, rollback, or acceptance boundary;
- safe execution or meaningful validation is impossible.

Do not guess an owner, silently substitute a nearby project, broaden scope, or load all projects to resolve uncertainty. Ask for the smallest missing decision only when canonical evidence cannot settle the blocker.

## Context boundary

Load one primary capability by default. Exclude unrelated projects, whole Knowledge trees, raw dumps, runtime artifacts, secrets, and copied methodology. Record inspected entrypoints, included files and reasons, excluded candidates and reasons, missing references, and context sufficiency.

## Output contract

Return:

- goal and routing decision;
- primary owner capability and canonical path;
- bounded context used and explicit exclusions;
- handoffs performed, or `none`;
- actions and changed scope;
- checks and observed results;
- risks and blockers;
- rollback;
- acceptance status;
- branch, PR, merge-gate, and production status when applicable.
