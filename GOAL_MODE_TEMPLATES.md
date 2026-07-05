# Goal Mode Templates

## Docs/config PR

```text
# GOAL -> Codex APP

Improve repo docs/config for: [goal]

Rules:
- inspect repo first;
- infer safe scope;
- make minimal reversible changes;
- create scoped branch;
- run checks;
- open PR if requested;
- do not merge automatically.

Forbidden:
- secrets;
- .env;
- production deploy;
- business logic;
- formulas;
- schemas;
- output contracts;
- vector DB / embeddings / semantic search;
- autonomous agents.

Final report:
Summary:
Files changed:
Branch:
Commit:
PR URL:
Checks run:
Risks:
Rollback:
Acceptance status:
Next step:
```

## PR Judge

```text
# PR Judge

Review PR: [link]

Check:
- goal match;
- changed files;
- scope creep;
- forbidden changes;
- checks;
- risks;
- rollback;
- acceptance status.

Verdict:
pass / revise / blocked

Required fixes:
...
```

## ChatGPT Project Update

```text
# ChatGPT Project Update

Goal:
Update project settings / knowledge bundle / command surface for: [project]

Rules:
- keep PROJECT_INSTRUCTIONS.md compact;
- move detailed workflow into Knowledge;
- update bundle if source Knowledge changes;
- do not claim ChatGPT UI sync unless manually confirmed;
- run repo checks.

Expected:
small PR / update report.
```
