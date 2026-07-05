# Sync Contract

## Source of Truth

GitHub is the live source of truth for AI-OS repository state.

ChatGPT Project Knowledge is a bootloader/cache: it provides baseline instructions and stable upload bundles, but it is not assumed to be current after every repository change.

## Fresh State

For fresh state, ChatGPT and Codex should read GitHub or repository files directly.

Codex reads the repository and obeys root `AGENTS.md` plus any task-specific instructions. Project Instructions stay compact as behavior kernels; detailed workflows and reusable knowledge live in repository files and Knowledge bundles.

## Knowledge Bundles

Knowledge Bundles are upload baselines, not live sync.

If source Knowledge changes, update or regenerate the matching bundle consistently before using it as a ChatGPT Project Knowledge upload artifact.

## Manual ChatGPT Sync

Manual ChatGPT UI upload remains a periodic formal sync for stable baselines. It is not the default day-to-day synchronization method and should not be required for every small repository change.

Daily fresh state should be read from GitHub or repository files.

Before a PR, run repository validation or `python3 scripts/sync_aios.py`. This script is a sync readiness/check helper: it validates repository consistency and prints guidance, but does not upload to ChatGPT, push to GitHub, or perform external sync.
