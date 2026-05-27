# Codex Long-Run Playbook

## Purpose

Help Codex keep working on scoped local tasks without unnecessary questions.

## Cycle

Use this cycle for long-running implementation:

```text
Inspect -> Plan -> Implement -> Test -> Retry once if safe -> Review -> Report
```

## Working rules

- Do not ask on reversible docs or configuration decisions inside allowed files.
- Use safe defaults from the task package and existing repository structure.
- Keep the diff small and trace every changed line to the task.
- Prefer updating existing files and cross-references over creating duplicate guidance.
- Do not widen scope to unrelated cleanup.
- Treat missing optional docs links as recoverable when a nearest valid path exists.

## Test and retry

Run the smallest meaningful checks for the task.

If a check fails:

1. decide whether the failure is local, reversible, and inside allowed files;
2. attempt one minimal fix only when safe;
3. rerun the smallest relevant check;
4. if it still fails, stop and report diagnostics.

Do not retry when the issue involves secrets, production systems, migrations, destructive commands, governed KB content outside scope, or output contracts.

## Reporting

Report:

- changed files;
- commands and checks run;
- assumptions;
- risks or limitations;
- rollback path;
- acceptance status.

Use `pass`, `partial`, `fail`, or `blocked` honestly. Do not claim checks passed unless they were run and observed.
