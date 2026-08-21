# [Thinkers OS] Project Setup

## Purpose

`[Thinkers OS]` owns authors, required corpus, source intake, evidence-backed author artifacts, bounded cross-author synthesis maintenance, portfolio state, and export package preparation.

## Canonical path

`ChatGPT/[Thinkers OS]`

## Repository sources

- `PROJECT_INSTRUCTIONS.md` — compact behavior kernel pasted manually into Project Instructions.
- `CURRENT_STATUS.md` — current repository-side portfolio and integration status.
- `SMOKE_QA_RESULTS.md` — observed repository smoke evidence and external-sync limitation.
- `Knowledge/INDEX.md` — granular source-of-truth index.

## Bundle-first upload

`Knowledge/` remains repository source of truth and is not part of standard manual upload.

Upload only files listed in `Knowledge_Bundles/UPLOAD_LIST.md`. The default required set is:

- `THINKERS_OS_01_PORTFOLIO_AND_CORPUS.md`
- `THINKERS_OS_02_ARTIFACTS_AND_SYNTHESIS.md`

Do not upload `README.md`, granular Knowledge, raw or normalized books, OCR dumps, manifests, logs, local paths, secrets, blocked artifacts, or rejected artifacts.

## Manual sync and maintenance

The external `[Thinkers OS]` Project was observed on 2026-08-21. Creation remains an owner action only if the Project is absent; repository work never creates or modifies it automatically.

1. Open the existing external ChatGPT Project `[Thinkers OS]`; create it manually only if absent.
2. Paste `PROJECT_INSTRUCTIONS.md` into Project Instructions.
3. Upload only the files listed in `Knowledge_Bundles/UPLOAD_LIST.md`.
4. Do not upload granular Knowledge simultaneously.
5. After an owner-authorized sync, run the focused source-gate case, then the twelve-case suite, and record actual external behavior separately.
6. Keep `owner_acceptance: pending` and production status `NOT AUTHORIZED` until explicit acceptance.

Repository implementation and validation do not perform these external steps.

## Rollback

Disable the two bundles in the external Project, remove the bounded routing entries, restore the previous registries/upload guidance, and rerun repository validation. Preserve the local Thinkers OS source repository, source artifacts, application history, and Judge results.
