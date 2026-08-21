# Upload List — [Thinkers OS]

This is the single authoritative manual upload list for ChatGPT Project `[Thinkers OS]`.

generated_date: 2026-08-21
target_project: `[Thinkers OS]`
default_upload_mode: `Knowledge_Bundles`
source_fingerprint_01: sha256:14a082ab7d06822bff1b54d0bfef03972ed4a9c97973f17329c47d9a70864b3e
source_fingerprint_02: sha256:a69b7ae66abd7019cd80b32188d23b2a365d5a7b92ada3ae0cd2ec0dd885688d
smoke_qa_reference: `../SMOKE_QA_RESULTS.md`

## Required upload files

- `THINKERS_OS_01_PORTFOLIO_AND_CORPUS.md`
- `THINKERS_OS_02_ARTIFACTS_AND_SYNTHESIS.md`

## Optional upload files

- none

## Do not upload

- `PROJECT_INSTRUCTIONS.md` — paste into Project Instructions instead.
- `README.md` — repository/local guidance.
- granular `Knowledge/` files when bundle files are used, unless controlled debugging.
- raw PDF or other source books.
- normalized books or full text.
- OCR dumps, excerpt dumps, source cards, or chunks.
- source manifests, acquisition manifests, or license manifests.
- execution logs, runtime artifacts, or temporary files.
- local absolute paths.
- blocked, revise, restricted, deprecated, rejected, or archival artifacts.
- secrets, credentials, tokens, or `.env` files.
- embeddings, semantic indexes, vector databases, or archives.

## File count

Required: 2
Optional: 0
Total if all uploaded: 2
Limit: 40
Status: pass

## Manual sync steps

1. Open the existing external ChatGPT Project `[Thinkers OS]`; create it manually only if absent.
2. Paste `../PROJECT_INSTRUCTIONS.md` into Project Instructions; do not upload it as Knowledge.
3. Upload exactly the two required bundle files above.
4. Do not upload granular Knowledge simultaneously.
5. After owner-authorized sync, run the focused source-gate case and then the twelve smoke questions referenced by `../SMOKE_QA_RESULTS.md`; record external results separately.
6. Keep owner acceptance pending and production status `NOT AUTHORIZED`.

Repository implementation does not perform external creation or upload.
