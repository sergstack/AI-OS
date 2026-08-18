# Merge Gate Owner Checklist

## Purpose

Owner-side verification checklist for the AI-OS Merge Gate.

Repository files define the workflow and CODEOWNERS paths. GitHub branch
protection, rulesets, labels, stale approval dismissal, and direct-push controls
are owner-verified GitHub settings, not Codex-managed settings.

## Expected Merge Gate Behavior

- Tier 0/1 docs-only PRs may auto-merge only through `.github/workflows/auto-merge.yml` after required checks pass.
- Tier 2 protected-path PRs must disable auto-merge, receive the
  `needs-human-review` label and a bot comment, and remain available for a
  manual owner merge decision without reporting a false CI failure.
- If a PR changes from Tier 0/1 to Tier 2, the Merge Gate must not continue trusting a previous bot approval or auto-merge state.
- Codex and agents must not manually merge PRs.

## Owner Verification

Confirm in GitHub repository settings:

- Required checks include the validation workflow needed for docs/config safety.
- CODEOWNERS paths match the protected-path classifier. In a solo-owner
  repository, do not require an approving review that the PR author cannot
  provide; the owner's manual merge decision is the acceptance action.
- Stale approval dismissal is enabled when approvals are required, so
  protected-path pushes invalidate earlier approvals.
- Direct pushes and force pushes to `main` are blocked unless explicitly owner-approved.
- Labels used by scheduled digest or triage workflows exist before depending on them.

## Operational Note

The Merge Gate classifies and signals owner-review requirements; it does not
replace repository validation or the owner's merge decision. A green Merge
Gate on a Tier 2 PR means classification and signaling completed successfully,
not that the protected change was automatically approved or merged.
