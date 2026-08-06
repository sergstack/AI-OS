# Goal Mode

Goal Mode is the default user-facing workflow for AI-OS and Codex. It is build-first: inspect, infer bounded scope, implement the smallest useful working version, check it, and report evidence.

Execution follows the canonical Autonomous Execution Standard in
`AUTONOMOUS_EXECUTION_STANDARD.md`. Project-specific requirements are
supplied by the applicable execution extension (see
`AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`). This reference does not
change the Goal Mode Contract or Merge Policy below.

## Goal Mode Contract

Future issues and handoffs may reference `Goal Mode Contract` by name instead of repeating this block.

```text
Work in Goal Mode from issue #...

Autonomy:
Proceed without asking on local, reversible, scoped changes.
Stop only on hard blockers.

Execution:
Inspect repo first.
Infer bounded scope.
Create/use codex/... branch.
Make smallest useful verified change.
Run relevant checks.
Fix safe in-scope failures once.
Open PR for human review.
Follow the canonical Merge Policy below.

Forbidden:
No sensitive/local config files.
No unapproved provider/API calls.
No source workbook mutation.
No Safe Apply.
No business logic/schema/formula/output contract changes unless explicit.
No runtime artifacts committed.
No deletion without quarantine.

Report:
Summary
Branch / PR
Files changed
Commands run
Tests
Assumptions
Risks
Rollback
Acceptance status
Merge / gate status
```

## Merge Policy

This is the canonical active merge-policy reference for AI-OS.

- Codex and agents must not manually merge pull requests or decide final mergeability by themselves.
- Tier 0/1 docs pull requests may auto-merge only through the deterministic GitHub Merge Gate after required checks pass.
- Tier 2 protected changes require owner review.
- GitHub branch protection, rulesets, labels, and CODEOWNERS enforcement are owner-verified repository settings.
- Passing smoke QA or documentation checks does not imply production readiness or `production_promotion=yes`.

Owner-side Merge Gate settings are tracked in
`docs/MERGE_GATE_OWNER_CHECKLIST.md`.

## Flow

```text
GOAL -> inspect repo -> infer bounded safe scope -> branch -> implement smallest useful version -> check/fix in scope -> report/PR -> owner review
```

## Outcome-First Acceptance

For any task that produces a user-facing artifact or business deliverable, success requires business acceptance and artifact/content verification, not only passing tests or opening a PR.

Technical checks passed, pipeline completed, files generated, or PR opened are not sufficient if the user-facing result does not satisfy the business outcome.

## Existing working script refactors

When Sergey asks to clean, simplify, modularize, or refactor an existing working script or pipeline, use `Existing Script Controlled Refactor Standard` from `EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`.

This standard is not mandatory for all tasks. It applies only when current behavior is useful and must be preserved.

Required order:

```text
baseline current behavior -> define output contract -> add safety tests -> refactor -> compare before/after output -> acceptance
```

Do not remove code, split modules, or restructure internals before the baseline, output contract, and safety checks exist.

## User Interface

In default Goal Mode, the user gives a broad goal, not an atomic task package.

Router, AI OS, LLM, or Codex may turn that goal into a route, scope, execution plan, checks, rollback path, and acceptance criteria. Codex keeps that execution package internal unless strict mode is requested, the task spans independent releases, or risk requires explicit review.

Do not produce a roadmap, epic, child-issue tree, or approval package for a clear implementation goal unless Sergey explicitly asks for planning or a hard blocker prevents bounded execution.

If the work is complex or high-risk enough to require sequenced child issues and PR gates, reference `Parent / Child Issue Gate Standard` from `PARENT_CHILD_ISSUE_GATE_STANDARD.md` instead of duplicating the standard. This is an advanced gate pattern, not a requirement for simple Goal Mode tasks.

## Autonomy

Codex may proceed with safe assumptions when the change is:

- docs or configuration only;
- local and reversible;
- inside allowed files;
- free of secrets, production/deploy/runtime changes, business logic, formulas, schemas, APIs, output contracts, metrics, or governed KB content changes;
- verifiable with a meaningful check.

Codex should ask a clarifying question or stop only for hard blockers, such as unsafe scope, missing secrets required for real execution, conflicting acceptance criteria, destructive actions, production/runtime mutation without approval, schema/metric/formula/provider-routing/output-contract changes without approval, or no possible validation.

## Advanced Mode

Atomic task packages remain available for strict, high-risk, or already-scoped work. They are an internal safety mechanism by default, not a required form Sergey must write for normal goals.

## Final Output

Keep the final user-facing report short:

- what changed;
- checks run;
- residual risks;
- next step.
