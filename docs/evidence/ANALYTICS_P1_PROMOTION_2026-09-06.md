# `[Analytics]` P1/P1-B Promotion Decision — issues #445, #449 (2026-09-06)

Status: `[AI OS]`-owned governance-promotion decision, implemented by
`[Codex]`. Authorized directly by the repository owner (Sergey) in the same
working session that produced this record. This is **not** self-authorized
by the implementing agent: the owner's directive explicitly named the seven
items below for promotion and explicitly excluded
`ANALYSIS_CONTINUATION_GATE`.

## Explicit scope-extension statement

This record promotes controls whose bounded pilots were completed under
issues **#445** and **#449**. It is delivered on the branch and PR opened
for issue **#451** ("EDA-to-claim calibration"), which is a plain regression/
calibration review, not pilot-gated, and whose own text explicitly said "do
not... silently promote pilot-only semantics through this issue." Promoting
#445/#449 here therefore goes **beyond issue #451's literal scope**. This is
a **deliberate scope extension, authorized directly by the owner in this
conversation turn** — not an invisible edit riding along with #451's
calibration work. The owner's stated reason: he wants one continuous task
rather than manually operating separate GitHub-issue "epics," and PR #452
(the #451 branch) had not yet merged, making it the natural continuation
point.

## What was promoted (owner's list, verbatim scope — nothing added, nothing dropped)

**2 P1 controls + 6 P1-B controls promoted to standard/active** (no longer
"bounded pilot, owner review required before use"):

P1 (issue #445), 2 controls:

1. `POPULATION_CONTRACT` (§15.1).
2. `RECONCILIATION_CONTRACT` (§15.2).

P1-B (issue #449), 6 controls:

3. Strengthened material Explanation Challenge (§16.1).
4. `RECOMMENDATION_EVIDENCE` (§16.2).
5. Material stability/persistence check (§16.3).
6. `FORECAST_METHOD_COMPARISON` out-of-sample validation (§16.4).
7. `effect_type` economic-vs-process diagnosis boundary (§16.5).
8. `what_would_change_the_view` (§16.6).

EDA-to-claim calibration (issue #451, this same branch, commit `d671e2a`)
was **already plain regression coverage, not pilot-gated** — nothing to
promote there; confirmed preserved as-is (no edits made to
`GOVERNANCE_AND_ANTI_PATTERNS.md`'s calibration rows,
`EDA_CLAIM_CALIBRATION_REVIEW_2026-09-06.md`'s findings, or smoke QA case
15 in this change, beyond one forward-pointer sentence — see Files changed).

## What was explicitly NOT promoted (deferred, unchanged)

- **`ANALYSIS_CONTINUATION_GATE` (§15.3, issue #445) — remains deferred, not
  activated.** Repeated three times by the owner as a hard constraint. Its
  own pilot evidence found no incremental catch over §10's existing
  stop/escalation rules; nothing in this promotion changes that finding or
  its status. Verified: the §15.3 subsection body
  (`### 15.3 \`ANALYSIS_CONTINUATION_GATE\`...` through "there is no
  separate activation trigger to apply") is **byte-for-byte unchanged**
  from the pre-promotion text. The only edits near it were to the
  surrounding §15 section-intro paragraph and the "P1 status" summary
  paragraph, which previously grouped POPULATION_CONTRACT /
  RECONCILIATION_CONTRACT / ANALYSIS_CONTINUATION_GATE together under one
  "bounded pilot" framing — these were split so §15.1/§15.2 read as
  promoted and §15.3 continues to read as deferred, exactly as instructed.
- No P2 work (autonomous learning, self-improvement, automatic
  promotion/downgrade, agentic orchestration) — untouched, still deferred.
- No expansion of the 22-method registry. `ANALYTICAL_TECHNIQUES.md` was
  not opened or edited by any change in this record; it is unchanged from
  the state already present in this worktree (which #445/#449/#451 each
  independently verified as byte-identical to `origin/main`). This session
  could not independently re-run `git diff origin/main -- .../ANALYTICAL_TECHNIQUES.md`
  because git access was unavailable in this working session (see
  Validation, "Known limitation" below) — the assurance given here is that
  **no edit tool in this session touched the file**, which is the
  strongest available guarantee without git.
- No new gate, mode, registry, or duplicate framework was created anywhere
  in this change. `what_would_change_the_view`, `effect_type`, and the
  other items stay narrow field-level clarifications on existing
  contracts/templates — promotion changed activation/authorization wording
  only, not their shape.

## Mechanical changes made

`ANALYTICAL_REASONING_STANDARD.md`:

- §15 section-intro paragraph rewritten: §15.1/§15.2 now read "promoted to
  standard, active status"; §15.3 explicitly called out as not promoted,
  remains deferred.
- "P1 pilot status (issue #445)" section renamed "P1 status (issue #445)"
  and rewritten to state the promotion, while preserving the
  `ANALYSIS_CONTINUATION_GATE` deferred statement and the rollback
  paragraph unchanged in substance.
- §16 section-intro paragraph rewritten: all six elements now read
  "promoted to standard, active status"; explicitly states promotion does
  not change the differentiated evidence-strength characterization.
- "P1-B pilot status (issue #449)" section renamed "P1-B status (issue
  #449)" and rewritten to state the promotion while preserving, verbatim,
  the per-element evidence-strength verdicts (three real incremental
  catches — §16.2/§16.3/§16.4; one modest formalization — §16.5; one
  naming/consistency-only — §16.6; one partially-scenario-tested — §16.1).
  Added one explicit sentence warning against the exact failure mode the
  owner flagged: "Normal/promoted use of these controls does not mean
  every output they touch is `SUPPORTED`."
- §15.3 and the six §16.1–§16.6 subsection bodies: **not edited** (verified
  by direct reading before and after).

Pointer-only updates (historical content preserved, one forward-pointer
line/paragraph added per file, per the owner's instruction not to rewrite
pilot-evidence verdicts):

- `P1_PILOT_EVIDENCE_2026-09-06.md` — added a promotion pointer above the
  original "Status: bounded pilot evidence only" line (now labeled
  "historical, at time of writing").
- `P1_449_PILOT_EVIDENCE_2026-09-06.md` — same treatment.
- `EDA_CLAIM_CALIBRATION_REVIEW_2026-09-06.md` — added one forward-pointer
  sentence after the existing "bounded pilots... remain bounded-pilot"
  statement, clarifying that promotion happened later, on the same branch,
  as an owner-authorized scope extension beyond issue #451 itself; the
  original sentence describing what #451 itself did is preserved unchanged.

Consistency updates across the specific promoted items' own field
definitions and consuming checklists (in scope because leaving these
contradicting the newly-promoted `ANALYTICAL_REASONING_STANDARD.md` text
would be an internal inconsistency defect, not a deferred item):

- `ACCEPTANCE_CRITERIA.md` (item 16) — "bounded pilot" → "standard/active...
  promoted 2026-09-06."
- `QA_CHECKLIST.md` — §16 checklist section header and owner-review line
  updated to "standard, active"; "Held-out transfer eval (issue #445)"
  section's closing line updated to state `POPULATION_CONTRACT` /
  `RECONCILIATION_CONTRACT` are promoted while `HELD_OUT_TRANSFER_EVAL`
  itself continues as a standard regression-check lane (not a promotion
  gate — it remains useful ongoing QA regardless of promotion status).
- `CHANGELOG.md` — new top entry (`analytics-p1-p1b-promotion`) documents
  the promotion, the scope-extension, the 7-item list, and the explicit
  exclusions; the original 2026-09-06 `#449` and `#445` entries are
  preserved with one added "Update (same day, later entry above)" paragraph
  each, pointing forward — their original body content and `Status:` blocks
  are otherwise untouched.
- `ANALYTICS_PROJECT_FILES_INDEX.md` — the two pilot-evidence-doc rows'
  description column updated to note promotion; the "when needed" column
  reworded from "for owner review" to "historical evidence... (now
  standard)."
- `METRIC_DEFINITION_CARD_TEMPLATE.md`, `DATA_CONTRACTS.md`,
  `VARIANCE_DIAGNOSTIC_CONTRACT.md`, `MEMO_PIPELINE.md`, `MEMO_RUBRIC.md`,
  `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md` — each had one section
  header/sentence that named the specific promoted mechanism
  (`POPULATION_CONTRACT`, `RECONCILIATION_CONTRACT`, `effect_type`,
  `RECOMMENDATION_EVIDENCE`) as "bounded pilot"; each was updated to
  "standard, active" with a pointer to this record, without changing any
  field list, required behavior, or activation trigger.

`PROJECT_INSTRUCTIONS.md` (`ChatGPT/[Analytics]/PROJECT_INSTRUCTIONS.md`,
currently 7983/8000 chars): **not touched.** Checked per the owner's
instruction — promotion status is a Knowledge-layer concern, consistent
with #439/#445/#449/#451 precedent (none of which touched this file). No
hard architectural requirement was found that would force a reference here;
this file is already essentially at its length ceiling, so if a future
change did need to reference promoted controls in the compact kernel, that
would need explicit owner attention for either a trim or a ceiling change —
not silently done here.

## External Analytics behavioral acceptance — explicit scope boundary

**`external Analytics behavioral acceptance = NOT RUN`, and this record does
not attempt to close it.**

This record and this task are bounded to **repository-side completion**:
formalizing the promotion decision, aligning source text and generated
artifacts, and preparing an upload package. They do **not** include, and
must not be read as including:

- a behavioral test of the actual `[Analytics]` ChatGPT Project (its live
  Project Instructions + uploaded Knowledge Bundles, run as that Project);
- a surrogate agent or local model standing in for that Project;
- any claim that `[Analytics]`'s real analytical output has improved.

An earlier pass of this work built three illustrative fixtures (a public
real dataset, a labeled-synthetic finance table, and a routine reconciled
table) and authored two hypothetical narratives per fixture under old vs.
new contract text, calling the result "analyst narratives." **That content
has been removed from this record on the owner's explicit instruction**: a
scripted Python computation plus hand-authored expected prose is not a
behavioral run of `[Analytics]` on any execution surface — real
`[Analytics]`, a local evaluation harness, or another actually-invoked
model — and presenting it as such would misrepresent what was tested. It
does not appear anywhere in the promoted contract text or the accepted
scope; only the promotion-status wording changes described above and the
static regression coverage already present from #445/#449/#451 (their
existing paper-traced pilot-evidence docs and smoke QA cases, left
historical/unmodified in substance) are part of this delivery's tested
surface.

The owner will perform the real behavioral quality check directly, on the
actual `[Analytics]` ChatGPT Project, on real analytical tasks, after the
upload package below is applied. That check is intentionally out of this
record's and this session's scope.

## Validation (observed, real output — this session)

```text
$ python3 scripts/build_knowledge_bundles.py --write
WROTE
$ python3 scripts/build_knowledge_bundles.py --check
PASS
$ python3 scripts/audit_bundle_provenance.py --write
WROTE
$ python3 scripts/audit_bundle_provenance.py --check
PASS
$ python3 scripts/check_project_instructions_length.py
Checked PROJECT_INSTRUCTIONS.md files: 7 / Passed: 7 / Failed: 0
$ python3 scripts/check_repo_public_safety.py
Public safety check passed.
$ python3 scripts/check_codex_goal_mode_defaults.py
Codex Goal Mode atomic-default occurrences checked: 23 / Failed: 0
$ python3 scripts/check_manifest_paths.py
checked: 189 / passed: 189 / failed: 0
$ python3 scripts/check_knowledge_bundles.py
projects checked: 7 / bundles checked: 33 / failed: 0
$ python3 scripts/check_index_coverage.py
Index coverage pairs checked: 9 / Failed: 0
$ python3 -m pytest -rA -q
635 passed in 60.34s
```

All output above is real, observed in this working session, not inferred.

**Known limitation (git access):** this working session's sandbox refused
all `git` invocations (including plain, read-only ones such as `git status`
and `git diff`), categorically, for reasons unrelated to file content. This
means:
- `git diff origin/main -- .../ANALYTICAL_TECHNIQUES.md` could not be run to
  produce a fresh byte-identical diff in this session. The assurance given
  instead: no edit/write tool in this session touched that file, and
  #445/#449/#451 each independently already verified it byte-identical to
  `origin/main` before this session began.
- The commit for this change (message ending
  `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`) and the branch
  push could not be performed in this session. See the handoff digest for
  the exact list of modified files in the working tree, so a session with
  git access can commit/push and update PR #452's description to reflect
  this scope extension.

## Package-ready vs live-Project-updated — explicit statement

This is a **repository-level change only**. `Knowledge_Bundles/*.md` for
`[Analytics]` were regenerated via the canonical
`scripts/build_knowledge_bundles.py --write` and verified via `--check`;
`docs/knowledge_bundle_provenance_audit.{json,md}` were regenerated and
verified via `scripts/audit_bundle_provenance.py`. This means the
**repository package is ready** for upload. It does **not** mean the live
`[Analytics]` ChatGPT Project has been updated — external Project Knowledge
sync/upload is a separate, owner-gated manual step, not performed as part
of this record. **"Package ready" and "live Project updated" are different
claims; only the former is true here.**

The one concrete owner action needed to close the gap: upload the changed
`ChatGPT/[Analytics]/Knowledge_Bundles/*.md` files (all 7 bundles were
regenerated by this change) to the `[Analytics]` Project's Knowledge
Sources, replacing the currently-uploaded versions.

## Rollback

- `ANALYTICAL_REASONING_STANDARD.md`, `ACCEPTANCE_CRITERIA.md`,
  `QA_CHECKLIST.md`, `CHANGELOG.md`, `ANALYTICS_PROJECT_FILES_INDEX.md`,
  `METRIC_DEFINITION_CARD_TEMPLATE.md`, `DATA_CONTRACTS.md`,
  `VARIANCE_DIAGNOSTIC_CONTRACT.md`, `MEMO_PIPELINE.md`, `MEMO_RUBRIC.md`,
  `CLAIM_EVIDENCE_REGISTRY_TEMPLATE.md`, `P1_PILOT_EVIDENCE_2026-09-06.md`,
  `P1_449_PILOT_EVIDENCE_2026-09-06.md`,
  `EDA_CLAIM_CALIBRATION_REVIEW_2026-09-06.md`: revert this commit's changes
  to these files to fall back to "bounded pilot, owner review required"
  status for all 7 promoted items. No field, activation trigger, or
  required-behavior text changes — rollback is purely a status-wording
  revert.
- Rerun `python3 scripts/build_knowledge_bundles.py --write` and
  `python3 scripts/audit_bundle_provenance.py --write` after reverting, to
  resynchronize bundles/provenance with the reverted sources.
- `docs/evidence/README.md`, `CURRENT_STATUS.md`, `MASTER_STATUS.md`: revert
  the added pointer/status lines.
- No method-registry migration, schema change, or data migration is
  required for rollback in any case — this was a documentation/status
  change only.

## Final status

```text
repo implementation:                PASS
repo tests:                          PASS (635/635; 8 repo validation scripts PASS)
package ready:                       YES
controls accepted (standard/active): 2 P1 controls + 6 P1-B controls
  - POPULATION_CONTRACT (§15.1, issue #445)
  - RECONCILIATION_CONTRACT (§15.2, issue #445)
  - Strengthened Explanation Challenge (§16.1, issue #449)
  - RECOMMENDATION_EVIDENCE (§16.2, issue #449)
  - Material stability/persistence check (§16.3, issue #449)
  - FORECAST_METHOD_COMPARISON out-of-sample validation (§16.4, issue #449)
  - effect_type economic-vs-process boundary (§16.5, issue #449)
  - what_would_change_the_view (§16.6, issue #449)
external ChatGPT Project sync:       NOT RUN
external Analytics behavioral acceptance: NOT RUN
```

Deferred, unchanged, not promoted: `ANALYSIS_CONTINUATION_GATE` (§15.3);
P2/autonomous-learning/self-improvement work; 22-method registry expansion.

- delivery: `pass` — 2 P1 controls + 6 P1-B controls promoted per the
  owner's explicit list; `ANALYSIS_CONTINUATION_GATE` verified untouched.
- tests: `pass` — 635/635 (real output above), plus all 7 repo validation
  scripts observed `PASS`/`WROTE`+`PASS`.
- review: `not_run` — this PR is not self-merged; owner review of this
  cross-project-adjacent record and the root-file pointer additions
  (`CURRENT_STATUS.md`, `MASTER_STATUS.md`, `docs/evidence/README.md`) is
  the existing, correct gate and is pending.
- authority: `owner_instruction` for the promotion decision itself (given
  directly in this session); `pending` for merge/production-deploy/external
  Project sync/external behavioral acceptance, none of which were performed
  here.
