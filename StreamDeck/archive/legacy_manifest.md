# StreamDeck legacy archive

The archive preserves the explicit rollback and evidence baseline. File integrity is recorded in `checksums.json`, generated with SHA-256 by `../tools/generate_v3.py`.

- `v2.7/`: last documented active physical baseline. Do not delete before v3 export/import, dual-deck smoke and owner acceptance.
- `v2.8/`: candidate maps, icons, Prompt QA notes and MCP pilot evidence.
- `v2.9/`: review-confirmed candidate JSON, setup guide and derived workbook used for the v3 baseline audit.
- `pre-releases/v3.0-pre-v3.1.2/`: superseded pre-release profile exports retained as historical comparison evidence; the active candidate surface is v3.1.2 outside this archive.

Archive taxonomy:

- Stable version directories are immutable historical evidence and rollback layers; pre-release snapshots live under `pre-releases/`.
- `legacy_manifest.md` declares their purpose and rollback boundary.
- `checksums.json` is the SHA-256 integrity manifest for every archived file except itself; regenerate it with `../tools/generate_v3.py` whenever archive content or this manifest changes.

These files are superseded in the repository active layer, not claimed to be removed from physical devices. Restore them by reverting the v3 change or using the owner-side Stream Deck backup.
