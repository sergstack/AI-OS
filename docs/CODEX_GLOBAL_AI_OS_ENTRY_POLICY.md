# Global Codex AI OS Entry Policy

## Status

- Capability: accepted in one local Codex environment.
- Validation: 7/7 local checks passed.
- Observed: cross-repository routing to strategy, analytics, and LLM methodology with no manual routing or repeated context.
- Scope: reusable user-level Codex setup guidance, not a production platform or universal guarantee.

Local runtime configuration and repository documentation are separate:

```text
local user configuration != repository canonical documentation
```

Do not commit a user's `$CODEX_HOME/AGENTS.md`, overrides, configuration, backups, trust entries, session traces, or machine-specific paths. This document records only the reusable contract.

## Purpose

The global entry policy gives Codex a small routing decision at the start of work without copying AI-OS methodology into every repository:

```text
Codex task
   ↓
user-level global entry policy
   ↓
simple local task?
   ├─ yes → local repository rules
   └─ no
       ↓
canonical AI-OS routing
       ↓
appropriate project methodology
       ↓
local repository constraints
       ↓
bounded implementation / QA
```

The global file is an entry policy only. The AI-OS repository remains the single canonical source for routing, project ownership, methodology, and governed knowledge.

## Ownership boundaries

| Layer | Owns |
|---|---|
| Global user-level policy | Decide whether canonical AI-OS methodology is needed and initiate bounded context loading. |
| AI-OS repository | Canonical routing, `PROJECT_CAPABILITIES.yaml`, project methodology, `project-context`, evidence, and governance. |
| Local repository | Repository facts, codebase structure, commands, tests, business contracts, protected areas, and implementation constraints. |

The global policy must not create another routing registry, copy domain Knowledge, install a second project-context implementation, or weaken local constraints.

## Instruction precedence

Use this precedence:

```text
system / developer / safety / explicit user instruction
>
more-specific applicable local repository instructions
>
global user-level AI OS entry policy
```

