# AES Cross-Project Pilot (Phase 5 — not executed)

Status: specification only. This pilot is not executed by this Phase 1
task and is not authorized by Phase 1 completion
(`AUTONOMOUS_EXECUTION_STANDARD.md` Section 20).

## Goal

Run a real multi-hop handoff chain under AES tracking, for example:

```text
[Thinking] -> [Analytics] -> [Codex] -> Judge
```

## Must verify persistence across every hop

- execution ID;
- parent execution ID;
- requirement IDs;
- defect IDs;
- iteration count;
- evidence references;
- acceptance scopes;
- authority status.

This mirrors the illustrative shape in
`docs/autonomous_execution/examples/cross_project_handoff.json`, but this
pilot must use a real task, not a fabricated example.

## Constraints

- Each hop uses that project's own existing handoff mechanism
  (`ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`,
  `ChatGPT/[Analytics]/Knowledge/ROUTING_AND_HANDOFF.md`,
  `ChatGPT/[Thinking]/Knowledge/ROUTING_AND_HANDOFF.md`) plus the AES
  handoff record shape (`AUTONOMOUS_EXECUTION_STANDARD.md` Section 15).
- No project's methodology is rewritten or merged into another's; AES adds
  tracking, not a new workflow.
- No automatic issue/PR creation, approval, or merge as part of the pilot
  itself (Section 17 non-goals still apply).

## Deliverables (Phase 5, separate issue/PR)

1. One real chained execution record set (parent + child executions) with
   at least two `handoff` entries.
2. Confirmation, hop by hop, that none of the eight tracked items above
   were dropped.
3. A short pilot report on any gap between the canonical handoff contract
   and what each project's existing handoff practice actually preserves
   today.

## Acceptance for the pilot itself

- Every handoff record includes `execution_id`, `requirement_ids`, and
  `authority_status`.
- A new execution ID appears only where an explicit parent/child link is
  recorded, per `AUTONOMOUS_EXECUTION_STANDARD.md` Section 15.
- The final authority/merge/production statuses at the end of the chain
  are still reported separately, not collapsed into one value.
