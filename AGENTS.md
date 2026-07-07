# AGENTS.md

This is Sergey's AI-OS repository.

## Default Mode

Use Goal Mode by default.

Sergey may give a broad goal instead of an atomic task package. Codex should inspect the repository, infer a bounded and reversible scope, create or use a non-main branch for repository changes, implement the smallest useful working version, run meaningful checks, fix in-scope failures once when safe, and report evidence, risks, rollback, and acceptance status.

Atomic task packages remain available for advanced, high-risk, strict, or ultra-long work, but they are not the default user burden. Do not turn a clear implementation goal into an epic, roadmap, child issue tree, or approval package unless Sergey asks for planning, the work cannot fit in one bounded PR, or a hard approval gate is reached.

## Source of Truth

- Use repository files as the source of truth.
- Read relevant files before editing.
- Obey this file and any more specific local instructions.
- Keep source files and Knowledge bundle files consistent when both represent the same content.

## Change Rules

- Make the smallest necessary change.
- Keep changes bounded and reversible.
- Do not refactor unrelated content.
- Do not add blocked promotion items: embeddings, semantic search, vector DB, web UI, autonomous retrieval, agentic workflows, autonomous agents, production deploys, secrets, credentials, or runtime artifacts.
- Do not claim production readiness or `production_promotion=yes`.
- Do not commit directly to `main`.
- Do not merge automatically.

## Validation

Run the smallest meaningful checks before reporting completion. For docs and project settings, prefer:

```bash
python3 scripts/check_project_instructions_length.py
python3 scripts/check_repo_public_safety.py
python3 scripts/check_manifest_paths.py
python3 scripts/check_knowledge_bundles.py
```

If checks cannot run, report the blocker instead of inventing results.
