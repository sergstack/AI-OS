# AI-OS

[![Docs Safety](https://github.com/sergstack/AI-OS/actions/workflows/docs-safety.yml/badge.svg)](https://github.com/sergstack/AI-OS/actions/workflows/docs-safety.yml)

AI-OS is a governed workspace for designing and operating ChatGPT Projects,
repository work, validation, and a versioned Stream Deck interface. It makes
the path from a broad goal to a reviewable change explicit: route the work,
bound the scope, preserve evidence, validate the result, and leave acceptance
with a human owner.

> **Status:** candidate / ready for human review. Production promotion is
> disabled until the documented sync, smoke-QA, and pilot gates are complete.
> This public repository is **not open source**; see the
> [rights posture](docs/rights_posture.md).

## What this repository provides

| Capability | Outcome |
|---|---|
| Seven ChatGPT Project packages | Clear ownership for routing, strategy, analytics, LLM quality, implementation, and corpus work. |
| Goal Mode and execution contracts | Broad goals become bounded, reversible work with checks, risks, rollback, and acceptance. |
| Deterministic validation | Scripts and regression tests keep manifests, instructions, bundles, indexes, and public-repo safety consistent. |
| Delivery surfaces | Compact Knowledge Bundles for ChatGPT upload and versioned Stream Deck artifacts with QA and rollback history. |

## How work moves

```text
goal or raw input
  -> route to one accountable project
  -> establish scope and evidence
  -> implement in Codex on a non-main branch
  -> run checks and review the diff
  -> human owner accepts, merges, or rolls back
```

Generated output is a candidate, not an accepted result. GitHub is the live
source of truth; ChatGPT Project Knowledge is a versioned baseline for
bootstrapping and formal sync.

## Explore the system

| Start here | Use it for |
|---|---|
| [Repository map](docs/REPOSITORY_MAP.md) | A guided map of canonical documents, projects, and lifecycle rules. |
| [Current status](CURRENT_STATUS.md) | Current maturity, observed evidence, open gates, and next actions. |
| [Project registry](PROJECT_REGISTRY.md) | The seven governed ChatGPT Projects and their canonical paths. |
| [Goal Mode](GOAL_MODE.md) | Normal workflow and merge policy for changes. |
| [Contributing guide](CONTRIBUTING.md) | Issue, branch, validation, and pull-request expectations. |
| [Security policy](.github/SECURITY.md) | Private vulnerability reporting route. |

### Repository areas

| Area | Purpose |
|---|---|
| [`ChatGPT/`](ChatGPT) | Project instructions, granular Knowledge sources, and compact upload bundles. |
| [`Codex APP/`](Codex%20APP) | Local execution contracts, setup, runbooks, and review guidance. |
| [`StreamDeck/`](StreamDeck) | Versioned configuration, exports, generators, QA, and rollback history. |
| [`scripts/`](scripts) and [`tests/`](tests) | Deterministic repository validation and regression tests. |
| [`.github/`](.github) | Issue intake, PR policy, ownership, and CI workflows. |
| [`docs/`](docs) | Architecture, routing, merge-gate, and operating documentation. |

## Get started

1. Read the [repository map](docs/REPOSITORY_MAP.md) and
   [`AGENTS.md`](AGENTS.md) before changing repository content.
2. Start broad work from the [Goal issue template](.github/ISSUE_TEMPLATE/goal.md),
   or use the strict [Codex task template](.github/ISSUE_TEMPLATE/codex-task.md)
   when scope is already fixed.
3. Create a non-`main` branch, keep the change reversible, and run the local
   readiness suite before opening a pull request:

   ```bash
   python3 scripts/sync_aios.py
   python3 -m pytest tests/ -rA
   ```

`sync_aios.py` validates repository consistency and prints sync guidance. It
does not upload to the ChatGPT UI, push to GitHub, merge a pull request, or
grant production approval.

## Working principles

- **One accountable destination.** Use the routing rules and project boundaries
  rather than duplicating methodology across packages.
- **Canonical sources first.** Granular `Knowledge/` files own content;
  `Knowledge_Bundles/` are derived upload artifacts. Upload bundles or
  granular files, not both, unless debugging a sync issue.
- **Evidence before claims.** Checks, smoke QA, pilots, owner acceptance, and
  production authorization are distinct gates.
- **Human authority remains explicit.** Automation does not merge, deploy,
  approve production, or enlarge the change scope.

## Validation and operating references

The readiness suite checks Project Instructions length, public-repo safety,
Goal Mode defaults, manifest paths, Knowledge Bundles, and index coverage.
For the exact gate definitions, read [`MASTER_STATUS.md`](MASTER_STATUS.md).

Useful operating references:

- [`docs/guides/CHATGPT_CODEX_OPERATING_GUIDE.md`](docs/guides/CHATGPT_CODEX_OPERATING_GUIDE.md)
- [`SYNC_CONTRACT.md`](SYNC_CONTRACT.md)
- [`HANDOFF_STYLE_STANDARD.md`](HANDOFF_STYLE_STANDARD.md)
- [`docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`](docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md)

## Boundaries

AI-OS does not add a production agent platform. Embeddings, semantic search,
vector databases, web UI, autonomous retrieval, agentic workflows, and
production deployments remain blocked promotion items. Public visibility does
not grant reuse rights; the repository has no open-source license.

## Local path placeholders

Public documentation uses placeholders rather than machine-specific paths:

- `<LOCAL_AI_OS_ROOT>` — local AI-OS checkout
- `<LOCAL_REPO_ROOT>` — current repository root
- `<LOCAL_CODEX_APP_ROOT>` — local Codex APP folder
- `<LOCAL_ARTIFACTS_ROOT>` — local working artifacts outside the repository
