# AI OS Stream Deck - setup instruction v2.8

Status: candidate / command-surface aligned.
Active version preserved: v2.7 remains active until Sergey manually migrates and accepts v2.8.

## Purpose

v2.8 redesigns StreamDeck as a two-level AI-OS operator panel: a daily HOME cockpit plus focused specialized screens. It is aligned with `COMMAND_SURFACE.md`, `GOAL_PACKS.md`, `docs/PROJECT_ROUTING.md`, and the current repository/runtime QA evidence from 2026-07-06.

## Safety rules

- Text buttons only insert text.
- Auto-send must stay disabled.
- Terminal commands are inserted as text only and run manually.
- No destructive actions.
- No deletion, sending, merging, publishing, package publishing, deployment, or production automation actions.
- No secrets, credentials, private data, runtime artifacts, raw transcripts, financial raw data, or production data.
- No autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents.
- Local AI remains candidate-only and must use non-sensitive or explicitly sanitized context.

## HOME cockpit

```text
ROUTE      AI OS      THINKING   ANALYTICS  LLM
CODEX      JUDGE      REVISOR    INBOX      MEMO
AI TREND   SYNC       LOCAL AI   PILOTS     KB
```

HOME is intentionally command-oriented. Broad domains open a focused screen; high-frequency daily actions such as JUDGE, REVISOR, INBOX, AI TREND, and SYNC insert the one-touch prompt directly.

## Migration from v2.7

- `QA`: Renamed/reframed as JUDGE on HOME with pass / revise / blocked verdict.
- `REVISOR`: Added to HOME as a one-touch revise-from-Judge-notes prompt.
- `REPO`: Replaced by SYNC on HOME; repo actions live under CODEX and SYNC Check.
- `SYSTEM`: Demoted from HOME; no clear daily command-surface use in current evidence.
- `STOP`: Removed from HOME; no destructive or app-control stop action is included. Use built-in back/Esc manually if needed.
- `RESEARCH`: Renamed/reframed as AI TREND for trend triage and hype filtering.

Do not overwrite v2.7 during pilot. Build v2.8 as a separate candidate profile or duplicate of the v2.7 profile, then replace buttons manually after review.

## Coordinates

```text
K1  K2  K3  K4  K5
K6  K7  K8  K9  K10
K11 K12 K13 K14 K15
```

## Screens and buttons

### Screen: `HOME`

```text
ROUTE | AI OS | THINKING | ANALYTICS | LLM
CODEX | JUDGE | REVISOR | INBOX | MEMO
AI TREND | SYNC | LOCAL AI | PILOTS | KB
```

#### K1 - `ROUTE`

- Action: `Folder`
- Setting: `Folder`
- Note: Classify raw input and choose destination

```text
Open screen ROUTE
```

#### K2 - `AI OS`

- Action: `Folder`
- Setting: `Folder`
- Note: AI concepts, trends, evidence, governance

```text
Open screen AI OS
```

#### K3 - `THINKING`

- Action: `Folder`
- Setting: `Folder`
- Note: Decisions, options, risks, assumptions

```text
Open screen THINKING
```

#### K4 - `ANALYTICS`

- Action: `Folder`
- Setting: `Folder`
- Note: Data contracts, deterministic calculations, QA

```text
Open screen ANALYTICS
```

#### K5 - `LLM`

- Action: `Folder`
- Setting: `Folder`
- Note: Prompts, context packs, model routing, evals

```text
Open screen LLM
```

#### K6 - `CODEX`

- Action: `Folder`
- Setting: `Folder`
- Note: Goal Mode repo execution and PR workflow

```text
Open screen CODEX
```

#### K7 - `JUDGE`

- Action: `Text`
- Setting: `System -> Text`
- Note: One-touch universal judge from HOME

```text
# HOME JUDGE - universal pass / revise / blocked verdict

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Review the pasted output, workflow result, PR summary, memo, claim, or analysis. Produce a strict verdict: pass, revise, or blocked. Deterministic checks override LLM judgment. List unsupported claims and required fixes.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict: pass / revise / blocked
Why:
Required fixes:
Unsupported or weak claims:
Checks observed:
Residual risks:
Next action:
```

#### K8 - `REVISOR`

- Action: `Text`
- Setting: `System -> Text`
- Note: One-touch revisor from HOME

```text
# HOME REVISOR - apply Judge notes without new facts

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Revise the pasted draft using only the provided source text and Judge notes. Do not add new unsupported facts, new claims, or invented evidence. If a requested fix needs missing evidence, mark it as blocked instead of filling the gap.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Revised version:
Applied Judge notes:
Facts preserved:
Claims removed or softened:
Blocked items:
```

#### K9 - `INBOX`

- Action: `Text`
- Setting: `System -> Text`
- Note: Fast capture and routing prompt

