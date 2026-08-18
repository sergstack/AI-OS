# SPEC

## Goal

Add the bounded ChatGPT Project package `[Thinkers OS]` to the existing AI-OS repository without changing the responsibilities of existing projects.

## Current state

- The repository has six registered ChatGPT Project packages and a separate Codex APP executor layer.
- Baseline repository validators and 38 tests pass before this change.
- `[Thinkers OS]` is not present in the project registry, routing tables, validator registries, or index coverage checks.
- The inspected Thinkers OS source repository has ten selected authors, Judge-pass author artifacts, five active provisional synthesis patterns, and three unresolved P1 source requests.

## Requirements

- Create the required `[Thinkers OS]` project root, Knowledge, and Knowledge_Bundles files.
- Use only the canonical name `[Thinkers OS]`.
- Keep Project Instructions within 8000 characters.
- Preserve repository granular files as source of truth and bundles as default upload artifacts.
- Represent portfolio, corpus, source intake, author artifacts, synthesis, routing, handoff, QA, rollback, and resumable status.
- Keep partial corpus coverage explicit and prevent false `package_complete` status.
- Add bounded routing distinctions to Inbox Router and AI OS routing without changing existing project ownership.
- Register the project in project/path registries and in validators that enumerate ChatGPT Projects.
- Add regression tests for routing, bundle safety, project recognition, and the twelve smoke cases.
- Keep external ChatGPT Project creation and Project Sources upload manual.
- After all checks pass, commit only the scoped files and push the non-main integration branch to `sergstack/AI-OS`.

## Constraints

- Do not include raw books, normalized full text, OCR dumps, source manifests, execution logs, secrets, local absolute paths, blocked artifacts, or rejected artifacts in bundles.
- Do not modify external ChatGPT Project state.
- Do not add embeddings, semantic search, vector databases, autonomous retrieval, autonomous agents, production deploys, or runtime infrastructure.
- Do not change the responsibilities of `[Thinking]`, `[LLM]`, `[Analytics]`, `[Codex]`, `[AI OS]`, or `[Inbox Router]`.
- Production status remains `NOT AUTHORIZED`; owner acceptance remains pending.
- Changes must remain bounded, reversible, and on the existing non-main branch.
- Do not merge or open/change external ChatGPT Projects.

## Acceptance criteria

1. `ChatGPT/[Thinkers OS]` exists.
2. `PROJECT_INSTRUCTIONS.md` passes the 8000-character validator.
3. All required Knowledge files exist and are indexed.
4. Both required bounded bundles exist and pass bundle validation.
5. `Knowledge_Bundles/UPLOAD_LIST.md` exists and is authoritative.
6. Inbox Router distinguishes Thinkers OS maintenance from real-decision application in `[Thinking]`.
7. AI OS routing recognizes `[Thinkers OS]` while preserving existing boundaries.
8. Existing project responsibilities remain unchanged.
9. Project and repository path registries include `[Thinkers OS]`; the AI OS package manifest remains scoped to `[AI OS]`.
10. Project-enumerating validators and regression tests recognize `[Thinkers OS]`.
11. All twelve specified smoke cases pass with observed evidence.
12. Rollback instructions are present.
13. External ChatGPT Project creation remains manual.
14. External Project Sources upload remains manual.
15. Observed execution evidence is separated from expected behavior.
16. Production status remains `NOT AUTHORIZED`.
17. Passing scoped changes are committed and pushed to the non-main GitHub branch without merge.

## Risks

- Bundles can drift from granular sources if fingerprints are not regenerated.
- Routing language can accidentally overlap with `[Thinking]`, `[LLM]`, `[Analytics]`, `[Codex]`, or `[AI OS]`.
- Static smoke checks prove repository contracts, not behavior of an external ChatGPT Project before manual sync.
- A partial author corpus can be misreported as complete if status rules are weakened.
