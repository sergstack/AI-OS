# LLM Cross-Project Live Eval Report

Date: 2026-08-21
Branch: `codex/llm-cross-project-live-eval`
Matrix: `LLM-XPROJECT-LIVE-001` / `1.0.0-candidate`
Delivery status: `PARTIAL`
Production status: `NOT AUTHORIZED`

## Outcome

The first comparable seven-project LLM boundary matrix now exists and two
cases completed in the ChatGPT in-app browser. `[Inbox Router]` passed with
9/10: it selected `[LLM]` with strong confidence, produced a bounded handoff,
and did not solve the target prompt/model/eval workflow itself.

`[AI OS]` scored 5/10 and reproduced a boundary defect: it correctly stated
`[AI OS] → [LLM]`, preserved evidence governance, then selected the model class
and designed the LLM workflow itself instead of returning a compact handoff.

`[LLM]` scored 9/10 with a `REVISE` verdict. The asset was complete and safe,
but its visible content was 3,528 characters, 28 above the explicit cap. The
hard-cap correction then passed 10/10 at 3,389 characters, with every requested
control preserved and 111 characters of buffer.

AI OS correction reruns removed the ownership violation. A later 1,800-character
handoff cap was an over-correction: it risked discarding execution context that
the receiving LLM needs. That arbitrary cap has been rolled back in AI OS and
Thinking. The replacement preserves a focused, executable handoff with relevant
context, acceptance criteria and next step, without asking the source project to
perform LLM work. The external settings were synchronized and read back exactly;
the clean live retry is `NOT RUN` because ChatGPT again showed the rate-limit
dialog before prompt submission.

The other four cases do not have a behavioral verdict. ChatGPT applied a
temporary account-level request limit. `[Analytics]` began a response but it
ended mid-word after 4,620 visible characters, so its apparent scope crossing
is diagnostic only and not scored. `[Codex]` also named `[LLM]` correctly and
then began writing the prompt before its answer was interrupted; this remains
diagnostic only. `[LLM]` rejected the submitted request without creating a
conversation; `[Thinking]` displayed the same dialog before submission.
`[Thinkers OS]` also named `[LLM]` correctly and preserved provenance before
starting the foreign prompt/model work; its answer was interrupted and remains
unscored.

## Evidence separation

| Evidence layer | Result | What it proves |
|---|---|---|
| Latest completed live state | 2 pass, 1 revise, 4 not run | Inbox Router and corrected LLM pass; AI OS focused-handoff rollback awaits a clean live retry |
| Repository contract review | present in 7/7 Project Instructions | intended LLM ownership and handoff boundaries |
| Contract test | pass | matrix version, seven-case coverage, gate fields and honest partial state |

Repository instructions for all seven Projects contain the expected static
boundary: LLM prompts/model routing/workflows belong to `[LLM]`, while domain
facts, calculations, sources, decisions and implementation stay with their
owners. This is supporting evidence only; it is not substituted for the four
missing live responses.

## Findings

1. AI OS reproduces an ownership-boundary defect after correctly identifying
   `[LLM]` as the owner.
2. Inbox Router's handoff is operationally complete, but it describes the
   downstream eval without naming `LLM-OUTPUT`; this is a minor discoverability
   gap, not a routing failure.
3. LLM preserves every requested control and the explicit pre-send hard cap
   corrected the 28-character overrun without functional loss.
4. The previous static smoke report could not express partial live coverage.
   It now separates static `pass` from live `partial`.
5. The LLM project previously had no versioned cross-project regression matrix.
   The new controlled matrix supplies exact prompts, gates, scoring, evidence
   fields and rerun triggers.

## Changes made

- added the versioned seven-project live-eval matrix;
- added a contract test for matrix coverage and partial-state honesty;
- added the matrix to the LLM setup and status inventory;
- updated LLM smoke QA to report the latest two pass, one revise and four `NOT RUN` state;
- implemented evidence-backed ownership corrections and rolled back only the
  arbitrary AI OS/Thinking length caps;
- synchronized AI OS, Thinking and LLM instruction files to their external
  Projects with exact settings read-back;
- completed two AI OS correction reruns and stopped after the third attempt was
  interrupted, preserving the AES correction limit.

## Required continuation

After the ChatGPT request limit clears, run only the four `NOT RUN` prompts in
fresh chats without changing project sources between cases. AI OS and Thinking
need one clean focused-handoff rerun; their external settings already match the
repository.
The LLM correction is validated and should not be rerun unless its contract or
UI-visible citation behavior changes. Score every completed response with the
same rubric and make no other behavioral correction without a reproduced
defect.

## Acceptance

- matrix and evidence traceability: pass;
- latest completed live state: two pass, one revise, four not run;
- full seven-project live baseline: partial;
- AI OS ownership correction: verified;
- AI OS/Thinking arbitrary compactness caps: rolled back; focused-handoff live rerun pending;
- LLM hard-cap correction: pass, 10/10;
- production promotion: not authorized.
