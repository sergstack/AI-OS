# Second Opinion — AI OS Dual Surface Phase 1 Simplification

## Problem restatement

Codex needs canonical project discovery and bounded context loading without maintaining a parallel copy of routing, methodology, or governance.

## Compared approaches

1. Keep six Skills and task-type routing in the registry.
2. Keep a location-only registry and one generic `project-context` Skill.
3. Add an independent runtime classifier.

## Assessment

- Approach 1 duplicates canonical contracts and creates synchronized-maintenance risk.
- Approach 2 preserves observed behavior with the smallest integration layer.
- Approach 3 could add technical routing evidence but would violate the current scope and create another routing framework.

## Recommendation

Use approach 2. Keep instruction-driven canonical routing explicit and do not imply independent classifier or technical enforcement.
