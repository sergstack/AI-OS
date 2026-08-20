# Plan

## Missing inputs

- None.

## Scope assumptions

- Repository-native skill discovery reads `.agents/skills/*/SKILL.md`.
- “Default” means repository and reusable global entry instructions select the orchestrator for AI-OS methodology work; simple local reversible tasks remain local-only.

## Affected files / areas

- `.agents/skills/`
- Root AI-OS entry instructions and command surface
- Reusable global-entry documentation
- Routing contract tests
- Implementation evidence

## Steps

1. Add the canonical orchestrator skill as a thin control layer over routing, the capability registry, and `project-context`.
2. Point default goal intake and the command surface to the orchestrator without copying routing tables.
3. Update contract tests for the second skill and its required behavior.
4. Run focused and repository-wide checks, parse observed results through LDW, and fix safe in-scope failures once.
5. Run an independent Judge review, correct any in-scope defects, rerun affected checks, and record acceptance evidence.

## Dependencies

- Step 2 depends on Step 1.
- Step 3 depends on Steps 1 and 2.
- Step 4 depends on Step 3.
- Step 5 depends on Step 4.

## Risks

- Wording may create a second routing source or weaken fail-closed behavior.
- Existing tests currently assert that only `project-context` exists.

## Validation strategy

- Focused routing-contract tests.
- Full pytest suite and canonical documentation/path/safety checks.
- LDW test parsing, Git facts, evidence build, acceptance check, and independent Judge review.

## Parallel work

- Judge review is independent only after a stable tested diff exists.
