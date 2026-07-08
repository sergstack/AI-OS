# Codex Task

Strict/advanced mode. For broad requests, use `goal.md`.

For raw or unclear inputs, use `[Inbox Router]` before creating a Codex task.
Codex issues should already be implementation-ready.

## Goal

What should be achieved?

## Scope

What is included?

## Allowed files

- 

## Forbidden changes

- Do not modify unrelated files.
- Do not change production logic unless explicitly allowed.
- Do not merge the PR.

## Business acceptance

- [ ] 

## Artifact/content acceptance

- [ ] 

## Technical checks

- [ ] 

## Non-acceptance examples

- [ ] 

## Checks to run

```bash
git status --short
python3 scripts/check_project_instructions_length.py
python3 scripts/check_repo_public_safety.py
python3 scripts/check_manifest_paths.py
python3 scripts/check_knowledge_bundles.py
python3 -m unittest  # optional, if tests exist
```

For project sync / pilot tasks, update:

- `CHATGPT_PROJECT_SYNC_CHECKLIST.md`
- `PILOT_CASES.md`
- `SMOKE_QA_REFRESH_PLAN.md`

## Expected PR summary

The PR must include:

- Issue reference;
- files changed;
- business acceptance status;
- artifact/content verification, if applicable;
- checks run;
- result;
- risks / residual risks;
- owner review needed;
- explicit note: Do not merge automatically.

## Notes for Codex

Create a separate branch, make only allowed changes, run checks, commit, push, and open a PR. Do not merge.
