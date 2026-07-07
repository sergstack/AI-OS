# Codex App Usage Policy

## Purpose

Control cost, time, scope and autonomy.

## Cheap tasks

Use Codex freely for:

- docs-only edits;
- path audits;
- grep checks;
- small bugfixes;
- smoke checks;
- task package validation.

## Expensive tasks

Use only after design package exists:

- large repo exploration;
- multi-agent work;
- long refactors;
- full pipeline implementation;
- repeated test/fix loops;
- data pipeline automation;
- analytical memo factory implementation;
- ultra-long multi-batch local work.

## Autonomy levels

| Level | Meaning | Allowed |
|---|---|---|
| 0 | inspect only | read and plan |
| 1 | docs patch | docs/setup edits |
| 2 | local patch | allowed files + tests |
| 3 | PR-ready | branch + PR |
| 4 | supervised ultra-long local | complete task package + batches + checkpoints + checks |
| 5 | automation | backlog, requires explicit approval |

## Default

Start with Level 0 or Level 1 unless the task package is complete or the
canonical `Goal Mode Contract` provides enough bounded scope for a local,
reversible docs/config change.

For Level 4, require `CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md` and `templates/ULTRA_LONG_TASK_PACKAGE.md` or an equivalent complete task package.

## Level 4 guardrails

Level 4 is for long supervised execution, not free-form autonomy.

Required controls:

- explicit allowed files;
- explicit forbidden actions;
- batch plan;
- checkpoint policy;
- smallest meaningful checks;
- safe retry once only;
- rollback path;
- final acceptance status.

## Not default

Do not enable by default:

- autonomous retrieval;
- background automation;
- MCP/tool installation;
- internet-enabled execution;
- production deploy;
- uncontrolled multi-agent execution.
