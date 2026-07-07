# Failure Modes

## Severity levels

Use one of these severity levels before deciding whether to stop.

### recoverable

Continue when the issue is local, reversible, and can be logged.

Examples:

- missing optional docs link;
- ambiguous wording in README;
- missing non-critical checklist item;
- no dedicated docs test command.

### needs_check

Continue only after checking the affected text and validating the diff.

Examples:

- changed instructions affect Codex behavior;
- changed file references;
- changed task contract wording;
- changed checklist acceptance language.

### hard_blocker

Stop when the issue creates governance, safety, or validation risk. Use the canonical hard-blocker list in `AUTONOMY_POLICY.md`; do not maintain a competing list here.

## Common failures

- Scope creep.
- Broad refactor instead of task.
- No tests.
- Business logic changed silently.
- Output schema changed silently.
- Secrets exposed.
- Sensitive values or raw provider responses exposed in repo files, PR bodies, logs, or Knowledge bundles.
- Real provider/API execution treated as approved only because local configuration exists.
- LLM narrative mixed with deterministic calculations.
- Validation deleted.
- Acceptance criteria missing.
- Rollback missing.
- Premature automation added.

## Response

If a failure mode appears:

1. classify it as `recoverable`, `needs_check`, or `hard_blocker`;
2. continue for `recoverable` issues and log the assumption;
3. inspect and validate before continuing for `needs_check` issues;
4. stop for `hard_blocker` issues and report blocker plus safe minimal next step.
