# Handoff Style Standard

## Purpose

Shared style for handoffs between ChatGPT project folders and Codex APP.

Use this as the canonical handoff field set for project-to-project handoffs.
It is not runtime automation and does not replace the source files owned by
each project.

## Default Style

Handoffs should be compact, scoped, and reviewable.

```text
From:
To:
Task type:
Mode: goal / strict
Objective:
Context:
Inputs:
Constraints:
Authority provenance:
Expected output:
Acceptance criteria:
  Business acceptance:
  Artifact/content checks:
  Non-acceptance examples:
Risks:
Evidence / confidence:
Open questions:
Suggested first step:
```

Use `Mode: goal` for broad repo/workflow/project goals where the receiving
project can infer bounded safe scope. Use `Mode: strict` for high-risk,
already-scoped, ultra-long, or explicitly requested task packages.

The three acceptance sub-fields are required for user-facing artifacts and business deliverables. `Objective:` preserves the original goal through continuation; do not replace it with a local subtask.

`Authority provenance:` is required whenever a handoff carries a
decision-relevant claim. For each such claim, retain the claim text, authority
class, source reference, and action eligibility. Use only the canonical AES
classes: `source_fact`, `owner_instruction`, `accepted_policy`,
`observed_execution_evidence`, `candidate_research`, and
`hypothesis_recommendation`. Candidate research and hypotheses may inform
review, but are never action-eligible; a source fact or observed evidence is
not itself an authorization. This field complements, and never replaces,
`authority_status` or a required owner/merge/production gate.

## Project-Specific Additions

- `[AI OS]`: include evidence status, confidence, routing decision, and unsupported claims.
- `[Thinking]`: include decision options, assumptions, tradeoffs, and recommended next step.
- `[Analytics]`: include question/scope, data status, grain/period/filters, method, QA, limitations, and decision or recommendation.
- `[LLM]`: include context boundaries, prompt or model-routing goal, judge/revise gate, and forbidden raw inputs.
- `[Codex]`: include branch expectation, allowed files/actions, checks, rollback, PR summary needs, and merge/gate status.
- `[Inbox Router]`: include classification, target project, urgency, confidence, and first safe action.

## Merge And Acceptance

- GitHub remains the live source of truth.
- Codex APP may create branches, commits, checks, and PRs when requested.
- Use the canonical merge policy in `GOAL_MODE.md`.
- Codex / Codex APP must not manually merge PRs or decide final mergeability by themselves.
- Acceptance statuses should stay conservative: `candidate / ready for owner review` unless production promotion was explicitly completed.

## Forbidden As Handoff Inputs

- secrets, `.env`, credentials, API keys, tokens;
- raw transcripts, source-card dumps, chunks, large raw dumps;
- logs, journals, runtime artifacts, zip archives;
- vector DB, embeddings, semantic search, autonomous retrieval;
- production deploy instructions or autonomous agent workflows without explicit approval.
