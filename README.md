# AI-OS

Repository for ChatGPT project settings, routing docs, Codex execution contracts, and governance checks.

## Governance Rule

Every `PROJECT_INSTRUCTIONS.md` file must be <= 8000 characters.

If a Project Instructions file grows beyond this limit, do not paste oversized instructions into ChatGPT Project Settings. Move supporting policies, examples, templates, checklists, and detailed workflows into `Knowledge/` files. Keep `PROJECT_INSTRUCTIONS.md` as the compact behavior kernel: routing, scope, evidence rules, output contract, and critical safety boundaries.

## Validation

Run before opening or merging documentation/configuration PRs:

```bash
python3 scripts/check_project_instructions_length.py
python3 scripts/check_repo_public_safety.py
```

The public safety scan also checks for blocked public-repo artifacts such as `.env`, logs, runtime files, vector/embedding folders, obvious secrets, unsafe local paths, and zip archives used as Knowledge sources.
