# StreamDeck export rollback before v3.1.2

This directory preserves the 16 tracked `.streamDeckProfile` packages that existed before canonical registry v3.1.2 integration.

- Repository baseline: `29c7ff8802fea292d1c9a7a0daa45f65928f7395`
- Backup scope: `exports/*.streamDeckProfile`
- Restore: copy the required packages back to `StreamDeck/exports/`, then regenerate repository manifests and run `python3 StreamDeck/tools/validate_v3.py`.
- App backup, physical import, device binding, and physical QA were not performed.

`StreamDeck/archive/checksums.json` records the SHA-256 of every preserved package after canonical generation.
