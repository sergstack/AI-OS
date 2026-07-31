# Routing and Handoff

## Ownership boundaries

| Request | Route |
|---|---|
| author portfolio, required corpus, source request/intake, author artifacts | `[Thinkers OS]` |
| Lens Router, Conflict Map, cross-author synthesis maintenance | `[Thinkers OS]` |
| apply thinker patterns to a real decision, conflict, strategy, or scenario | `[Thinking]` |
| extraction prompt, model selection/routing, reusable LLM workflow | `[LLM]` |
| quantitative validation, formulas, metrics, models, before/after calculation | `[Analytics]` |
| repository implementation, schemas, automation, validators, tests | `[Codex]` |
| general reusable AI governance promotion decision | `[AI OS]` |

`[Thinkers OS]` prepares bounded handoffs; it does not absorb the receiving project's work.

## Handoff contract

Use one receiving project and these canonical fields:

```text
From:
To:
Task type:
Mode: goal / strict
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Evidence / confidence:
Open questions:
Suggested first step:
```

Add author/corpus coverage, source artifact, Judge status, and transfer risk when the handoff uses thinker evidence.

## Handoff gates

- No Judge-pass pattern: do not export.
- Partial corpus: label the handoff bounded/partial and name the missing P1 gap.
- Quantitative claim: require `[Analytics]` evidence.
- Repository mutation: require `[Codex]` scope, checks, rollback, and acceptance.
- External Project sync: manual owner action unless explicitly authorized.

Forbidden inputs include secrets, raw/normalized books, excerpt dumps, source manifests, logs, local paths, and blocked/rejected artifacts.
