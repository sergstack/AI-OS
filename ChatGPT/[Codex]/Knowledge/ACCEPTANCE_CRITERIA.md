# Codex Acceptance Criteria

Implementation is accepted when:

1. Task objective is met.
2. Scope stayed within allowed files.
3. Forbidden actions were not taken.
4. Tests or smoke checks were run, or blocker stated.
5. Output contract is preserved unless explicitly changed.
6. Final report lists files changed, assumptions, risks.
7. Rollback path is clear for risky changes.
8. Safe autonomy assumptions are logged when long-run mode is used.

## Status format

```text
acceptance_status: pass / partial / fail / blocked
tests:
files_changed:
residual_risks:
next_step:
```
