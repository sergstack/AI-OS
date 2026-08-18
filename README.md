# AI-OS

[![Docs Safety](https://github.com/sergstack/AI-OS/actions/workflows/docs-safety.yml/badge.svg)](https://github.com/sergstack/AI-OS/actions/workflows/docs-safety.yml)

AI-OS is a governed workspace for ChatGPT project settings, routing rules,
Codex execution contracts, validation checks, and Stream Deck automation.
It keeps reasoning, implementation, and human approval connected without
treating generated output as accepted by default.

> **Status:** candidate / ready for human review. Production promotion remains
> disabled until the documented sync, smoke-QA, and pilot gates are complete.
> This public repository is **not open source**; see the
> [rights posture](docs/rights_posture.md).

## Repository Map

| Area | Purpose |
|---|---|
| [`ChatGPT/`](ChatGPT) | Project instructions, granular Knowledge sources, and compact upload bundles. |
| [`Codex APP/`](Codex%20APP) | Local execution contracts, setup, runbooks, and review guidance. |
| [`StreamDeck/`](StreamDeck) | Versioned Stream Deck configuration, exports, generators, and QA evidence. |
| [`scripts/`](scripts) and [`tests/`](tests) | Deterministic repository validation and regression tests. |
| [`.github/`](.github) | Issue templates, PR policy, ownership, and CI workflows. |
| [`docs/`](docs) | Architecture, routing, merge-gate, and operating documentation. |

For detailed routing, see the [repository map](docs/REPOSITORY_MAP.md). For the
current maturity and open gates, see [`CURRENT_STATUS.md`](CURRENT_STATUS.md).

## Default Workflow

```text
GOAL -> route -> infer scope -> Codex execution package -> checks -> PR -> ChatGPT reads GitHub for fresh state
```

Goal Mode is the default user-facing workflow. Sergey can provide a broad goal; Router, AI OS, LLM, or Codex should infer the route, scope, checks, rollback, and acceptance criteria before implementation. Future issues may reference `Goal Mode Contract` from `GOAL_MODE.md` by name.

Atomic task packages remain available as advanced/strict mode, but they are not the default user burden. GitHub is the live source of truth; ChatGPT Project Knowledge is a cached baseline for Project bootstrapping and formal sync.

## Quick Start

Run the repository readiness checks before opening a PR:

```bash
python3 scripts/sync_aios.py
python3 -m pytest tests/ -q
```

This helper validates repo settings and prints sync guidance. It does not perform external ChatGPT UI upload. GitHub remains the live source of truth.

See `GOAL_MODE.md`, `PARENT_CHILD_ISSUE_GATE_STANDARD.md`, `EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md`, and `SYNC_CONTRACT.md`.

Changes should start from the [Goal issue template](.github/ISSUE_TEMPLATE/goal.md)
or the strict [Codex task template](.github/ISSUE_TEMPLATE/codex-task.md). Read
[`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting a pull request, and use
the private reporting path in [the security policy](.github/SECURITY.md) for
potential vulnerabilities.

## Autonomous Execution Standard

`AUTONOMOUS_EXECUTION_STANDARD.md` is the canonical cross-project execution
layer that connects requirements, validation, defect handling, corrective
iterations, and terminal reporting into one closed loop, without replacing
Goal Mode, routing, Codex autonomy, testing, reporting, Judge/Revisor,
handoffs, Analytics methodology, or the merge/production gates above. See
`AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` for the project-extension
interface and `docs/AUTONOMOUS_EXECUTION_ADOPTION_PLAN.md` for phased
adoption status.

## Daily Use

- Use ChatGPT Projects for reasoning, routing, analytics framing, prompts, and evidence.
- Use Codex APP for repo/file execution, branches, checks, PRs, and local run reports.
- GitHub remains the live source of truth.
- ChatGPT Project Knowledge is a baseline/cache for upload and bootstrapping.
- Codex APP execution must report checks, risks, rollback, and acceptance status.
- Use `HANDOFF_STYLE_STANDARD.md` for cross-project handoff wording and required fields.
- Use `Existing Script Controlled Refactor Standard` only when an existing working script or pipeline must be cleaned or refactored without behavior loss.

See `CHATGPT_CODEX_OPERATING_GUIDE.md`, `GOAL_MODE_TEMPLATES.md`, and `Codex APP/CODEX_APP_RUNBOOK.md`.

## Review Model

AI-OS uses solo-owner governance by default. The canonical active merge policy is
`Merge Policy` in `GOAL_MODE.md`. PRs should include the checks run, risks or
residual risks, rollback notes, and merge/gate status. Owner-side Merge Gate
settings are checked with `docs/MERGE_GATE_OWNER_CHECKLIST.md`.

Rights posture: this repository has no open-source license. See
`docs/rights_posture.md`.

## Goal Packs

Use `GOAL_PACKS.md` for reusable broad-goal workflows, `COMMAND_SURFACE.md` for one-touch commands, and `CONTEXT_PACK_STANDARD.md` for compact reusable context.

Use `PARENT_CHILD_ISSUE_GATE_STANDARD.md` only for complex or high-risk analytics / Codex work that needs sequenced child issues, dependency gates, PR gates, and final QA. Do not require parent/child issue decomposition for simple Goal Mode tasks.

Use `EXISTING_SCRIPT_CONTROLLED_REFACTOR_STANDARD.md` only when an existing working script or pipeline needs cleanup/refactor while preserving behavior. The required order is baseline current behavior, define output contract, add safety tests, then clean/refactor and compare before/after output.

## Governance Rule

Every `PROJECT_INSTRUCTIONS.md` file must be <= 8000 characters.

If a Project Instructions file grows beyond this limit, do not paste oversized instructions into ChatGPT Project Settings. Move supporting policies, examples, templates, checklists, and detailed workflows into `Knowledge/` files. Keep `PROJECT_INSTRUCTIONS.md` as the compact behavior kernel: routing, scope, evidence rules, output contract, and critical safety boundaries.

## Validation

Run before opening or merging documentation/configuration PRs:

```bash
python3 scripts/check_project_instructions_length.py
python3 scripts/check_repo_public_safety.py
python3 scripts/check_codex_goal_mode_defaults.py
python3 scripts/check_manifest_paths.py
python3 scripts/check_knowledge_bundles.py
```

The public safety scan also checks tracked text files, including scripts, CSVs, workflow YAML, and docs, for blocked public-repo artifacts such as `.env`, logs, runtime files, vector/embedding folders, obvious secrets, unsafe local paths, and zip archives used as Knowledge sources.

The Codex Goal Mode scan reports every remaining atomic-task-package wording in Codex-facing files and fails if any wording implies atomic task packages are required by default.

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
