# [LLM] Smoke QA

Date: 2026-05-25
Verdict: pass

## Checks

| Test | Expected | Result | Status |
|---|---|---|---|
| Routing test | calculation goes to [Analytics] | LLM routing rules send deterministic calculation to `[Analytics]` | pass |
| Implementation test | implementation goes to [Codex] | handoff rules route code and repo changes to `[Codex]` | pass |
| AI OS evidence test | use [AI OS] for KB evidence | evidence rules point to `[AI OS]` for KB-backed claims | pass |
| Fact / interpretation test | facts separated from interpretation | evidence rules require explicit separation | pass |
| Unsupported claims test | unsupported claims are marked | judge and eval gate require unsupported claims listing | pass |
| Secrets / raw dumps test | reject raw dumps / secrets / .env | context rules forbid them | pass |
| Model class test | choose class by task, not permanent model name | routing matrix uses task class | pass |
| Judge/revise test | high-risk outputs run judge then revise | workflow includes judge and revise before final | pass |
| Codex handoff test | package handoff with acceptance criteria | task package requires objective, files, acceptance, rollback | pass |
| Gemini test | treat Gemini output as candidate sources | KB hunter rules treat Gemini output as candidate sources only | pass |

## Issues found

- none

## Required fixes

- none

## Acceptance status
pass
