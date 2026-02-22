# Git Basics Quick Reference

**Category:** Version Control
**Last Updated:** 2026-02-14

---

## Common Commands

```bash
# Check status
git status

# Stage changes
git add .
git add file.txt

# Commit with message
git commit -m "Your message"

# Push to remote
git push

# Pull latest changes
git pull

# View commit history
git log --oneline -10
```

---

## Key Concepts

- **Working Directory**: Your actual files
- **Staging Area**: Files ready to commit (git add)
- **Repository**: Committed history (git commit)
- **Remote**: GitHub/GitLab server (git push/pull)

---

## Best Practices

1. Commit often with clear messages
2. Pull before you push
3. Use branches for features
4. Never commit sensitive data (.env files)

---

## Common Pitfalls

❌ **Don't do this**
```bash
git add .
git commit -m "updates"  # Vague message
```

✅ **Do this instead**
```bash
git add .
git commit -m "feat: add user authentication endpoint"
```

---

## Examples

### Daily Workflow
```bash
git status              # Check what changed
git add .               # Stage all changes
git commit -m "fix: resolve login bug"
git push                # Push to remote
```

### Branch Workflow
```bash
git checkout -b feature/new-feature
# ... make changes ...
git add .
git commit -m "feat: add new feature"
git push -u origin feature/new-feature
```

---

## Related Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)

---

*Quick reference for common Git operations*
