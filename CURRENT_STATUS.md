# Current Status — AI OS

- repo_version: v05
- project: AI-OS repository
- last_checked: 2026-06-15
- production_promotion: no
- project_instructions_path: ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md
- knowledge_path: ChatGPT/[AI OS]/Knowledge/
- smoke_qa_status: pending
- validation_gates:
  - PROJECT_INSTRUCTIONS.md <= 8000 characters
  - public safety scan required
  - smoke QA required
  - pilot case required before production promotion
- blocked_items:
  - embeddings
  - semantic search
  - vector DB
  - web UI
  - agentic workflows
  - autonomous retrieval

## Current state

The repository contains ChatGPT project packages, Codex APP execution contracts, routing docs, and repository governance checks.

`PROJECT_INSTRUCTIONS.md` files must stay compact. Supporting policies, examples, templates, checklists, and detailed workflows belong in `Knowledge/`.

## Next action

Run repository validation before PR review:

```bash
python3 scripts/check_project_instructions_length.py
python3 scripts/check_repo_public_safety.py
```
