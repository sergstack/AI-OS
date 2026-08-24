# Autonomous Execution Standard — Acceptance-Case Specification

Canonical standard: `AUTONOMOUS_EXECUTION_STANDARD.md` Section 12
(Validation responsibility matrix).
Schema: `schemas/autonomous_execution_record.schema.json`.

Phase 1 creates this specification. It does not create a semantic
validator. Cases in Section 2 below are documented for future automation
(Phase 6) and are not claimed as automated or passed today.

## 1. Structural cases (checkable today by JSON Schema + `python3 -m json.tool`)

Each case below can be produced as a minimal negative fixture and checked
against `schemas/autonomous_execution_record.schema.json`. None of these
fixtures are committed in Phase 1 — this table specifies what a Phase 6
(or an ad hoc local) schema conformance test should assert.

| # | Case | Expected result |
| --- | --- | --- |
| 1 | Missing `execution_id` | schema validation fails: required property missing |
| 2 | Missing `schema_version` | schema validation fails: required property missing |
| 3 | Invalid enum value, e.g. `execution_state: "Completed"` (wrong case) | schema validation fails: not one of the enum values |
| 4 | Wrong field type, e.g. `requirements` as an object instead of an array | schema validation fails: type mismatch |
| 5 | Malformed ID pattern, e.g. `execution_id: "EXEC_001"` (uppercase, underscore) | schema validation fails: pattern mismatch |
| 6 | Missing required nested field, e.g. a `defect` entry without `severity` | schema validation fails: required property missing inside `defects[]` |
| 7 | Non-nullable field set to `null`, e.g. `execution_id: null` | schema validation fails: type mismatch (string required) |
| 8 | Unknown top-level property, e.g. `extra_field: "x"` at the record root | schema validation fails: `additionalProperties: false` at root |
| 9 | `acceptance_scopes` missing a mandatory scope key (e.g. no `rollback_readiness`) | schema validation fails: required property missing inside `acceptance_scopes` |
| 10 | `judge_verdict` set to an Analytics-style value (`"blocked"` is valid, but `"revise "` with trailing space, or `"REVISE"`) | schema validation fails: not one of the enum values |

Verification command for any fixture set added later:

```bash
python3 -m json.tool <file>
python3 -c "import json, jsonschema; jsonschema.Draft7Validator(json.load(open('schemas/autonomous_execution_record.schema.json'))).validate(json.load(open('<file>')))"
```

The second command requires the `jsonschema` package. As of Phase 1 this
package is not declared as a repository dependency (it is not installed by
`.github/workflows/*`), so it is not used as an automated repository check;
see Section 3.

## 2. Semantic cases (documented for Phase 6; not automated in Phase 1)

These require cross-field reasoning beyond a structural JSON Schema and are
intentionally left to normative rules plus Judge/manual review until a
Phase 6 semantic validator exists.

1. `overall_delivery: pass` without any populated `requirements` array
   (no requirements traceability at all).
2. `overall_delivery: pass` while any mandatory requirement has
   `status: failed`.
3. `overall_delivery: pass` while any correctable defect has
   `status: open` or `status: correcting`.
4. A mandatory artifact's `generated_from_revision` predates the final
   relevant source revision (stale artifact reported as current).
5. A validation run's `validated_revision` predates the final relevant
   source revision without a documented `freshness_justification` and
   `unaffected_paths_evidence`.
6. A defect marked `resolved` with an empty `resolution_evidence_refs`.
7. A defect uses `status: blocked` while `correction_eligible: true` and
   the iteration/retry limits have not been reached (i.e. `blocked` used
   in place of an available, permitted local correction).
8. A handoff record that drops the parent execution's `execution_id`.
9. `production_status: authorized` without a populated
   `authority_evidence_ref` on the corresponding `external_actions` entry.
10. An iteration count exceeding the effective limit defined in
    `AUTONOMOUS_EXECUTION_STANDARD.md` Section 9.6 without a recorded
    `stopped` terminal reason.
11. A project extension that widens `merge_status` or `production_status`
    reachability beyond what the canonical standard allows.
12. A project extension document that reproduces the canonical standard's
    state model, defect model, or schema in full instead of referencing it.
13. A changed file outside the exact scope manifest recorded for the
    execution (scope-boundary violation).
14. `judge_verdict` and `authority_status` (or `qa_status`) merged into a
    single field or value instead of being reported separately.
15. `merge_status: merged` used to imply `production_status: authorized`.

## 3. Validation responsibility summary

| Property checked | Phase 1 mechanism | Automated in this repo today? |
| --- | --- | --- |
| JSON syntax | `python3 -m json.tool` | yes |
| Required fields / types / enums / ID patterns / nested shape | `schemas/autonomous_execution_record.schema.json` | not_run — no approved `jsonschema` dependency wired into `.github/workflows/*` or `tests/`; verified manually and via ad hoc local `jsonschema` use, not claimed as a repository CI check |
| Semantic cases (Section 2) | normative rule + acceptance-case documentation | not_run — Phase 6 scope |
| Allowed-file scope | exact scope manifest + `git diff --stat` review | manual, per PR |
| Business-rule / formula / metric preservation | project-specific checks | out of Phase 1 scope entirely |

Phase 1 does not assert that any Section 2 case is automatically enforced.

## 4. Closure Review acceptance cases (issue #268)

| ID | Case | Expected result | Deterministic evidence |
| --- | --- | --- | --- |
| AC1 | Adjacent class defect after green tests | register, correct, rerun, revalidate, review again | SEM-009/011 fixtures |
| AC2 | No gap exists | pass without invented defect or iteration | clean closure fixture |
| AC3 | Non-critical unfixable limitation | existing `partial`, no new status | status mapping |
| AC4 | Mandatory owner decision missing | blocked/stopped, not partial | AES 10.3 |
| AC5 | Closure budget exhausted | `closure_iteration_limit_reached` | SEM-010 fixture |
| AC6 | Mutation only reasoned about | `NOT_RUN`/hypothesis, not observed | AES 10.3 |
| AC7 | Late closure correction | old affected evidence stale | SEM-011 fixture |
| AC8 | Material handoff | identity/evidence/authority persist | existing handoff schema |
| AC9 | Codex stricter rule | one-fix policy is not widened | AES 10.3 |
| AC10 | Research Intelligence OS PR #4 | trust-boundary review finds/fixes adjacent defect; merge separate | retrospective below |

### AC10 retrospective mapping

Research Intelligence OS PR #4 (`806ea31`, documentation `d9e754a`) is a
retrospective fixture, not an external rerun. A closure review generalized a
known defect's invariant, found an in-scope forged derived-state trust-boundary
bypass, then the bounded correction/revalidation path closed. Merge remained a
separate owner action.
