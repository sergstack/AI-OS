# Codex Issue Execution Prompt

Use this prompt when assigning a GitHub Issue to Codex for controlled implementation.

For raw or unclear inputs, use `[Inbox Router]` before creating a Codex task. Codex Issues should already be implementation-ready.

```text
Take GitHub Issue #<NUMBER> and execute it as a controlled batch.

Rules:
- Work from current main.
- Create a separate branch.
- Respect the Issue scope.
- Modify only allowed files.
- Do not modify forbidden files.
- Run required checks.
- Commit changes.
- Push branch.
- Open a Pull Request.
- Follow `Merge Policy` in `GOAL_MODE.md`.

Before starting:
- inspect the Issue;
- inspect current branch and status;
- confirm working tree is clean;
- list allowed files and forbidden changes.

Implementation:
- make the smallest safe change that satisfies the Issue;
- avoid unrelated refactoring;
- avoid changing production logic unless explicitly allowed;
- do not add secrets, logs, raw dumps, runtime artifacts, embeddings, or vector DB files.

Checks:
- run all checks listed in the Issue;
- if a check cannot be run, explain why in the PR;
- do not claim checks passed unless they were actually run.

Acceptance:
- distinguish business acceptance from technical checks;
- verify artifact/content output when the Issue produces a user-facing deliverable;
- do not report success if technical checks pass but the business artifact or user-facing deliverable is not verified;
- include acceptance status and merge/gate status in the final report and PR.

PR must include:
- linked Issue;
- summary;
- files changed;
- business acceptance;
- artifact/content verification, if applicable;
- checks run;
- check results;
- acceptance status;
- risks / residual risks;
- human review note;
- merge/gate status.

After finishing, report:
- branch name;
- PR number;
- commands run;
- final status;
- any unresolved risks.
```

## Output Contract

Codex should end every run with the canonical Codex final report schema:

```text
Summary:
Issue:
Branch:
Files inspected:
Files changed:
Commands run:
Test results:
Evidence / artifacts:
Business acceptance:
Artifact/content verification:
Technical checks:
Assumptions:
Blockers:
Risks:
Rollback:
PR:
Acceptance status:
Merge / gate status:
```
