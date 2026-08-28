# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[LLM]/Knowledge_Bundles/LLM_03_QUALITY_GATES_AND_EVAL.md`.

## Legacy section: `ChatGPT/[LLM]/Knowledge/SMOKE_QA_FOR_LLM.md`

| `[AI OS]` → `[LLM]` | blocked, 5/10 | route named correctly, but `[AI OS]` selected the model class and designed the workflow instead of handing off |
| `[LLM]` compact asset | revise, 9/10 | safe complete asset exceeded the 3,500-character cap by 28 visible content characters |
- one reproduced LLM compactness defect;

## Legacy section: `ChatGPT/[LLM]/Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md`

- matrix_id: `LLM-XPROJECT-LIVE-001`
- version: `1.0.0-candidate`
- owner_project: `[LLM]`
- status: `optimization_partial`
- production_status: `NOT AUTHORIZED`
The matrix uses one exact prompt for each of the seven ChatGPT Projects and
scores route correctness, scope boundary, handoff completeness, evidence/QA
preservation and compact operability. A rate limit, authentication loss or
ambiguous Project identity is recorded as `NOT RUN`, not fail.
Observed baseline: `[Inbox Router]` passed 9/10 with one strong route to
`[LLM]`, a bounded handoff and no target-workflow solution. `[AI OS]` scored
5/10: it named `[LLM]` as owner, then selected the model class and designed the
workflow itself. `[Analytics]`, `[Codex]` and `[Thinkers OS]` produced partial
diagnostic fragments before the rate-limit dialog interrupted generation;
`[Thinking]` did not produce a response. `[LLM]` completed at 3,528 visible
content characters and remains `REVISE` against its 3,500 cap. The four
incomplete cases remain `NOT RUN`. Overall baseline status: `PARTIAL`.
AI OS corrective evidence: two completed reruns fixed ownership; response size
fell from 4,794 to 2,475 characters but remains above the compact target. A
third rerun was interrupted and is `NOT RUN`. The synchronized `[LLM]` hard-cap
rule passed its completed post-change rerun at 3,389 visible characters with
all requested controls preserved.
## Autonomous Execution Standard
Execution in `[LLM]` now also follows the canonical Autonomous Execution
Standard defined in `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` at the repo root
(canonical owner: `[AI OS]`). It sits above the output QA, hallucination
checks, and judge/eval workflow above as a shared execution/validation/
defect/acceptance loop, without replacing them or the merge policy in
`GOAL_MODE.md`. No `[LLM]`-specific AES extension exists yet; only the
canonical standard is in scope here. New v2 Closure Review rechecks prompt and
input-context contracts, output schema, unsupported claims, eval regressions,
and routing ownership before acceptance.
For an `Invoke AI-OS` continuation, the canonical AES envelope preserves the
original goal, acceptance criteria, resolved owner, stage, and freshness
state; it does not replace LLM quality gates, eval evidence, or owner review.
After routing resolves a material decision or deliverable owner, `[LLM]` may
preserve evidence, contradictions, constraints, and a bounded handoff, but it
must not silently substitute its judgment for the resolved owner.

## Legacy section: `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`

- workflow: risk-triggered memo review
- registry status: active
- owner acceptance: accepted on 2026-08-18
- corpus: 10 real memo cases from one workbook and period `2026-05`
- case mix: routine 4, material 2, evidence-sensitive 2, QA-defect 1, Judge-defect 1
- quality: OLD 154/160; NEW 154/160
- blind verdict: equivalent 10/10
- false bypass count: 0
- Judge runs: 10 -> 6 (40% reduction)
- Revise runs: 10 -> 2 (80% reduction)
- semantic LLM stages: 30 -> 18 (40% reduction)
- workflow quality: PASS
- safety: PASS
- logical execution efficiency: PASS
- token savings: NOT PROVEN
- billing savings: NOT PROVEN
- generalization beyond the current corpus: NOT PROVEN
- one real workbook and one period, `2026-05`
- frozen drafts; review-loop tested, not draft-generation variability
- blind Judge used the current environment model, not an independent model
- provider-level token usage unavailable
- elapsed-time attribution unavailable
The accepted memo workflow does not resolve the separate legacy prompt-eval debt.
- Reusable prompt entries are legacy/unversioned and have no recorded eval or owner-acceptance evidence. Priority migration debt is listed in `PROMPT_REGISTRY.md`; no eval pass is inferred.
- Cross-project live coverage is partial: `[Inbox Router]` passed; `[AI OS]` reproduced a scope-boundary defect that was fixed in two completed reruns. Its later arbitrary compactness cap was rolled back in favour of a focused executable handoff; the clean rerun is `NOT RUN` under the ChatGPT account-level request limit. `[LLM]` passed the corrected explicit hard cap at 3,389 visible characters; four baseline cases remain `NOT RUN`.
- External AI OS, Thinking and LLM Project Instructions match the corrected repository files by exact settings read-back.
- LLM post-change validation passed 10/10 at 3,389 visible content characters, preserving the prompt, gates, registry and handoffs with 111 characters of buffer under the explicit maximum.
- Rerun the synchronized `[AI OS]` focused-handoff rule after a clean cooldown; do not change it without a completed reproduced defect.
- Complete the four `NOT RUN` cases in `CROSS_PROJECT_LIVE_EVAL_MATRIX.md` after the ChatGPT rate limit clears; use only completed responses to justify additional Project Instruction changes.
- Migrate priority reusable prompts to identifiable candidate revisions and run risk-appropriate evals before any new activation decision.
