# Response Quality Live Pilot Report

Date range: 2026-08-24 to 2026-08-25
Initial pilot branch: `codex/response-quality-live-pilots`
Related deterministic harness: PR [#274](https://github.com/sergstack/AI-OS/pull/274), merged at `d31b949`
Delivery status: `CANDIDATE`
Production status: `NOT AUTHORIZED`

## Scope and evidence handling

Three supervised, non-sensitive prompts were sent in the ChatGPT `[Codex]`
Project. Each explicitly prohibited external actions. This report records only
the requested controls, observed control presence, verdict and available chat
reference. It intentionally stores neither raw provider responses nor response
hashes, so it is not a reproducible content archive.

The deterministic harness validates the corresponding fixture contracts. A
live observation validates only the visible response for that single run; it
does not establish stable model behaviour.

## Results

| Pilot | Response class | Observed controls | Independent Judge | Status | Chat reference |
| --- | --- | --- | --- | --- | --- |
| `LIVE-RQE-DIRECT-001` | direct | Required answer and limitation markers were present; the response stated that execution and production readiness were not performed. | Not required by this class. | `pass` | [ChatGPT conversation](https://chatgpt.com/g/g-p-69f7c5794ab481919143830fc1a513b9-codex/c/6a8c64d7-1664-83ed-b4c7-bb24c7ca9431) |
| `LIVE-RQE-EVIDENCE-001` | evidence-sensitive | Required facts, interpretation and limitations markers were present; the response did not promote inference to observed fact. | Required; not run. | `blocked` | [ChatGPT conversation](https://chatgpt.com/g/g-p-69f7c5794ab481919143830fc1a513b9-codex/c/6a8c64f9-1748-83eb-a8c5-68a19c482123) |
| `LIVE-RQE-CODEX-001` | Codex handoff | Required objective, acceptance and rollback markers were present; the response retained the no-owner-review/no-merge constraint. | Required; not run. | `blocked` | Not recorded; raw response intentionally not retained. |

## Fresh material pilot

On 2026-08-25, both canonical Projects exposed enabled composers. The two
material classes were rerun in fresh chats and each response was judged in the
independent `[LLM]` Project within the same supervised session. Raw responses
were not retained in this report.

| Pilot | Response class | Deterministic controls observed | Independent Judge | Status | Run references |
| --- | --- | --- | --- | --- | --- |
| `LIVE-RQE-EVIDENCE-002` | evidence-sensitive | Required fact, interpretation and limitation markers were present; no inference was presented as observed fact. | `pass`; material findings: none; required revision: none. | `pass` | [response](https://chatgpt.com/g/g-p-69f7c5794ab481919143830fc1a513b9/c/6a8cb3b8-fa90-83eb-a8d6-65e8d77611ca); [Judge](https://chatgpt.com/g/g-p-69e9f1058440819181beb1f41cfd672c/c/6a8cb3f0-8f10-83eb-be90-70192ffced9a) |
| `LIVE-RQE-CODEX-002` | Codex handoff | Required objective, acceptance and rollback markers were present; owner review and merge were explicitly `NOT RUN`. | `pass`; material findings: none; required revision: none. | `pass` | [response](https://chatgpt.com/g/g-p-69f7c5794ab481919143830fc1a513b9/c/6a8cb40c-da7c-83eb-8a9b-3ddf7477e45f); [Judge](https://chatgpt.com/g/g-p-69e9f1058440819181beb1f41cfd672c/c/6a8cb42b-b614-83eb-abb2-0197ed1a4b4b) |

## Closure

The initial live pilot supplies one positive observation for the direct-response
contract. Its two material records remain blocked because the independent Judge
step was not performed. This is the intended fail-safe outcome: required review
cannot be inferred from a structurally compliant response or from a successful
live submission.

The fresh material pilot adds one independently judged `pass` observation for
each material class. It does not retroactively change the historical `001`
records, establish stable model behaviour, or authorize production use.

## Judge access attempt

On 2026-08-24, the two material chat references were opened from both the
in-app and signed-in browser surfaces to run the independent Judge. Each
reference showed an empty, disabled conversation view, not the original
response. Because this report intentionally retains no raw provider transcript,
there was no admissible input for a substitute review. No Judge verdict was
created; both material cases remain `blocked`.

## Fresh access smoke

On 2026-08-25, a fresh access smoke repeated the first required condition for
the material-class rerun. The canonical `[Codex]` Project URL again opened an
empty temporary-chat view with no enabled composer. The run stopped before
opening `[LLM]`: an independent Judge is not a substitute for an inaccessible
target surface. No prompt, response, Judge input or verdict was created.

No owner acceptance, deployment, production-readiness decision, source update
or merge decision is evidenced by this report.

## Required continuation

1. Obtain an owner decision on whether this three-class candidate baseline is
   sufficient for `ready for owner review`.
2. Rerun the affected class only when its Project instructions, quality contract
   or evaluation harness changes; keep the same-session Judge boundary.
3. Do not infer a release gate or production readiness from these three pilot
   observations.

## Rollback

Revert the commits that introduce or amend this report. The report changes no
runtime, project source, schema, routing or evaluation policy.
