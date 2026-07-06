# AI-OS

Repository for ChatGPT project settings, routing docs, Codex execution contracts, and governance checks.

## Default Workflow

```text
GOAL -> route -> infer scope -> Codex execution package -> checks -> PR -> ChatGPT reads GitHub for fresh state
```

Goal Mode is the default user-facing workflow. Sergey can provide a broad goal; Router, AI OS, LLM, or Codex should infer the route, scope, checks, rollback, and acceptance criteria before implementation.

Atomic task packages remain available as advanced/strict mode, but they are not the default user burden. GitHub is the live source of truth; ChatGPT Project Knowledge is a cached baseline for Project bootstrapping and formal sync.

Run sync readiness checks before opening a PR:

```bash
python3 scripts/sync_aios.py
```

This helper validates repo settings and prints sync guidance. It does not perform external ChatGPT UI upload. GitHub remains the live source of truth.

See `GOAL_MODE.md` and `SYNC_CONTRACT.md`.

## Daily Use

- Use ChatGPT Projects for reasoning, routing, analytics framing, prompts, and evidence.
- Use Codex APP for repo/file execution, branches, checks, PRs, and local run reports.
- GitHub remains the live source of truth.
- ChatGPT Project Knowledge is a baseline/cache for upload and bootstrapping.
- Codex APP execution must report checks, risks, rollback, and acceptance status.
- Use `HANDOFF_STYLE_STANDARD.md` for cross-project handoff wording and required fields.

See `CHATGPT_CODEX_OPERATING_GUIDE.md`, `GOAL_MODE_TEMPLATES.md`, and `Codex APP/CODEX_APP_RUNBOOK.md`.

## Goal Packs

Use `GOAL_PACKS.md` for reusable broad-goal workflows, `COMMAND_SURFACE.md` for one-touch commands, and `CONTEXT_PACK_STANDARD.md` for compact reusable context.

## Governance Rule

Every `PROJECT_INSTRUCTIONS.md` file must be <= 8000 characters.

If a Project Instructions file grows beyond this limit, do not paste oversized instructions into ChatGPT Project Settings. Move supporting policies, examples, templates, checklists, and detailed workflows into `Knowledge/` files. Keep `PROJECT_INSTRUCTIONS.md` as the compact behavior kernel: routing, scope, evidence rules, output contract, and critical safety boundaries.

## Validation

Run before opening or merging documentation/configuration PRs:

```bash
python3 scripts/check_project_instructions_length.py
python3 scripts/check_repo_public_safety.py
python3 scripts/check_manifest_paths.py
python3 scripts/check_knowledge_bundles.py
```

The public safety scan also checks for blocked public-repo artifacts such as `.env`, logs, runtime files, vector/embedding folders, obvious secrets, unsafe local paths, and zip archives used as Knowledge sources.

The manifest/path consistency scan checks that `MANIFEST.json` paths exist, upload guide paths use canonical repo paths, project registry paths match actual folders, and legacy path variants stay blocked.

The Knowledge bundle scan checks compact `Knowledge_Bundles/` upload artifacts for source paths, upload counts, required sections, and unsafe content.

## Knowledge Bundles

Use `Knowledge_Bundles/` as the default ChatGPT Project Sources upload mode.

Granular `Knowledge/`, `Templates/`, and task files remain the source of truth. Granular Knowledge upload is advanced/debug mode only. Upload bundles OR granular files, not both, unless debugging a sync issue.

## Operational verification

Repository validation is not enough to claim ChatGPT Project readiness.

Before production promotion:

1. Sync Project Instructions manually into ChatGPT Projects.
2. Upload expected Knowledge files.
3. Run smoke QA.
4. Complete at least one pilot case.
5. Record results in `CHATGPT_PROJECT_SYNC_CHECKLIST.md` and `PILOT_CASES.md`.

## Analytical Memo Factory

For analytical memo production, use the `Analytical Memo Factory via Codex APP` workflow:

```text
Analyst -> [Analytics] -> [Codex] -> Codex APP -> Python -> LLM -> Judge/QA -> Human
```

Use `[Analytics]` for analytical task framing, `[Codex]` for the ultra-long Codex APP task package, and Codex APP for execution. Python calculates; LLM writes only from evidence.

## Local Path Placeholders

Public docs must not contain raw machine-specific absolute paths from local user profiles, home directories, or mounted volumes.

Use placeholders instead:

- `<LOCAL_AI_OS_ROOT>` for the local AI-OS repository root.
- `<LOCAL_REPO_ROOT>` for the current repository root in generic examples.
- `<LOCAL_CODEX_APP_ROOT>` for the local `Codex APP` folder.
- `<LOCAL_ARTIFACTS_ROOT>` for local working artifacts outside the public repository.
