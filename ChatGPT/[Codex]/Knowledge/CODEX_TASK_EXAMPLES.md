# Codex Task Examples

## Good Goal Mode Task

```text
GOAL -> Codex APP

Improve the README onboarding for ChatGPT Projects + Codex APP.

Constraints:
- docs-only;
- inspect repo first;
- infer safe scope;
- update bundles if source docs change;
- run repo checks;
- open PR;
- do not merge automatically.
```

Why it is good:

- goal is clear;
- safety constraints are explicit;
- Codex can infer files, checks, rollback, and acceptance;
- no atomic task burden on Sergey.

## Good Strict Codex Task

```text
# Codex Task

Objective:
Fix failing parser test for date normalization.

Allowed files:
- src/date_parser.py
- tests/test_date_parser.py

Forbidden:
- schema changes;
- output contract changes;
- dependency additions;
- broad refactor.

Checks:
- pytest tests/test_date_parser.py
- git diff --check

Acceptance:
- failing case is covered by a test;
- existing parser behavior is preserved;
- rollback is revert commit.
```

Why it is good:

- allowed files are bounded;
- tests are specific;
- forbidden changes are visible;
- acceptance is testable.

## Weak Task To Improve

```text
Make the pipeline better.
```

Improve it by adding:

- expected behavior;
- affected repo or file area;
- forbidden changes;
- checks;
- acceptance criteria.

## PR Judge Prompt

```text
PR Judge

Review PR: [link]

Check:
- goal match;
- scope creep;
- forbidden changes;
- tests/checks;
- risks;
- rollback;
- acceptance status.

Verdict:
pass / revise / blocked
```
