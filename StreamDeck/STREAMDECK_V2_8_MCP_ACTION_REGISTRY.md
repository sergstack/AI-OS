# StreamDeck v2.8 MCP Action Registry

Status: registry pilot / candidate-only
Profile targeted: `MCP Actions`
Source profile: `AI OS StreamDeck v2.8 Candidate`
Safety mode: supervised only
Promotion status: candidate only

## Purpose

This registry defines a small supervised MCP Actions pilot for StreamDeck v2.8.

The pilot moves from MCP server connectivity evidence to a documented action layer that ChatGPT or Codex can list and execute safely after Sergey manually creates the actions in the Stream Deck `MCP Actions` profile.

This file does not claim that actions were created or executed unless recorded in the QA section below.

## Registry

| action_id | title | owner project | safe_to_execute | requires_confirmation |
|---|---|---|---:|---:|
| `AIOS_HOME_JUDGE` | HOME Judge | `[LLM]` / Judge | yes | yes |
| `AIOS_HOME_REVISOR` | HOME Revisor | `[LLM]` / Revisor | yes | yes |
| `AIOS_HOME_SYNC` | HOME Sync | `[Codex]` | yes | yes |
| `AIOS_KB_SOURCE_TRUTH` | KB Source Truth | `[AI OS]` | yes | yes |
| `AIOS_LOCAL_AI_SAFETY` | Local AI Safety | `[LLM]` / Local AI | yes | yes |
| `AIOS_CODEX_ISSUE_TO_PR` | Codex Issue to PR | `[Codex]` | yes | yes |
| `AIOS_AI_TREND` | AI Trend | `[AI OS]` | yes | yes |

Safe to execute means safe only under the constraints in this file: supervised, text-only, auto-send disabled, candidate-only, no destructive actions, and human acceptance required.

## Action Details

### `AIOS_HOME_JUDGE`

- Title: HOME Judge
- Description: Inserts the v2.8 HOME JUDGE prompt for a pass / revise / blocked verdict.
- Owner project: `[LLM]` / Judge
- Allowed input: last meaningful message, selected text, or material pasted by Sergey.
- Forbidden actions: destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, autonomous agents.
- Expected output: verdict, reason, required fixes, unsupported or weak claims, checks observed, residual risks, next action.
- safe_to_execute: yes, if configured as text-only with auto-send disabled.
- requires_confirmation: yes.
- Smoke QA check: execute through MCP and confirm it inserts or returns the HOME JUDGE prompt only.
- Residual risk: active app focus may affect where inserted text lands.

### `AIOS_HOME_REVISOR`

- Title: HOME Revisor
- Description: Inserts the v2.8 HOME REVISOR prompt to revise using Judge notes without adding new facts.
- Owner project: `[LLM]` / Revisor
- Allowed input: draft text, Judge notes, selected text, or material pasted by Sergey.
- Forbidden actions: destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, autonomous agents.
- Expected output: revised version, applied Judge notes, facts preserved, claims removed or softened, blocked items.
- safe_to_execute: yes, if configured as text-only with auto-send disabled.
- requires_confirmation: yes.
- Smoke QA check: execute through MCP and confirm it inserts or returns the HOME REVISOR prompt only.
- Residual risk: the revisor can over-smooth missing evidence unless the prompt's no-new-claims boundary is preserved.

### `AIOS_HOME_SYNC`

- Title: HOME Sync
- Description: Inserts the v2.8 HOME SYNC prompt for repo, branch, main, working tree, and check alignment.
- Owner project: `[Codex]`
- Allowed input: repo state request, PR/task context, selected text, or material pasted by Sergey.
- Forbidden actions: destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, autonomous agents.
- Expected output: repo, current branch, main/remote status, working tree, checks to run, mismatch status, required action, PR need, risks.
- safe_to_execute: yes, if configured as text-only with auto-send disabled.
- requires_confirmation: yes.
- Smoke QA check: execute through MCP and confirm it inserts or returns the HOME SYNC prompt only; no git command should run from the Stream Deck action.
- Residual risk: users may treat the inserted prompt as a command result unless the assistant runs and reports checks separately.

### `AIOS_KB_SOURCE_TRUTH`

- Title: KB Source Truth
- Description: Inserts the v2.8 KB Source Truth prompt to identify source-of-truth and bundle/source sync needs.
- Owner project: `[AI OS]`
- Allowed input: source file, Knowledge bundle file, upload list, manifest, selected text, or material pasted by Sergey.
- Forbidden actions: destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, autonomous agents.
- Expected output: summary, facts used, assumptions, risks, next step.
- safe_to_execute: yes, if configured as text-only with auto-send disabled.
- requires_confirmation: yes.
- Smoke QA check: execute through MCP and confirm it inserts or returns the KB Source Truth prompt only.
- Residual risk: source and Knowledge bundle drift may require repo inspection before any conclusion is treated as verified.

### `AIOS_LOCAL_AI_SAFETY`