```text
# ROUTE - Capture, sort, and formulate the next action without solving the owner-project work

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Capture, sort, and formulate the next action without solving the owner-project work.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K10 - `MEMO`

- Action: `Folder`
- Setting: `Folder`
- Note: Finance and management memo workflow

```text
Open screen MEMO
```

#### K11 - `AI TREND`

- Action: `Text`
- Setting: `System -> Text`
- Note: Renames v2.7 RESEARCH into command-oriented AI Trend

```text
# HOME AI TREND - trend triage / hype filter

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Route to [AI OS]. Triage the AI topic, release, tool, link, or question. Separate supported, weak, and unsupported claims. If facts may have changed, label them as needs fresh check and ask Sergey before any live web check. Recommend adopt, watch, ignore, or investigate.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict: adopt / watch / ignore / investigate
What changed:
Supported claims:
Weak claims:
Unsupported claims:
Sergey relevance:
Risks:
Next step:
```

#### K12 - `SYNC`

- Action: `Text`
- Setting: `System -> Text`
- Note: Replaces v2.7 REPO with daily Sync Check

```text
# HOME SYNC - repo/main/checks sync check

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Codex] / Codex APP. Check local repo branch, remote main, working tree status, and relevant checks. Identify whether there is a mismatch between local files, branch, main, and expected validation. Avoid creating a PR unless a mismatch/change is found and human review is required.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Repo:
Current branch:
Main/remote status:
Working tree:
Checks to run:
Mismatch found: yes / no
Required action:
Create PR: no unless mismatch/change requires review
Risks:
```

#### K13 - `LOCAL AI`

- Action: `Folder`
- Setting: `Folder`
- Note: Candidate-only Ollama/Open WebUI safe pilot

```text
Open screen LOCAL AI
```

#### K14 - `PILOTS`

- Action: `Folder`
- Setting: `Folder`
- Note: Pilot cases, results, acceptance gates

```text
Open screen PILOTS
```

#### K15 - `KB`

- Action: `Folder`
- Setting: `Folder`
- Note: Knowledge bundle evidence checks

```text
Open screen KB
```


### Screen: `ROUTE`

```text
BACK | Raw -> Route | Things? | Calendar? | Notes?
AI OS? | Thinking? | Analytics? | LLM? | Codex?
Codex APP? | Handoff | Clarify | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Raw -> Route`

- Action: `Text`
- Setting: `System -> Text`
- Note: Router: classify and hand off, do not solve

```text
# ROUTE - Raw unclear input; find best destination

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Raw unclear input; find best destination.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K3 - `Things?`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - Check whether input is a concrete Things action

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Check whether input is a concrete Things action. Preferred route to test: Things.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K4 - `Calendar?`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - Check whether input is a hard time commitment, event, meeting, or deadline

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Check whether input is a hard time commitment, event, meeting, or deadline. Preferred route to test: Calendar.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K5 - `Notes?`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - Check whether input is reference material, context, or a note

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Check whether input is reference material, context, or a note. Preferred route to test: Notes / Obsidian.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K6 - `AI OS?`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - Check whether input is AI concept, AI pattern, evidence, governance, or use case

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Check whether input is AI concept, AI pattern, evidence, governance, or use case. Preferred route to test: [AI OS].

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K7 - `Thinking?`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - Check whether input is decision, strategy, options, scenario, or risk review

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Check whether input is decision, strategy, options, scenario, or risk review. Preferred route to test: [Thinking].

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K8 - `Analytics?`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - Check whether input is data, metrics, calculation, reconciliation, dashboard, mart, or data quality

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Check whether input is data, metrics, calculation, reconciliation, dashboard, mart, or data quality. Preferred route to test: [Analytics].

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K9 - `LLM?`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - Check whether input is prompt, context pack, workflow, model routing, or eval

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Check whether input is prompt, context pack, workflow, model routing, or eval. Preferred route to test: [LLM].

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K10 - `Codex?`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - Check whether input is implementation, tests, repo change, refactor, script, or release

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Check whether input is implementation, tests, repo change, refactor, script, or release. Preferred route to test: [Codex].

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K11 - `Codex APP?`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - Check whether input needs long-running Codex APP execution with batches, checks, and PR workflow

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work as [Inbox Router]. Route first, solve never. Classify raw input as Things, Calendar, Notes/Obsidian, [AI OS], [Thinking], [Analytics], [LLM], [Codex], Codex APP, or clarify. Do not solve owner-project work inside Router. Focus: Check whether input needs long-running Codex APP execution with batches, checks, and PR workflow. Preferred route to test: Codex APP.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Reason:
Confidence: strong / medium / weak
Status: direct / clarify / handoff / park / trash
Facts:
Assumptions:
Missing information:
Risks:
Next action:
Handoff package, if needed:
- From:
- To:
- Objective:
- Context:
- Constraints:
- Expected output:
- Acceptance criteria:
- Open questions:
```

#### K12 - `Handoff`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - project handoff

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare a compact handoff package to the chosen owner project. Do not solve the task. If destination is unclear, ask at most 1-3 critical questions.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Destination:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:
```

#### K13 - `Clarify`

- Action: `Text`
- Setting: `System -> Text`

```text
# ROUTE - clarification required

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Explain why the route cannot be chosen safely yet. Ask only the critical questions needed to route correctly.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Preliminary route:
Missing information:
Risk of wrong routing:
Critical questions, max 3:
What can proceed now:
What is blocked:
```

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `AI OS`

