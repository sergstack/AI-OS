# Codex App Review Checklist

## Before task

- [ ] Mode selected.
- [ ] Objective clear.
- [ ] Allowed files listed.
- [ ] Forbidden actions listed.
- [ ] Acceptance criteria present.
- [ ] Test / smoke check planned.
- [ ] Rollback known.

## Before ultra-long task

- [ ] Autonomy profile selected.
- [ ] Batch plan present.
- [ ] Checkpoint policy present.
- [ ] Support files allowed: yes / no.
- [ ] Context reload rule present.
- [ ] Safe retry policy present.
- [ ] Hard blockers listed.
- [ ] Final response format includes batches, checkpoint, rollback, acceptance status, and next safe action.

## During task

- [ ] Inspect before edit.
- [ ] Keep diff minimal.
- [ ] Stay within allowed files.
- [ ] Do not change business logic unless approved.
- [ ] Do not change schema / output contract unless approved.
- [ ] Do not remove validation.
- [ ] Do not touch secrets.

## During ultra-long task

- [ ] Execute one batch at a time.
- [ ] Checkpoint after each batch.
- [ ] Run the smallest meaningful checks.
- [ ] Retry a failed check once only when local, reversible, and inside allowed files.
- [ ] Stop on hard blockers instead of widening scope.
- [ ] Do not start background automation or uncontrolled multi-agent work.

## After task

- [ ] Changed files listed.
- [ ] Checks run listed.
- [ ] Tests pass / fail / blocked stated.
- [ ] Risks stated.
- [ ] Rollback stated.
- [ ] Acceptance status set.

## After ultra-long task

- [ ] Batches completed listed.
- [ ] Remaining batches or next safe action listed.
- [ ] Checkpoint state included or checkpoint file path reported.
- [ ] Assumptions separated from facts.
- [ ] Residual risks listed.
- [ ] Acceptance status is honest: `pass`, `partial`, `fail`, or `blocked`.

## Acceptance status

```text
pass / fail / blocked / partial
```
