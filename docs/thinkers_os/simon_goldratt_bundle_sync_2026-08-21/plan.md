# Plan

## Missing inputs

- None.

## Scope assumptions

- Simon and Goldratt remain isolated Judge-pass patterns; cross-author synthesis is not performed.

## Affected files / areas

- Thinkers OS current status, synthesis source, bundles 01/02, and upload list.
- Thinking bundle 04.
- This run's documentation.

## Steps

1. Record the bounded worktree scope and baseline.
2. Update the Thinkers OS granular status and synthesis projection.
3. Update Thinkers OS bundles 01/02 and Thinking bundle 04.
4. Recalculate affected source fingerprints and upload-list fingerprints.
5. Run focused and repository bundle-safety checks.
6. Complete acceptance, commit the exact files, push the branch, and open a non-draft PR.
7. Observe the GitHub Merge Gate and report the resulting merge status.

## Dependencies

- Step 3 depends on Step 2.
- Step 4 depends on Steps 2–3.
- Step 5 depends on Step 4.
- Steps 6–7 depend on passing checks.

## Risks

- Merge Gate or required checks may require external owner action.

## Validation strategy

- Use repository-native bundle, public-safety, manifest, index, and focused pytest checks; verify diff and Git state before commit.

## Parallel work

- None.