```text
BACK | AI Trend | Pattern Explain | Use Case | Evidence Check
Governance | To Thinking | To LLM | To Codex | Agent Loop
StreamDeck | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `AI Trend`

- Action: `Text`
- Setting: `System -> Text`
- Note: Trend triage / hype filter

```text
# HOME AI TREND - trend triage / hype filter

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Route to [AI OS]. Triage the AI topic, release, tool, link, or question. Separate supported, weak, and unsupported claims. If facts may have changed, label them as needs fresh check and ask Sergey before any live web check. Recommend adopt, watch, ignore, or investigate.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict: adopt / watch / ignore / investigate
What changed:
Supported claims:
Weak claims:
Unsupported claims:
Sergey relevance:
Risks:
Next step:
```

#### K3 - `Pattern Explain`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Explain the AI pattern, where it is useful, where it fails, and what evidence supports it.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Explain the AI pattern, where it is useful, where it fails, and what evidence supports it..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Separate fact, inference, assumption, and unsupported claim.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K4 - `Use Case`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Translate the AI topic into a practical Sergey use case or reject it if relevance is weak.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Translate the AI topic into a practical Sergey use case or reject it if relevance is weak..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Do not claim adoption readiness without evidence.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K5 - `Evidence Check`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Check evidence for the pasted AI claim or recommendation.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Check evidence for the pasted AI claim or recommendation..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Label every claim as supported, weak, mixed, unsupported, or needs fresh check.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K6 - `Governance`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Check whether the proposed AI workflow violates blocked promotion items or safety boundaries.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Check whether the proposed AI workflow violates blocked promotion items or safety boundaries..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Block embeddings, semantic search, vector DB, autonomous retrieval, production web UI workflow, autonomous agents, secrets, and production automation unless explicitly approved and promoted.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K7 - `To Thinking`

- Action: `Text`
- Setting: `System -> Text`

```text
# AI OS - handoff to Thinking

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare a decision/risk handoff from [AI OS] to [Thinking].

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Decision needed:
Options:
Evidence:
Assumptions:
Risks:
Reversibility:
Open questions:
```

#### K8 - `To LLM`

- Action: `Text`
- Setting: `System -> Text`

```text
# AI OS - handoff to LLM

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare a prompt/workflow/model-routing handoff from [AI OS] to [LLM].

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Goal:
Context:
Evidence:
Constraints:
Expected prompt/workflow output:
Quality gate:
```

#### K9 - `To Codex`

- Action: `Text`
- Setting: `System -> Text`

```text
# AI OS - handoff to Codex

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare a repo-work handoff only if implementation is actually needed.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Repo goal:
Files to inspect:
Allowed changes:
Forbidden actions:
Checks:
Acceptance:
Rollback:
```

#### K10 - `Agent Loop`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Design a supervised loop with owner, allowed actions, checks, stop conditions, and human acceptance gate.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Design a supervised loop with owner, allowed actions, checks, stop conditions, and human acceptance gate..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
No autonomous retrieval, vector DB, embeddings, semantic search, production web UI, or autonomous agents.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K11 - `StreamDeck`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Evaluate whether a StreamDeck command or prompt should be kept, revised, demoted, or rejected.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Evaluate whether a StreamDeck command or prompt should be kept, revised, demoted, or rejected..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Keep prompts short, routable, evidence-aware, and manual-only.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `THINKING`

```text
BACK | Decision Memo | Options | Risks | Assumptions
Reversible? | Judge Decision | To Analytics | To Codex | Scenario
Next Step | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Decision Memo`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Thinking] - Create a decision memo from the pasted context.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Thinking]. Create a decision memo from the pasted context..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Separate facts, assumptions, options, downside, reversibility, and revisit trigger.

Return:
Decision:
Context:
Options:
Recommendation:
Risks:
Reversibility:
Revisit trigger:
```

#### K3 - `Options`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Thinking] - Generate realistic options and trade-offs for the decision.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Thinking]. Generate realistic options and trade-offs for the decision..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Do not invent constraints or facts.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K4 - `Risks`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Thinking] - Identify downside, failure modes, mitigation, and stop conditions.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Thinking]. Identify downside, failure modes, mitigation, and stop conditions..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Separate likely risks from speculative risks.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K5 - `Assumptions`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Thinking] - Extract assumptions, unknowns, and what would change the decision.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Thinking]. Extract assumptions, unknowns, and what would change the decision..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Mark assumptions explicitly.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K6 - `Reversible?`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Thinking] - Classify reversibility and propose the smallest reversible next step.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Thinking]. Classify reversibility and propose the smallest reversible next step..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Prefer reversible action unless irreversible action is justified.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K7 - `Judge Decision`

- Action: `Text`
- Setting: `System -> Text`

```text
# THINKING - judge decision

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the decision memo or option set. Require verdict pass, revise, or blocked.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict: pass / revise / blocked
Reason:
Missing facts:
Risks:
Required revision:
Next action:
```

#### K8 - `To Analytics`

- Action: `Text`
- Setting: `System -> Text`

```text
# THINKING - handoff to Analytics

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare analytics handoff for questions requiring data, metrics, calculations, variance, or reconciliation.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Question:
Data sources:
Period:
Grain:
Metrics:
Formulas:
QA checks:
Expected output:
```

#### K9 - `To Codex`

- Action: `Text`
- Setting: `System -> Text`

```text
# THINKING - handoff to Codex

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare Codex handoff after the decision is clear and implementation is needed.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Objective:
Scope:
Allowed files:
Forbidden actions:
Checks:
Acceptance:
Rollback:
```

#### K10 - `Scenario`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Thinking] - Build best/base/worst scenarios and leading indicators.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Thinking]. Build best/base/worst scenarios and leading indicators..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Do not calculate numbers without Analytics/Python/SQL.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K11 - `Next Step`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Thinking] - Reduce the decision to one next action and one stop condition.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Thinking]. Reduce the decision to one next action and one stop condition..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Make the next step local, reversible, and verifiable when possible.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `ANALYTICS`

```text
BACK | Data Contract | Variance | Reconcile | Audit Anomaly
Memo Facts | QA Checks | Analytics Loop | Supervised Loop | Mart Spec
Formula Review | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Data Contract`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Draft a data contract before analysis.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Draft a data contract before analysis..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Input layer:
Output layer:
Period:
Grain:
Currency/units:
Metrics:
Formulas:
Filters:
QA checks:
Risks:
```

#### K3 - `Variance`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Analyze a variance using deterministic calculation only.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Analyze a variance using deterministic calculation only..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Period:
Baseline:
Actual:
Formula:
Python/SQL check needed:
Findings:
Risks:
```

