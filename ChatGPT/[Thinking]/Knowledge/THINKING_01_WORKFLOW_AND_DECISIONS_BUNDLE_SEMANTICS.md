# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Thinking]/Knowledge_Bundles/THINKING_01_WORKFLOW_AND_DECISIONS.md`.

## Legacy section: `ChatGPT/[Thinking]/Knowledge/DECISION_MEMO_TEMPLATE.md`

## Autonomous Execution Standard
Execution in `[Thinking]` now also follows the canonical Autonomous
Execution Standard defined in `AUTONOMOUS_EXECUTION_STANDARD.md` at the repo
root (canonical owner: `[AI OS]`). It connects the frame -> facts -> options
-> decision -> handoff workflow above into the shared execution/validation/
defect/acceptance loop without replacing decision status tracking or the
merge policy in `GOAL_MODE.md`. No `[Thinking]`-specific AES extension exists
yet; only the canonical standard is in scope here. New v2 Closure Review rechecks the
original question, assumptions, alternatives, unsupported conclusions,
downside, and owner boundary; it does not make a downstream owner decision.
When an `Invoke AI-OS` continuation applies, its durable AES envelope preserves
the original acceptance boundary and owner/stage; warm resume requires the
envelope to remain valid, not merely an unchanged revision.
When routing resolves `[Thinking]` as the owner of a material decision, an
upstream project may supply evidence, contradictions, options, risks, and a
bounded handoff, but it must not silently make or approve the decision in
`[Thinking]`'s place.
