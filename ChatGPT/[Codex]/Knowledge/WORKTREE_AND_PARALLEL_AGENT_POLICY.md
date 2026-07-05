# Worktree And Parallel Agent Policy

## Purpose

Allow safe isolated work while preventing uncontrolled multi-agent edits.

## Safe Worktree Use

Use a separate branch or worktree when:

- two tasks need independent diffs;
- a review must compare alternatives;
- a long-running local task should not disturb the main checkout;
- generated outputs or experiments must stay isolated.

Each worktree must have:

- one clear goal;
- one branch;
- allowed files;
- forbidden actions;
- checks;
- rollback or close-without-merge path.

## Parallel Agents

Parallel agents are allowed only when their scopes are isolated and reviewable.

Allowed examples:

- one agent reviews a PR while another works on unrelated docs in a different branch;
- one agent inspects logs or check output read-only while another edits allowed files;
- one agent drafts test ideas while the main agent implements the selected scoped change.

## Forbidden

Do not use parallel agents for:

- uncontrolled edits to the same files;
- hidden background automation;
- autonomous retrieval;
- production deploys;
- broad refactors;
- secrets handling;
- schema, API, output contract, formula, metric, or business logic changes without explicit approval.

## Coordination Rules

- Main agent owns the final diff.
- Review all changes before staging.
- Stage only intended files.
- Report which checks were actually run.
- Stop if branches diverge in a way that makes review unclear.
