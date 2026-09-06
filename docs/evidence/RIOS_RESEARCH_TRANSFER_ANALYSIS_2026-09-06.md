# RIOS Research-Transfer Gap Analysis (Issue #446)

Status: decision evidence for Issue #446 ("Research-backed AI-OS optimization:
adaptive escalation, dynamic context, verification and recovery"). This is a
`candidate_research` / `hypothesis_recommendation` input turned into concrete
repository decisions by direct repository inspection, not a claim that RIOS
findings are self-authorizing. RIOS itself is not expanded: no Golden Set, no
pilot registry, no new promotion bureaucracy is created here.

## Method

For each of the issue's five research-backed directions, this record: (1)
names the existing AI-OS mechanism(s) already covering it, found by direct
repository search and reading; (2) states the concrete gap, if any; (3)
classifies the direction as `already_covered`, `needs_strengthening`, or
`new_capability_required`; (4) states the accept/reject call and, where
accepted, the smallest viable change implemented in this PR.

Per the issue's explicit instruction, a direction is **rejected** (not
implemented) when repository inspection shows it is already adequately
covered — implementing it anyway would create a duplicate control plane,
which the issue's non-goals forbid.

---

## Direction 1 — Adaptive model/reasoning escalation

**Existing mechanism found:** a static task-type → model-class routing table
in `ChatGPT/[LLM]/Knowledge/MODEL_ROUTING.md` (bundled into
`LLM_01_ROUTING_AND_MODEL_SELECTION.md`) and `ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md`
("fast lookup/formatting → fast model; synthesis/critique/judge → reasoning
model; complex planning/long context → high-reasoning model"). `JUDGE_CALIBRATION.md`
already defines the model-class vocabulary (`fast`/`reasoning`/`high-reasoning`/
`local`/`judge`) used elsewhere (`LLM_EVAL_STANDARD.md`,
`CROSS_PROJECT_LIVE_EVAL_MATRIX.md`).

**Gap:** the existing table selects a tier once, from the task's declared
type, at the start. There is no cascade: no rule for escalating one tier when
the current tier's output fails a quality gate or shows low confidence, and
no abstention criterion distinguishing "escalate further" from "stop, this is
not a model-capability problem." This is exactly the gap the RIOS-cited
cascaded-LLM-decision research targets (base → stronger → human/abstain).

**Classification:** `needs_strengthening` (existing static routing is real
but does not cover the adaptive/cascade behavior).

**Verdict:** accept — smallest viable change.

**Change implemented:** added an "Adaptive escalation" section to
`ChatGPT/[LLM]/Knowledge/MODEL_ROUTING.md` (rebuilt into
`LLM_01_ROUTING_AND_MODEL_SELECTION.md`): a one-step-at-a-time ladder
`fast → reasoning → high-reasoning → human/owner review or abstain`, explicit
escalation triggers (quality-gate failure at current tier, `material`/
`complex`/high-risk flag, low/contradictory confidence signals including a
Judge `revise`/`blocked` citing reasoning depth, long-context/planning need
beyond the tier's checklist), and explicit abstention triggers (already tried
`high-reasoning` and still failing; the gap is a missing fact/business-rule/
authority question no model tier can resolve; resolving it needs an
unapproved schema/formula/metric/output-contract/business-logic/provider
change). Explicitly states escalation never widens authority: a higher tier
still cannot self-accept `accepted_risk`, override deterministic checks, or
bypass Judge/owner acceptance — reusing `JUDGE_CALIBRATION.md`'s existing
override rule rather than inventing a new authority mechanism.

**Regression/blast-radius risk:** low. Documentation-only change to one
granular Knowledge file plus its regenerated bundle; no schema, executable
code, or validator changed; no existing routing row removed or reworded.

**Rollback:** revert the two changed files
(`ChatGPT/[LLM]/Knowledge/MODEL_ROUTING.md`,
`ChatGPT/[LLM]/Knowledge_Bundles/LLM_01_ROUTING_AND_MODEL_SELECTION.md`) and
rerun `python3 scripts/build_knowledge_bundles.py --write` to restore the
prior bundle fingerprint.

**Acceptance criteria:** escalation ladder is stepwise and bounded (no skip);
explicit escalation triggers and explicit abstention triggers both stated;
authority boundary preserved (no self-acceptance, no override of deterministic
checks); `python3 scripts/check_knowledge_bundles.py` and
`python3 scripts/build_knowledge_bundles.py --check` pass — both observed
`PASS` (see Validation below).

---

## Direction 2 — Dynamic / selective context

**Existing mechanism found:** `docs/standards/CONTEXT_PACK_STANDARD.md`
("should contain the context needed for the next decision or output, not
every available file... do not dump all files... use curated context");
`.agents/skills/project-context/SKILL.md` (loads only the one resolved
capability's bounded pack, records included files with selection reasons and
excluded candidates with reasons, verifies every selected path exists, stops
when there is enough context to act); and
`docs/standards/BOUNDED_PROJECT_CONTEXT_FRESHNESS.md`'s `required_knowledge`
field (mandatory, schema-enforced list of governance/knowledge files a
capability must expose, with a `repo_only`/`bundle`/`project_instructions`/
`external` delivery guarantee and a `BLOCKED_UNDECLARED` result if a
`schema_version: 3` capability omits the declaration — silence is never
mistaken for "nothing required").

**Gap:** none demonstrated. The repository already implements exactly the
`goal → route → select minimum required context → execute` pattern the issue
asks for, already separates "curated" from "load everything," and already has
a mandatory-context guarantee that prevents silently omitting required
governance content (the issue's own acceptance criterion for this direction).

**Classification:** `already_covered`.

**Verdict:** **reject** — implementing a new context-selection subsystem here
would duplicate `CONTEXT_PACK_STANDARD.md` / `project-context` /
`BOUNDED_PROJECT_CONTEXT_FRESHNESS.md` under a new name, which the issue's
non-goals explicitly forbid. No change made.

---

## Direction 3 — Structured failure reflection before retry

**Existing mechanism found (governed/AES path):** `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`
§9 "Defects and the corrective loop" — a 9-value defect `classification`
(`implementation`, `validation`, `test`, `artifact`, `traceability`,
`contract`, `governance`, `authority`, `external_dependency`), a `severity`
model (`recoverable`/`needs_check`/`hard_blocker`, cross-referenced to
`ChatGPT/[Codex]/Knowledge/FAILURE_MODES.md`), and a mandatory sequence
`validate → register defect → classify defect → determine correction
eligibility and authority → apply minimal correction → rerun affected checks
→ ...`. This already forbids fixing before registering/classifying.

**Existing mechanism found (lightweight/local path):** the canonical
`ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md` "Retry policy" and its mirror
in `Codex APP/CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md` — used for local,
non-AES-record Codex CLI/App work, which is common in this repo.

**Gap:** the lightweight/local retry policy only classified *scope*
("local, reversible, inside allowed files") before attempting "one minimal
fix." It did not require naming *why* the check failed before fixing it —
exactly the blind-retry pattern the RIOS-cited tool-interaction research
reports as a source of redundant calls and poor recovery. This is a real,
narrow gap distinct from the AES path, which already has a much richer
defect-classification model.

**Classification:** `needs_strengthening` for the lightweight/local retry
path only; `already_covered` for the governed AES path.

**Verdict:** accept — smallest viable change, scoped to the lightweight path
only, explicitly deferring to the existing AES classification where an AES
record applies (no duplicate classification under a new name).

**Change implemented:** added a diagnosis step to the canonical Retry policy
in `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md` (rebuilt into
`CODEX_02_EXECUTION_AUTONOMY_REPORTING.md`, the one Codex bundle that embeds
this file's content): before attempting a fix, name one of
`tool` / `parameters` / `state` / `assumption` / `dependency` as the
diagnosed cause, using the failing command's actual output as evidence; then
fix that diagnosed cause, not just "try something." Explicitly states this
is a lightweight label for the one-fix budget, not a new control plane, and
that where a full AES record applies, AES's own `classification`/`subtype`
(§9.2) governs instead — no two competing classifications for the same
defect. Mirrored the same diagnose-before-fix step into
`Codex APP/CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md`'s retry policy, which
already referenced scope-classification and now references the canonical
cause-diagnosis step by name instead of duplicating it.

**Regression/blast-radius risk:** low. Documentation-only; does not change
the one-fix budget, does not add a new defect status, does not touch AES
schema/validators. Slightly increases the work required before a retry
(name a cause), which is the intended, bounded behavior change.

**Rollback:** revert `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`, the three
regenerated Codex bundle files, and
`Codex APP/CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md`; rerun
`python3 scripts/build_knowledge_bundles.py --write`.

**Acceptance criteria:** diagnosis step is bounded (5 named categories, one
required before fix); explicitly distinguishes diagnosis from blind retry;
explicitly defers to AES classification when AES applies (no duplicate
control plane); `python3 scripts/check_knowledge_bundles.py` passes — observed
`PASS`.

---

## Direction 4 — Trajectory / original-goal verification (not output-only acceptance)

**Existing mechanism found:** AES §9.5.1 "Trace-grounded repair eligibility"
(a failed execution is evidence of an observed defect, not by itself evidence
that the harness/prompt/skill/workflow caused it; a repair candidate that
changes one of those control surfaces requires a bounded attribution
statement naming the target, the failed trace, the connecting evidence, and
plausible alternatives — enforced by `scripts/validate_autonomous_execution_record.py`
and covered by `tests/test_trace_attribution_contract.py::test_harness_repair_requires_trace_grounded_attribution`,
observed passing in this run); AES §10.3 "Closure Review (v1.1)" (`overall_delivery: pass`
requires reviewing "the original goal rather than the last fix list,"
preserving `NOT_RUN != PASS` / `PROBABLE != CONFIRMED` distinctions, and — for
material/complex/high-risk work — a bounded adversarial attempt to reject
acceptance across explicit classes including "unsupported defaults,"
"aggregation loss," "status inflation," and "forged intermediate state").

**Gap:** none demonstrated. This is precisely the failure mode the RIOS-cited
program-repair research describes (tests pass, patch is semantically wrong) —
and AES v2.0 already has two independent, complementary controls aimed at it:
one gates *repairing the harness itself* on trace-grounded attribution, the
other gates *closure* on reviewing the original goal and adversarially
probing for exactly the "looks done but isn't" failure modes.

**Classification:** `already_covered`.

**Verdict:** **reject** — no new verification layer added. Adding one would
duplicate §9.5.1/§10.3 under a new name.

---

## Direction 5 — Judge/QA independence from evidence/method, not agent count

**Existing mechanism found:** `ChatGPT/[AI OS]/Knowledge/JUDGE_CALIBRATION.md`
already states the exact principle the issue asks for: "Judge is a reviewer,
not truth," and — the operative rule — "Deterministic checks override LLM
judge for calculations, tests, schemas, output contracts, source
traceability, formulas, metric definitions, column names, and business
logic." It also has a "Material-Evidence Integration Gate," a "Judge
Volatility" section (rerun golden cases when judge model class/prompt/rubric
changes; do not silently promote new judge behavior), four bias/reference
golden regression cases (self-preference, language parity, ambiguity
calibration, reference-available precedence), and an explicit "Override Rule."
None of this is agent-count-based; all of it is evidence/method-based
(deterministic check vs. LLM judgment).

**Gap:** none demonstrated. The repository already implements "evidence/
method independence, not agent count" as its stated Judge doctrine, with a
working override rule and a golden-case regression discipline for judge
volatility.

**Classification:** `already_covered`.

**Verdict:** **reject** — no new Judge/QA layer added; Analyst + Judge +
Revisor is not treated as independent evidence anywhere inspected, and the
existing override rule already subordinates judge opinion to deterministic
checks. Implementing anything further here would duplicate
`JUDGE_CALIBRATION.md` under a new name.

---

## Summary table

| # | Direction | Classification | Verdict | Change |
|---|---|---|---|---|
| 1 | Adaptive model escalation | needs_strengthening | accept | `MODEL_ROUTING.md` + bundle |
| 2 | Dynamic context selection | already_covered | reject | none |
| 3 | Structured failure reflection | needs_strengthening (lightweight path only) | accept | `AUTONOMY_POLICY.md` + bundles + `CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md` |
| 4 | Trajectory/original-goal verification | already_covered | reject | none |
| 5 | Judge/QA independence | already_covered | reject | none |

Three of five directions are rejected as already adequately covered, per the
issue's own explicit instruction to reject rather than force implementation.
This is a complete, valid outcome under the issue's acceptance criteria, not
a partial result.

## Files changed

- `ChatGPT/[LLM]/Knowledge/MODEL_ROUTING.md` — added "Adaptive escalation".
- `ChatGPT/[LLM]/Knowledge_Bundles/LLM_01_ROUTING_AND_MODEL_SELECTION.md` —
  regenerated (`scripts/build_knowledge_bundles.py --write`).
- `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md` — added diagnose-before-fix
  step to Retry policy.
- `ChatGPT/[Codex]/Knowledge_Bundles/CODEX_02_EXECUTION_AUTONOMY_REPORTING.md`
  — regenerated (this is the one Codex bundle that embeds
  `AUTONOMY_POLICY.md`'s content via `## From:`; `CODEX_01_TASKS_AND_HANDOFF.md`
  and `CODEX_05_AGENT_REFERENCES.md` only reference it by name and were
  unaffected).
- `Codex APP/CODEX_APP_ULTRA_LONG_RUN_PROTOCOL.md` — retry policy now
  references the canonical diagnose-before-fix step instead of a shallower
  local duplicate.
- `docs/knowledge_bundle_provenance_audit.json` /
  `docs/knowledge_bundle_provenance_audit.md` — regenerated
  (`scripts/audit_bundle_provenance.py --write`) so committed audit
  artifacts match the rebuilt bundle fingerprints; required for
  `tests/test_audit_bundle_provenance.py::test_check_mode_rejects_stale_committed_artifacts`
  to pass.
- `docs/evidence/README.md` — pointer to this record.

No CODEOWNERS-protected path (`AGENTS.md`, `CLAUDE.md`, `GOAL_MODE.md`,
`MASTER_STATUS.md`, `CURRENT_STATUS.md`, `SYNC_CONTRACT.md`, `scripts/`,
`tests/`, `.github/`, any `PROJECT_INSTRUCTIONS.md`) was touched. All changed
files are granular Knowledge files, their generated bundles, one Codex-App
operating doc, and one generated audit artifact — none of them on that list.

## Validation (observed, real output)

```text
$ python3 scripts/build_knowledge_bundles.py --check
(exit 0 after --write; bundles match source fingerprints)

$ python3 scripts/check_knowledge_bundles.py
Summary:
- projects checked: 7
- bundles checked: 33
- upload files max: 7
- failed: 0

$ python3 scripts/check_manifest_paths.py
Summary:
- checked: 189
- passed: 189
- failed: 0

$ python3 scripts/check_index_coverage.py
Index coverage pairs checked: 9
Failed: 0

$ python3 scripts/check_project_instructions_length.py
Checked PROJECT_INSTRUCTIONS.md files: 7
Passed: 7
Failed: 0

$ python3 scripts/check_repo_public_safety.py
Public safety check passed.

$ python3 scripts/check_codex_goal_mode_defaults.py
Codex Goal Mode atomic-default occurrences checked: 23
Failed: 0

$ python3 scripts/audit_bundle_provenance.py --write && python3 scripts/audit_bundle_provenance.py --check
WROTE
PASS

$ python3 -m pytest -rA -q
635 passed
```

All checks were run against this branch's working tree after the changes
above; none were inferred.

## Evidence states

- delivery: `pass` for the two accepted, implemented directions (1 and the
  lightweight-path part of 3); `pass` (by rejection, per the issue's own
  acceptance criteria) for directions 2, 4, 5.
- tests: `pass` (635/635, real output above).
- review: `not_run` — owner review pending; this PR is not self-merged.
- authority: `not_required` for the documentation changes made (no schema,
  business-logic, formula, metric, or output-contract touched); `pending`
  for owner acceptance of the overall analysis and disposition.

## Residual risks

- The "Adaptive escalation" and "diagnose before fixing" additions are
  documentation contracts, not enforced by a validator; an executor could
  still skip them. This matches the existing pattern for most AES/Retry-policy
  prose in this repo (advisory unless a specific validator is later added) and
  is not a new class of risk.
- Rejecting directions 2, 4, 5 relies on this analysis being an accurate
  reading of current mechanisms; if repository evidence is later found to
  contradict this (per the issue's own revisit triggers), the rejection
  should be revisited, not treated as final.

## Rollback

Revert the commit(s) touching the files listed above; rerun
`python3 scripts/build_knowledge_bundles.py --write` and
`python3 scripts/audit_bundle_provenance.py --write` to resynchronize
bundles/audit artifacts with the reverted sources.