#### K4 - `Reconcile`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Plan or perform a reconciliation with explicit join keys and exception handling.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Plan or perform a reconciliation with explicit join keys and exception handling..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Sources:
Join keys:
Period:
Currency/units:
Expected equality/control:
Exceptions:
QA:
```

#### K5 - `Audit Anomaly`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Review an anomaly or suspicious record.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Review an anomaly or suspicious record..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Anomaly:
Evidence:
Likely cause:
Risk:
Required deterministic checks:
Action:
```

#### K6 - `Memo Facts`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Prepare verified facts for a finance or management memo.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Prepare verified facts for a finance or management memo..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Approved facts:
Source layer:
Calculations performed:
Limitations:
Claims not supported:
```

#### K7 - `QA Checks`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Design the smallest meaningful QA checks for the analysis.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Design the smallest meaningful QA checks for the analysis..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Checks:
Expected results:
Failure meaning:
Blockers:
```

#### K8 - `Analytics Loop`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Run the analytics factory loop from question to data contract, mart, findings, memo facts, QA, and next run trigger.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Run the analytics factory loop from question to data contract, mart, findings, memo facts, QA, and next run trigger..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Status: candidate / ready for review / blocked
Method:
QA:
Findings:
Next run trigger:
```

#### K9 - `Supervised Loop`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Iterate analysis until QA passes or blockers are clear.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Iterate analysis until QA passes or blockers are clear..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks. Stop on data quality failure, unclear grain, missing contract, or no validation path.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K10 - `Mart Spec`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Specify a mart or compact output table.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Specify a mart or compact output table..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Mart name:
Source:
Grain:
Columns:
Metrics:
Formulas:
QA:
Consumers:
```

#### K11 - `Formula Review`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Analytics] - Review formulas for correctness and reproducibility.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Analytics]. Review formulas for correctness and reproducibility..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Formula:
Inputs:
Python/SQL implementation needed:
Edge cases:
QA:
```

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `LLM`

```text
BACK | Prompt Build | Context Pack | Judge Screen | Revisor Screen
Model Routing | Eval Rubric | Workflow Design | Local AI Prompt | StreamDeck
No Raw Dump | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Prompt Build`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] - Build a short, routable prompt for the pasted goal.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM]. Build a short, routable prompt for the pasted goal..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
No raw dumps, no unsupported facts, no hidden automation.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K3 - `Context Pack`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] - Build a compact context pack from goal, facts, constraints, expected output, and quality gate.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM]. Build a compact context pack from goal, facts, constraints, expected output, and quality gate..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Curated context only; no raw dumps, logs, transcripts, secrets, chunks, vector DB, embeddings, or autonomous retrieval.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K4 - `Judge Screen`

- Action: `Folder`
- Setting: `Folder`
- Note: Open full Judge screen

```text
Open screen JUDGE
```

#### K5 - `Revisor Screen`

- Action: `Folder`
- Setting: `Folder`
- Note: Open full Revisor screen

```text
Open screen REVISOR
```

#### K6 - `Model Routing`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] - Recommend a model or surface only from current verified needs and constraints.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM]. Recommend a model or surface only from current verified needs and constraints..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
For prices, limits, availability, or release status, label as needs fresh official check and ask Sergey before any live web check.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K7 - `Eval Rubric`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] - Create an evaluation rubric for the output or workflow.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM]. Create an evaluation rubric for the output or workflow..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Rubric must include pass/revise/blocked and unsupported-claim handling.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K8 - `Workflow Design`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] - Design a safe manual workflow with owner, inputs, outputs, checks, and stop conditions.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM]. Design a safe manual workflow with owner, inputs, outputs, checks, and stop conditions..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
No production automation or autonomous agents.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K9 - `Local AI Prompt`

- Action: `Text`
- Setting: `System -> Text`

```text
# LLM - local AI prompt

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Create a local AI prompt for draft-only use.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Prompt:
Sensitive-data boundary:
Eval matrix:
Judge step:
Limitations:
```

#### K10 - `StreamDeck`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] - Improve a StreamDeck prompt or command.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM]. Improve a StreamDeck prompt or command..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Keep it short, command-oriented, manual-only, and aligned with COMMAND_SURFACE.md.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K11 - `No Raw Dump`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] - Convert raw context into a safe concise context pack.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM]. Convert raw context into a safe concise context pack..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Remove secrets, private data, logs, transcripts, runtime artifacts, and unsupported source dumps.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `CODEX`

```text
BACK | Goal -> Issue | Build First | PR Judge | Sync Check
Run Checks | Fix Mismatch | Release Notes | No Auto-Merge | Branch Pack
Review Report | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Goal -> Issue`

- Action: `Text`
- Setting: `System -> Text`

```text
# CODEX - goal to issue

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Convert a broad repo/workflow goal into a GitHub issue-ready task brief without requiring Sergey to write atomic task wording.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Use Goal Mode Build-First: inspect relevant files first, infer bounded safe scope, create or use a non-main branch following repo branch prefix conventions such as `codex/...` when present, make the smallest useful reversible change, run checks, fix failures within scope when safe, report blockers honestly, open a PR for human review when repository files changed and checks are meaningful, and never auto-merge.

Return:
Goal:
Context:
Allowed scope:
Forbidden actions:
Expected files:
Checks:
Acceptance criteria:
Rollback:
Human review:
```

#### K3 - `Build First`

- Action: `Text`
- Setting: `System -> Text`
- Note: Goal Mode implementation-first execution

```text
# CODEX - Goal Mode Build First

Work in Goal Mode.

Do not produce a roadmap unless explicitly asked.
Do not create an epic unless explicitly asked.
Do not stop for soft uncertainty.
Do not create a new approval package after approval already exists for the same bounded execution.

