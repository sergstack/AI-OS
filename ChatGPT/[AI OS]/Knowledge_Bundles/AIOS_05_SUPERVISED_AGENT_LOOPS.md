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

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:64a5c38e669d3ac5d825ddbcf9070e8eeba3c2c591f7df798fde617b151f07e4
- default_upload_mode: `Knowledge_Bundles`

---

# Content

## Supervised Loop Pattern

Allowed loop shape:

```text
goal
-> action
-> check
-> revise/rerun
-> acceptance
-> next trigger
```

Supervised loops require explicit owner, bounded action, checks, stop conditions, and human acceptance.

## Allowed Loops

| Loop | Owner | Allowed retry |
|---|---|---|
| Analytics `autoloop` | `[Analytics]` | revise/rerun from visible QA findings |
| Codex long-run | `[Codex]` / Codex APP | retry once when local, reversible, and inside allowed files |
| PR Judge loop | `[Thinking]` / `[Codex]` | revise PR until pass/revise/blocked is clear |
| ChatGPT routing loop | `[Inbox Router]` | reroute when task type is unclear |
| Prompt QA Factory | `[AI OS]` -> owner project | candidate -> test -> judge -> revise -> selected, with human acceptance |

## Boundary

Supervised loops are not autonomous agents, autonomous retrieval, production agentic workflows, background automation, vector DB, embeddings, semantic search, web UI, or uncontrolled multi-agent execution.

## Stop Conditions

Stop on no validation path, secrets, production/runtime/deploy, schema/formula/business logic/output contract changes, autonomous retrieval, uncontrolled multi-agent work, or conflicting acceptance criteria.

## Acceptance Checklist

Pass when the loop has goal, owner, allowed actions, forbidden actions, checks, bounded retry/rerun, stop conditions, and human acceptance point.

Use `revise` when the loop is close but missing checks, stop conditions, owner, retry rule, or human acceptance point.

Use `blocked` when the loop requires secrets, production/runtime/deploy access, unapproved schema/formula/business logic changes, autonomous retrieval, vector DB, embeddings, semantic search, web UI, production agentic workflow, uncontrolled multi-agent edits, or no validation path.

## AutoResearch Backlog

AutoResearch / Karpathy-style loops are backlog or future pilot candidates only. They are not production workflows, autonomous agents, autonomous retrieval, vector DB, embeddings, semantic search, web UI, or background automation.

Future pilots require explicit owner, source boundaries, no autonomous retrieval, reproducible checks, 3 accepted pilot cases, rollback path, and human acceptance.

## Skills / Hooks / MCP Decision Matrix

Prefer prompt/runbook/checklist first. Consider skills, hooks, MCP tools, or sub-agents only when repeated friction is proven and the source, permission, isolation, checks, and human acceptance gate are clear.

Do not enable new tools, hooks, MCP workflows, sub-agent patterns, or automation as standard workflow without human acceptance and promotion gate.
