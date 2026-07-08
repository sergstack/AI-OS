# Merge Gate Owner Checklist

## Purpose

Owner-side verification checklist for the AI-OS Merge Gate.

Repository files define the workflow and CODEOWNERS paths. GitHub branch
protection, rulesets, labels, stale approval dismissal, and direct-push controls
are owner-verified GitHub settings, not Codex-managed settings.

## Expected Merge Gate Behavior

- Tier 0/1 docs-only PRs may auto-merge only through `.github/workflows/auto-merge.yml` after required checks pass.
- Tier 2 protected-path PRs must fail the Merge Gate, disable auto-merge, and receive a bot `request changes` review.
- If a PR changes from Tier 0/1 to Tier 2, the Merge Gate must not continue trusting a previous bot approval or auto-merge state.
- Codex and agents must not manually merge PRs.

## Owner Verification

Confirm in GitHub repository settings:

- Required checks include the validation workflow needed for docs/config safety.
- CODEOWNERS review is required for protected paths in `.github/CODEOWNERS`.
- Stale approval dismissal is enabled when available, so protected-path pushes invalidate earlier approvals.
- Direct pushes and force pushes to `main` are blocked unless explicitly owner-approved.
- Labels used by scheduled digest or triage workflows exist before depending on them.

## Operational Note

The Merge Gate intentionally fails for Tier 2 protected paths. If GitHub rules
make the Merge Gate a required green check for every PR, protected-path PRs may
need an owner-approved ruleset/bypass decision before merge. Do not treat a
failed protected-path Merge Gate as a Codex failure by itself; treat it as the
expected owner-review stop.
