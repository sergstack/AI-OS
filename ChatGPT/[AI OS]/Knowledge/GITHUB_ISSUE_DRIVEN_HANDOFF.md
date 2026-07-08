# GitHub Issue-Driven Handoff

## Purpose

Use a GitHub Issue as the task contract when `[AI OS]` needs to hand implementation work to `[Codex]`.

## Standard route

```text
AI OS / LLM task framing -> GitHub Issue -> Codex branch -> checks -> Pull Request -> human review -> human-owned merge
```

## When to use

Use this handoff for:

- code changes;
- repository docs;
- CI or test workflow updates;
- scripts and repo tooling;
- repeatable task packaging for Codex.

## Responsibilities

### [AI OS]

- prepare the task;
- define evidence, risks, and constraints;
- specify acceptance criteria;
- avoid executing production changes.

### [Codex]

- create a branch;
- change only allowed files;
- run required checks;
- commit and push;
- open a PR;
- do not merge.

## Required handoff fields

- Goal
- Scope
- Allowed files
- Forbidden changes
- Business acceptance
- Artifact/content checks
- Technical checks
- Non-acceptance examples
- Checks to run
- Expected PR summary
- Risks
- Do not merge automatically

## Governance

- The Issue is the task contract.
- The PR is the review package.
- The human owner is the release gate.
- Passing technical checks is not acceptance when a user-facing artifact or business deliverable is incomplete, empty, or unusable.
- Weak or unsupported evidence must not become an implementation requirement.

## Related repository files

- `docs/AI_DEVELOPMENT_WORKFLOW.md`
- `docs/templates/CODEX_ISSUE_EXECUTION_PROMPT.md`
- `.github/ISSUE_TEMPLATE/codex-task.md`
- `.github/pull_request_template.md`
