# [AI OS] — Governance and Evidence

## Purpose

Compact upload artifact for [AI OS] covering governance and evidence.

## Source files

- `ChatGPT/[AI OS]/Knowledge/GOVERNANCE_RULES.md`
- `ChatGPT/[AI OS]/Knowledge/ANTI_PATTERNS.md`
- `AUTONOMOUS_EXECUTION_STANDARD.md`
- `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:bd0884e394431e20bc24ac2b2f2fe00dd1686c454e9db2082a90aaf545606783

---

# Content

## From: `ChatGPT/[AI OS]/Knowledge/GOVERNANCE_RULES.md`

# Governance Rules
## 1. Governed pipeline
```text
source material
→ source cards / clean notes
→ concept / workflow / pattern extraction
→ grounded synthesis
→ publish package
→ compact package
→ smoke QA
→ acceptance check
→ next scope decision
→ use-case routing
```
Smoke QA — это не финальная готовность. Финальная готовность требует acceptance status, residual risks, known gaps, next scope и routing.
## 2. Confidence rules
| Confidence | Значение |
| medium | подтверждено одним package file или ограниченным evidence |
- нельзя продвигать в canonical facts;
- нельзя использовать как grounded operational fact;
- нужно помечать как backlog/review item;
- нельзя выдавать как production-ready.
## 3. Promotion gates
```text
embeddings
semantic search
vector DB
web UI
agentic workflows
autonomous retrieval
```
## 3A. Karpathy-inspired minimal verifiable loop
Status: candidate governance pattern.
Evidence: adapted pattern, not canonical AI OS production rule.

Use as anti-bloat check:
```text
input → minimal transformation → QA → output → acceptance → revisit
```

Promotion rule:
- evidence status recorded;
- 3 pilot cases passed;
- no new folder, mode, automation, dashboard, agent, or broad workflow added;
- routing remains unchanged;
- rollback rule exists.

Do not use this pattern to justify autonomous retrieval:
- embeddings / vector DB;
- semantic search;
- web UI;
- agentic workflows;
- broad refactoring.

## 4. Review queue
Если обнаружено weak/unsupported/mixed evidence:
```text
Review item:
- claim:
- source files checked:
- evidence status:
- risk if used:
- recommended action:
- owner project:
```
## 5. Acceptance checklist
- [ ] KB files checked.
- [ ] Evidence listed.
- [ ] Confidence label set.
- [ ] Weak/unsupported claims separated.
- [ ] Routing clear.
- [ ] Risks named.
- [ ] Next step concrete.
- [ ] No blocked promotion items recommended as current implementation.
## 6. Boundary rules
- raw transcripts;
- source card dumps без packaging;
- clean notes dumps;
- chunks;
- temp files;
- logs;
- runtime artifacts;
- embeddings;
- vector DB;
- secrets;
- API keys;
- zip archives как knowledge source.
## 7. Conflict rule
1. `KB__RELEASE_MANIFEST.md` и `KB__PROMOTION_GATES.md` выше всего.
2. Затем `KB__CONFIDENCE_RULES.md` и `KB__REVIEW_QUEUE.md`.
3. Затем canonical KB files.
4. Затем рабочие настройки этого пакета.
## 8. Status of this package


## Autonomous Execution Standard

`[AI OS]` is the canonical owner of the Autonomous Execution Standard (AES).
Execution across all projects now also follows the canonical loop defined in
`AUTONOMOUS_EXECUTION_STANDARD.md` at the repo root: requirements -> execution
-> validation -> defect registration -> corrective action -> affected-scope
rerun -> revalidation -> scope acceptance -> final evidence. It does not
replace Goal Mode, routing, autonomy policy, or the merge policy in
`GOAL_MODE.md`; it connects them into one closed loop, and the stricter rule
wins on any conflict. `[AI OS]` also owns the generic project-extension
interface in `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`, which a project
implements to add domain-specific defect subtypes, evidence, and acceptance
scopes without restating the canonical state machine or schema.

After routing resolves a primary owner for a material decision or deliverable,
an upstream project may prepare evidence, contradictions, options, risks, and a
bounded handoff, but it must not silently replace that owner. The handoff keeps
the affected decision boundary, requirements, constraints, acceptance, and
first safe step so the receiving owner can continue without re-decomposing the
goal.

## From: `ChatGPT/[AI OS]/Knowledge/ANTI_PATTERNS.md`

# Anti-patterns
## Knowledge anti-patterns
| Выдать weak evidence как supported | Нарушение governance | Пометить weak и отправить в review queue |
| Игнорировать `KB__RELEASE_MANIFEST.md` | Можно принять blocked статус за ready | Проверить release status |
## Routing anti-patterns
| Давать Codex размытое пожелание | Codex can use Goal Mode build-first and infer bounded safe scope | Передать цель с constraints; scoped task package нужен только для strict/high-risk work |
## Promotion anti-patterns
```text
embeddings
semantic search
vector DB
web UI
agentic workflows
autonomous retrieval
```
```text
Это future backlog / hypothesis. Внедрять только после acceptance gate и clearing review queue.
```
## Response anti-patterns
- длинная теория без применения к работе Сергея;
- отсутствие confidence/evidence;
- нет risks/limitations;
- нет next step;
- нет routing при выходе за scope;
- скрыта неопределённость;
- нет web-проверки для текущих AI-релизов.
