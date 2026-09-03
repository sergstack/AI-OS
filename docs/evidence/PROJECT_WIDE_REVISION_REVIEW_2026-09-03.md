# Project-Wide Revision Review — 2026-09-03

- Baseline: `origin/main` at `20dcf24` (merge of PR #364)
- Requested by: Sergey (owner), via the "Supervised AI-OS subagent dispatch"
  (`STANDARDIZED BOUNDED`) mechanism in `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md`
- Method: 7 parallel `Plan`-type dispatches, one per governed capability in
  `PROJECT_CAPABILITIES.yaml` (`ai_os`, `thinking`, `analytics`, `llm`, `codex`,
  `inbox_router`, `thinkers_os`). Each dispatch was read-only, bounded to its
  own `canonical_path`, instructed to fetch and read against `origin/main`
  (not the dispatching session's local branch, which was stale), and given a
  free-form objective ("find what needs revision in your domain, self-determined
  scope") per the owner's explicit instruction. No child dispatched a further
  child; root performed no domain work itself, only aggregation.
- Evidence status: repository evidence from this session's observed dispatch
  results. Not an owner acceptance, not a production-readiness signal.

## Verdict

```text
REVIEW COMPLETE — 34 findings across 7 projects (7 high / 13 medium / 14 low)
No blocking defect found. No schema/business-logic/output-contract issue found.
```

All findings are documentation/consistency/process gaps inside the ChatGPT
project packages (`Knowledge/`, `Knowledge_Bundles/`, status files,
`PROJECT_INSTRUCTIONS.md`). None require a schema, formula, metric, or
output-contract change; several require a small wording reconciliation, a
status-file refresh, or a bundle-content addition.

## Cross-cutting themes

### Theme 1 — status/evidence files understate actual current state (dominant pattern, 5/7 projects)

| Project | Gap | Staleness |
| --- | --- | --- |
| `[Thinking]` | `CURRENT_STATUS.md` omits `PILOT-THINKING-001` (ran 2026-08-27); three Thinkers-synthesis files still say `deployment_status: repository_candidate_not_uploaded` / "NOT RUN" despite `SMOKE_QA_RESULTS.md` recording a live run | ~5 weeks |
| `[AI OS]` | `docs/evidence/SMOKE_QA_RESULTS.md` dated 2026-07-06, predates ~15 Knowledge additions (2026-08-25–09-02), including the eval-gate family itself | ~2 months |
| `[Analytics]` | `SMOKE_QA_RESULT.md` does not cover the 2 newest `SMOKE_QA_FOR_ANALYTICS.md` sections (Quantitative Sanity Gate, Analytical Judge gate; added 2026-09-01/02) | days |
| `[Thinkers OS]` | `CURRENT_STATUS.md` portfolio snapshot says 12 authors / 2 partial packages; `Knowledge/SYNTHESIS_AND_EXPORT.md` (more current) shows 15 authors / 4 partial (Rumelt, Rogers added 2026-08-21, never reflected upstream) | ~2 weeks, direct numeric contradiction |
| `[Inbox Router]` | `CURRENT_STATUS.md` claims `v06`; `Knowledge/INDEX.md` and `Knowledge/INBOX_ROUTER_FILES_INDEX.md` still say `v05`; 5 of 6 `SMOKE_QA_RESULTS.md` rows are `not_run` since 2026-06-15 | ~2.5 months unexecuted |

### Theme 2 — new content added but not reaching the upload surface

- `[AI OS]` (high): `ACT_OR_ABSTAIN_EVAL_GATE.md`, `GOAL_CONSISTENCY_CLOSURE_CHECK.md`, `FAILURE_REGISTRY.md`, `REGRESSION_GATE.md`, `INTERMEDIATE_STATE_ASSERTIONS.md` are named/described in one bundle but never embedded as `## From:` content in any of the 6 bundles — a normal ChatGPT sync never uploads their normative text.
- `[Codex]` (high): `README.md`'s granular-file list omits 9 real `Knowledge/` files, 3 of which `PROJECT_INSTRUCTIONS.md` names as required reading.
- `[Inbox Router]` (medium): `README.md`'s folder diagram omits `Knowledge_Bundles/` entirely, despite instructing its upload two sections later.

### Theme 3 — parallel sources of truth that have already diverged

- `[Inbox Router]` (high): `PROJECT_INSTRUCTIONS.md` (the file actually pasted into the live system prompt) still carries its own destinations table, diverged from the canonical root `ROUTING_RULES.md` since the 2026-08-27 routing consolidation — an orphaned "Someday / Maybe" destination, a missing Codex-APP row.
- `[Analytics]` (high): two package manifests (`Knowledge/MANIFEST.md`, root `package_manifest.json`), both stale, neither enforced by any check script.
- `[Inbox Router]` (medium): `Knowledge/INDEX.md` vs `Knowledge/INBOX_ROUTER_FILES_INDEX.md` are ~80% duplicate and have diverged; the version `PROJECT_CAPABILITIES.yaml` actually loads (`INBOX_ROUTER_FILES_INDEX.md`) is missing the conflict-resolution rule only `INDEX.md` carries.
- `[Codex]` (low): `EXECUTION_REPORTING_RULES.md` (declared canonical report format) vs. an independently-defined shorter format in `PROJECT_CONTEXT.md`.

### Theme 4 — a genuinely live rule contradiction, introduced this session

- `[LLM]` (high): `LLM_EVAL_STANDARD.md` (merged via PR #364, this session) explicitly bans self-reported confidence scoring as a governance metric. `PROJECT_INSTRUCTIONS.md` and `QUALITY_GATES.md` still instruct agents to "show confidence" on every output. An agent following either file literally violates the other.

### Scope-boundary / misplaced-content findings (single occurrence, still real)

- `[Thinking]`: `DECISION_LOG.md` is the sole repository record of two `[AI OS]`-governance decisions (PR #28, #29) — arguably `[AI OS]`'s to own, not `[Thinking]`'s.
- `[Analytics]`: `Codex_Tasks/llm-text-standards/MODEL_ROUTING_MAX_CHAIN_DOCTRINE.md` is model-routing doctrine that, per `[Analytics]`'s own routing rule, belongs with `[LLM]`.
- `[Thinkers OS]`: 4 of 15 authors (Drucker, Boyd, Munger, Ohno) are marked "export ready, Judge pass" with no documented pattern content anywhere in the repo.

### Confirmed closed (no action needed)

- `[Analytics]`: the `ANALYTICAL_REASONING_STANDARD.md` near-duplicate risk flagged earlier in this session (closed PR #361 vs. the independently-created canonical file from issue #232) is confirmed resolved on `origin/main` — `docs/knowledge_bundle_provenance_audit.json` reports `unresolved_bundle_only_semantic_count: 0`, `blocking_record_count: 0` for the affected bundles.

## Full findings by project

The complete, evidence-cited finding list per project (file paths, line-level
citations, exact wording diffs) is preserved in this session's subagent
dispatch transcripts, not reproduced verbatim here to keep this record
navigable. Each project section below is the ranked summary; consult the
dispatch evidence records (see Method) for full citations before acting on a
specific finding.

**`[AI OS]`** — 2 high (bundle-coverage gap for 5 eval-gate files; stale smoke QA), 2 medium (bundle-02 scope-table mismatch), 2 low (long-candidate files; unverifiable external KB).

**`[Thinking]`** — 3 high (stale status vs. pilot evidence; deployment-status contradiction; misplaced AI-OS decisions), 2 medium (decision-status enum drift; missing bundle-04 semantics file), 3 low (workflow-file drift; stray status bullet; duplicated revisit-trigger wording).

**`[Analytics]`** — 2 high (stale smoke QA; dual unenforced manifests), 2 medium (confirmed-closed duplicate finding; stale `Codex_Tasks/` content), 2 low (dangling operational note; clean link-integrity spot-check) — plus 2 cross-domain notes (`[LLM]`-owned doctrine file misplaced; `[Codex]` task-archiving convention question).

**`[LLM]`** — 1 high (confidence-reporting contradiction), 2 medium (eval standard not wired into `EVAL_RUN_TEMPLATE.md`; registry/library identifier mismatch), 2 low (duplicated bundle content; pre-existing stale eval-matrix cases). Confirms PR #364's two new files are correctly wired, not orphaned.

**`[Codex]`** — 1 high (README omits 9 real Knowledge files, 3 required-reading), 3 low (duplicate report-format definitions; `CLAUDE.md`/`AGENTS.md` duplication — intentional; minor LDW wording nuance). Otherwise clean: bundle pipeline, index, and all cross-references verified intact.

**`[Inbox Router]`** — 2 high (`PROJECT_INSTRUCTIONS.md` destinations table diverged from root `ROUTING_RULES.md`; v05/v06 version-label conflict), 3 medium (mostly-unexecuted smoke QA; duplicate/diverged index files; README omits Knowledge_Bundles), 2 low (legacy files silent on Thinkers-OS anti-pattern; stale `last_checked`) — plus 1 cross-domain note (`HANDOFF_STYLE_STANDARD.md` missing a `[Thinkers OS]` row).

**`[Thinkers OS]`** — 1 high (portfolio-count contradiction: 12 vs. 15 authors), 1 medium (4 authors' patterns claimed export-ready with no content), 2 low/no-action (bundle freshness and `PROJECT_INSTRUCTIONS.md` length both verified correct — flagged only to avoid being mistaken for staleness).

## Next action

Not authorized by this record: any file edit. This is a review-and-plan record
only. Owner-approved next step (per the same conversation) is to work the
plan, starting with the high-priority items, in bounded follow-up PRs —
tracked separately, not in this evidence file.

Items explicitly flagged above as needing an owner decision rather than a
mechanical fix: the long-candidate status of `[AI OS]`'s
`WEEKLY_AI_OS_REVIEW_TEMPLATE.md`/`ARCHIVE_SUPERSEDED_RULE.md`; disposition of
`[Analytics]`'s stale `Codex_Tasks/` working files; whether to publish or
downgrade `[Thinkers OS]`'s 4 undocumented "export ready" patterns.
