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

## Repository preparation

Every repo used with Codex should contain:

- `README.md`;
- `AGENTS.md`;
- test commands;
- acceptance criteria;
- forbidden files list;
- rollback note.

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
