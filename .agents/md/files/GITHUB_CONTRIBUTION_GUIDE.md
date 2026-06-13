# GitHub Contribution Guide - Pre-Release Checklist

## ⚡ Quick Summary
Gw buat kontribusi ke GitHub repo orang, step-nya:
1. **Fork** repo → **Clone** ke lokal → **Branch baru** → **Kerjain** → **Test**
2. **Push** ke fork → **Buat PR** → **Tunggu review** → **Fix feedback** → **Merge**

---

## 🔍 CHECKLIST PRE-RELEASE (Sebelum ajuin PR)

### ✅ Code Quality
- [ ] **Tidak ada `console.log`, `debugger`, atau unused code**
- [ ] **Linting pass** (jalankan linter kalau ada: `npm run lint` atau `eslint .`)
- [ ] **Code formatting consistent** (prettier/fmt: `npm run format`)
- [ ] **Variabel & function names jelas** (bukan `a`, `temp`, `x`)
- [ ] **Comments hanya untuk logic yang non-obvious**, bukan narasi kode
- [ ] **Error handling ada** (try-catch, fallback, validation)

### ✅ Testing
- [ ] **Test di lokal** (buka dev server, test setiap fitur)
- [ ] **Semua happy path work** (case normal)
- [ ] **Edge cases tested** (empty input, null, boundary values)
- [ ] **Browser compatibility** (kalau relevant: Chrome, Firefox, Safari)
- [ ] **Mobile/responsive tested** (kalau UI)
- [ ] **Tidak ada console errors atau warnings**

### ✅ Documentation
- [ ] **README updated** 
  - Fitur baru dijelaskan
  - Perubahan API dijelaskan (parameter baru, removed API, dll)
  - Installation/setup instructions updated kalau ada
- [ ] **CHANGELOG entry** 
  - `## [Unreleased]` atau `## [X.Y.Z] - YYYY-MM-DD`
  - Setiap fitur + bug fix dijelaskan
  - Format: `- Added/Fixed/Changed: deskripsi`
- [ ] **Code comments** (jika logic kompleks)
  - Explain why, bukan what
- [ ] **Function/class docstrings** (JSDoc, Python docstring, etc)
  - Parameter & return types dijelaskan

### ✅ Git & Commits
- [ ] **Commit messages jelas & meaningful**
  - Format: `feat: deskripsi` atau `fix: deskripsi`
  - Jangan: "update", "fix bug", "work in progress"
- [ ] **Commit history clean** (tidak ada "oops typo" commits)
  - Gunakan `git rebase -i` kalau ada banyak commit kecil
  - Ideal: 1-3 commits per fitur
- [ ] **No merge conflicts** (pull latest dari upstream dulu)
- [ ] **Branch up-to-date dengan main/master**

### ✅ Project-Specific
- [ ] **Dependencies updated** (jika tambah library)
  - `package.json`, `requirements.txt`, `Cargo.toml`, etc updated
  - Tidak ada unused dependencies
- [ ] **Tests pass** (kalau ada automated tests)
  - `npm test`, `pytest`, `cargo test`, etc
- [ ] **CI/CD checks pass** (kalau ada GitHub Actions)
  - Build, lint, test semua hijau
- [ ] **No security issues** (no hardcoded credentials, API keys)

---

## 📋 STEP-BY-STEP: SETUP AWAL

### 1️⃣ Fork Repo (jika belum punya fork)
```
Buka: https://github.com/OWNER/REPO
Klik tombol "Fork" di atas kanan
Tunggu selesai (fork muncul di akun mu)
```

### 2️⃣ Clone Fork ke Lokal
```bash
git clone https://github.com/USERNAME/REPO.git
cd REPO
```
*(ganti USERNAME dengan username GitHub mu)*

### 3️⃣ Add Upstream Remote
```bash
git remote add upstream https://github.com/OWNER/REPO.git
```
Ini biar lu bisa pull update dari repo original:
```bash
git fetch upstream
git pull upstream main  # atau master
```

### 4️⃣ Buat Branch Baru
```bash
git checkout -b fitur-nama-deskriptif
# atau: git switch -c fitur-nama-deskriptif
```
**Naming convention:**
- `feat/add-dark-mode`
- `fix/handle-null-error`
- `docs/update-readme`
- `refactor/clean-up-utils`

### 5️⃣ Kerjain Fitur
- Edit files, add fitur, fix bugs
- Test lokal (dev server, tests, manual testing)
- Commit perlahan-lahan dengan message yang jelas

### 6️⃣ Sync dengan Upstream (sebelum push)
```bash
git fetch upstream
git rebase upstream/main
# atau kalau ada conflict, gunakan merge:
git merge upstream/main
```

### 7️⃣ Push ke Fork
```bash
git push origin fitur-nama-deskriptif
```

### 8️⃣ Buat Pull Request
```
GitHub → Fork mu → Tombol "Compare & pull request"
Atau: Pull Requests tab → New PR
```

---

## 🎯 PULL REQUEST TEMPLATE (Apa yang harus ditulis)

