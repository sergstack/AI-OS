# AI Development Workflow

## Purpose

This repository uses an issue-driven AI development workflow.

ChatGPT is used for task framing and review. Codex is used for controlled implementation. GitHub Issues are the task contract. Pull Requests are the review and acceptance gate. Human review is required before merge.

For raw or unclear inputs, use `[Inbox Router]` before creating a Codex task.
Codex issues should already be implementation-ready.

## Standard Flow

1. Create a GitHub Issue.
2. Define goal, scope, allowed files, forbidden changes, acceptance criteria, and checks.
3. Ask Codex to work from the Issue.
4. Codex creates a separate branch.
5. Codex changes only allowed files.
6. Codex runs required checks.
7. Codex commits and pushes.
8. Codex opens a Pull Request.
9. Codex does not merge.
10. Human owner reviews and merges only after acceptance.

## Roles

| Role | Responsibility |
|---|---|
| ChatGPT | Task framing, scope, risks, acceptance criteria |
| GitHub Issue | Source of truth for the task |
| Codex | Implementation in a separate branch |
| CI / checks | Automated verification |
| Pull Request | Review package |
| Human owner | Final review and merge |

## Issue Contract

Every Codex-ready Issue should include:

```text
Goal:
Scope:
Allowed files:
Forbidden changes:
Acceptance criteria:
Checks to run:
Expected PR summary:
Risks:
Do not merge.
```

## PR Requirements

Each PR must include:

- linked Issue;
- changed files summary;
- checks run;
- pass/fail result;
- risks / residual risks;
- human review needed;
- clear note: ready for review or not ready.

## Hard Rules

- Do not work directly on `main`.
- Do not merge automatically.
- Do not change files outside allowed scope.
- Do not skip checks.
- Do not treat AI output as accepted without review.
- Do not introduce production workflows without acceptance gates.
- Do not add secrets, raw dumps, runtime artifacts, logs, vector DB files, or embeddings to the repository.

## Acceptance

A PR can be merged only when:

- scope matches the Issue;
- allowed files rule is respected;
- required checks pass;
- PR summary is clear;
- risks are documented;
- human reviewer accepts the change.

## Recommended Labels

| Label | Use |
|---|---|
| `ai-task` | Work item intended for AI-assisted execution |
| `codex` | Ready or suitable for Codex execution |
| `docs-only` | Documentation-only change |
| `ci` | CI / checks / workflow change |
| `governance` | Rules, templates, gates, or operating standards |
| `needs-human-review` | Human review is required before merge |
| `do-not-merge` | Merge is blocked until explicitly cleared |
| `ready-for-codex` | Issue has enough detail for Codex execution |

## Minimal Codex Command

```text
Execute GitHub Issue #<NUMBER> as a controlled Codex batch.
Create a branch, make only allowed changes, run checks, commit, push, and open a PR.
Do not merge.
```
