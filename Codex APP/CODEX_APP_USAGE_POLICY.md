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
- analytical memo factory implementation.

## Autonomy levels

| Level | Meaning | Allowed |
|---|---|---|
| 0 | inspect only | read and plan |
| 1 | docs patch | docs/setup edits |
| 2 | local patch | allowed files + tests |
| 3 | PR-ready | branch + PR |
| 4 | automation | backlog, requires approval |

## Default

Start with Level 0 or Level 1 unless task package is complete.

## Not default

Do not enable by default:

- autonomous retrieval;
- background automation;
- MCP/tool installation;
- internet-enabled execution;
- production deploy.
