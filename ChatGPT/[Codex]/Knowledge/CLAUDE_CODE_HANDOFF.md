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
