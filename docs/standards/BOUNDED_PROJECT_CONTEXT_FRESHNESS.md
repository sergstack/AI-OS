# Bounded Project-Context Freshness (P0)

Advisory diagnostic layer for Issue #369 ("Bounded Project Execution").
Owner-approved bounded scope, dated 2026-09-03, following a `[Thinking]`
architecture review (`docs/evidence/` pilot findings, see revision review
2026-09-03). It is **advisory only** — no execution path is blocked by this
standard. Promotion to a blocking gate is a separate owner decision, gated on
the promotion trigger in "Status and promotion" below.

## Already covered elsewhere — do not duplicate

This standard adds exactly two new things: a declared `required_knowledge`
list per capability, and a declared status-freshness anchor for hand-written
status files. Everything else Issue #369's P0 scope asked for already exists
and is not restated here:

| P0 concern | Already covered by |
|---|---|
| Bounded project-context contract (root selects owner, one bounded context per child, no self-rerouting, canonical path + declared entrypoints only, fixed revision, read-only vs. write-capable, no nested delegation, structured evidence) | `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md` § Supervised AI-OS Subagent Dispatch (Pilot) — mandatory bounds list |
| Freshness-status vocabulary (`current \| stale \| unverifiable \| not_applicable`) and the "no false current/pass" invariant | `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` §4.10, §11.2 (validation freshness), §11.3 (artifact-freshness record), enforced by `scripts/validate_autonomous_execution_record.py` SEM-005 |
| Canonical-source → bundle freshness (recomputed, not trusted) | `scripts/build_knowledge_bundles.py`, `scripts/check_knowledge_bundles.py` (blocking in `docs-safety.yml`) |
| Revision-bound QA, evidence-preserving handoff, root closure check (Issue #369 P1) | `AUTONOMOUS_EXECUTION_STANDARD.md` SEM-006, SEM-009/010/011 — out of scope here |
| Structured dispatch evidence | `schemas/subagent_dispatch_evidence.schema.json`, `scripts/check_subagent_dispatch_evidence.py` |

Do not create a parallel capability registry, a parallel freshness enum, or a
parallel dispatch contract. `PROJECT_CAPABILITIES.yaml` remains the only
capability registry (`AGENT_LOOP_PLAYBOOK.md`).

## Scope

Two new, additive checks, both advisory:

1. **Required-knowledge presence.** For each of the 7 registered capabilities,
   a declared list of files `PROJECT_INSTRUCTIONS.md` names as required
   reading. Detects a file that is required but absent from the repo, or
   required to reach a live ChatGPT project via a bundle but not actually
   embedded in any bundle that project uploads.
2. **Status-artifact freshness.** For a project's hand-written status file
   (`CURRENT_STATUS.md` or equivalent), a declared scope of paths it claims to
   describe and the revision at which it was last verified. Detects "not
   re-verified since its declared scope changed."

## `required_knowledge` — field spec

Additive sibling of `executor` in each capability block of
`PROJECT_CAPABILITIES.yaml`:

```yaml
required_knowledge:
  - path: "ChatGPT/[LLM]/Knowledge/LLM_EVAL_STANDARD.md"
    delivery: bundle
    reason: "cited by name in PROJECT_INSTRUCTIONS.md"
```

`delivery` is one of:

- `bundle` — must exist at `path` **and** be embedded (`## From: \`path\``) in
  at least one bundle listed in that capability's own
  `Knowledge_Bundles/UPLOAD_LIST.md`. A live ChatGPT project that only
  uploads bundles (the default upload mode) would not otherwise have this
  file's normative text.
- `project_instructions` — must be named (by basename) in the capability's
  own `PROJECT_INSTRUCTIONS.md` text. Used for content that is inline policy,
  not a separate file.
- `repo_only` — must exist at `path`. Used for shared root standards
  referenced "by reference" (e.g. `GOAL_MODE.md`,
  `docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md`) that are not meant to
  be duplicated into every project's own bundle.
- `external` — never checked for presence in this repo by design. Used for
  content that deliberately lives only in the live ChatGPT Project Knowledge
  base and must not be re-uploaded from the repo (e.g. `[AI OS]`'s `KB__*`
  files — see `MANIFEST.json`'s `do_not_reupload_existing_kb: true`). An
  `external` entry always reports `unverifiable`, never `pass` and never
  `fail` — the repo has no way to confirm or deny its live state.

A capability with `schema_version: 3` and no `required_knowledge` block
reports `BLOCKED_UNDECLARED` — the declaration is mandatory once this schema
version is adopted, so silence is never mistaken for "nothing required."

**Known residual, stated rather than hidden:** the reverse direction (a new
file added to `PROJECT_INSTRUCTIONS.md` and never declared here) is not
closable by this check alone — the declaration itself is hand-authored and
can drift. An automated `PROJECT_INSTRUCTIONS.md`-parsing extraction was
tested and rejected: applied naively across all 7 projects it produced ~50%
false positives (10 of 24 findings were `[AI OS]`'s deliberately-external
`KB__*` files; ~9 more were references to files that are contractually not
bundle content — `PROJECT_INSTRUCTIONS.md`, `CURRENT_STATUS.md`, `AGENTS.md`,
`CLAUDE.md`, `GOAL_MODE.md`, `UPLOAD_LIST.md`). A declaration-driven check,
hand-curated once and advisory thereafter, is the accepted tradeoff.

## Status-artifact freshness — field spec

Optional block in a project's status file (only where one exists — 3 of 7
capabilities have no status artifact, and none is required by this
standard):

```text
- status_scope: <repo path>[, <repo path>, ...]
- status_verified_revision: <commit sha>
```

Computation:

- `current` — no commit touching any path in `status_scope` is newer than
  `status_verified_revision` (`git log --oneline <rev>..HEAD -- <scope>` is
  empty for every scope path).
- `stale` — at least one is; the report names the offending paths and the
  newer commit(s).
- `unverifiable` — the block is absent, or `status_verified_revision` does
  not resolve in the current clone (e.g. a shallow checkout).
- `not_applicable` — the capability declares no status artifact.

**Stated limitation, not implied coverage:** this detects "the declared
scope changed since the file was last verified." It does not detect a status
file that was wrong on the day it was written, and it does not detect
cross-file token contradictions (e.g. a version label disagreeing between two
files, a count disagreeing between two files) — that class of finding is real
(see the 2026-09-03 revision review) but requires per-pair declared
assertions and is out of scope for P0.

A content hash is deliberately not used for status-file freshness. A bundle
has an expected, regenerable content, so "stale" is a decidable predicate
(`render(sources) != file_on_disk`). A hand-written status file has no
expected content — hashing it proves only that it changed, which has the
wrong sign: a status file hand-edited yesterday to say something false
hashes as "fresh," and a correct status file untouched for a month hashes as
"changed → suspicious." `AUTONOMOUS_EXECUTION_STANDARD.md:728-730` and
`ChatGPT/[AI OS]/Knowledge/SKILLS_HOOKS_MCP_DECISION_MATRIX.md` already
forbid date-only freshness for the same reason; a revision anchor, not a
date, is used here.

## Check script

`scripts/check_project_context_contract.py`:

- `--advisory` (default): prints the full report, always exits 0.
- `--enforce`: prints the full report, exits 1 if any finding exists.

Not wired as a blocking step. Added to `.github/workflows/docs-safety.yml` in
`--advisory` mode only.

## Non-goals

- No new runtime, service, or database.
- No auto-regeneration of any status file, bundle, or manifest.
- Does not replace `check_index_coverage.py` (directory-vs-index
  completeness — a different question), `check_manifest_paths.py`, or
  `check_knowledge_bundles.py` (bundle fingerprinting — already blocking and
  correct).
- Does not emit or modify an AES execution record; is not a second closure
  gate alongside AES SEM-009/010/011.
- Does not detect cross-file token contradictions (out of scope, see above).
- Does not attempt Issue #369's P1/P2 scope (revision-bound QA,
  evidence-preserving handoff, root closure check, a repair pass across all
  7 status files, or the 7-project pilot itself).
- Not a blocking gate. Not a general-purpose linter framework.

## Status and promotion

`STANDARDIZED — advisory only`, dated 2026-09-03. Owner-approved direction
(per the same conversation as the 2026-09-03 revision review and Issue #369).

**Promotion trigger:** review `--enforce` promotion after the advisory
`required_knowledge` findings across all 7 capabilities reach zero, or every
remaining finding is explicitly justified (e.g. accepted as a permanent
`external` classification). Until that review happens, this check stays
advisory and its findings are not a merge blocker. This is a deliberate,
named trigger — an advisory check with no promotion criterion decays into
ignored noise, per the same review's own risk flag.

## Rollback

If the advisory findings prove noisy or low-value: delete
`scripts/check_project_context_contract.py`, remove its step from
`docs-safety.yml`, and remove the `required_knowledge` blocks from
`PROJECT_CAPABILITIES.yaml` (revert `schema_version` to 2). No other
mechanism in this repo depends on this standard — the bundle
fingerprinting, dispatch contract, and AES freshness machinery it explicitly
does not duplicate are all unaffected by removing it.
