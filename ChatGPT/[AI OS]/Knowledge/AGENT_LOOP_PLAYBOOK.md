# Agent Loop Playbook

## Purpose

Define supervised agent loops for AI-OS without promoting autonomous agents or production agentic workflows.

## Supervised Loop Pattern

```text
goal
-> action
-> check
-> revise/rerun
-> acceptance
-> next trigger
```

The loop is supervised when a human or explicit project gate controls scope, stop conditions, acceptance, and promotion.

## Allowed Loop Types

| Loop | Owner | Allowed retry |
|---|---|---|
| Analytics `autoloop` | `[Analytics]` | revise/rerun from visible QA findings |
| Codex long-run | `[Codex]` / Codex APP | retry once when local, reversible, and inside allowed files |
| PR Judge loop | `[Thinking]` / `[Codex]` | revise PR until pass/revise/blocked is clear |
| ChatGPT routing loop | `[Inbox Router]` | reroute when task type is unclear |
| Prompt QA Factory | `[AI OS]` -> owner project | candidate -> test -> judge -> revise -> selected, with human acceptance |
| Supervised AI-OS subagent dispatch (pilot) | `[AI OS]` root `ai-os-orchestrator` | root re-routes only via `ROUTING_RULES.md`; a child never selects the next owner |

## Supervised AI-OS Subagent Dispatch (Pilot)

Owner-approved bounded exception, dated 2026-09-02, for one MVP only. It is
**not** a general permission for agentic workflows or autonomous agents, and it
does not become a standard workflow automatically. Standardization requires a
separate owner decision.

Scope: the root `ai-os-orchestrator` may spawn a native built-in coding-agent
subagent to execute one bounded, already-routed capability slice, then resume.

Mandatory bounds:

- hub-and-spoke only: `root -> child -> root`; no `child -> child` delegation.
  Structurally enforced: every executor `agent_type` is a built-in type whose
  tool set excludes the `Agent` tool (`Plan`, `Explore`), so a child cannot
  spawn a sub-agent. Only the root holds the `Agent` tool;
- root `ai-os-orchestrator` is the only controller and the only canonical
  routing entrypoint; a child may return a `cross_domain_need` but never
  selects or invokes the next owner;
- one AES `execution_id` for the whole user goal;
- reuse the existing AES state machine, `continuation`, `route_trace`, `guards`,
  handoff, and `authority_provenance`; do not create a parallel model;
- `PROJECT_CAPABILITIES.yaml` remains the only capability registry;
- each child receives bounded `project-context` for its resolved capability
  only;
- the child gets no new authority; merge, deploy, production, destructive, and
  external-action gates are unchanged;
- no Temporal / LangGraph / CrewAI / AutoGen / Mastra and no new
  runtime, service, or database;
- `.claude/agents` is not a canonical source and `.gitignore` is unchanged;
- every dispatch uses `isolation: "worktree"` (`executor.workspace:
  isolated_worktree`): the child works in a clean, locked git worktree at a
  deterministic revision, never the parent working tree. No child is
  `write_capable`; an implementation slice returns a patch and the root applies
  and validates it. The root is the only writer;
- no subagent timeout primitive exists; this is a recorded runtime limitation,
  mitigated by `TaskStop` (explicit cancel) and guard limits;
- every actual spawn, result, and failure must be observable evidence
  (`NOT RUN != PASS`); a runtime failure is registered as an AES defect, not
  hidden by retry.

## Not Autonomous Agents

Supervised loops are not:

- autonomous retrieval;
- autonomous agents;
- production agentic workflows;
- background automation;
- vector DB / embeddings / semantic search;
- web UI;
- uncontrolled multi-agent execution (the pilot above is the only bounded,
  owner-approved, root-controlled exception).

## Stop Conditions

Stop when:

- no validation path exists;
- secrets, credentials, tokens, or `.env` values are needed;
- production, runtime, deploy, or migration work appears;
- formulas, schemas, output contracts, column names, metric definitions, or business logic may change;
- autonomous retrieval is needed;
- uncontrolled multi-agent work would be required beyond the bounded pilot;
- acceptance criteria conflict.

## Human Acceptance

Human acceptance is required before:

- merge;
- deploy;
- final adoption;
- promotion from candidate/pilot to standard workflow;
- adding automation, retrieval, persistent memory, or new runtime tools.
