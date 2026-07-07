# Current Status — AI OS

- repo_version: v05
- project: AI-OS repository
- last_checked: 2026-07-07
- production_promotion: no
- project_instructions_path: ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md
- knowledge_path: ChatGPT/[AI OS]/Knowledge/
- smoke_qa_status: candidate / ready for human review
- smoke_qa_evidence: SMOKE_QA_RESULTS.md; CROSS_PROJECT_SMOKE_QA_RESULTS.md
- validation_gates:
  - PROJECT_INSTRUCTIONS.md <= 8000 characters
  - public safety scan required
  - no raw absolute local paths required
  - manifest/path consistency required
  - Knowledge bundle consistency required
  - Codex Goal Mode default scan required
  - pytest validation script regression tests required
  - ChatGPT Project sync checklist required
  - smoke QA refresh after sync required
  - pilot result evidence required before production promotion
- blocked_items:
  - embeddings
  - semantic search
  - vector DB
  - web UI
  - agentic workflows
  - autonomous retrieval

## Current state

The repository contains ChatGPT project packages, compact Knowledge bundles,
Codex APP execution contracts, routing docs, StreamDeck candidate artifacts, and
repository governance checks.

`PROJECT_INSTRUCTIONS.md` files must stay compact. Supporting policies, examples, templates, checklists, and detailed workflows belong in `Knowledge/`.

Recent verified state:

- Goal Mode is the default; strict task packages are reserved for high-risk,
  already-scoped, ultra-long, or explicitly requested work.
- ChatGPT Project upload mode is compact `Knowledge_Bundles` by default.
- `SMOKE_QA_RESULTS.md` and `CROSS_PROJECT_SMOKE_QA_RESULTS.md` record
  2026-07-06 smoke QA evidence.
- `PILOT_CASES.md` remains backlog/unsupported until pilot result evidence is
  recorded.
- StreamDeck v2.7 remains active; v2.8 remains candidate/manual-only.

## Next action

Run repository validation before PR review:

```bash
python3 scripts/check_project_instructions_length.py
python3 scripts/check_repo_public_safety.py
python3 scripts/check_manifest_paths.py
python3 scripts/check_knowledge_bundles.py
python3 scripts/check_codex_goal_mode_defaults.py
python3 -m pytest tests/ -q
```

Then complete operational verification:

- `CHATGPT_PROJECT_SYNC_CHECKLIST.md`
- execute and record pilot results from `PILOT_CASES.md`
- keep production promotion blocked until accepted pilot evidence exists
