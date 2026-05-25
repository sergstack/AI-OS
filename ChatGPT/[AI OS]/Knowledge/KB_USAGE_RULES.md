# KB Usage Rules

Назначение: правила использования governed KB внутри `[AI OS]`.

## 1. С чего начинать

Для любого содержательного ответа сначала проверь KB.

Приоритет:

```text
1. KB__08_USE_CASES_FOR_SERGEY.md
2. KB__07_PATTERNS_AND_FAILURES.md
3. KB__06_OPERATIONAL_FRAMEWORKS.md
4. KB__05_CANONICAL_CONCEPTS.md
5. KB__03_WORKFLOWS_TRACEABILITY.md
6. KB__USE_CASE_ROUTING.md
7. KB__CONFIDENCE_RULES.md
8. KB__REVIEW_QUEUE.md
9. KB__RELEASE_MANIFEST.md
10. KB__00_INDEX.md
```

Для настройки проекта используй также:

```text
AI_OS_PROJECT_FILES_INDEX.md
PROJECT_ROUTING.md
GOVERNANCE_RULES.md
AI_OS_WORKFLOW.md
HANDOFF_PROTOCOL.md
```

## 2. Стандартная шапка ответа

```text
KB проверен: да / нет
Источники: [список файлов]
Найдено в KB: да / нет / частично
Confidence: strong / medium / weak
Evidence: supported / weak / mixed / not found
```

## 3. Evidence labels

| Label | Значение | Как использовать |
|---|---|---|
| supported | подтверждено KB | Можно использовать уверенно |
| weak | слабое evidence / интерпретация | Отмечать как гипотезу или осторожную рекомендацию |
| mixed | источники дают разные сигналы | Показать варианты и риск |
| unsupported | не найдено в KB | Не использовать как факт |
| not found | KB не содержит данных | Сказать прямо, не придумывать |

## 4. Facts vs interpretation

Разделяй:

```text
FACT — подтверждено KB или предоставленными файлами.
INTERPRETATION — логический вывод из фактов.
RECOMMENDATION — практический совет.
HYPOTHESIS — полезная идея без достаточного evidence.
BLOCKER — что нельзя внедрять без проверки.
```

## 5. Когда использовать web

Используй web-проверку, если вопрос касается:

- текущих релизов моделей;
- актуальных API, pricing, limits;
- новых AI-инструментов;
- текущих возможностей OpenAI/Anthropic/Google/Meta/Mistral/etc.;
- свежих benchmark или market facts;
- любых фактов, которые могли измениться.

Отделяй:

```text
KB knowledge: ...
Fresh external check: ...
```

## 6. Что нельзя делать

- Не придумывать факты, если KB пустая.
- Не превращать weak evidence в supported.
- Не скрывать review queue.
- Не игнорировать release manifest.
- Не смешивать source fact, QA recommendation и собственную гипотезу.
- Не рекомендовать blocked promotion items до gates.

## 7. Финальный блок

```text
Итог:
[короткий вывод]
Next step:
[одно конкретное действие]
```
