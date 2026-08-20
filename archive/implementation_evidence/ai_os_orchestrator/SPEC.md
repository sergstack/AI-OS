# SPEC

## Goal

Add one canonical `ai-os-orchestrator` entrypoint skill so a user can provide a goal without manually naming the routing sequence or owner capability.

## Current state

- `PROJECT_CAPABILITIES.yaml` is the canonical capability location registry.
- `project-context` loads bounded context only after routing and does not classify requests.
- Root instructions describe the sequence but do not name one reusable entrypoint skill.
- The command surface exposes `ChatGPT Route` for explicit routing, not a default goal entrypoint.

## Requirements

- Classify goals using the canonical front-door routing rules.
- Resolve exactly one primary owner through `PROJECT_CAPABILITIES.yaml`.
- Use `project-context` only after owner resolution.
- Preserve ownership boundaries and use explicit handoffs for additional capabilities.
- Apply relevant checks, acceptance, rollback, reporting, and merge rules.
- Load only task-relevant context.
- Fail closed on ambiguous ownership, missing registry entries, unsafe paths, missing canonical paths, or unresolved required entrypoints.
- Make the orchestrator the default AI-OS goal behavior while keeping direct strict or already-routed workflows available.

## Constraints

- Keep canonical routing semantics in `ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md`.
- Keep `PROJECT_CAPABILITIES.yaml` a location resolver; the orchestrator is not a domain capability.
- Do not duplicate project methodology or Knowledge in the new skill.
- Do not modify local user configuration, merge a PR, or claim production promotion.
- Keep the change bounded, reversible, and based on `origin/main`.

## Acceptance criteria

- `.agents/skills/ai-os-orchestrator/SKILL.md` exists and specifies the complete routing, resolution, bounded-context, handoff, validation, fail-closed, and reporting contract.
- `AGENTS.md`, `GOAL_MODE.md`, `COMMAND_SURFACE.md`, and the reusable global-entry documentation point goals to the canonical orchestrator without restating domain routing tables.
- Tests verify both canonical skills, registry/path integrity, default entry behavior, and fail-closed requirements.
- At least three branch-specific pilot records cover one-owner context loading, mixed explicit handoff, and blocked routing/path failure.
- Relevant repository checks and the full test suite pass through observed LDW test parsing.
- A separate Judge review returns `pass`, or correctable findings are fixed and rechecked.
- Final evidence reports changed files, checks, risks, rollback, acceptance, and branch/PR status.

## Risks

- Duplicated routing semantics could drift from Inbox Router rules.
- “Default” could accidentally force heavy AI-OS loading for simple local work.
- Cross-domain goals could blur primary ownership or imply autonomous multi-project execution.
- Documentation alone cannot guarantee already-running clients reload skills or user-level instructions.
