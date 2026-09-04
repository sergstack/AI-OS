# AIOS AutoResearch — Preflight for the MD-2 Semantic-Completion Handoff — 2026-09-05

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409). Runtime: PR
[#434](https://github.com/sergstack/AI-OS/pull/434) (issue #433), `main`@
`3b81126cb754a3b4021fa16666b418e62eda5c90`.

Status: **read-only preflight only.** No code change, no live call, no
merge. Produced in response to a `[Thinking]`-authored candidate task
package (`AUTORESEARCH_SEMANTIC_COMPLETION_REVIEWED_V2.md`, reviewed-v2,
2026-09-05) that is explicitly a recommendation, not an execution
authorization. This document, plus the MD-2 decision package and the
subject-content-propagation memo in this same directory, are the "bounded
execution plan" its own "Suggested first step" asks for.

## Revision state

- `origin/main` HEAD: `3b81126cb754a3b4021fa16666b418e62eda5c90` — unchanged
  since the #434 merge and since the C1-R1 live run (2026-09-04). This is
  the revision every check below and every source reference in the
  companion documents was read against.
- Working branch for this handoff: `codex/autoresearch-md2-handoff`,
  branched directly from `origin/main` at this revision (not from the
  divergent branch the C1-R1 freeze package was previously, and
  incorrectly, left on — see "Branch lineage correction" below).

## Checks run fresh on this revision (not reused from any prior session)

```bash
python3 -m pytest tests/ -q
# 613 passed in 42.85s

python3 scripts/check_manifest_paths.py
# checked: 189, passed: 189, failed: 0

python3 scripts/check_repo_public_safety.py
# Public safety check passed.

python3 scripts/check_index_coverage.py
# Index coverage pairs checked: 9, Failed: 0

python3 scripts/check_knowledge_bundles.py
# projects checked: 7, bundles checked: 33, failed: 0
```

No live/network/model call was made producing this document.

## C1-R1 freeze package durability check

Copied from `docs/evidence/autoresearch_c1r1_freeze/` (as it existed on the
divergent working branch) into this branch's identical path. Verified
byte-for-byte after copy:

- `candidate.patch` sha256 unchanged:
  `9e7d0a1ea07f4b626b7be9a5bbd42b3df950b3481016fddf43d86d26bc45509c`
  (matches `spec.json`'s declared `candidate_patch_hash`).
- `git apply --check` of `candidate.patch` against its original baseline
  `0b1ce29386342ef4e1884d8a58b574445572575e` still applies cleanly.
- Ledger `scratchpad/arpilot/evidence/autoresearch_manual_evaluations.jsonl`
  (left in place on the executor's machine, not copied here — it is
  disposable-scratch, non-canonical, per the run's own closure record)
  hash-chain re-verified via the real `av.verify_ledger`: 0 findings.

## Branch lineage correction

The C1-R1 freeze package and its live-run evidence doc were originally
written into the working tree of `codex/chatgpt-project-live-optimization-source`
(head `cf294f3` at the time), a branch that does **not** descend from
`3b81126` and carries none of the AutoResearch scripts at all
(`git merge-base --is-ancestor` false in both directions — confirmed
2026-09-04, re-confirmed here). That was flagged at the time and is now
corrected: this branch (`codex/autoresearch-md2-handoff`) is cut directly
from `origin/main`@`3b81126`, and the freeze package has been copied here
with hashes re-verified, not regenerated. The original untracked copy on
the divergent branch has not been deleted (kept until this copy's integrity
is independently confirmed, per the task package's own instruction not to
treat "removed the old copy" as a durability test).

## Central finding independently re-verified by direct code reading

`scripts/autoresearch_decision_comparator.py::evaluate_case_material_improvement`
requires, for every matched (baseline, candidate) rerun pair:
`severity(candidate) < severity(baseline)`. `scripts/autoresearch_cli.py::_contributes_to_pair`
(the MD-2 mapping) can only ever produce `(pass, pass)` — equal severities
— or `(None, None)` — excluded from the matched set entirely. Equal values
can never satisfy a strict `<`. **`material_improvement_result` is
therefore structurally incapable of returning `"keep"` under the current
wiring, for any candidate, real or hypothetical** — not a C1-R1-specific
artifact, not a probabilistic near-miss. Full analysis: see
`AUTORESEARCH_MD2_DECISION_PACKAGE_2026-09-05.md` in this directory.

## What this preflight does not establish

- Whether any of the remediation options in the MD-2 decision package is
  acceptable to `[LLM]` / `[Analytics]` / `[AI OS]` — that is the open
  decision this handoff routes to them.
- Whether the subject-content-propagation gap (see the companion memo) is
  a defect or an intentional anti-dump design choice — also routed, not
  resolved here.
- Semantic readiness of AutoResearch v0.2 as a whole. This preflight
  confirms the measurement contour's current inability to detect
  improvement; it does not certify anything else about the program.
