# Repository Archive

This directory is the repository's historical layer. It preserves audit
evidence and superseded reports; it is not a source of current policy or
active project behavior.

## Areas

| Path | Contents | Use |
|---|---|---|
| `implementation_evidence/` | Closed implementation packages, including scope, review and acceptance records | Audit an earlier repository change |
| `reports/` | Dated or superseded reports with recorded replacements and traceability | Inspect historical findings without treating them as current guidance |

## Rules

- Keep current instructions, registries, manifests and status files outside
  this directory.
- Preserve archived paths and Git history unless an approved migration updates
  every live reference and validation artifact.
- Do not delete an archive item as part of organization; use a separate,
  explicitly approved retention decision.
