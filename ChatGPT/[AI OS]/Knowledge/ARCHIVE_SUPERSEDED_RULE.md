# Archive / Superseded Rule

Status: candidate / ready for human review.
Purpose: traceability rule for removing items from the active layer. This is not an auto-archive rule and not a deletion rule.

## Required record

Item:
Status:
Reason:
Replacement, if any:
Source / affected file:
Owner project:
Removal from active layer:
Traceability note:
Reviewer:
Date:

## Status values

- `active`
- `candidate`
- `superseded`
- `archived`
- `rejected`
- `blocked`

## Rules

- Do not delete without reason, replacement, and status.
- Do not auto-archive.
- Keep traceability from old item to replacement or decision record.
- Remove from active layer only after reviewer acceptance.
- Preserve enough context to understand why the item changed state.
- Do not archive private data, secrets, raw dumps, logs, runtime artifacts, embeddings, vector DB files, or zip archives into Project Knowledge.

## Superseded checklist

- [ ] Status is set.
- [ ] Reason is explicit.
- [ ] Replacement is listed or marked `none`.
- [ ] Source / affected file is listed.
- [ ] Owner project is listed.
- [ ] Active-layer removal is described.
- [ ] Traceability note links old item to replacement or decision.
- [ ] Reviewer accepted the change.

## Removal from active layer

Active layer:
Change needed:
Replacement pointer:
Rollback note:

## Human acceptance

- [ ] Reviewer accepted archive / superseded status.
- [ ] Reviewer accepted replacement or `none`.
- [ ] Reviewer accepted traceability note.
- [ ] No production promotion is implied.
