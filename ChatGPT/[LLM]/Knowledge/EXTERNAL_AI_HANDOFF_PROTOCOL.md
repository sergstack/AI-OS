# External AI Handoff Protocol

## Purpose

Define when to use external AI surfaces and what context package to send.

## Rule

Function first, tool second.

Do not choose a tool because it is fashionable.
Choose a tool because the task requires its surface, context handling, tools, or workflow.

## Surfaces

| Surface | Use when | Inputs | Outputs | Owner project | QA gate |
|---|---|---|---|---|---|
| ChatGPT / Claude Chat | reasoning, alternative judge, revisor, executive writing | compact context, constraints, desired output | critique, rewrite, structured memo | [Thinking] / [LLM] | unsupported claims listed |
| Gemini Deep Research | fresh web / YouTube / creator / repo scouting | research prompt, criteria, scope | sourced research report | [LLM] / [AI OS] | sources checked, hype filtered |
| Codex | implementation, tests, repo hygiene, docs changes | atomic task package | changed files, tests, PR / commit | [Codex] | tests / smoke checks |
| Claude Code | coding agent alternative, repo review, CLAUDE.md workflows, hooks / skills / MCP | task package, allowed files, constraints | code/doc changes, review, PR | [Codex] | diff review and tests |
| Ollama | local memo reasoning over prepared payloads | metrics, signals, evidence cards, prompts | draft memo, local judgement | [Analytics] / [LLM] | deterministic facts preserved |
| Kestra | orchestration of stable workflows | validated scripts, configs, artifact policy | execution, artifacts, run_summary | [Codex] | validation + run_summary |

## Never send

- secrets;
- `.env`;
- API keys;
- raw financial dumps unless explicitly approved;
- source-card dumps;
- raw transcripts;
- chunks;
- vector DB files;
- private client data;
- production credentials.

## Handoff package

Every handoff should include:

- goal;
- owner project;
- context summary;
- allowed inputs;
- forbidden inputs;
- expected output;
- evidence rules;
- acceptance criteria;
- rollback / stop condition.

## Failure modes

- tool chosen before task;
- raw dump sent instead of curated context;
- coding agent given vague wish instead of task package;
- research result accepted without source filtering;
- orchestration marked successful without business validation.