Task:
[PASTE GOAL]

Default behavior:
- inspect relevant files;
- infer bounded safe scope;
- create/use non-main branch;
- implement smallest useful working version;
- run checks;
- fix failures within scope;
- open PR if repo files changed;
- never auto-merge.

Stop only for hard blockers:
- missing secrets required for real execution;
- source mutation / Safe Apply / real provider API without approval;
- schema / metric / formula / provider-routing / output-contract change without approval;
- destructive or production action;
- no meaningful validation path.

Final report:
Summary:
Branch:
Files changed:
Commands run:
Test results:
Evidence/artifacts:
Assumptions:
Blockers:
Risks:
Rollback:
PR:
Acceptance status:
No auto-merge:
```

#### K4 - `PR Judge`

- Action: `Text`
- Setting: `System -> Text`

```text
# CODEX - PR judge

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Review a PR or PR summary for correctness, checks, risks, and merge readiness.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict: pass / revise / blocked
Required fixes:
Missing checks:
Risks:
No auto-merge reminder:
```

#### K5 - `Sync Check`

- Action: `Text`
- Setting: `System -> Text`
- Note: Repo/main/checks sync prompt

```text
# HOME SYNC - repo/main/checks sync check

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Codex] / Codex APP. Check local repo branch, remote main, working tree status, and relevant checks. Identify whether there is a mismatch between local files, branch, main, and expected validation. Avoid creating a PR unless a mismatch/change is found and human review is required.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Repo:
Current branch:
Main/remote status:
Working tree:
Checks to run:
Mismatch found: yes / no
Required action:
Create PR: no unless mismatch/change requires review
Risks:
```

#### K6 - `Run Checks`

- Action: `Text`
- Setting: `System -> Text`

```text
# CODEX - run checks plan

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare the smallest relevant local check list. Insert terminal commands as text only; Sergey/Codex runs them manually.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Use Goal Mode Build-First: inspect relevant files first, infer bounded safe scope, create or use a non-main branch following repo branch prefix conventions such as `codex/...` when present, make the smallest useful reversible change, run checks, fix failures within scope when safe, report blockers honestly, open a PR for human review when repository files changed and checks are meaningful, and never auto-merge.

Return:
Commands to run manually:
Expected result:
Failure handling:
What not to run:
```

#### K7 - `Fix Mismatch`

- Action: `Text`
- Setting: `System -> Text`

```text
# CODEX - fix mismatch

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
If sync/checks find mismatch, propose the smallest file change to repair it.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Use Goal Mode Build-First: inspect relevant files first, infer bounded safe scope, create or use a non-main branch following repo branch prefix conventions such as `codex/...` when present, make the smallest useful reversible change, run checks, fix failures within scope when safe, report blockers honestly, open a PR for human review when repository files changed and checks are meaningful, and never auto-merge.

Return:
Mismatch:
Root cause:
Allowed files:
Patch plan:
Checks:
Risk:
```

#### K8 - `Release Notes`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Codex] - Draft concise release notes from actual changed files and observed checks.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Codex]. Draft concise release notes from actual changed files and observed checks..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Do not invent changed files, tests, or results.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K9 - `No Auto-Merge`

- Action: `Text`
- Setting: `System -> Text`

```text
# CODEX - no auto-merge reminder

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
State the safe PR workflow for this repo task.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Use Goal Mode Build-First: inspect relevant files first, infer bounded safe scope, create or use a non-main branch following repo branch prefix conventions such as `codex/...` when present, make the smallest useful reversible change, run checks, fix failures within scope when safe, report blockers honestly, open a PR for human review when repository files changed and checks are meaningful, and never auto-merge.

Return:
Branch:
Commit:
Checks:
Draft PR:
Human review required:
Auto-merge: prohibited:
```

#### K10 - `Branch Pack`

- Action: `Text`
- Setting: `System -> Text`

```text
# CODEX - branch task pack

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare a compact Codex APP task package for bounded repo work.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Use Goal Mode Build-First: inspect relevant files first, infer bounded safe scope, create or use a non-main branch following repo branch prefix conventions such as `codex/...` when present, make the smallest useful reversible change, run checks, fix failures within scope when safe, report blockers honestly, open a PR for human review when repository files changed and checks are meaningful, and never auto-merge.

Return:
Objective:
Allowed files:
Forbidden actions:
Checks:
Acceptance:
Rollback:
Final report format:
```

#### K11 - `Review Report`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Codex] - Summarize actual changed files, commands run, test results, blockers, and final status.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Codex]. Summarize actual changed files, commands run, test results, blockers, and final status..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Report only observed facts.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `JUDGE`

```text
BACK | Universal | PR Judge | Memo Judge | Analytics
Evidence | Risk | Blocker | Local AI | Route Judge
Final Gate | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Universal`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - universal

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the pasted output. Verdict must be exactly pass, revise, or blocked. Deterministic checks and repository/source evidence override LLM preference.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict: pass / revise / blocked
Reason:
Required fixes:
Unsupported claims:
Evidence checked:
Residual risks:
Next action:
```

#### K3 - `PR Judge`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - PR

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the pasted output. Verdict must be exactly pass, revise, or blocked. Deterministic checks and repository/source evidence override LLM preference. Focus on PR scope, diff, checks, risks, and no auto-merge.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict:
Blocking issues:
Missing checks:
Risk:
Human review note:
```

#### K4 - `Memo Judge`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - memo

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the pasted output. Verdict must be exactly pass, revise, or blocked. Deterministic checks and repository/source evidence override LLM preference. Focus on facts, audience, finance/data support, and unsupported management claims.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict:
Unsupported claims:
Required revisions:
Residual risks:
```

