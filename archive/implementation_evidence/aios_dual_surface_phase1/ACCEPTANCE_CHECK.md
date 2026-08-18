# Acceptance Check — AI OS Dual Surface Phase 1 Simplification

## Requirements traceability

| Requirement | Implementation location | Validation evidence | Status | Risk |
|---|---|---|---|---|
| Preserve seven canonical projects | `ChatGPT/[Project]`; protected-path test | All seven paths and Project Instructions present | PASS | Existing unrelated canonical edits remain outside scope |
| Resolver-only registry | `PROJECT_CAPABILITIES.yaml` | Schema test rejects extra semantic fields | PASS | Capability IDs still require canonical routing before lookup |
| Generic bounded context loader | `.agents/skills/project-context/SKILL.md` | Contract test plus six context packages | PASS | Procedural, not sandbox-enforced |
| Remove redundant Skills | `.agents/skills/` | Only `project-context/SKILL.md` remains | PASS | None material |
| Keep routing canonical | Inbox Router routing contract; `AGENTS.md` | Test verifies canonical destinations and root reference | PASS | Instruction-driven judgment remains |
| Preserve five behavioral cases | Runtime context packages | Runs `RUN-f69fe52232dac9ae`, `RUN-04d10c84dcebad8d`, `RUN-dff2f1b03449bd1f`, `RUN-fcf0c3ce2cbd44e3` → `RUN-76e78f43ad0eb3d9`, `RUN-3fa48976b762b94a` | PASS | General classifier correctness is not implied |
| Prevent context explosion/mixing | `project-context`; package provenance | 25 candidates per case; 18–19 excluded | PASS | Caller still supplies deterministic selection signals |
| Targeted/full tests | `tests/test_aios_dual_surface.py`; full suite | Post-documentation runs: 7 targeted, 86 full | PASS | None material |
| Canonical validators | Existing scripts | Baseline: five pass; manifest 122/14 | PASS_WITH_LIMITATIONS | Strict repository-wide validation remains red on existing worktrees |
| Rollback and external gate | Local diff only | No data or external mutation | PASS | Must preserve unrelated worktree changes during rollback |

## Acceptance status

`PASS_WITH_LIMITATIONS`. The strict manifest validator remains at its unchanged baseline 122/14; production promotion remains `no`.
