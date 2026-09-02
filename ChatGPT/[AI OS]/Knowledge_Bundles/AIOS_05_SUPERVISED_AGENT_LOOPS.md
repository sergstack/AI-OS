# [AI OS] — Supervised Agent Loops

## Purpose

Compact upload artifact for [AI OS] covering supervised agent loops, loop acceptance, AutoResearch backlog, and skills/hooks/MCP decisions.

## Source files

- `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md`
- `ChatGPT/[AI OS]/Knowledge/LOOP_ACCEPTANCE_CHECKLIST.md`
- `ChatGPT/[AI OS]/Knowledge/AUTO_RESEARCH_BACKLOG.md`
- `ChatGPT/[AI OS]/Knowledge/SKILLS_HOOKS_MCP_DECISION_MATRIX.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- default_upload_mode: `Knowledge_Bundles`
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:274d77935b7fc633725ae5da1bb025a477aef0ef54d99bc08cc745c306ba061f
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md`

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
- hub-and-spoke only: `root -> child -> root`; no `child -> child` delegation;
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
- shared filesystem is a known risk: do not give a write-capable child unless
  the slice genuinely requires writes;
- no subagent timeout primitive exists; this is a recorded runtime limitation,
  mitigated by explicit cancel and guard limits;
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

## From: `ChatGPT/[AI OS]/Knowledge/LOOP_ACCEPTANCE_CHECKLIST.md`

# Loop Acceptance Checklist
## Purpose
Decide whether a loop is safe to run as supervised work.
## Required Before Running
- [ ] Goal is explicit.
- [ ] Owner project is named.
- [ ] Allowed actions are clear.
- [ ] Forbidden actions are clear.
- [ ] Checks are listed.
- [ ] Retry/rerun rule is bounded.
- [ ] Stop conditions are visible.
- [ ] Human acceptance point is defined.
## Pass Criteria
- loop follows `goal -> action -> check -> revise/rerun -> acceptance -> next trigger`;
- each action is reviewable;
- checks are deterministic or explicitly human-reviewed;
- retry does not widen scope;
- artifacts are source docs or PR diffs, not runtime stores;
- final status is `candidate / ready for human review` unless separately promoted.
## Revise Criteria
Use `revise` when:
- checks are missing but easy to add;
- stop conditions are incomplete;
- owner project is unclear;
- retry/rerun rule is too broad;
- human acceptance point is missing.
## Blocked Criteria
Use `blocked` when the loop requires:
- secrets or credentials;
- production/runtime/deploy access;
- schema, formula, metric, output contract, column, or business logic changes without approval;
- autonomous retrieval;
- vector DB, embeddings, semantic search, web UI, or production agentic workflow;
- uncontrolled multi-agent edits;
- no meaningful validation path.

## From: `ChatGPT/[AI OS]/Knowledge/AUTO_RESEARCH_BACKLOG.md`

# AutoResearch Backlog
## Purpose
Track future research-loop ideas without treating them as current production workflows.
## Status
AutoResearch / Karpathy-style loops are backlog or future pilot candidates only.
They are not:
- production workflows;
- autonomous agents;
- autonomous retrieval;
- vector DB / embeddings / semantic search;
- web UI;
- background automation.
## Candidate Pilot Shape
```text
research question
-> bounded source set
-> extraction
-> deterministic or human QA
-> synthesis
-> review
-> acceptance
-> next pilot decision
```
## Promotion Gates
Before promotion, require:
- explicit owner;
- source boundaries;
- no autonomous retrieval;
- reproducible checks;
- 3 accepted pilot cases;
- rollback path;
- human acceptance.
## Backlog Items
| Idea | Status | Next safe step |
|---|---|---|
| AutoResearch loop for AI trend triage | backlog | design one read-only pilot |
| Karpathy-style minimal verifiable research loop | backlog | define sources and QA gate |
| Multi-agent research critique | backlog | keep as review-only until isolated scopes are proven |

## From: `ChatGPT/[AI OS]/Knowledge/SKILLS_HOOKS_MCP_DECISION_MATRIX.md`

# Skills Hooks MCP Decision Matrix
## Purpose
Decide when skills, hooks, MCP tools, or sub-agents are useful as workflow aids. This file does not enable runtime tools.
## Decision Matrix
| Tooling option | Use when | Do not use when | Gate |
|---|---|---|---|
| Skill | workflow is repeated, bounded, and human-readable | one-off task is enough | document trigger and checks |
| Hook | local guardrail is deterministic and reversible | it mutates production/runtime state | dry-run or human review first |
| MCP tool | existing source/tool access is needed | it expands retrieval beyond approved scope | explicit source and permission |
| Sub-agent | scope is isolated and final diff owner is clear | agents would edit same files uncontrolled | branch/file isolation |
| Background automation | almost never in this repo layer | task lacks production approval | separate promotion gate |
## Default
Prefer prompt/runbook/checklist first. Add tools only when repeated friction is proven.
## Forbidden Before Promotion
- autonomous retrieval;
- production agentic workflow;
- vector DB;
- embeddings;
- semantic search;
- web UI;
- persistent runtime artifact store;
- uncontrolled multi-agent edits.
## Human Acceptance
Human acceptance is required before enabling any new tool, hook, MCP workflow, sub-agent pattern, or automation as a standard workflow.
## MCP verification freshness
An approved source and permission are not indefinite verification. For each
MCP tool considered for a standard workflow, keep a compact, human-reviewed
verification record:
```text
verification_status: not_verified | verified | reverify_required | blocked
verified_at:
verified_revision_or_fingerprint:
provider_or_server_identity:
tool_or_schema_identity:
permissions_or_auth_scope:
freshness_status: current | stale | unverifiable | not_applicable
authority_evidence_ref:
reverify_trigger:
```
Reuse AES freshness semantics: `current` requires that the verification can
be tied to the current revision/fingerprint and unchanged relevant scope;
`stale` applies after a relevant known change; `unverifiable` applies when
the current implementation/revision cannot be compared with the verification
record. A timestamp alone, unchanged registry description, or matching name
is not sufficient proof of implementation or security freshness.
Set `reverify_required` when the provider/server, package or registry
revision, tool list/schema identity, permissions/auth scope, or current
implementation fingerprint changes; also reverify when the previous record
cannot be tied to the current artifact. Higher-risk proposed use may require
fresher, explicitly scoped owner evidence, but this file intentionally sets
no arbitrary global time-to-live.
An auth/permission expansion is new authority: prior verification and approval
do not authorize it. Reverification supplies evidence only; it never installs,
executes, promotes, or authorizes an MCP server automatically. Human
acceptance remains required for standardization.
