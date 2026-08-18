# Repository Map

## Purpose

This is the canonical human-readable navigation map for AI-OS. It explains
where to start, where work belongs, and which document answers each status or
governance question. It does not replace `AGENTS.md`, project instructions, or
the machine-readable capability registry.

## Start Here

| Need | Start with | Authority |
|---|---|---|
| Understand the repository | [`README.md`](../README.md) | Human-facing entry point |
| Execute repository work | [`AGENTS.md`](../AGENTS.md) | Local agent instructions |
| Route work to one capability | [`PROJECT_CAPABILITIES.yaml`](../PROJECT_CAPABILITIES.yaml) | Machine-readable capability registry |
| Find a ChatGPT Project package | [`PROJECT_REGISTRY.md`](../PROJECT_REGISTRY.md) | Canonical project paths and roles |
| Check the current state | [`CURRENT_STATUS.md`](../CURRENT_STATUS.md) | Concise repository status and next action |
| Check required gates | [`MASTER_STATUS.md`](../MASTER_STATUS.md) | Canonical validation and operational gates |
| Prepare or review a change | [`GOAL_MODE.md`](../GOAL_MODE.md) | Execution and merge policy |
| Sync ChatGPT Project settings | [`UPLOAD_GUIDE.md`](../UPLOAD_GUIDE.md) | Upload and sync guidance |

## Working Architecture

```text
raw input
  -> ChatGPT/[Inbox Router]
  -> one domain project
  -> Codex APP when repository execution is required
  -> scripts/tests and GitHub checks
  -> pull request and human review
```

| Canonical path | Primary responsibility |
|---|---|
| `ChatGPT/[Inbox Router]` | Turn raw or mixed input into a destination or bounded handoff |
| `ChatGPT/[AI OS]` | AI patterns, evidence, confidence, governance, and supported use cases |
| `ChatGPT/[Thinking]` | Strategy, options, risks, decisions, and Judge/Revisor work |
| `ChatGPT/[Analytics]` | Calculations, metrics, reconciliation, and deterministic data QA |
| `ChatGPT/[LLM]` | Prompts, model routing, LLM workflows, evaluation, and quality gates |
| `ChatGPT/[Codex]` | Implementation framing, code review, tests, and release handoff |
| `ChatGPT/[Thinkers OS]` | Thinker corpus, provenance, synthesis, and pattern status |
| `Codex APP/` | Repository execution contracts and runbooks; not a ChatGPT Project |
| `StreamDeck/` | Versioned physical interface, exports, tools, QA, and rollback history |
| `scripts/` and `tests/` | Deterministic validation and regression coverage |
| `benchmarks/` | Behavioral evaluation cases and evaluators |
| `.github/` | Issue intake, pull request policy, ownership, and CI |

Detailed project boundaries belong in each project's
`PROJECT_INSTRUCTIONS.md`; do not duplicate them in this map.

## ChatGPT Project Package Pattern

```text
PROJECT_INSTRUCTIONS.md   compact behavior kernel, <= 8000 characters
Knowledge/                granular source material
Knowledge_Bundles/        compact delivery layer for ChatGPT upload
README.md                 local package guidance
CURRENT_STATUS.md         project-local state when present
```

Granular `Knowledge/` files are the content source of truth.
`Knowledge_Bundles/` are a derived delivery surface and must stay consistent
with their declared sources. Upload bundles or granular files, not both, unless
debugging a sync problem.

## Document Classes

| Class | Examples | Rule |
|---|---|---|
| Entry and routing | `README.md`, this map, registries | Explain where to start; do not copy domain methodology |
| Governance and contracts | `AGENTS.md`, `GOAL_MODE.md`, active standards | Normative rules; protected-path review applies |
| Current status | root and project-local `CURRENT_STATUS.md` | State maturity and next action; do not redefine gates |
| Gate definitions | `MASTER_STATUS.md` | Define validation and operational gates and point to evidence |
| Operational records | checklists, pilot plans, manifests | Track one operation or package; not general policy |
| Evidence | smoke-QA, pilot, and acceptance results | Record what was checked; passing evidence is not production approval |
| Delivery artifacts | `Knowledge_Bundles/`, Stream Deck exports | Distributable surfaces derived from canonical sources |
| History | archives and completed task packages | Preserve audit history; not current guidance unless actively referenced |

When files disagree, follow system and user instructions first, then the
applicable `AGENTS.md`, canonical contracts, registries and manifests, current
status, evidence, and finally historical material.

## Status Contract

| Question | Canonical answer |
|---|---|
| What is the repository's current state and next action? | `CURRENT_STATUS.md` |
| What validation and operational gates exist? | `MASTER_STATUS.md` |
| What is the state of one ChatGPT Project? | That project's `CURRENT_STATUS.md`, when present |
| Did a specific check or pilot pass? | The named smoke-QA, pilot, or acceptance evidence file |
| Is production promotion allowed? | Explicit `production_promotion` state plus all required operational evidence |

Status files should link to evidence instead of copying full results. Evidence
files should record observations instead of creating new governance rules.

## Placement and Lifecycle Rules

- Keep a file in the root only when it is a cross-repository entry point,
  active contract, canonical registry, current status, or checked package
  manifest.
- Put explanatory architecture and workflow documentation in `docs/`.
- Put project-specific methodology inside its canonical
  `ChatGPT/[Project]/` package.
- Put deterministic validation in `scripts/` and regression coverage in
  `tests/`.
- Treat `StreamDeck/archive/`, root `archive/`, and completed task packages as
  audit history, not current policy.
- Move historical material only in a dedicated migration that updates every
  affected manifest, link, test, and upload contract.
- Keep secrets, local settings, caches, worktrees, runtime output, and search
  indexes out of Git.
- Prefer updating an existing canonical document over creating another status
  or policy surface.

Bracketed project names and paths containing spaces are canonical because they
match ChatGPT Project names. Quote them in shell commands. Renaming them is a
contract migration, not cosmetic cleanup.

## Structural Change Checklist

Before adding or moving a structural file:

1. Identify its document class and canonical owner.
2. Check registries, manifests, upload lists, tests, and cross-references.
3. Preserve the distinction between source, delivery artifact, status, and
   evidence.
4. Run `python3 scripts/sync_aios.py` and the relevant tests.
5. Use a pull request and follow `GOAL_MODE.md`.

## External Destinations

| Destination | Role |
|---|---|
| Things | Next actions; not a knowledge base |
| Calendar | Time-bound commitments |
| Notes / Obsidian | Personal context and reference material outside this repository |

The canonical Inbox Router repository path is `ChatGPT/[Inbox Router]`. Its
ChatGPT display name may remain `[Inbox / Router]`; the display name does not
change the repository path.
