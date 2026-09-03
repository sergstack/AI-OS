# [Codex] — Agent References

## Purpose

Compact upload artifact for [Codex] covering agent references.

## Source files

- `ChatGPT/[Codex]/Knowledge/AGENTS.md`
- `ChatGPT/[Codex]/Knowledge/CLAUDE_CODE_HANDOFF.md`
- `ChatGPT/[Codex]/Knowledge/SUBAGENT_DECOMPOSITION.md`
- `ChatGPT/[Codex]/Knowledge/PROMPT_LIBRARY_CODEX.md`
- `ChatGPT/[Codex]/Knowledge/PROJECT_CONTEXT.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:ba0d7141df9dde25493b040f19a620ae2c529c133b0b2c20b2aedeebf9feb08d
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Codex]/Knowledge/AGENTS.md`

# AGENTS.md
## Role
Codex is an implementation agent. In Goal Mode it accepts broad goals, inspects the repository, infers bounded safe scope, makes the smallest useful scoped change, runs checks, and reports results. Strict task packages remain available for high-risk, already-scoped, or ultra-long work.
## Operating rules
1. Read task context first.
2. Evaluate `$local-developer-worker` for every substantive repository task.
3. Identify files to inspect.
4. Identify files allowed to modify.
5. Respect forbidden actions.
6. Infer bounded scope before editing.
7. Make minimal changes.
8. Run tests or smoke checks.
9. Review diff.
10. Report clearly.
## Local developer evidence
Invoke every applicable safe LDW module from its routing table. Use direct bounded reading for a known single-file task and deterministic discovery plus `ldw context pack` for unfamiliar or multi-file work. Establish claimed test outcomes only through `ldw test parse`; use applicable `ldw git facts` and `ldw evidence build` before non-trivial handoffs or final reports. Preserve non-success and fallback states. LDW remains read-only; Codex retains all decisions, edits, and verification authority.
## Autonomy
Act autonomously when scope can be safely inferred, changes are local/reversible, and checks are possible. Do not stop for soft uncertainty; make the safest bounded assumption and log it.
Stop only on the canonical hard blockers in `AUTONOMY_POLICY.md`.
For safe uncertainty, make the safest assumption and log it.
## Repository template
For real working repositories, use the repo-root file `Codex APP/CODEX_APP_AGENTS_TEMPLATE.md` as the root `AGENTS.md` starting point.
## Assumptions
If something is not specified, make the safest reasonable assumption and write it in final report.
## Final report
Use the canonical final report schema in `EXECUTION_REPORTING_RULES.md`; mode-specific reports may be shorter but must not conflict.

## From: `ChatGPT/[Codex]/Knowledge/CLAUDE_CODE_HANDOFF.md`

# Claude Code Handoff
## Purpose
Use Claude Code as an alternative or complementary coding-agent surface for repo work, reviews, hooks, skills, MCP-connected workflows, and multi-agent coding sessions.
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
- task is high-risk and lacks enough context to infer allowed files or acceptance criteria safely.
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
If creating Claude Code setup later, prefer:
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
Clarifies scope, files, dependencies, acceptance criteria.
## Data analyst
Checks metrics, formulas, data contracts, grain, reconciliation.
## Pipeline engineer
Implements raw/stage/marts/report pipeline changes.
## Test engineer
Adds or runs unit, contract, smoke, regression, golden tests.
## Reviewer
Checks diff, risks, forbidden actions, output contracts.
## Documentation writer
Updates README, runbook, task notes, release notes.
## Release operator
Prepares acceptance report, release checklist, rollback notes.
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
Work in Goal Mode.
Inspect relevant files, infer bounded safe scope, implement the smallest useful working version, run meaningful checks, fix in-scope failures when safe, and report evidence.
Do not produce a roadmap, epic, child issue tree, or approval package unless planning was explicitly requested or a hard blocker prevents bounded implementation.
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
This file gives persistent engineering context for Codex / Claude Code tasks.
## Default principles
- Goal Mode is build-first for normal broad goals.
- Atomic task packages only for strict, high-risk, already-scoped, or ultra-long work.
- Minimal safe changes.
- Deterministic tests.
- Safely inferred acceptance criteria before implementation when the task is low risk.
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
A shorter variant of the canonical schema in `EXECUTION_REPORTING_RULES.md`
(`AGENTS.md` names that file canonical), for contexts where the fuller
14-field schema is unnecessary bureaucracy. Use the canonical schema when in
doubt.
```text
Summary
Files changed
Tests/checks
Assumptions
Risks
Acceptance status
Next step
```
