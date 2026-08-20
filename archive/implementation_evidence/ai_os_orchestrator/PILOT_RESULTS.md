# AI-OS Orchestrator Pilot Results

Status: branch-specific manual contract pilots

Branch: `codex/ai-os-orchestrator`

Base: `origin/main` at `f6d96c4`
Method: apply the branch skill contract to bounded inputs, verify routing against the canonical Inbox Router rules, derive registry matches from `PROJECT_CAPABILITIES.yaml`, and verify paths without loading unrelated content. These are documentation-contract pilots, not proof of client runtime discovery.

## Pilot 1 — one owner and bounded context

- Input: `Сравни варианты решения и порекомендуй один с рисками.`
- Canonical route evidence: strategy / decision / risks / scenarios → `[Thinking]`.
- Registry-derived match: final path component `[Thinking]` uniquely matches capability id `thinking`.
- Path verification: `ChatGPT/[Thinking]`, `PROJECT_INSTRUCTIONS.md`, and `Knowledge/INDEX.md` exist inside the canonical project.
- Context action: owner instructions first; only the indexed decision context required by the goal; all other projects excluded.
- Handoffs: none.
- Result: `pass` — one owner resolved before bounded `project-context` use.

## Pilot 2 — mixed reasoning and implementation

- Input: `Оцени варианты, выбери минимальный безопасный подход и затем реализуй его в репозитории.`
- Current-stage owner: `[Thinking]`, uniquely matched to capability id `thinking`.
- First context action: bounded `[Thinking]` context only.
- Cross-domain need: repository mutation requires an explicit handoff to `[Codex]`, uniquely matched to capability id `codex` only after the reasoning outcome exists.
- Handoff boundary: objective, allowed files/actions, local constraints, checks, rollback, acceptance, and merge policy are required; the result returns for primary-outcome reporting.
- Result: `pass` — no simultaneous multi-owner load; implementation occurs only through explicit handoff.

## Pilot 3 — ambiguous cross-domain goal

- Input: `Разберись с метриками и спроектируй prompt, результат важнее порядка.`
- Canonical candidates: `[Analytics]` and `[LLM]`.
- Missing evidence: no current-stage priority or dependency order selects one destination.
- Context action: none; `project-context` is not invoked and Inbox Router is not used as a fallback for conflicting candidates.
- Result: `blocked` — request the smallest missing decision: which outcome is primary or which stage comes first.

## Pilot 4 — missing canonical path

- Input: a strategy goal routed to `[Thinking]` against a fixture where the registry entry remains but its canonical directory is absent.
- Registry-derived match: exactly one capability id, `thinking`.
- Path verification: fails before owner instructions or any Knowledge file is read.
- Context action: none; no substitute path or nearby project is selected.
- Result: `blocked` — report the missing canonical directory and require registry/checkout repair.

## Acceptance summary

- One-owner resolution: pass.
- Registry-derived label matching: pass.
- Bounded context after routing: pass.
- Explicit cross-capability handoff: pass.
- Ambiguous routing fail-closed: pass.
- Missing canonical path fail-closed: pass.
- Runtime discovery/reload across already-open clients: not tested; remains a documented limitation.
