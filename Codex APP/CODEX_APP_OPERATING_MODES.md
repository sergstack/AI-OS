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
| `ultra-long-local` | scoped multi-batch local work | decompose, execute batches, checkpoint, validate, safe retry once |

## Rule

If the user does not specify a mode, Codex infers one, records it in the
AES/execution record, and reports it in the final report. This recording is
non-blocking and does not require a user round-trip before editing.

For `ultra-long-local`, Codex must also state:

- autonomy profile;
- batch plan;
- checkpoint policy;
- checks to run;
- hard blockers.

## Ultra-long execution rule

`ultra-long-local` does not mean uncontrolled autonomy.

It means:

```text
complete task package + allowed files + batch execution + checkpoint + validation + honest acceptance status
```

Codex must use `CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md` before starting this mode.

## Stop conditions

Stop on the canonical Codex hard blockers in `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`. Operating-mode setup also stops for genuinely unsafe or
conflicting objective, allowed-file, or forbidden-action scope; safely
inferable Goal Mode ambiguity is recorded and handled conservatively.
