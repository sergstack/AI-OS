# AES Artifact-Freshness Pilot (Phase 3 — not executed)

Status: specification only. This pilot is not executed by this Phase 1
task and is not authorized by Phase 1 completion
(`AUTONOMOUS_EXECUTION_STANDARD.md` Section 20).

## Goal

Demonstrate the artifact-freshness contract
(`AUTONOMOUS_EXECUTION_STANDARD.md` Section 11.3) end to end:

```text
generate -> validate -> detect defect -> fix source -> regenerate
-> validate final artifact -> compare source revision
```

## Candidate artifact types

DOCX, XLSX, PDF, PPTX, or another deterministic generated artifact already
produced somewhere in this repository's tooling (e.g. an Analytics memo or
a StreamDeck export bundle) — chosen during Phase 3 scoping, not fixed here.

## Constraints

- Use a real generation pipeline that already exists in the repository;
  do not build a new generator just for the pilot.
- The seeded defect must be a real, reproducible mismatch between source
  input and generated output (e.g. a stale formula), not a fabricated one
  used only to pad the demonstration.
- Rollback must retain the prior artifact version through git history.

## Deliverables (Phase 3, separate issue/PR)

1. One real execution record demonstrating: `artifact.generated_from_revision`
   at the first (stale) generation, a registered `artifact` or
   `traceability`-classified defect, a source fix, regeneration, and a
   final artifact record with `freshness_status: current`.
2. Confirmation that `source_inputs[].content_hash` on the final artifact
   record matches the actual final source content.
3. A short pilot report identifying any gap between the canonical
   freshness contract and what was actually observable/measurable for the
   chosen artifact type.

## Acceptance for the pilot itself

- The first artifact is honestly recorded as `stale`, not silently skipped.
- The regenerated artifact's `generated_from_revision` matches the final
  source revision.
- `overall_delivery: pass` is only asserted once the final artifact is
  `current`, per the artifact-freshness rule in Section 11.3 of the
  standard.
