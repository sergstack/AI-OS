# Implementation Evidence Archive

This directory preserves completed repository implementation packages that no
longer belong in the active `docs/` navigation surface. The packages retain
their original specifications, plans, task lists, scope locks, reviews, and
acceptance records for audit and rollback context.

## Archived Packages

| Package | Repository acceptance at capture | External state at capture |
|---|---|---|
| `aios_dual_surface_phase1/` | `PASS_WITH_LIMITATIONS`; repository implementation delivered | Production promotion remained `no` |
| `thinkers_os_integration/` | Repository-side acceptance complete | External owner acceptance remained pending |
| `thinkers_thinking_integration/` | Repository implementation passed | Manual ChatGPT sync remained an owner handoff |

## Archive Rules

- Treat these files as historical implementation evidence, not current policy.
- Preserve internal path references as records of the original execution
  scope; do not rewrite them merely because the package moved to the archive.
- Use current project instructions, registries, status files, and tests for the
  live repository contract.
- Archive another package only after its acceptance record clearly closes the
  repository-side work and all live path dependencies are updated.