#### K5 - `Analytics`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - analytics

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the pasted output. Verdict must be exactly pass, revise, or blocked. Deterministic checks and repository/source evidence override LLM preference. Focus on deterministic calculations, data contract, period, grain, formulas, and QA.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict:
Calculation checks:
Data contract gaps:
QA gaps:
Required fixes:
```

#### K6 - `Evidence`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - evidence

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the pasted output. Verdict must be exactly pass, revise, or blocked. Deterministic checks and repository/source evidence override LLM preference. Label claims as supported, weak, mixed, unsupported, or needs fresh check.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict:
Supported:
Weak:
Mixed:
Unsupported:
Needs fresh check:
```

#### K7 - `Risk`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - risk

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the pasted output. Verdict must be exactly pass, revise, or blocked. Deterministic checks and repository/source evidence override LLM preference. Focus on downside, reversibility, blocked actions, and stop conditions.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict:
Risks:
Stop conditions:
Required mitigation:
```

#### K8 - `Blocker`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - blocker review

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Determine whether the task is truly blocked or can continue with a smaller safe next step.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict: pass / revise / blocked
Blocker:
Can proceed with:
Cannot proceed because:
Question needed:
```

#### K9 - `Local AI`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - local AI output

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the pasted output. Verdict must be exactly pass, revise, or blocked. Deterministic checks and repository/source evidence override LLM preference. Treat local AI output as draft/candidate until reviewed.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Verdict:
Safety boundary:
Sensitive data risk:
Unsupported claims:
Next step:
```

#### K10 - `Route Judge`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - route decision

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge whether the route chosen by Inbox Router is correct and safe.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict:
Correct destination:
Wrong-route risk:
Clarifying question if needed:
Next action:
```

#### K11 - `Final Gate`

- Action: `Text`
- Setting: `System -> Text`

```text
# JUDGE - final acceptance gate

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Compare output to stated acceptance criteria and observed checks only.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict:
Acceptance criteria met:
Not met:
Checks observed:
Residual risks:
Ready for human review: yes / no
```

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `REVISOR`

```text
BACK | Apply Notes | Shorten | Clearer | Exec Version
File-ready | No New Claims | Memo Revise | Prompt Revise | EMPTY
EMPTY | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Apply Notes`

- Action: `Text`
- Setting: `System -> Text`

```text
# REVISOR - apply Judge notes

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Revise only using the pasted draft, approved source facts, and Judge notes. Do not add new unsupported facts or invented evidence. Apply all actionable Judge notes.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Revised output:
Applied notes:
Unapplied notes and why:
No-new-claims check:
```

#### K3 - `Shorten`

- Action: `Text`
- Setting: `System -> Text`

```text
# REVISOR - shorten

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Revise only using the pasted draft, approved source facts, and Judge notes. Do not add new unsupported facts or invented evidence. Make it shorter without losing required facts or caveats.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Short version:
Removed detail:
Preserved facts:
```

#### K4 - `Clearer`

- Action: `Text`
- Setting: `System -> Text`

```text
# REVISOR - make clear

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Revise only using the pasted draft, approved source facts, and Judge notes. Do not add new unsupported facts or invented evidence. Improve clarity and structure.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Clear version:
Ambiguities resolved:
Remaining blockers:
```

#### K5 - `Exec Version`

- Action: `Text`
- Setting: `System -> Text`

```text
# REVISOR - executive version

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Revise only using the pasted draft, approved source facts, and Judge notes. Do not add new unsupported facts or invented evidence. Produce an executive version for a busy reader.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Executive version:
Key caveats:
Decisions needed:
```

#### K6 - `File-ready`

- Action: `Text`
- Setting: `System -> Text`

```text
# REVISOR - file-ready final

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Revise only using the pasted draft, approved source facts, and Judge notes. Do not add new unsupported facts or invented evidence. Format as a clean final artifact ready to paste into a file.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Final artifact:
Source facts used:
Unsupported items excluded:
```

#### K7 - `No New Claims`

- Action: `Text`
- Setting: `System -> Text`

```text
# REVISOR - no new claims check

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Check the revision against the source/Judge notes and flag any new unsupported facts.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
New claims found:
Unsupported claims removed:
Safe revised text:
```

#### K8 - `Memo Revise`

- Action: `Text`
- Setting: `System -> Text`

```text
# REVISOR - memo revise

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Revise only using the pasted draft, approved source facts, and Judge notes. Do not add new unsupported facts or invented evidence. Revise memo narrative while preserving only Analytics-approved facts.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Revised memo:
Approved facts preserved:
Claims softened/removed:
Residual risks:
```

#### K9 - `Prompt QA`

- Action: `Text`
- Setting: `System -> Text`
- Note: Judge prompt safety and UX; do not rewrite

```text
# REVISOR - prompt QA

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the prompt or prompt revision request only. Do not rewrite the prompt. Check whether it is safe, routable, compact, and free of raw input-template placeholders. If a rewrite is needed, return `Verdict: revise` with exact requirements for Sergey or another revisor; do not produce the rewritten prompt yourself.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict: pass / revise / blocked
Placeholder risk: none / present
Routing risk:
Unsupported automation risk:
Required changes:
Human decision needed:
```

#### K10 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K11 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `MEMO`

```text
BACK | Finance Memo | Exec Summary | Findings | Risks
Recommend | Appendix | Final Memo | Mgmt Memo | Judge/Revise
EMPTY | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Finance Memo`

- Action: `Text`
- Setting: `System -> Text`

