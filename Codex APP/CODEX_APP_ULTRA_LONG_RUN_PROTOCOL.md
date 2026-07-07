# Codex App Ultra-Long Run Protocol

## Purpose

Make Codex App / Codex Web / Codex CLI work on long tasks by forcing structured execution, checkpoints, validation, and resumable state.

This is not background automation and not a permission bypass. It is a control protocol for scoped, local, reversible, testable work.

## When to use

Use this protocol only when all conditions are true:

- task package is complete;
- repo and local path are known;
- branch is specified or can be safely created;
- files to inspect are known;
- files allowed to modify are explicit;
- forbidden actions are explicit;
- tests or smoke checks are available;
- rollback path is defined.

If any required field is missing, use `inspect-only` or return a blocker.

## Default ultra-long cycle

```text
Intake gate
→ Repo map
→ Task decomposition
→ Batch execution
→ Checkpoint
→ Smallest meaningful checks
→ Safe retry once
→ Diff review
→ Next batch or final report
```

## Batch rules

Codex must not attempt the whole task as one giant edit.

Each batch must have:

- one objective;
- one allowed file group;
- one expected output;
- one validation method;
- one rollback note.

After each batch, Codex must update or report:

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

## Checkpoint state

For ultra-long work, Codex must maintain a resumable checkpoint in the final response and, when allowed by the task package, in a local markdown file such as:

```text
.codex/RUN_STATE.md
```

Checkpoint format:

```text
Goal:
Mode:
Autonomy profile:
Branch:
Allowed files:
Forbidden actions:
Completed batches:
Current batch:
Remaining batches:
Checks run:
Known failures:
Assumptions:
Risks:
Rollback:
Next safe action:
```

Do not create `.codex/RUN_STATE.md` unless the task package allows creating support files.

## Context reload rule

Before continuing a long task, Codex must re-read:

1. task package;
2. `AGENTS.md`;
3. relevant README / setup docs;
4. prior checkpoint or previous final report;
5. current `git status` and relevant diff.

Then Codex must state the next safe action before editing.

## Safe autonomy

Continue without asking only when the next action is:

- local;
- reversible;
- inside allowed files;
- not destructive;
- not a production/runtime/deploy/migration action;
- not a business logic, schema, API, output contract, column name, metric, formula, or governed KB change;
- testable by a meaningful check.

For safe uncertainty, make the smallest safe assumption and log it.

## Retry policy

If a check fails:

1. classify whether the failure is local, reversible, and inside allowed files;
2. apply one minimal fix only if safe;
3. rerun the smallest relevant check;
4. if it still fails, stop and report diagnostics.

Do not enter infinite test/fix loops.

## Hard stop conditions

Stop on the canonical Codex hard blockers in `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`. Ultra-long mode also stops when dependencies, MCP/tools, background automation, or internet-enabled execution are required without explicit approval.

## Multi-agent / parallel work

Multi-agent or parallel execution is allowed only as supervised decomposition, not as autonomous uncontrolled execution.

Allowed:

- split task into independent branches or batches;
- assign each batch a clear file scope;
- merge only after checks and diff review.

Not allowed by default:

- autonomous retrieval;
- background automation;
- production deploy;
- broad refactor;
- touching overlapping files from multiple agents without coordination.

## Final report

Every ultra-long run must use the canonical Codex final report schema from `ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`. Add these ultra-long fields when relevant: Mode, Autonomy profile, Batches completed, Current checkpoint, Remaining batches, and Next safe action.

Do not claim `pass` unless checks were actually run and observed.

## Best use

This protocol is strongest for:

- docs/config refactors;
- repo hygiene;
- test coverage improvement;
- safe bugfix batches;
- data pipeline work with explicit contracts;
- task package execution prepared by `ChatGPT/[Codex]`.

It is weakest for vague goals like “make it better”, “refactor everything”, or “make production-ready”. Codex is strong, but not telepathic. Feed it contracts, not fog.
