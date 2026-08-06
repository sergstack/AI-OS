# Autonomous Execution Standard — Status Migration Map

Canonical standard: `AUTONOMOUS_EXECUTION_STANDARD.md`.

This is a compatibility document. It maps existing repository status
vocabularies onto the AES v1 status namespaces (Section 4 of the standard)
without renaming or destructively replacing the existing vocabularies. No
existing script, template, or Project Instructions file is required to
change its wording because of this mapping.

## 1. Existing Codex acceptance status

Source: `ChatGPT/[Codex]/Knowledge/ACCEPTANCE_CRITERIA.md`
(`acceptance_status: pass / partial / fail / blocked`).

```text
legacy Codex acceptance_status -> overall_delivery
and, where an execution record is kept, -> the relevant acceptance_scopes entries
```

This does **not** map into `judge_verdict` or `authority_status`. Those
remain separate fields (Section 13 of the standard).

| Legacy value | `overall_delivery` |
| --- | --- |
| `pass` | `pass` |
| `partial` | `partial` |
| `fail` | `fail` |
| `blocked` | `blocked` |

## 2. Judge verdict

Source: `ChatGPT/[AI OS]/Knowledge/JUDGE_CALIBRATION.md`
(`pass / revise / blocked`).

Maps only into `judge_verdict`:

| Legacy value | `judge_verdict` |
| --- | --- |
| `pass` | `pass` |
| `revise` | `revise` |
| `blocked` | `blocked` |
| (not yet run) | `not_run` |

## 3. Analytics QA status

Source: `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`
(`qa_status: pass/fail/blocked`).

Maps into `qa_status`:

| Legacy value | `qa_status` |
| --- | --- |
| `pass` | `pass` |
| `fail` | `fail` |
| `blocked` | `blocked` |
| (not yet run) | `not_run` |

## 4. Analytics `accepted: yes/no`

This is **not** mapped mechanically. `accepted: yes` on an Analytics
deliverable is a business/content acceptance decision, not automatically
equivalent to `overall_delivery: pass`. A future `[Analytics]` execution
extension (Phase 4, `docs/pilots/AES_ANALYTICS_PILOT.md`) must define which
domain conditions (claim/evidence mapping complete, reconciliation passed,
management conclusion supported) are required before `accepted: yes` may be
reflected as `overall_delivery: pass`. Until that extension exists, treat
`accepted: yes` as informative only, not as an automatic `overall_delivery`
input.

## 5. Supervised-loop status

Source: `ChatGPT/[AI OS]/Knowledge/LOOP_ACCEPTANCE_CHECKLIST.md`
(`candidate`, `ready for human review`).

These map into adoption/authority metadata, not into execution success:

| Legacy value | AES field |
| --- | --- |
| `candidate` | informative note in `final_report`; does not set `overall_delivery` |
| `ready for human review` | `authority_status: owner_review_pending` |

## 6. Merge classification (`tier=auto` / `tier=owner`)

Source: `GOAL_MODE.md` Merge Policy.

Remains a merge-policy classification, unchanged. It is **not** mapped into
`overall_delivery`. It informs `merge_status` handling only insofar as
`tier=auto` PRs may progress through `checks_pending -> merge_ready ->
merged` via the deterministic GitHub Merge Gate, while `tier=owner` PRs stay
at `owner_review_pending` until an explicit owner decision.

## 7. Production promotion flag

Source: `MANIFEST.json` (`production_promotion: "no"` at the `[AI OS]`
project-settings level).

May be represented in an execution record as:

```yaml
production_status: not_authorized
```

The source manifest contract itself (`production_promotion`) is **not**
renamed or restructured by this mapping; that would require a separate,
explicitly approved migration. AES simply provides the equivalent status
value for use inside an execution record.

## 8. Non-goals of this mapping

This document does not: rename any existing field in any existing file;
require any existing script or template to change; imply that any project
already produces `AUTONOMOUS_EXECUTION_STANDARD.md`-shaped execution
records (that is Phase 2-5 adoption work); or claim that any of the above
mappings are automatically enforced. They are a normative correspondence
table for humans and future extension authors.