```
## Deskripsi
Jelaskan fitur/fix yang kamu buat. Singkat tapi jelas.

Contoh:
- Menambahkan dark mode toggle di settings
- Fix infinite loop ketika loading data
- Update documentation untuk setup baru

## Tipe perubahan
- [ ] Fitur baru (non-breaking)
- [ ] Bug fix
- [ ] Breaking change
- [ ] Dokumentasi
- [ ] Refactoring

## Testing
Jelaskan testing yang sudah lu lakukan:
- Manual testing:
  - [ ] Feature X works
  - [ ] Edge case Y handled
- Automated tests:
  - [ ] All tests pass: `npm test`
  - [ ] No console errors

## Screenshot/Demo (kalau UI changes)
Attach screenshot atau GIF kalau ada perubahan UI

## Checklist
- [ ] Dokumentasi updated
- [ ] Tidak ada breaking changes
- [ ] Commit messages meaningful
- [ ] No console errors/warnings
- [ ] Tests pass
```

---

## 📝 DOKUMENTASI YANG HARUS DI-UPDATE

### README.md
```markdown
# Fitur Baru (Heading baru kalau perlu)

## Cara pakai
Explain dengan contoh kode.

```python
# Contoh
result = new_feature()
```

### Changelog/HISTORY.md
```
## [Unreleased]

### Added
- Dark mode toggle dalam settings
- New API endpoint `/api/v2/users`

### Fixed
- Memory leak dalam cache manager
- Incorrect timestamp formatting

### Changed
- Updated Python minimum version ke 3.8
- Deprecated `old_function()` (use `new_function()`)
```

### API Documentation (kalau applicable)
- Update parameter descriptions
- Add new endpoints
- Update response examples
- Document breaking changes

---

## 🔄 SETELAH PR DIBUAT: ITERASI

### Jika Owner Minta Perubahan:
1. **Read feedback dengan teliti**
2. **Buat perubahan** di branch yang sama
3. **Commit baru:** `git commit -am "refactor: address feedback"`
4. **Push:** `git push origin fitur-nama-deskriptif`
   - PR auto-update dengan commit baru
5. **Reply di PR:** "Updated per feedback on line X"

### Jika Ada Conflict:
```bash
git fetch upstream
git rebase upstream/main
# Resolve conflicts di text editor
git add .
git rebase --continue
git push -f origin fitur-nama-deskriptif  # Force push (hati-hati!)
```

### Jika PR Approved & Ready to Merge:
- Owner akan merge (atau merge sendiri kalau punya permission)
- Delete local branch: `git branch -d fitur-nama-deskriptif`
- Update lokal: `git pull upstream main`

---

## 💡 TIPS & TRICKS

### Sebelum mulai kontribusi:
```bash
# Check apakah sudah ada issue/discussion tentang ini
# Kalau belum, buat issue dulu dan describe:
# - Problem statement
# - Proposed solution
# - Feedback dari maintainer
```

### Workflow yang baik:
```bash
# 1. Update upstream
git fetch upstream && git merge upstream/main

# 2. Buat branch
git switch -c fix/issue-123

# 3. Kerjain + commit berkali-kali
git add .
git commit -m "feat: implement feature X"

# 4. Sebelum push, squash commits kalau banyak
git rebase -i upstream/main
# Pilih "squash" untuk combine commits

# 5. Push & buat PR
git push -u origin fix/issue-123
```

### Cleanup setelah merge:
```bash
# Delete local branch
git branch -d fitur-nama

# Delete remote branch (kalau masih ada)
git push origin --delete fitur-nama

# Cleanup tracking branches
git fetch upstream --prune
```

---

## 🎓 BEST PRACTICES

### Commit Message Format
```
feat: add dark mode toggle
^--^  ^------------------
|     └─ summary 50 chars, imperative, lowercase
└─ type: feat|fix|docs|refactor|test|chore

Body (optional, 72 chars per line):
Explain why, not what.

Footer (optional):
Fixes #123
Closes #456
```

### Atomic Commits
```
BAIK:
- feat: add dark mode UI
- feat: implement theme switch logic
- docs: update dark mode guide

JELEK:
- WIP: dark mode
- fix stuff
- oops
```

### PR Size
- **Small PR (<250 lines):** Lebih mudah di-review, faster merge
- **Large PR (1000+ lines):** Bikin berat untuk di-review
  - Jika besar, split into multiple PRs kalau possible

### Communication
- Comment on PR dengan konteks
- Link ke related issues: `Fixes #123`
- Respectful & professional tone
- Don't take feedback personally (ini tentang kode, bukan kamu)

---

## 🆘 COMMON ISSUES & SOLUTIONS

### Merge Conflict
```bash
# Approach 1: Rebase (cleaner history)
git fetch upstream
git rebase upstream/main
# Fix conflicts, then:
git add .
git rebase --continue

# Approach 2: Merge (simpler)
git fetch upstream
git merge upstream/main
# Fix conflicts, then:
git add .
git commit -m "Merge upstream/main"
```

### Accidentally Committed to Main
```bash
# Undo last commit tapi keep changes
git reset --soft HEAD~1

# Create branch & push
git switch -c fitur-baru
git push -u origin fitur-baru
```

### Force Push (use with caution!)
```bash
# Hanya gunakan pada branch pribadi
git push -f origin fitur-nama

# Jangan pernah force push ke main!
```

### Forgot to Update Fork dari Upstream
```bash
# Before push, sync:
git fetch upstream
git rebase upstream/main
git push origin fitur-nama
```

---

## ✨ SELESAI!

Setelah PR di-merge, kamu udah jadi official contributor! 🎉

### Cleanup:
```bash
cd ..
git fetch -p
git branch -d fitur-nama
```

### Next time:
- Start fresh dari updated main
- Repeat the process

**Terima kasih sudah berkontribusi!**
