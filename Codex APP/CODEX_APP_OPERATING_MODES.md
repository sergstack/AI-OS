# Codex App Operating Modes

## Purpose

Define safe Codex operating modes.

## Modes

| Mode | Use when | Allowed actions |
|---|---|---|
| `inspect-only` | new repo, unclear scope, high risk | read repo, identify files, return plan |
| `docs-only` | README, manifest, upload guide, project docs | edit only allowed docs |
| `repo-hygiene` | structure, paths, setup consistency | docs/config only |
| `implementation` | feature, bugfix, pipeline, script | edit allowed implementation files |
| `test-qa` | tests, smoke checks, validation | add/run tests |
| `release` | acceptance, changelog, rollback | release docs/checks |

## Rule

If user does not specify mode, Codex must infer one and state it before editing.

## Stop conditions

Stop and report blocker if:

- objective is unclear;
- allowed files are missing;
- forbidden actions conflict with task;
- tests cannot be run or proposed;
- business logic change is required without approval;
- schemas or output contracts would change without approval;
- secrets or credentials are needed.
