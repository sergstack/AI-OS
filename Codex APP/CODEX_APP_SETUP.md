# Codex App Setup

## Purpose

Define how to use Codex App / Web / CLI / IDE surfaces safely.

## Surfaces

| Surface | Best use |
|---|---|
| Codex Web / ChatGPT | GitHub repo tasks, PR review, docs, remote implementation |
| Codex App | managing multiple coding tasks and longer agent sessions |
| Codex CLI | local repo patches, test loops, terminal workflow |
| IDE extension | focused interactive coding inside editor |

## Default settings

- Default mode: inspect before edit.
- Default branch: never direct `main`.
- Default scope: allowed files only.
- Default output: changed files + checks + acceptance status.
- Default risk rule: if no test is possible, report `blocked` or `partial`.

## Goal Mode default

Broad user goals are valid before the Codex APP layer.

Goal Mode is build-first. `ChatGPT/[Codex]`, `[LLM]`, or a Goal Mode GitHub issue should help Codex inspect relevant files, infer bounded safe scope, create or use a non-main branch, implement the smallest useful working version, run checks, fix in-scope failures when safe, and report evidence.

`Codex APP` must still inspect before edit, state inferred mode, confirm safe scope, and report blockers when scope cannot be safely inferred. It should not create roadmaps, epics, child issue trees, or approval packages for normal bounded implementation goals.

Do not ask Sergey for atomic task wording when the producer layer can compile it.

## Ultra-long local setup

Use `CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md` when a task needs more than one execution batch.

Ultra-long work requires:

- complete task package;
- explicit autonomy profile;
- branch or PR plan;
- batch plan;
- checkpoint policy;
- tests / smoke checks;
- rollback plan;
- final report format.

Default ultra-long profile: `ultra-long-local` from `CODEX_CONFIG_PROFILES.md`.

Codex must not start ultra-long implementation from a vague instruction. It must first convert the request into a task package or return a blocker.

## Repository preparation

Every repo used with Codex should contain:

- `README.md`;
- `AGENTS.md`;
- test commands;
- acceptance criteria;
- forbidden files list;
- rollback note.

For real working repositories, start from `CODEX_APP_AGENTS_TEMPLATE.md` and customize the project-specific sections.

## Security defaults

Codex must not touch:

- `.env`;
- secrets;
- tokens;
- credentials;
- private keys;
- production credentials;
- raw client data;
- governed KB internals unless explicitly allowed.
