# 🚀 Quick Commands - GitHub Contribution Workflow

## Setup Awal (One-time)

```bash
# 1. Fork repo owner di GitHub web

# 2. Clone fork mu
git clone https://github.com/USERNAME/REPO.git
cd REPO

# 3. Add upstream (original repo)
git remote add upstream https://github.com/OWNER/REPO.git

# 4. Verify
git remote -v
# Harus ada:
# origin    → fork mu
# upstream  → original repo
```

---

## Setiap Kali Mau Kontribusi

### 1. Persiapan
```bash
# Pull latest dari original repo
git fetch upstream
git pull upstream main  # atau master

# Buat branch baru
git switch -c feat/deskripsi-fitur
# atau: git checkout -b feat/deskripsi-fitur
```

### 2. Develop
```bash
# Edit files, develop feature

# Check status
git status

# Stage changes
git add .
# atau selektif:
git add file1.js file2.js

# Commit dengan message meaningful
git commit -m "feat: tambahkan fitur X"
# atau
git commit -m "fix: handle null case pada function Y"
```

### 3. Testing & Documentation
```bash
# Jalankan tests (kalau ada)
npm test
# atau
pytest
# atau
cargo test

# Linting (kalau ada)
npm run lint
# atau
pylint .

# Format code (kalau ada)
npm run format
# atau
black .
```

### 4. Push & Create PR
```bash
# Sync dengan upstream dulu
git fetch upstream
git rebase upstream/main
# kalau ada conflict, resolve dan:
# git add .
# git rebase --continue

# Push ke fork
git push origin feat/deskripsi-fitur

# Atau set upstream tracking:
git push -u origin feat/deskripsi-fitur

# Buka GitHub, PR otomatis ditawarkan
# Atau manual: https://github.com/USERNAME/REPO → New Pull Request
```

---

## During Review (Owner memberikan feedback)

```bash
# Pull latest feedback (if any changes)
git pull origin feat/deskripsi-fitur

# Make changes
# Edit files, fix issues dari feedback

# Commit changes
git commit -am "refactor: address feedback"

# Push
git push origin feat/deskripsi-fitur
# PR automatically update dengan commit baru
```

---

## Merge & Cleanup

```bash
# Tunggu owner merge (atau merge sendiri kalau punya permission)

# Pull latest main
git pull upstream main

# Delete local branch
git branch -d feat/deskripsi-fitur

# Delete remote branch (optional)
git push origin --delete feat/deskripsi-fitur

# Cleanup tracking branches
git fetch upstream --prune
```

---

## Common Issues & Fixes

### Merge Conflict
```bash
# Jika ada conflict sebelum push:
git fetch upstream
git rebase upstream/main

# Resolve conflicts di text editor, then:
git add .
git rebase --continue
git push origin feat/deskripsi-fitur
```

### Undo Last Commit (tapi keep changes)
```bash
git reset --soft HEAD~1
```

### Undo Specific File
```bash
git checkout HEAD -- filename.js
```

### Stash Changes (temporary save)
```bash
git stash
# do something else
git stash pop
```

### Squash Multiple Commits
```bash
# Before push:
git rebase -i upstream/main

# Di editor: pilih "squash" untuk combine commits
# Then force push:
git push -f origin feat/deskripsi-fitur
```

### Update Fork dari Upstream
```bash
git fetch upstream
git merge upstream/main
git push origin main
```

---

## PRE-RELEASE QUICK CHECK

```bash
# ✅ Code quality
npm run lint
npm run format --check

# ✅ Testing
npm test

# ✅ No debug code
grep -r "console.log\|debugger" src/
# Should return nothing!

# ✅ Check git status
git status
# Should be clean (nothing to commit)

# ✅ Review last commits
git log --oneline -10

# ✅ Check if up-to-date
git fetch upstream
git log --oneline main..upstream/main
# If empty = you're up-to-date

# ✅ Documentation check
# - README updated? ✓
# - CHANGELOG updated? ✓
# - Comments added? ✓
```

---

## Git Config (Recommended)

```bash
# Set identity (one-time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Better diff format
git config --global diff.algorithm histogram

# Auto-fix whitespace
git config --global apply.whitespace fix

# Useful aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
git config --global alias.visual "log --graph --oneline --all"

# Usage:
git st        # same as: git status
git co main   # same as: git checkout main
git visual    # pretty log
```

---

## Useful Commands

### View Changes
```bash
# See what changed in current branch
git diff upstream/main

# See commits in current branch
git log upstream/main..HEAD

# See all branches
git branch -a

# See branch info
git log --graph --oneline --all --decorate
```

### Undo Things
```bash
# Undo last push (careful!)
git push -f origin HEAD~1:feat/branch

# Undo all changes (⚠️ irreversible)
git reset --hard HEAD

# Undo git add (unstage)
git reset HEAD filename

# See what was deleted
git reflog
```

---

## Checklist Before ajuin PR

```
☐ Latest code pulled dari upstream
☐ Branch created dari updated main
☐ Kerjain fitur selesai
☐ All tests pass: npm test
☐ Linting pass: npm run lint
☐ No console.log atau debugger
☐ README updated (kalau diperlukan)
☐ CHANGELOG updated
☐ Commit messages meaningful
☐ Synced dengan upstream (no conflict)
☐ PR description lengkap
☐ Ready untuk diserah ke owner!
```

---

## Good Commit Message Examples

```
✅ GOOD:
git commit -m "feat: add dark mode toggle"
git commit -m "fix: handle null error in getUserData"
git commit -m "docs: update installation guide"
git commit -m "refactor: extract component logic"
git commit -m "test: add unit tests for utils"

❌ BAD:
git commit -m "update"
git commit -m "fix bug"
git commit -m "work in progress"
git commit -m "asd"
git commit -m "oops typo"
```

---

## Git Flow Overview

```
You (Fork)                    Owner (Original)
   |                               |
   ├─ git clone ────────────────→ |
   ├─ git add upstream ────→ Owner's repo
   |
   ├─ Create branch: feat/X
   ├─ Make commits
   ├─ git push → your fork
   ├─ Create PR ──────────────→ |
   |                               |
   |                           Owner reviews
   |                               |
   | ← Owner requests changes ─────┤
   ├─ Make more commits
   ├─ git push ────────────────→ |
   |                               |
   |                         Approved! ✅
   |                               |
   |                    Owner clicks Merge
   |                         (on GitHub)
   |
   ├─ git pull upstream/main
   └─ Done! 🎉
```

---

## Troubleshooting

### "Permission denied (publickey)"
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "email@example.com"

# Add to GitHub: Settings → SSH and GPG keys
# Add content of ~/.ssh/id_ed25519.pub
```

### "You don't have permission to push to..."
```bash
# Check if using right fork (your username)
git remote -v

# Or use HTTPS instead of SSH
git remote set-url origin https://github.com/USERNAME/REPO.git
```

### "fatal: could not read Username"
```bash
# Cache credentials (HTTPS)
git config --global credential.helper store
# Then enter password once, saved

# Or use SSH key (recommended)
# See "Permission denied" solution above
```

---

## Useful Resources

- Git documentation: https://git-scm.com/doc
- GitHub's guide: https://guides.github.com/
- Commit conventions: https://www.conventionalcommits.org/
- Keep a changelog: https://keepachangelog.com/
