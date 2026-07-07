# Knowledge Bundles — [AI OS]

## Purpose

This folder contains compact upload artifacts for ChatGPT Project Sources / Knowledge.

Granular files in `ChatGPT/[AI OS]/Knowledge/` and other listed source paths remain the source of truth. Do not delete or replace granular files with these bundles.

## Upload policy

- Paste `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md` into the ChatGPT Project Instructions field.
- Upload bundle files from `UPLOAD_LIST.md` into ChatGPT Project Sources / Knowledge.
- Upload bundles OR granular files, not both, unless debugging a sync issue.
- Do not upload raw transcripts, source-card dumps, logs, runtime artifacts, embeddings, vector DB files, zip archives, secrets, or `.env` files.

## Content rule

- Each bundle `## From:` section must carry the complete normative content of its source file: rules, required fields, checklists, and status values.
- Condensing formatting is allowed; dropping normative lines is not.
- When a source file changes, update every bundle section that embeds it in the same PR.

## Status

- bundle_type: compact upload artifact set
- source_of_truth: granular repository files
- production_promotion: no
