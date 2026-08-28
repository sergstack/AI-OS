# AI-OS

[![Docs Safety](https://github.com/sergstack/AI-OS/actions/workflows/docs-safety.yml/badge.svg)](https://github.com/sergstack/AI-OS/actions/workflows/docs-safety.yml)

AI-OS is a governed operating system for work that spans ChatGPT Projects,
repository delivery, validation, and a versioned Stream Deck interface. It
turns a broad goal into a reviewable path: identify one accountable owner,
bound the change, preserve evidence, validate the result, and keep acceptance
and irreversible decisions with a human owner.

> **Current status:** candidate / ready for human review. Production promotion
> remains disabled until the documented sync, smoke-QA, and pilot gates are
> satisfied. This public repository is **not open source**; see the
> [rights posture](docs/rights_posture.md).

## Why AI-OS is different

Most AI workspaces stop at a prompt, a collection of documents, or an agent
loop. AI-OS makes the operational boundaries explicit and versioned.

| Design choice | What it provides | What it deliberately does not claim |
|---|---|---|
| **One accountable destination** | Seven named ChatGPT Project packages split routing, governance, decisions, analytics, LLM quality, implementation, and corpus work. | A single general-purpose agent that owns every decision. |
| **Two content surfaces** | Granular `Knowledge/` files are canonical; compact `Knowledge_Bundles/` are derived upload artifacts with source fingerprints. | That a ChatGPT Project UI is always current after a repository change. |
| **Goal Mode** | A broad goal can become a bounded, reversible branch change with checks, risks, rollback, and acceptance. | Permission to widen scope, merge, deploy, or change protected business rules. |
| **Evidence-bearing gates** | Manifests, paths, bundle provenance, instruction length, public-repo safety, smoke QA, and pilots are separate checks. | That a passing test or generated file is owner acceptance or production readiness. |
| **Human authority** | Review, merge, production promotion, and other consequential actions stay explicit. | Autonomous approval, deployment, or a persistent production agent platform. |
| **Versioned operating surfaces** | ChatGPT packages, Codex APP contracts, and Stream Deck artifacts can evolve through Git review and rollback. | A hidden runtime state outside the repository. |

The result is a repository that can be inspected at every boundary: where a
task should go, which source owns its content, which artifact is uploaded, what
was checked, and what still needs an owner decision.

## How the system works

```text
goal or raw input
  -> route to one accountable Project
  -> establish scope, evidence, and constraints
  -> work in the relevant domain or hand off to Codex
  -> validate sources, artifacts, and the changed behavior
  -> human owner reviews, accepts, merges, or rolls back
```

`[Inbox Router]` handles unclear intake. The routed project keeps domain
ownership; `[Codex]` prepares implementation work and Codex APP performs
repository changes on a non-`main` branch. The canonical map is
[`ROUTING_RULES.md`](ROUTING_RULES.md), not this overview.

### The seven ChatGPT Projects

| Project | Use it when you need | Typical output |
|---|---|---|
| `[Inbox Router]` | A raw request needs classification or a clear destination. | A bounded route or handoff. |
| `[AI OS]` | Governance, AI patterns, evidence, confidence, or supported use cases. | Evidence-aware guidance and a next owner. |
| `[Thinking]` | Options, trade-offs, decisions, risks, or a Judge/Revisor pass. | A decision memo with assumptions and revisit triggers. |
| `[Analytics]` | Deterministic calculations, data QA, reconciliations, metrics, or charts. | A method, calculations, checks, and limitations. |
| `[LLM]` | Prompts, model routing, evaluation, quality gates, or workflow design. | A governed prompt/workflow proposal and evaluation boundary. |
| `[Codex]` | Implementation framing, code review, tests, and release handoff. | A scoped execution package for repository work. |
| `[Thinkers OS]` | Thinker corpus, provenance, synthesis, and pattern status. | Source-aware synthesis without invented attribution. |

The authoritative paths, instruction limits, and AES applicability are in the
[project registry](PROJECT_REGISTRY.md). Project packages are deliberately
separate so that a strategy discussion does not silently become an analytics
calculation or a repository mutation.

### Canonical sources and upload artifacts

```text
canonical granular Knowledge/ source
  -> declared source fingerprint
  -> generated Knowledge_Bundle
  -> manual ChatGPT Project Knowledge upload
```

The repository is the live source of truth. ChatGPT Project Knowledge is a
versioned baseline for bootstrapping and periodic formal sync, not a live
replica of every commit. Upload only the bundle files named by a project's
`Knowledge_Bundles/UPLOAD_LIST.md`; do not upload both bundles and their
granular sources unless debugging a sync issue.

Read the [Sync Contract](SYNC_CONTRACT.md) for the exact freshness rules and
[Upload Guide](UPLOAD_GUIDE.md) before a manual ChatGPT update.

### Goal Mode and AES

[Goal Mode](GOAL_MODE.md) is the default execution model for broad repository
work: inspect first, infer the smallest safe scope, implement on a branch, run
relevant checks, and report evidence, risks, rollback, and acceptance status.

The [Autonomous Execution Standard (AES)](docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md)
defines the shared execution vocabulary for requirements, validation, defects,
corrective action, traceability, and closure review. It does not override
project ownership or authorize an agent to approve its own work. Current AES
applicability and the limited evidence for each Project are recorded in the
[registry](PROJECT_REGISTRY.md).

## Start using AI-OS

### 1. Find the right entry point

| Your need | Start here |
|---|---|
| Understand the repository | [Repository map](docs/REPOSITORY_MAP.md) |
| Choose ChatGPT Projects or Codex APP for daily work | [Operating guide](docs/guides/CHATGPT_CODEX_OPERATING_GUIDE.md) |
| Change repository content | [`AGENTS.md`](AGENTS.md), then [Goal Mode](GOAL_MODE.md) |
| Prepare a goal or fixed task | [Goal issue template](.github/ISSUE_TEMPLATE/goal.md) or [Codex task template](.github/ISSUE_TEMPLATE/codex-task.md) |
| Upload a ChatGPT Project baseline | [Upload Guide](UPLOAD_GUIDE.md) and the project's `UPLOAD_LIST.md` |
| Check evidence, maturity, and open gates | [Current status](CURRENT_STATUS.md) and [Master status](MASTER_STATUS.md) |

### 2. Work from a goal, not from a guessed implementation

For a repository change, state the desired outcome. Goal Mode then constrains
the work to a branch, a minimal reversible scope, relevant checks, a rollback
path, and explicit acceptance. Do not treat a passing test, a ready PR, or a
generated artifact as proof that the user's outcome has been accepted.

For a simple local and reversible change with sufficient repository context,
follow the applicable local instructions directly. For AI-OS methodology work,
use the canonical routing and bounded-context flow defined in `AGENTS.md`.

### 3. Validate before opening a pull request

From a local checkout, run the repository readiness helper and the relevant
tests:

```bash
python3 scripts/sync_aios.py
python3 -m pytest tests/ -rA
```

`sync_aios.py` checks project-instruction length, public-repository safety,
Goal Mode defaults, manifest paths, Knowledge Bundles, and index coverage. It
does **not** upload to ChatGPT, push to GitHub, merge a pull request, or grant
production approval.

For contribution and branch requirements, follow the
[contributing guide](CONTRIBUTING.md). For the exact merge policy, follow
[Goal Mode](GOAL_MODE.md).

## Repository layout

| Area | Purpose |
|---|---|
| [`ChatGPT/`](ChatGPT) | Project instructions, canonical granular Knowledge, and compact upload bundles. |
| [`Codex APP/`](Codex%20APP) | Local execution contracts, setup, runbooks, and review guidance. |
| [`StreamDeck/`](StreamDeck) | Versioned configuration, exports, generators, QA, and rollback history. |
| [`docs/`](docs) | Maps, guides, shared standards, operations, evidence, and reference material. |
| [`scripts/`](scripts) and [`tests/`](tests) | Deterministic validation and regression coverage. |
| [`.github/`](.github) | Issue intake, PR policy, ownership, security reporting, and CI workflows. |

## Evidence and limits

AI-OS distinguishes repository consistency from external or operational proof.
The repository records passing checks and bounded candidate evidence, but these
do not by themselves prove that every ChatGPT Project is synced, that every
workflow is generally reliable, or that production promotion is allowed.

Current candidate status, smoke-QA evidence, pilot boundaries, and blocked
promotion items are maintained in [Current status](CURRENT_STATUS.md). Exact
validation and operational gates live in [Master status](MASTER_STATUS.md).

AI-OS does **not** add embeddings, semantic search, vector databases, web UI,
autonomous retrieval, agentic workflows, persistent runtime memory, or
production deployments. Public visibility does not grant reuse rights; the
repository has no open-source license.

## Useful references

- [Repository map](docs/REPOSITORY_MAP.md)
- [Project registry](PROJECT_REGISTRY.md)
- [Goal Mode](GOAL_MODE.md)
- [Sync Contract](SYNC_CONTRACT.md)
- [Autonomous Execution Standard](docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md)
- [Current status](CURRENT_STATUS.md)
- [Security policy](.github/SECURITY.md)

## Local path placeholders

Public documentation uses placeholders rather than machine-specific paths:

- `<LOCAL_AI_OS_ROOT>` — local AI-OS checkout
- `<LOCAL_REPO_ROOT>` — current repository root
- `<LOCAL_CODEX_APP_ROOT>` — local Codex APP folder
- `<LOCAL_ARTIFACTS_ROOT>` — local working artifacts outside the repository
