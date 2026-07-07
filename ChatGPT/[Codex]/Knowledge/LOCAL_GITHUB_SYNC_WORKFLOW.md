# Local GitHub Sync Workflow

## Purpose

Keep local repo, branch, commit, pushed branch, and PR aligned.

## Preconditions

- local path is known;
- remote is correct;
- working tree is clean or dirty files are understood;
- task package defines allowed files;
- branch name is defined.

## Standard flow

```bash
cd "<LOCAL_REPO>"

git remote -v
git status --short --branch
git fetch origin
git switch main
git pull --ff-only origin main

git switch -c <branch>
```

If branch exists:

```bash
git switch <branch>
git rebase main
```

## Before editing

```bash
git status --short --branch
```

Stop if dirty files are outside allowed scope.

## After editing

```bash
git status --short --branch
git diff --stat
git diff --check
git diff -- <allowed_paths>
```

Run task-specific tests/checks.

## Commit

```bash
git add <allowed_paths>
git commit -m "<type>: <summary>"
```

## Push and PR

```bash
git push -u origin <branch>
```

Create PR with:

- summary;
- changed files;
- checks run;
- assumptions;
- risks;
- rollback;
- acceptance status.

## After merge

```bash
git switch main
git pull --ff-only origin main
git branch -d <branch>
```

If remote branch remains:

```bash
git push origin --delete <branch>
```

## Rollback

Before any rollback:

```bash
git status
```

For local file restoration before commit:

```bash
git restore --source=HEAD -- <allowed_paths>
```

For pushed commits or merged PRs:

```bash
git revert <commit_or_merge_sha>
```

Do not use destructive rollback commands as the default. Commands such as
`git reset --hard` require explicit human confirmation and a clean
understanding of what uncommitted work would be lost.

## Hard blockers

These are local GitHub sync blockers in addition to the canonical hard blockers in `AUTONOMY_POLICY.md`. Stop if:

- remote does not match expected repo;
- local branch has unrelated dirty files;
- pull requires non-fast-forward merge;
- branch contains unrelated commits;
- PR would include files outside allowed scope.
