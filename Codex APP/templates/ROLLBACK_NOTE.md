# Rollback Note

## Change to rollback

## Reason

## Safe rollback command / steps

Start with:

```bash
git status
```

For local file restoration, prefer:

```bash
git restore --source=HEAD -- <path>
```

For pushed commits, prefer:

```bash
git revert <commit>
```

Do not use destructive rollback commands by default. Commands such as
`git reset --hard` require explicit human confirmation and a clear check for
uncommitted work that would be lost.

## Data or artifact impact

## Verification after rollback
