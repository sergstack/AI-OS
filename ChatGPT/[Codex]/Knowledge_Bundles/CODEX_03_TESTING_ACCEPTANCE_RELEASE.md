# [Codex] — Testing Acceptance Release

## Purpose

Compact upload artifact for [Codex] covering testing acceptance release.

## Source files

- `ChatGPT/[Codex]/Knowledge/TESTING_WORKFLOW.md`
- `ChatGPT/[Codex]/Knowledge/ACCEPTANCE_CRITERIA.md`
- `ChatGPT/[Codex]/Knowledge/REVIEW_CHECKLIST.md`
- `ChatGPT/[Codex]/Knowledge/RELEASE_CHECKLIST.md`
- `ChatGPT/[Codex]/Knowledge/DONE_DEFINITION.md`
- `ChatGPT/[Codex]/Knowledge/SMOKE_QA_CHECKLIST.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Codex]/Knowledge/TESTING_WORKFLOW.md`

# Testing Workflow
## Test types
- unit tests;
- integration tests;
- contract tests;
- smoke tests;
- golden output regression;
- data quality checks;
- artifact validation.
## Steps
1. Identify risk.
2. Choose smallest useful test.
3. Run existing tests first if possible.
4. Add tests only where useful.
5. Report pass/fail/blocked.
## Docs-only fallback checks
```bash
git status --short
git diff --stat
git diff --check
find <affected_dir> -name "*.md" -type f | sort
```
For the AI-OS repository, use the standard validation scripts in `scripts/`.
If `markdownlint` is available, run it against the affected markdown files. Do not install it just for a docs-only task unless the task explicitly asks.
## Smoke test command format
```bash
# example
pytest tests/
python scripts/validate_artifact_outputs.py
```


## From: `ChatGPT/[Codex]/Knowledge/ACCEPTANCE_CRITERIA.md`

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


## From: `ChatGPT/[Codex]/Knowledge/REVIEW_CHECKLIST.md`

# Review Checklist
- [ ] Did I inspect the right files?
- [ ] Did I keep scope small?
- [ ] Did I avoid forbidden actions?
- [ ] Did I preserve business logic?
- [ ] Did I run or explain tests?
- [ ] Did I review diff?
- [ ] Did I document assumptions?
- [ ] Did I classify recoverable issues, needs_check items, and hard_blocker risks correctly?
- [ ] Did I provide acceptance status?


## From: `ChatGPT/[Codex]/Knowledge/RELEASE_CHECKLIST.md`

# Release Checklist
- [ ] Acceptance criteria passed.
- [ ] Tests passed or blockers recorded.
- [ ] Release notes written.
- [ ] Rollback plan exists.
- [ ] Long-run assumptions and hard blockers are documented when relevant.
- [ ] No secrets or local files included.
- [ ] Generated artifacts separated from source.
- [ ] Known risks listed.
- [ ] Next scope defined.


## From: `ChatGPT/[Codex]/Knowledge/DONE_DEFINITION.md`

# Definition of Done
- objective is complete;
- changes are scoped;
- files changed are listed;
- tests/checks are run or blocker explained;
- acceptance criteria are evaluated;
- risks are listed;
- assumptions and hard blockers are recorded when relevant;
- rollback or next step is clear;
- final report is concise and usable.


## From: `ChatGPT/[Codex]/Knowledge/SMOKE_QA_CHECKLIST.md`

# Smoke QA Checklist
- [ ] Project imports or starts.
- [ ] Main entrypoint runs or is dry-run checked.
- [ ] Required config exists.
- [ ] Required output files are generated.
- [ ] Existing tests pass.
- [ ] No secrets printed.
- [ ] No forbidden files modified.
- [ ] Output contract preserved.
- [ ] Acceptance criteria checked.
