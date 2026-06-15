# Ultra-Long Codex Task Package

Use this template when `ChatGPT/[Codex]` prepares a task for Codex App / Web / CLI / IDE and the work is expected to require multiple execution batches.

## Objective

<One concrete outcome.>

## Context

<Business / repo / technical context. Include links to source issue, PR, or handoff.>

## Executor surface

- Surface: Codex App / Codex Web / Codex CLI / IDE
- Autonomy profile: `ultra-long-local`
- Mode: inspect-only / docs-only / repo-hygiene / implementation / test-qa / release

## Repo

- GitHub repo:
- Local path:
- Base branch:
- Working branch:

## Files to inspect

```text
<file or folder>
```

## Files allowed to modify

```text
<file or folder>
```

## Forbidden actions

- Do not touch `.env`, secrets, tokens, credentials, private keys.
- Do not change production/runtime/deploy/migration behavior without explicit approval.
- Do not change business logic, formulas, schemas, APIs, output contracts, column names, or metric definitions without explicit approval.
- Do not add dependencies, MCP/tools, background automation, internet-enabled execution, semantic search, vector DB, or autonomous retrieval unless explicitly approved.
- Do not perform destructive filesystem actions.

## Batch plan

| Batch | Objective | Allowed files | Validation | Rollback |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

## Checkpoint policy

- After every batch, report batch status.
- Maintain checkpoint in final response.
- Create `.codex/RUN_STATE.md` only if explicitly allowed below.

Support files allowed: yes / no

## Tests / smoke checks

```bash
<smallest meaningful checks>
```

Fallback docs checks:

```bash
git status --short --branch
git diff --stat
git diff --check
```

## Safe retry policy

- Retry failed checks once only when the fix is local, reversible, and inside allowed files.
- If the same check still fails, stop and report diagnostics.

## Acceptance criteria

- [ ] Required files inspected.
- [ ] Changes stay inside allowed files.
- [ ] No forbidden files/actions touched.
- [ ] Each batch has checkpoint output.
- [ ] Tests/checks are reported honestly.
- [ ] Risks and assumptions are listed.
- [ ] Rollback path is clear.
- [ ] Acceptance status is `pass`, `partial`, `fail`, or `blocked`.

## Rollback plan

<How to undo changes: branch deletion, revert commit, file restore, etc.>

## Final response format

```text
Summary:
Mode:
Branch:
Batches completed:
Files changed:
Tests/checks run:
Assumptions:
Risks/limitations:
Rollback:
Acceptance status: pass / partial / fail / blocked
Next safe action:
```
