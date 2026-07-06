# Handoff Style Standard

## Purpose

Shared style for handoffs between ChatGPT project folders and Codex APP.

Use this as wording guidance. It is not runtime automation and does not replace the source files owned by each project.

## Default Style

Handoffs should be compact, scoped, and reviewable.

```text
Handoff to:
Goal:
Context:
Evidence / sources:
Scope:
Allowed changes:
Forbidden changes:
Expected output:
Checks:
Risks / limitations:
Rollback:
Acceptance status:
Next step:
```

## Project-Specific Additions

- `[AI OS]`: include evidence status, confidence, routing decision, and unsupported claims.
- `[Thinking]`: include decision options, assumptions, tradeoffs, and recommended next step.
- `[Analytics]`: include question/scope, data status, grain/period/filters, method, QA, limitations, and decision or recommendation.
- `[LLM]`: include context boundaries, prompt or model-routing goal, judge/revise gate, and forbidden raw inputs.
- `[Codex]`: include branch expectation, allowed files/actions, checks, rollback, PR summary needs, and no-auto-merge rule.
- `[Inbox Router]`: include classification, target project, urgency, confidence, and first safe action.

## Merge And Acceptance

- GitHub remains the live source of truth.
- Codex APP may create branches, commits, checks, and PRs when requested.
- Pull requests require human review before merge unless Sergey explicitly asks Codex APP to merge.
- Acceptance statuses should stay conservative: `candidate / ready for human review` unless production promotion was explicitly completed.

## Forbidden As Handoff Inputs

- secrets, `.env`, credentials, API keys, tokens;
- raw transcripts, source-card dumps, chunks, large raw dumps;
- logs, journals, runtime artifacts, zip archives;
- vector DB, embeddings, semantic search, autonomous retrieval;
- production deploy instructions or autonomous agent workflows without explicit approval.
