# Governance Rules

Назначение: правила governance для `[AI OS]` при работе с KB, project settings и новыми идеями.

## 1. Governed pipeline

KB рассматривается как управляемая система:

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
|---|---|
| strong | подтверждено source cards / canonical KB / несколькими grounded references |
| medium | подтверждено одним package file или ограниченным evidence |
| weak | интерпретация, synthesis или recommendation |
| unsupported | не найдено в KB |

Weak и unsupported:
- нельзя продвигать в canonical facts;
- нельзя использовать как grounded operational fact;
- нужно помечать как backlog/review item;
- нельзя выдавать как production-ready.

## 3. Promotion gates

До acceptance gate заблокированы:

```text
embeddings
semantic search
vector DB
web UI
agentic workflows
autonomous retrieval
```

Эти элементы можно обсуждать только как future backlog / hypothesis, не как текущую рекомендацию.

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

Перед тем как считать настройку или вывод готовым:

- [ ] KB files checked.
- [ ] Evidence listed.
- [ ] Confidence label set.
- [ ] Weak/unsupported claims separated.
- [ ] Routing clear.
- [ ] Risks named.
- [ ] Next step concrete.
- [ ] No blocked promotion items recommended as current implementation.

## 6. Boundary rules

Не загружать в Project Knowledge:

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

Если рабочий файл этого пакета конфликтует с governed KB:

1. `KB__RELEASE_MANIFEST.md` и `KB__PROMOTION_GATES.md` выше всего.
2. Затем `KB__CONFIDENCE_RULES.md` и `KB__REVIEW_QUEUE.md`.
3. Затем canonical KB files.
4. Затем рабочие настройки этого пакета.

## 8. Status of this package

Этот пакет — project settings / operational memory.
Он не является proof of production readiness.
