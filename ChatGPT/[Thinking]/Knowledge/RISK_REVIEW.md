# Risk Review

## Use when

- решение дорогое;
- последствия трудно откатить;
- evidence неполный;
- есть operational или reputational risk;
- задача передаётся в Codex.

## Checklist

| Area | Questions |
|---|---|
| Assumptions | Что мы считаем правдой без проверки? |
| Evidence | Какие выводы supported, weak, unsupported? |
| Reversibility | Можно ли откатить решение? |
| Blast radius | Что сломается при ошибке? |
| Dependencies | От кого/чего зависит успех? |
| Timing | Почему сейчас? Что изменится позже? |
| QA | Как понять, что решение сработало? |
| Stop conditions | Когда остановиться? |

## Output

```text
Risk level: low / medium / high
Main blocker:
Weak assumptions:
Mitigations:
Decision: proceed / revise / stop / handoff
```
