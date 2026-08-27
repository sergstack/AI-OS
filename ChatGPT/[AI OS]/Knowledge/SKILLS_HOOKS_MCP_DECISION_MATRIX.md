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
