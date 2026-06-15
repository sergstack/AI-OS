# [Codex] — Agent References

## Purpose

Compact upload artifact for [Codex] covering agent references.

## Source files

- `ChatGPT/[Codex]/Knowledge/AGENTS.md`
- `ChatGPT/[Codex]/Knowledge/CLAUDE.md`
- `ChatGPT/[Codex]/Knowledge/CLAUDE_CODE_HANDOFF.md`
- `ChatGPT/[Codex]/Knowledge/SUBAGENT_DECOMPOSITION.md`
- `ChatGPT/[Codex]/Knowledge/PROMPT_LIBRARY_CODEX.md`
- `ChatGPT/[Codex]/Knowledge/PROJECT_CONTEXT.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Codex]/Knowledge/AGENTS.md`

# AGENTS.md
## Role
## Operating rules
1. Read task context first.
2. Identify files to inspect.
3. Identify files allowed to modify.
4. Respect forbidden actions.
5. Plan before editing.
6. Make minimal changes.
7. Run tests or smoke checks.
8. Review diff.
9. Report clearly.
## Autonomy
- secrets are needed;
- production/runtime/deploy/migration is involved;
- schema/API/output contract/business logic may change;
- destructive action is required;
- no meaningful validation is possible;
- acceptance criteria conflict.
## Repository template
For real working repositories, use `../../../Codex APP/CODEX_APP_AGENTS_TEMPLATE.md` as the root `AGENTS.md` starting point.
## Assumptions
## Final report
```text
Summary:
Files changed:
Tests run:
Assumptions:
Risks:
Acceptance status:
Next step:
```


## From: `ChatGPT/[Codex]/Knowledge/CLAUDE.md`

# CLAUDE.md
## Project context
## Workflow
1. Inspect repository.
2. Restate task and constraints.
3. Create short plan.
4. Edit only allowed files.
5. Run tests/checks.
6. Review before commit or final answer.
7. Report changes and risks.
## Safe edit rules
- Do not modify secrets.
- Do not remove validation.
- Do not change business logic unless explicitly requested.
- Do not broaden scope.
- Do not commit unless instructed.
- Do not add new infrastructure without acceptance.
## Subagent decomposition
- planner;
- implementation engineer;
- test engineer;
- reviewer;
- release operator.
## Testing expectations
- unit tests;
- contract tests;
- smoke checks;
- golden output checks;
- regression checks.


## From: `ChatGPT/[Codex]/Knowledge/CLAUDE_CODE_HANDOFF.md`

# Claude Code Handoff
## Purpose
## Use when
- repo documentation needs review;
- `CLAUDE.md` project memory is useful;
- hooks / skills / MCP workflows are relevant;
- multi-agent coding review is useful;
- local terminal / IDE coding surface is preferred;
- PR review or repo-wide cleanup is needed.
## Do not use when
- task is purely strategic → use `[Thinking]`;
- task is deterministic analytics → use `[Analytics]`;
- task is AI concept / evidence check → use `[AI OS]`;
- task is prompt architecture → use `[LLM]`;
- task lacks allowed files / acceptance criteria.
## Required handoff package
- goal;
- repo;
- branch;
- files to inspect;
- files allowed to modify;
- forbidden files;
- commands allowed;
- tests to run;
- acceptance criteria;
- rollback note.
## Forbidden by default
- secrets;
- `.env`;
- credentials;
- production deploy;
- broad refactor;
- changing metric definitions;
- changing schemas;
- changing governed KB content;
- adding semantic search / vector DB / web UI / autonomous retrieval without approval.
## Claude Code specific assets
- `CLAUDE.md`;
- skills;
- hooks;
- MCP config;
- PR review checklist.
Do not add these unless explicitly requested.
## Acceptance criteria
Pass if:
- changes are atomic;
- diff is reviewable;
- tests / smoke checks are reported;
- forbidden files are untouched;
- final answer includes branch / commit / PR.


## From: `ChatGPT/[Codex]/Knowledge/SUBAGENT_DECOMPOSITION.md`

# Subagent Decomposition
## Planner
## Data analyst
## Pipeline engineer
## Test engineer
## Reviewer
Checks diff, risks, forbidden actions, output contracts.
## Documentation writer
## Release operator
## Rule
Do not create subagents for complexity theatre. Use roles only to make the work clearer.


## From: `ChatGPT/[Codex]/Knowledge/PROMPT_LIBRARY_CODEX.md`

# Prompt Library for Codex
## Inspect repo
```text
Inspect the repository for this task.
Do not edit yet.
Return relevant files, entrypoints, risks, and proposed plan.
```
## Implement
```text
Implement the scoped task below.
Respect files allowed to modify and forbidden actions.
Run tests if available.
Report files changed and acceptance status.
```
## Long-run implementation
```text
Implement the scoped task below in long-run mode.

Do not ask unless a hard blocker appears.
For reversible local decisions, make the safest assumption and continue.
Keep the diff minimal.
Run the smallest meaningful checks.
If a check fails, attempt one minimal fix.
Report changed files, checks, assumptions, risks, rollback, and acceptance status.
```
## Refactor safely
```text
Refactor only the specified files.
Do not change behavior.
Add or run regression checks.
Explain how behavior is preserved.
```
## Bugfix
```text
Reproduce or explain the bug.
Identify root cause.
Patch minimally.
Run tests.
Report residual risks.
```
## Review
```text
Review the diff for bugs, scope creep, missing tests, business logic changes, and output contract risks.
Return pass/revise/blocked.
```


## From: `ChatGPT/[Codex]/Knowledge/PROJECT_CONTEXT.md`

# Project Context
## Purpose
## Default principles
- Atomic task packages.
- Minimal safe changes.
- Deterministic tests.
- Acceptance criteria before implementation.
- Long-run autonomy only for scoped, local, reversible, testable work.
- Diff review before final.
- Rollback notes for risky changes.
## Forbidden by default
- secrets handling;
- broad refactors;
- changing business logic without approval;
- deleting QA checks;
- changing output contracts without explicit acceptance;
- adding vector DB / embeddings / web UI / agentic automation before governance approval.
## Preferred final answer
```text
Summary
Files changed
Tests/checks
Assumptions
Risks
Acceptance status
Next step
```