- Title: Local AI Safety
- Description: Inserts the v2.8 Local AI safety judge prompt for candidate-only local AI output review.
- Owner project: `[LLM]` / Local AI
- Allowed input: non-sensitive or explicitly sanitized local AI output, selected text, or material pasted by Sergey.
- Forbidden actions: destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, financial raw data, production data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, autonomous agents.
- Expected output: verdict, safety boundary, sensitive data risk, unsupported claims, next step.
- safe_to_execute: yes, if configured as text-only with auto-send disabled and only sanitized input is used.
- requires_confirmation: yes.
- Smoke QA check: execute through MCP and confirm it inserts or returns the Local AI safety prompt only.
- Residual risk: sensitive data can be pasted by mistake; this action must remain supervised and candidate-only.

### `AIOS_CODEX_ISSUE_TO_PR`

- Title: Codex Issue to PR
- Description: Inserts the v2.8 Codex Issue -> PR prompt for minimal branch, checks, and draft PR work from a GitHub issue.
- Owner project: `[Codex]`
- Allowed input: GitHub issue URL, issue body, handoff package, selected text, or material pasted by Sergey.
- Forbidden actions: destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, autonomous agents, auto-merge.
- Expected output: branch, files inspected, files changed, checks, PR needed, human review, no-auto-merge status.
- safe_to_execute: yes, if configured as text-only with auto-send disabled.
- requires_confirmation: yes.
- Smoke QA check: execute through MCP and confirm it inserts or returns the Codex Issue -> PR prompt only; no branch, commit, push, or PR should be created by the Stream Deck action itself.
- Residual risk: downstream Codex work may modify files and open a PR after human-directed execution; no auto-merge remains mandatory.

### `AIOS_AI_TREND`

- Title: AI Trend
- Description: Inserts the v2.8 AI TREND prompt for AI topic triage and hype filtering.
- Owner project: `[AI OS]`
- Allowed input: AI topic, release note, tool, link, question, selected text, or material pasted by Sergey.
- Forbidden actions: destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, autonomous agents, automatic live web checks.
- Expected output: adopt / watch / ignore / investigate verdict, what changed, supported claims, weak claims, unsupported claims, Sergey relevance, risks, next step.
- safe_to_execute: yes, if configured as text-only with auto-send disabled.
- requires_confirmation: yes.
- Smoke QA check: execute through MCP and confirm it inserts or returns the AI TREND prompt only and asks before live web checks.
- Residual risk: AI product facts can be volatile; fresh checking requires explicit approval and source citation.

## Manual Setup

Manual setup is required because the Elgato MCP server exposes executable actions, not full profile-authoring operations.

1. Open the Stream Deck desktop app.
2. Confirm the active v2.7 profile remains present and is not overwritten.
3. Open or create the Stream Deck `MCP Actions` profile.
4. For each registry entry, add a safe action that exposes the exact `action_id`.
5. Use the matching v2.8 prompt text from `StreamDeck/AIOS_StreamDeck_Setup_Instruction_v2.8_COMMAND_SURFACE_ALIGNED.md`.
6. Configure each action as text-only or MCP-safe prompt insertion.
7. Keep auto-send disabled for every action.
8. Do not add delete, send, merge, publish, deploy, secret, production, autonomous retrieval, vector DB, semantic search, embeddings, production web UI, or autonomous-agent actions.
9. Save the profile.
10. In Codex, run `streamdeck__get_executable_actions` and compare the visible action IDs with this registry.
11. Execute only 1-2 safe smoke actions after visibility is confirmed.
12. Record observed results in this file or a follow-up pilot note.

## Pilot QA

MCP check performed in this run:

- `streamdeck__get_executable_actions`

Observed result:

```json
{
  "actions": []
}
```

| QA item | Result |
|---|---|
| Actions visible | no |
| Actions executed | none |
| Observed result | MCP returned an empty executable action list |
| Verdict | blocked |
| Blocker | Registry actions have not been created in the Stream Deck `MCP Actions` profile for this Codex session |

No actions were executed in this run because no registered safe action IDs were visible through MCP.

## Safety Constraints

Allowed:

- List MCP actions.
- Execute safe registered actions after visibility is confirmed.
- Record evidence.
- Create or update documentation.

Forbidden:

- Deleting profiles.
- Overwriting the active v2.7 profile.
- Enabling auto-send.
- Sending messages automatically.
- Auto-merge.
- Delete, publish, or deploy actions.
- Secrets, credentials, private data, raw transcripts, runtime artifacts.
- Production automation.
- Autonomous retrieval.
- Vector DB.
- Semantic search.
- Embeddings.
- Production web UI workflow.
- Autonomous agents.

## Status Rules

- v2.7 remains active.
- v2.8 remains candidate-only.
- Human acceptance is required before promotion.

## Residual Risks

- This registry is documented but not yet MCP-visible in the current session.
- Manual setup can drift from this file unless the visible MCP action list is checked after configuration.
- Action focus and text insertion behavior may vary by active application.
- The registry covers only seven safe pilot actions, not the full v2.8 StreamDeck map.
- Any downstream Codex work triggered by inserted prompts still requires normal repo inspection, checks, PR review, and no auto-merge.

## Next Step

Create the seven registry actions manually in the Stream Deck `MCP Actions` profile, rerun `streamdeck__get_executable_actions`, and smoke-test 1-2 visible safe actions such as `AIOS_HOME_JUDGE`, `AIOS_HOME_REVISOR`, or `AIOS_KB_SOURCE_TRUTH`.