```text
# MEMO - finance memo factory

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Create a finance memo only from verified Analytics facts. If calculations are needed, route to [Analytics] first.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
All numeric calculations, totals, deltas, percentages, ratios, variances, reconciliations, and statistics must be performed deterministically by Python or SQL, not by LLM reasoning. Always state data contract, source layer, output layer, period, grain, currency or units, metrics, formulas, filters, QA checks, assumptions, and residual risks.

Return:
Audience:
Period:
Currency:
Approved facts:
Findings:
Risks:
Recommendations:
Evidence appendix:
Blocked claims:
```

#### K3 - `Exec Summary`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] / [MEMO] - Draft an executive summary from approved facts only.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM] / [MEMO]. Draft an executive summary from approved facts only..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
No new facts; no unsupported management claims.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K4 - `Findings`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] / [MEMO] - Turn approved facts into findings with source traceability.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM] / [MEMO]. Turn approved facts into findings with source traceability..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Each finding must trace to provided evidence.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K5 - `Risks`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] / [MEMO] - Write the risks section from provided evidence and assumptions.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM] / [MEMO]. Write the risks section from provided evidence and assumptions..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Separate evidence-backed risks from assumptions.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K6 - `Recommend`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] / [MEMO] - Draft recommendations that do not exceed the evidence.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM] / [MEMO]. Draft recommendations that do not exceed the evidence..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Tie each recommendation to a finding or mark it as assumption.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K7 - `Appendix`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] / [MEMO] - Prepare an evidence appendix.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM] / [MEMO]. Prepare an evidence appendix..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
List sources, calculations observed, limitations, and unsupported exclusions.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K8 - `Final Memo`

- Action: `Text`
- Setting: `System -> Text`

```text
# MEMO - final memo

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Assemble final memo from approved sections only.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Title:
Executive summary:
Facts and findings:
Risks:
Recommendations:
Evidence appendix:
Residual risks:
```

#### K9 - `Mgmt Memo`

- Action: `Text`
- Setting: `System -> Text`

```text
# [LLM] / [MEMO] - Prepare a management memo from verified facts and decision context.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [LLM] / [MEMO]. Prepare a management memo from verified facts and decision context..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
No invented business rules or metrics.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K10 - `Judge/Revise`

- Action: `Text`
- Setting: `System -> Text`

```text
# MEMO - judge then revise

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge memo as pass/revise/blocked, then revise only if notes are actionable and source facts are sufficient.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Return:
Verdict:
Required revisions:
Revised memo if safe:
Blocked items:
```

#### K11 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `LOCAL AI`

```text
BACK | Ollama Smoke | Model Compare | Open WebUI | Draft Only
Safety | Record Pilot | Candidate? | No Sensitive | Judge Output
EMPTY | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Ollama Smoke`

- Action: `Text`
- Setting: `System -> Text`

```text
# LOCAL AI - Ollama smoke plan

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare a non-sensitive local smoke test plan for Ollama. Commands are text only and run manually.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Manual commands:
Non-sensitive prompt:
Expected behavior:
Pass/revise/blocked criteria:
Risks:
```

#### K3 - `Model Compare`

- Action: `Text`
- Setting: `System -> Text`

```text
# LOCAL AI - model compare

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Compare local model outputs using sanitized prompts only.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Models:
Prompt:
Eval matrix:
Verdict:
Limitations:
```

#### K4 - `Open WebUI`

- Action: `Text`
- Setting: `System -> Text`

```text
# LOCAL AI - Open WebUI check

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare a safe Open WebUI check without private data or production workflow claims.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Check:
Sensitive-data boundary:
Expected result:
Limitations:
```

#### K5 - `Draft Only`

- Action: `Text`
- Setting: `System -> Text`

```text
# LOCAL AI - local draft only

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Rewrite or generate a draft using local AI boundaries.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Draft:
Human review required:
Unsupported claims:
Next judge step:
```

#### K6 - `Safety`

- Action: `Text`
- Setting: `System -> Text`

```text
# LOCAL AI - safety boundary

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
State whether the proposed local AI use is allowed, revise, or blocked.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Verdict: pass / revise / blocked
Sensitive data risk:
Blocked items:
Allowed next step:
```

#### K7 - `Record Pilot`

- Action: `Text`
- Setting: `System -> Text`

```text
# LOCAL AI - record pilot result

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Prepare a pilot result note from observed local checks only.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Pilot ID:
Date:
Input:
Observed behavior:
Checks run:
Verdict:
Residual risks:
Next step:
```

#### K8 - `Candidate?`

- Action: `Text`
- Setting: `System -> Text`

```text
# LOCAL AI - candidate verdict

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Decide whether a local AI result remains candidate, ready for review, revise, or blocked.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Status:
Evidence:
Risks:
Promotion blocked by:
Next step:
```

#### K9 - `No Sensitive`

- Action: `Text`
- Setting: `System -> Text`

```text
# LOCAL AI - sensitive data guard

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Check the pasted plan or prompt for sensitive/private/production data risk before local AI use.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Allowed: yes / no
Sensitive items to remove:
Safe sanitized prompt:
Blocked items:
```

#### K10 - `Judge Output`

- Action: `Text`
- Setting: `System -> Text`
- Note: Judge local AI output as candidate/draft

```text
# JUDGE - local AI output

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Judge the pasted output. Verdict must be exactly pass, revise, or blocked. Deterministic checks and repository/source evidence override LLM preference. Treat local AI output as draft/candidate until reviewed.

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Candidate-only local experiment. Use only non-sensitive or explicitly approved sanitized context. Do not use secrets, credentials, private data, financial raw data, production data, runtime artifacts, autonomous retrieval, embeddings, vector DB, semantic search, production web UI workflow, or autonomous agents. Output is draft/candidate until judged and accepted by a human.

