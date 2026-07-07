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
- Do not merge.

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

Provider/API work:
- local scaffold, dry-run, no-network paths, preflight checks, config variable name checks, and mock-value tests may proceed without extra approval;
- local configuration presence is not approval;
- real provider/API execution requires explicit bounded approval;
- never print or commit sensitive values, local config files, raw provider responses, runtime logs, or sensitive outputs;
- report only redacted evidence for approved real execution.

Checks:
- run all checks listed in the Issue;
- if a check cannot be run, explain why in the PR;
- do not claim checks passed unless they were actually run.

PR must include:
- linked Issue;
- summary;
- files changed;
- checks run;
- check results;
- risks / residual risks;
- human review note;
- explicit note: Do not merge automatically.

After finishing, report:
- branch name;
- PR number;
- commands run;
- final status;
- any unresolved risks.
```

## Output Contract

Codex should end every run with:

```text
Summary:
Issue:
Branch:
PR:
Files changed:
Checks run:
Result:
Risks:
Human review needed:
Do not merge automatically.
```
