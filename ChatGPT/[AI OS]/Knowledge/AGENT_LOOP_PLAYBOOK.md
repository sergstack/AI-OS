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

## Not Autonomous Agents

Supervised loops are not:

- autonomous retrieval;
- autonomous agents;
- production agentic workflows;
- background automation;
- vector DB / embeddings / semantic search;
- web UI;
- uncontrolled multi-agent execution.

## Stop Conditions

Stop when:

- no validation path exists;
- secrets, credentials, tokens, or `.env` values are needed;
- production, runtime, deploy, or migration work appears;
- formulas, schemas, output contracts, column names, metric definitions, or business logic may change;
- autonomous retrieval is needed;
- uncontrolled multi-agent work would be required;
- acceptance criteria conflict.

## Human Acceptance

Human acceptance is required before:

- merge;
- deploy;
- final adoption;
- promotion from candidate/pilot to standard workflow;
- adding automation, retrieval, persistent memory, or new runtime tools.
