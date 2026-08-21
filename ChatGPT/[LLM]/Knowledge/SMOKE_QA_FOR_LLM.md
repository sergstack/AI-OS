# [LLM] Smoke QA

Date: 2026-08-21
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

## Cross-project live coverage

Matrix: `CROSS_PROJECT_LIVE_EVAL_MATRIX.md` (`LLM-XPROJECT-LIVE-001`,
`1.0.0-candidate`).

| Live case | Result | Evidence |
|---|---|---|
| `[Inbox Router]` → `[LLM]` | pass, 9/10 | strong single route, bounded handoff, target workflow not solved in the router |
| `[AI OS]` → `[LLM]` | revise, 8/10 latest completed | ownership fixed; handoff shrank 48%, but remains above compact target |
| `[LLM]` compact asset | pass, 10/10 post-change | 3,389 visible characters; prompt, gates, registry and handoffs preserved |
| `[Thinking]`, `[Analytics]`, `[Codex]`, `[Thinkers OS]` | not run | ChatGPT rate limit prevented completed observable responses |

Static smoke QA remains `pass`. Cross-project live coverage is `partial`; a
rate-limited case is not a product failure and is not evidence for changing
Project Instructions.

## Issues found

- the reproduced AI OS/LLM scope-boundary defect is resolved in two completed reruns;
- the temporary AI OS compactness cap was rolled back; the replacement preserves
  executable handoff context without an arbitrary length limit, pending a clean live rerun;
- the reproduced LLM compactness defect is resolved by a 3,389-character post-change pass;
- four live cases remain unobserved because of an external ChatGPT rate limit.

## Required fixes

- rerun the synchronized AI OS compact override after a clean cooldown; do not widen it after three correction attempts;
- rerun only the four `NOT RUN` cases after the rate limit clears;
- make no other Project behavior change without a reproduced defect.

## Acceptance status
static pass; cross-project live coverage partial
