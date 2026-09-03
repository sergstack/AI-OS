# [Thinking] Decision Log

Rows prefixed `AIOS-` are `[AI OS]` repo-governance decisions, mirrored here
because no dedicated `[AI OS]`-owned decision-log artifact exists yet
(revision review 2026-09-03, `docs/evidence/PROJECT_WIDE_REVISION_REVIEW_2026-09-03.md`
flagged this as scope creep to fix on the `[AI OS]` side — this note marks
them as an intentional cross-reference in the meantime, not `[Thinking]`'s
own decisions). Rows prefixed `TH-` are genuine `[Thinking]` decisions.

| Decision ID | Date | Decision | Status | Confidence | Owner | Revisit trigger | Next review | Handoff | Accepted by | Acceptance evidence | Supersedes | Superseded by | Outcome | Link |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-2026-05-25-01 | 2026-05-25 | Add standalone status, QA, decision, and revisor governance files for [Thinking] | recommended | strong | Sergey / Thinking Lead | new data; routing conflict; judge/revisor failure; smoke QA fail | on next governance update | none | Sergey | `SMOKE_QA_RESULTS.md` pass | none | none | active | `CURRENT_STATUS.md` |
| TH-2026-06-26-01 | 2026-06-26 | Adopt Karpathy-inspired minimal verifiable loop as candidate anti-bloat review pattern. Start in [LLM] prompt registry and [Thinking] judge check. Do not implement as repo-wide mode. | candidate decision | medium | Sergey / Thinking Lead | 3 pilot cases fail; prompt adds complexity; routing conflict; Codex task proposed without acceptance; user stops using it | After 3 pilot cases | [LLM] for prompt; [Thinking] for judge; [AI OS] only after candidate evidence; [Codex] only after task package | pending | no pilot evidence yet | no new folder / no automation / no routing changes | none | candidate |  |
| AIOS-2026-06-15-03 | 2026-06-15 | Add manifest and path consistency validator | accepted | medium-strong | Sergey / AI-OS | Docs Safety fail; manifest/path validator false positive; path governance drift | on next governance update | PR #28 | Sergey | PR #28 merged; Docs Safety pass; manifest/path validator 103/103 pass; negative smoke passed | none | none | active | https://github.com/sergstack/AI-OS/pull/28 |
| AIOS-2026-06-15-04 | 2026-06-15 | Add pilot case framework and ChatGPT Project sync checklist | accepted | strong | Sergey | new ChatGPT Project added; Project Instructions changed; Knowledge upload policy changed; smoke QA fail; pilot case fail; production promotion requested | on next governance update | PR #29 | Sergey | PR #29 merged; docs-safety pass; length/safety/manifest validators pass; no PROJECT_INSTRUCTIONS.md or governed Knowledge files changed | none | none | active | https://github.com/sergstack/AI-OS/pull/29 |
