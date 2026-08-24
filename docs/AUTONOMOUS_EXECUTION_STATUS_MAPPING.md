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
equivalent to `overall_delivery: pass`.

The `[Analytics]` execution extension now exists:
`docs/autonomous_execution/extensions/ANALYTICS_EXTENSION.md`. This section
is the single normative source for the mapping rule; the extension
document references this section rather than restating it.

### 4.1 Normative rule

`accepted: yes` MAY be reflected as `overall_delivery: pass` only when it
coincides with satisfying every mandatory `acceptance_scope` already
required by the canonical standard (`AUTONOMOUS_EXECUTION_STANDARD.md`
Section 10.1: `requirements_traceability`, `implementation`, `tests`,
`validation`, `output_artifacts`, `corrective_loop`,
`rollback_readiness`) **and** the domain-specific
`acceptance_scope_additions` defined in the `[Analytics]` extension
(`analytics_data_contract`, `analytics_lineage`,
`analytics_reconciliation`, `analytics_claim_evidence`). Accepted status
alone, without those, is not sufficient — an executor or extension may not
treat `accepted: yes` as a shortcut around any mandatory or
domain-specific acceptance scope.

`accepted: no` always blocks `overall_delivery: pass`, regardless of the
state of any other acceptance scope.

This rule does not invent new Analytics acceptance criteria; it only
states the conditions under which the existing Analytics `accepted:
yes/no` field (`ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`) may
or may not be reflected in the canonical `overall_delivery` field. It does
not convert `accepted` into `overall_delivery` mechanically in either
direction.

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

## 9. Closure Review compatibility

`closure_review.status` uses `not_run / pass / revise / blocked`; it does not
create `PASS_WITH_LIMITATIONS` or replace `overall_delivery`. A limitation can
remain only when it is non-critical, explicit, safe, not technically fixable
inside current scope/authority, and Closure Review passes. A missing mandatory
owner decision is `blocked`, not a limitation. Historical artifacts that use
`PASS_WITH_LIMITATIONS` must be marked `historical_pre_aes` and map to
`overall_delivery: partial` with their limitation text retained; new records
must use only the canonical namespace.
owner/business/policy decision is `blocked`, not partial success. A Closure
Review pass is evidence only: `authority_status`, `merge_status`, and
`production_status` retain their independent meanings.
