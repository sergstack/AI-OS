# AGENTS.md

## Project purpose

<Describe what this repository does.>

## Architecture

<Key folders, entrypoints, data flow, important scripts.>

## Operating mode

Default mode:

- inspect first;
- plan before edit;
- make minimal scoped changes;
- run checks;
- review diff;
- report clearly.

Long-run mode:

- continue on safe, local, reversible assumptions;
- stop only on hard blockers;
- log assumptions in final report.

Ultra-long mode:

- use only with a complete ultra-long task package;
- decompose work into batches before editing;
- keep each batch scoped to one objective and one file group;
- checkpoint after every batch;
- run the smallest meaningful checks after each batch or logical group;
- retry failed checks once only when the fix is local, reversible, and inside allowed files;
- stop when hard blockers appear.

## Task package source

Prefer tasks prepared by `ChatGPT/[Codex]`.

Before implementation, verify the task contains:

- objective;
- context;
- repo;
- local path;
- branch;
- files to inspect;
- files allowed to modify;
- forbidden actions;
- expected outputs;
- acceptance criteria;
- tests / smoke checks;
- rollback plan.

For ultra-long tasks, also verify:

- autonomy profile;
- operating mode;
- batch plan;
- checkpoint policy;
- support files allowed: yes / no;
- safe retry policy;
- context reload rule;
- final response format.

## Allowed actions

- read repository files;
- edit only files allowed by task;
- run listed tests/checks;
- add focused tests only when useful and inside scope;
- create branch / commit / push only when explicitly requested;
- create a checkpoint file only when support files are explicitly allowed.

## Forbidden actions

- do not touch `.env`, secrets, credentials, tokens;
- do not change business logic without explicit approval;
- do not change schemas, APIs, output contracts, column names, or metric definitions without explicit approval;
- do not remove validation, tests, judge checks, or QA gates;
- do not add unrelated dependencies;
- do not deploy;
- do not add semantic search, vector DB, web UI, autonomous retrieval, or agentic workflows without explicit approval;
- do not run uncontrolled multi-agent or background automation.

## Hard blockers

Stop and report blocker when:

- secrets or credentials are needed;
- production/runtime/deploy/migration is involved;
- schema/API/output contract/business logic may change;
- destructive action is required;
- no meaningful validation is possible;
- acceptance criteria conflict;
- allowed file scope is missing or conflicts with requested work.

## Checkpoint discipline

For ultra-long work, report this after each batch:

```text
Batch completed:
Files changed:
Checks run:
Result:
Assumptions:
Risks:
Next batch:
Stop/blocker:
```

If the task package allows support files, use `.codex/RUN_STATE.md` for resumable state. Otherwise keep the checkpoint in the final response.

## Test commands

```bash
<insert project-specific test commands>
```

Fallback docs-only checks:

```bash
git status --short --branch
git diff --stat
git diff --check
find . -name "*.md" -type f | sort
```

## Final report

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