Return:
Verdict:
Safety boundary:
Sensitive data risk:
Unsupported claims:
Next step:
```

#### K11 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `PILOTS`

```text
BACK | Pilot Plan | Pilot Result | Candidate? | Acceptance
Residual Risk | Registry | Runtime Smoke | Rollback | Status Note
EMPTY | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `Pilot Plan`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] / [LLM] / [Codex] - Draft a pilot plan with owner, status, inputs, checks, acceptance gate, residual risks, and stop condition.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS] / [LLM] / [Codex]. Draft a pilot plan with owner, status, inputs, checks, acceptance gate, residual risks, and stop condition..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Pilot remains candidate until evidence and human review.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K3 - `Pilot Result`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] / [LLM] - Record a pilot result from observed behavior only.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS] / [LLM]. Record a pilot result from observed behavior only..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Do not invent checks or results.

Return:
Pilot ID:
Date:
Owner project:
Input:
Observed behavior:
Checks run:
Verdict:
Residual risks:
Next step:
```

#### K4 - `Candidate?`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Assess candidate to active promotion readiness.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Assess candidate to active promotion readiness..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Do not claim production readiness. Promotion requires evidence, checks, and human acceptance.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K5 - `Acceptance`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Map pilot evidence to acceptance criteria.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Map pilot evidence to acceptance criteria..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Use observed evidence only.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K6 - `Residual Risk`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Thinking] - List residual risks and whether they block promotion.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Thinking]. List residual risks and whether they block promotion..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Separate blocker, risk, assumption, and next check.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K7 - `Registry`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Codex] - Prepare a minimal registry update plan if pilot status changes.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Codex]. Prepare a minimal registry update plan if pilot status changes..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
No file changes unless requested; no production_promotion=yes.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K8 - `Runtime Smoke`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Prepare a live smoke QA prompt and expected result for a project runtime.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Prepare a live smoke QA prompt and expected result for a project runtime..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
No secrets, private data, runtime artifacts, or raw transcripts.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K9 - `Rollback`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Thinking] / [Codex] - Define rollback or stop condition for a candidate pilot.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Thinking] / [Codex]. Define rollback or stop condition for a candidate pilot..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Keep action manual and reversible.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K10 - `Status Note`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Write a concise pilot status note.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Write a concise pilot status note..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Allowed status must be explicit; avoid production readiness claims.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K11 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered


### Screen: `KB`

```text
BACK | KB Search | Evidence Label | Review Item | Support Mix
Manifest | Source Truth | Bundle Sync | Upload Check | EMPTY
EMPTY | EMPTY | EMPTY | EMPTY | EMPTY
```

#### K1 - `BACK`

- Action: `Navigation Back`
- Setting: `Built-in folder back`
- Note: Do not reprogram

```text
Built-in folder back
```

#### K2 - `KB Search`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] / [LLM] - Plan a KB evidence lookup from known repository/Knowledge files.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS] / [LLM]. Plan a KB evidence lookup from known repository/Knowledge files..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
No autonomous retrieval or semantic search; use provided files or explicit manual lookup.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K3 - `Evidence Label`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Label claims as supported, weak, mixed, unsupported, or needs fresh check.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Label claims as supported, weak, mixed, unsupported, or needs fresh check..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Separate source fact from inference.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K4 - `Review Item`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Review a KB item for owner, status, manifest/upload role, evidence, and residual risk.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Review a KB item for owner, status, manifest/upload role, evidence, and residual risk..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Do not promote candidate material without evidence.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K5 - `Support Mix`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Classify the pasted claim set as supported, weak, mixed, or unsupported.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Classify the pasted claim set as supported, weak, mixed, or unsupported..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Every material claim needs a label.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K6 - `Manifest`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Codex] - Check whether manifest paths and upload lists stay consistent.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Codex]. Check whether manifest paths and upload lists stay consistent..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Use repository files and validation scripts only.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K7 - `Source Truth`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Identify the source of truth and whether a bundle/source sync is needed.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Identify the source of truth and whether a bundle/source sync is needed..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Keep source files and Knowledge bundle files consistent.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K8 - `Bundle Sync`

- Action: `Text`
- Setting: `System -> Text`

```text
# [Codex] - Prepare a minimal bundle sync task if source and Knowledge bundle diverge.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [Codex]. Prepare a minimal bundle sync task if source and Knowledge bundle diverge..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
No broad rewrite; run manifest/bundle checks.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K9 - `Upload Check`

- Action: `Text`
- Setting: `System -> Text`

```text
# [AI OS] - Prepare a manual ChatGPT Project upload/sync checklist.

Use the last meaningful message above, selected text, or material pasted below.
If no material is available, ask Sergey to paste it in one message.

Task:
Work in [AI OS]. Prepare a manual ChatGPT Project upload/sync checklist..

Safety:
Text insert only. Auto-send disabled. Manual execution only. No destructive actions, deletion, sending, merging, publishing, secrets, credentials, private data, runtime artifacts, production automation, autonomous retrieval, vector DB, semantic search, embeddings, production web UI workflow, or autonomous agents. Terminal commands, when mentioned, are inserted as text only and run manually by Sergey.

Required constraints:
Repository file checks do not prove live runtime sync.

Return:
Summary:
Facts used:
Assumptions:
Risks:
Next step:
```

#### K10 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K11 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K12 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K13 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K14 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered

#### K15 - `EMPTY`

- Action: `Empty`
- Setting: `Leave blank`
- Note: Reserved; keep HOME uncluttered
