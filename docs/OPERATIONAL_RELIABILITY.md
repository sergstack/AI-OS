# Operational Reliability — кандидатный контракт

[English](OPERATIONAL_RELIABILITY_EN.md) | [Русский](OPERATIONAL_RELIABILITY.md)

## Статус и назначение

Статус: `candidate`. Этот парный документ описывает возможный слой
operational reliability для проверяемой фиксации evidence, run intent, faults и
regressions. Это только documentation contract. Он не создаёт runtime service,
persistent memory, autonomous retrieval, automatic policy change или
production workflow.

Действующие source-of-truth, routing, validation и acceptance rules репозитория
не меняются. Если кандидат когда-либо будет activated, потребуются
identifiable version, evaluation cases, observed results, owner acceptance и
явное scope decision.

## Четыре кандидатных контракта

| Общая механика | Английское название | Русское название |
| --- | --- | --- |
| Жизненный цикл evidence | Evidence lifecycle ledger | Журнал жизненного цикла evidence |
| Намерение запуска | Versioned run intent | Версионированное намерение запуска |
| Наблюдаемость отказов | Typed fault telemetry | Типизированная телеметрия сбоев |
| Превращение сбоя в проверку | Failure-to-regression harness | Контур «сбой → регрессия» |

### 1. Evidence lifecycle ledger

`EvidenceUnit` — ограниченная ссылка на observed evidence, его provenance,
scope и lifecycle status. Точные status names: `ACTIVE`, `SUPERSEDED` и
`REVOKED`.

- `ACTIVE` означает, что unit — текущий referenced evidence для заявленного
  scope; это не означает accepted, complete или production-ready.
- `SUPERSEDED` означает, что позднее identified unit заменяет его в том же
  заявленном scope; раннее evidence остаётся traceable.
- `REVOKED` означает, что на evidence нельзя полагаться для прежнего claim;
  причина и replacement state должны оставаться видимыми.

Этот кандидат не разрешает agent выводить lifecycle status только из текста
или удалять historical evidence.

### 2. Versioned run intent

Run фиксирует goal, scope, constraints, expected evidence и relevant contract
version, которые были авторизованы для его выполнения. Intent versioned, чтобы
поздний читатель отличал результат раннего scope от результата revised scope.

Кандидатное правило — `fail-closed`, когда required intent reference
отсутствует, двусмысленен или несовместим с requested action: остановиться и
сообщить о недостающем решении, а не молча подставлять current intent.

### 3. Typed fault telemetry

Fault record использует named type, affected scope, observed evidence и
disposition. Он делает failures reviewable, не превращая каждое warning в
system-wide policy change. `digest` может суммировать несколько records, но не
должен скрывать их identifiers, scope или unresolved state.

`Candidate Gate` и `Human Gold` остаются точными именами, когда встречаются в
related evaluation context. Это не синонимы; кандидат не меняет ни один gate,
его data, criteria или owner decision.

### 4. Failure-to-regression harness

Когда material evidenced failure исправлен, correction должен сопровождаться
bounded replay или deterministic check, способным обнаружить тот же failure
class. Harness связывает observed fault, correction scope, check и result; он
не утверждает general prevention за пределами этого scope.

Нельзя выдумывать regression test, если failure нельзя воспроизвести,
использовать unrelated passing check как proof correction или автоматически
promote candidate change.

## Границы и activation gate

Этот candidate layer не меняет project routing, owner boundaries, canonical
governance semantics, formulas, model routing или external ChatGPT Project
state. Он не может сам авторизовать merge, deployment, production promotion,
изменение `Candidate Gate` или решение `Human Gold`.

Перед любым activation зафиксируйте: candidate version, target scope,
evaluation cases, Judge results, applied revisions where required, final
acceptance и owner acceptance. До этого authoritative остаются existing
canonical documents: [Goal Mode](../GOAL_MODE.md),
[Sync Contract](../SYNC_CONTRACT.md),
[AES](standards/AUTONOMOUS_EXECUTION_STANDARD.md) и
[Master Status](../MASTER_STATUS.md).
