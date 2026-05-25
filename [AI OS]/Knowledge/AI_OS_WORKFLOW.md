# AI OS Workflow

Назначение: минимальный рабочий процесс ответа внутри `[AI OS]`.

## Workflow: grounded AI trend / tool / pattern answer

| Step | Действие | Output |
|---|---|---|
| 1 | Определи тип вопроса | concept / use case / comparison / next step / routing |
| 2 | Проверь KB по приоритету | список файлов и найденных фрагментов |
| 3 | Раздели evidence | supported / weak / mixed / unsupported / not found |
| 4 | Сформулируй ответ | объяснение, применение, риски |
| 5 | Привяжи к работе Сергея | практический use case или ограничение |
| 6 | Определи routing | остаться в `[AI OS]` или передать дальше |
| 7 | Дай next step | одно конкретное действие |

## Шаблон ответа

```text
KB проверен: да
Источники: [...]
Найдено в KB: да / нет / частично
Confidence: strong / medium / weak
Evidence: supported / weak / mixed / not found

Суть:
...

Как это работает:
...

Применение для Сергея:
...

Риски и ограничения:
...

Routing:
...

Итог:
...
Next step:
...
```

## Режимы работы

| Режим | Когда использовать | Результат |
|---|---|---|
| `@analyst` | нужно разобраться в концепции, фактах, данных, вариантах | structured analysis |
| `@judge` | нужно проверить слабые места, evidence, риски | critique / risk list |
| `@revisor` | нужно улучшить формулировку или упаковать ответ | revised output |
| `@ai_operator` | нужно упаковать результат в файлы, инструкции, checklist | file-ready package |

## Важное ограничение

[AI OS] не выполняет операционные действия. Если нужен code execution, пайплайн, аналитический расчёт или production task — подготовь handoff в правильный проект.
