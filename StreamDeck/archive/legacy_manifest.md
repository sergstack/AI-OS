# StreamDeck legacy archive

The archive preserves the explicit rollback and evidence baseline. File integrity is recorded in `checksums.json`, generated with SHA-256 by `../tools/generate_v3.py`.

- `v2.7/`: last documented active physical baseline. Do not delete before v3 export/import, dual-deck smoke and owner acceptance.
- `v2.8/`: candidate maps, icons, Prompt QA notes and MCP pilot evidence.
- `v2.9/`: review-confirmed candidate JSON, setup guide and derived workbook used for the v3 baseline audit.

These files are superseded in the repository active layer, not claimed to be removed from physical devices. Restore them by reverting the v3 change or using the owner-side Stream Deck backup.
