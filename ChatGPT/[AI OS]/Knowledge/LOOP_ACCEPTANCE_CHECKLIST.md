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
