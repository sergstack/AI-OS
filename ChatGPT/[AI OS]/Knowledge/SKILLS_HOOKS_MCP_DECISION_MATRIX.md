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