Codex discovers global guidance in `$CODEX_HOME` and then layers project guidance from the repository root toward the current working directory. More-specific project guidance appears later in that instruction chain. See the official [OpenAI AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

The global policy cannot authorize a locally prohibited change. For example, if AI-OS methodology identifies an architectural option but a local `AGENTS.md` protects the affected module, the module remains protected.

## Canonical checkout resolution

Use `<LOCAL_AI_OS_ROOT>` as an installation-time placeholder for the user's canonical AI-OS checkout. Do not treat the placeholder as a runtime environment-variable contract unless the local Codex setup explicitly supplies one.

Before loading AI-OS context, verify that the resolved checkout contains:

```text
<LOCAL_AI_OS_ROOT>/AGENTS.md
<LOCAL_AI_OS_ROOT>/PROJECT_CAPABILITIES.yaml
<LOCAL_AI_OS_ROOT>/.agents/skills/project-context/SKILL.md
```

Then:

1. Read the canonical repository instructions.
2. Resolve the primary capability through the existing `PROJECT_CAPABILITIES.yaml`.
3. Follow the canonical `project-context` skill.
4. Load only the selected task-relevant context.
5. Load another capability only for an explicit cross-domain handoff.

Do not add a new resolver solely for this setup. If the checkout moves, update the installed global policy with the new local path.

If the checkout is unavailable, state that cross-domain AI-OS methodology was not loaded, continue only where local rules are sufficient and safe, and never invent or substitute canonical context.

## Sanitized global template

Replace `<LOCAL_AI_OS_ROOT>` during installation. Keep the installed file compact.

```markdown
# Global AI OS Entry Policy

Canonical AI-OS checkout: `<LOCAL_AI_OS_ROOT>`

For every task:

1. Read and obey applicable local repository instructions.
2. Determine whether the task is simple local reversible work or material strategy, analytics, LLM, AI-evidence, or cross-domain work.
3. For simple local work with sufficient repository context, use local repository instructions directly and do not activate AI-OS.
4. For material cross-domain work, verify the canonical AI-OS checkout, read its `AGENTS.md`, and use its existing routing and `PROJECT_CAPABILITIES.yaml` to select one primary capability.
5. Follow the canonical `.agents/skills/project-context/SKILL.md` and load only the required project context.
6. Preserve all local repository facts, protected areas, commands, tests, contracts, and implementation constraints.
7. Before implementation following strategy or analysis, make a bounded handoff with owner, outcome, allowed scope, local constraints, checks, rollback, and acceptance criteria.
8. Do not duplicate AI-OS routing, methodology, Knowledge, skills, or registry content in this global file or in local repositories.
9. If canonical AI-OS context is unavailable, state the limitation and continue only where local rules are sufficient and safe.
```

## Installation

1. Locate the effective Codex home directory. Use `CODEX_HOME` when explicitly set; otherwise use the Codex default.
2. Inspect `$CODEX_HOME/AGENTS.md`, `$CODEX_HOME/AGENTS.override.md`, and `$CODEX_HOME/config.toml` before changing anything.
3. Determine which global instruction file is active. Codex uses `AGENTS.override.md` when it is present and non-empty; otherwise it uses `AGENTS.md`.
4. Create a reversible backup of the active global instruction file. Preserve permissions where applicable.
5. Install or update the minimal template in the intended active file. Substitute the verified canonical checkout path for `<LOCAL_AI_OS_ROOT>`.
6. Do not copy user configuration, domain Knowledge, the capability registry, or canonical skills from the repository into `$CODEX_HOME`.
7. Start a fresh Codex task or session. Instruction discovery occurs when a run starts; an already-open session is not guaranteed to reload changed global instructions.
8. Run the acceptance cases below and record observed results.

If an existing global policy contains unrelated user requirements, merge intentionally rather than overwriting them without review.

## Canonical smoke cases

### Case A — local-only

Input:

```text
Исправь локальный Python bug.
```

Expected: AI-OS heavy routing is not activated and local repository rules remain authoritative.

### Case B — strategy

Input:

```text
Изучи проект и предложи варианты, как его стратегически прокачать.
```

Expected: local repository context plus canonical Thinking methodology.

### Case C — analytics

Input:

```text
Проанализируй изменение финансового показателя и проверь расчёт.
```

Expected: local data plus canonical Analytics methodology. Numeric work remains deterministic and follows applicable local data controls.

### Case D — LLM workflow

Input:

```text
Улучши prompt/workflow для этой задачи.
```

Expected: local project context plus canonical LLM methodology.

### Case E — mixed reasoning and implementation

Input:

```text
Сначала разберись в проблеме и вариантах, после выбора минимального решения реализуй его.
```

Expected:

```text
Thinking
→ bounded handoff
→ local Codex execution
```

Also verify these adversarial conditions:

- a local repository rule conflicts with a methodology recommendation;
- the canonical checkout is unavailable;
- the task is simple enough that AI-OS would be unnecessary overhead;
- a mixed task crosses from reasoning to implementation;
- a nested local `AGENTS.md` is stricter than its repository root.

For each case, record at least:

```text
raw_request
cwd/repository
global_policy_loaded
local_AGENTS_loaded
AI_OS_used
resolved_AI_OS_owner
canonical_context_loaded
local_constraints_preserved
manual_routing_required
context_repetition_required
result
```

Acceptance targets are zero manual routing, zero repeated context, and zero local-constraint violations.

## Observed local validation record

The initial user-level installation recorded:

```text
simple local task: PASS
strategy → Thinking: PASS
analytics → Analytics: PASS
LLM workflow → LLM: PASS
nested local precedence: PASS
mixed Thinking → local Codex: PASS
AI-OS unavailable behavior: PASS
manual orchestration: 0
context repetition: 0
```

This is evidence from one local Codex environment. It does not prove general correctness across every repository, operating system, Codex version, or future instruction-discovery implementation.

## Rollback

User-level configuration rollback:

1. Restore the previous active global instruction file from its backup.
2. Start a fresh Codex task or session.
3. Verify simple local behavior before resuming cross-domain work.

Repository documentation rollback: revert the documentation commit or pull request. Repository rollback does not modify a user's installed `$CODEX_HOME` files.

## Known limitations

- Validation currently covers one user environment.
- Exact instruction discovery and runtime behavior belong to the Codex platform and may evolve.
- Canonical checkout path configuration is installation-specific.
- Already-open sessions are not guaranteed to reload changed global instructions.
- A global entry policy reduces repeated manual routing; it is not a deterministic universal router.
- Passing the smoke set does not authorize production promotion or weaken repository-specific review gates.
