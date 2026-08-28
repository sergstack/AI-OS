# Knowledge Bundles — [AI OS]

## Purpose

This folder contains compact upload artifacts for ChatGPT Project Sources / Knowledge.

Granular files in `ChatGPT/[AI OS]/Knowledge/` and other listed source paths remain the source of truth. Do not delete or replace granular files with these bundles.

## Upload policy

- Paste `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md` into the ChatGPT Project Instructions field.
- Upload bundle files from `UPLOAD_LIST.md` into ChatGPT Project Sources / Knowledge.
- Upload bundles OR granular files, not both, unless debugging a sync issue.
- Do not upload raw transcripts, source-card dumps, logs, runtime artifacts, embeddings, vector DB files, zip archives, secrets, or `.env` files.

## Bundle scopes

Use this table to decide which bundle to re-upload after a source file changes.

| Bundle | Embedded sources |
|---|---|
| `AIOS_01_ROUTING_AND_WORKFLOW.md` | `AI_OS_PROJECT_FILES_INDEX.md`, `PROJECT_ROUTING.md`, `AI_OS_WORKFLOW.md`, `KB_USAGE_RULES.md`, `ANALYTICAL_MEMO_FACTORY_CODEX_APP_WORKFLOW.md` |
| `AIOS_02_GOVERNANCE_AND_EVIDENCE.md` | `GOVERNANCE_RULES.md`, `ANTI_PATTERNS.md` |
| `AIOS_03_HANDOFF_AND_SMOKE_QA.md` | `HANDOFF_PROTOCOL.md`, `GITHUB_ISSUE_DRIVEN_HANDOFF.md`, `SMOKE_QA_FOR_AI_OS.md`, repo-root `HANDOFF_STYLE_STANDARD.md` |
| `AIOS_04_GOAL_PACKS_AND_COMMAND_SURFACE.md` | repo-root `docs/standards/GOAL_PACKS.md`, `docs/standards/COMMAND_SURFACE.md`, `docs/standards/CONTEXT_PACK_STANDARD.md`, `docs/standards/PROMPT_QA_FACTORY.md`; Knowledge `WEEKLY_AI_OS_REVIEW_TEMPLATE.md`, `ARCHIVE_SUPERSEDED_RULE.md` |
| `AIOS_05_SUPERVISED_AGENT_LOOPS.md` | `AGENT_LOOP_PLAYBOOK.md`, `LOOP_ACCEPTANCE_CHECKLIST.md`, `AUTO_RESEARCH_BACKLOG.md`, `SKILLS_HOOKS_MCP_DECISION_MATRIX.md` |
| `AIOS_06_CROSS_PROJECT_AI_EVALS.md` | `AI_EVAL_REGISTRY.md`, `JUDGE_CALIBRATION.md`, `GOLDEN_EVAL_CASES.md`, `CROSS_PROJECT_EVAL_PLAYBOOK.md` |

Unqualified names live in `ChatGPT/[AI OS]/Knowledge/`. Keep this table in sync with each bundle's own source list; the bundle file remains authoritative.

## Content rule

- Each bundle `## From:` section must carry the complete normative content of its source file: rules, required fields, checklists, and status values.
- Condensing formatting is allowed; dropping normative lines is not.
- When a source file changes, update every bundle section that embeds it in the same PR.

## Status

- bundle_type: compact upload artifact set
- source_of_truth: granular repository files
- production_promotion: no
