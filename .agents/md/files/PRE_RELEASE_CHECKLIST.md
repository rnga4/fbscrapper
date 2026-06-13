# 🚀 PRE-RELEASE CHECKLIST

**Project:** _________________  
**Version:** _________________  
**Date:** _________________  
**Prepared by:** _________________

---

## 📋 CODE QUALITY & TESTING

### Functionality
- [ ] Semua fitur baru berjalan sesuai spec/requirements
- [ ] Tidak ada fitur yang regress (broken)
- [ ] Edge cases ditangani (null, empty, boundary values)
- [ ] Error handling proper (try-catch, validation, user feedback)
- [ ] Performance acceptable (no memory leaks, timeouts)

### Code Review & Cleanup
- [ ] Tidak ada `console.log`, `console.error`, `debugger`
- [ ] Tidak ada commented-out code atau TODOs yang masih pending
- [ ] Tidak ada unused imports, variables, functions
- [ ] Code consistent dengan project style
- [ ] Linting pass (no warnings)
- [ ] Code formatting pass (prettier/autopep8/rustfmt)

### Testing (Manual)
- [ ] Happy path tested di lokal
- [ ] Error scenarios tested
- [ ] Browser compatibility (Chrome, Firefox, Safari, Edge) - kalau web
- [ ] Mobile/responsive tested - kalau UI
- [ ] Different OS tested (Windows, macOS, Linux) - kalau native app
- [ ] No console errors, warnings, or exceptions

### Automated Tests
- [ ] Unit tests pass: `npm test` / `pytest` / `cargo test`
- [ ] Integration tests pass (kalau ada)
- [ ] End-to-end tests pass (kalau ada)
- [ ] Test coverage maintained or improved (kalau using coverage)
- [ ] CI/CD pipeline passing (GitHub Actions, Jenkins, etc)

---

## 📚 DOCUMENTATION

### README.md / Main Documentation
- [ ] New features documented with examples
- [ ] Installation/setup instructions updated (if changed)
- [ ] API changes documented (new endpoints, deprecations, breaking changes)
- [ ] Usage examples included for new features
- [ ] Prerequisites/requirements updated (new dependencies, version constraints)
- [ ] Troubleshooting section updated (if applicable)

### CHANGELOG / RELEASE NOTES
```markdown
Format reference:
## [Version X.Y.Z] - YYYY-MM-DD

### Added
- New feature 1 description
- New feature 2 description

### Fixed
- Bug fix 1 description
- Bug fix 2 description

### Changed
- API change description
- Dependency updates

### Deprecated
- List any deprecated features/APIs

### Removed
- Removed features/APIs
```

- [ ] CHANGELOG updated dengan format yang consistent
- [ ] Version number correct (semantic versioning)
- [ ] Release date included
- [ ] All major changes listed (features, fixes, breaking changes)
- [ ] Links to related issues/PRs included (optional tapi good practice)

### Code Documentation
- [ ] Function/class docstrings added (JSDoc, Python docstring, Rust doc)
- [ ] Complex logic commented (explain why, not just what)
- [ ] API documentation updated (Swagger/OpenAPI, Javadoc, etc)
- [ ] Type hints/signatures clear
- [ ] No misleading or outdated comments

### Migration Guide (if breaking changes)
- [ ] Old API vs new API comparison
- [ ] Step-by-step migration instructions
- [ ] Code examples for common use cases
- [ ] Known issues or gotchas documented

---

## 🔧 GIT & VERSION CONTROL

### Commits
- [ ] Commit messages meaningful (feat:, fix:, docs:, refactor: format)
- [ ] No "WIP", "fix typo", "oops", "asd" commits
- [ ] Commits are atomic (logical groupings)
- [ ] History is clean (no excessive small commits)

### Branch & Sync
- [ ] Branch up-to-date with main/master
- [ ] No merge conflicts
- [ ] All commits from feature branch included
- [ ] No accidental merges of unrelated branches

### Files
- [ ] No debug files committed (.swp, .DS_Store, node_modules, etc)
- [ ] .gitignore properly configured
- [ ] No secrets committed (API keys, passwords, tokens)
- [ ] File permissions correct (executable scripts have +x)

---

## 🔐 SECURITY & DEPENDENCIES

### Security
- [ ] No hardcoded credentials, API keys, or secrets
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities (if web)
- [ ] No CSRF vulnerabilities (if web)
- [ ] Input validation & sanitization done
- [ ] Security best practices followed

### Dependencies
- [ ] All new dependencies necessary
- [ ] No unused dependencies
- [ ] Dependency versions pinned (or using lock file)
- [ ] No deprecated/unmaintained dependencies
- [ ] Package lock file updated (package-lock.json, Cargo.lock, etc)
- [ ] License compatibility checked (GPL, MIT, Apache, etc)

---

## 🎨 UI/UX (if applicable)

### Design & Usability
- [ ] UI consistent with existing design
- [ ] Responsive design works on all screen sizes
- [ ] Colors have sufficient contrast (accessibility)
- [ ] Font sizes readable
- [ ] Icons/images load properly
- [ ] Loading states visible
- [ ] Error messages user-friendly

### Accessibility (a11y)
- [ ] Keyboard navigation works
- [ ] Screen reader compatible (alt text, aria labels)
- [ ] Focus indicators visible
- [ ] Color not only indicator (WCAG AA minimum)
- [ ] Form labels accessible

---

## 📊 PERFORMANCE

### Speed & Resources
- [ ] No obvious performance regressions
- [ ] Large operations don't block UI (async/await, threading)
- [ ] Memory usage acceptable
- [ ] No memory leaks (check browser DevTools, valgrind, etc)
- [ ] Bundle size acceptable (if frontend)
- [ ] Database queries optimized (no N+1 problems)

### Monitoring & Logging
- [ ] Error logging implemented
- [ ] Performance metrics tracked (if applicable)
- [ ] Debug logs can be disabled in production
- [ ] No excessive logging in hot paths

---

## 🌍 COMPATIBILITY

### Platform/Version Support
- [ ] Minimum Node/Python/Rust version requirement met
- [ ] Platform-specific issues addressed (Windows vs Linux vs macOS)
- [ ] Database version compatibility checked
- [ ] API version compatibility maintained

### Browser Support (if web)
- [ ] Works in supported browsers (document minimum versions)
- [ ] Polyfills included for older browsers (if needed)
- [ ] No unsupported ES6+ features for target browsers

---

## 📦 BUILD & DEPLOYMENT

### Build Process
- [ ] Build succeeds: `npm run build` / `cargo build --release`
- [ ] Build artifacts correct size
- [ ] Source maps generated (for debugging in production)
- [ ] No build warnings

### Release Artifacts
- [ ] Distribution files ready (tar.gz, .exe, .dmg, wheels, etc)
- [ ] Checksums calculated (SHA256, MD5)
- [ ] Signatures created (if applicable)
- [ ] Release notes prepared

### Deployment Readiness
- [ ] Deployment instructions documented
- [ ] Database migrations tested (if applicable)
- [ ] Configuration documented (env variables, config files)
- [ ] Rollback plan documented
- [ ] No database/environment-specific code in commits

---

## ✅ FINAL CHECKS

### Before Merge
- [ ] All checklist items completed
- [ ] Code review approved by maintainer
- [ ] All CI checks passing
- [ ] No merge conflicts
- [ ] Documentation complete

### Before Tag/Release
- [ ] Version number updated in:
  - [ ] package.json (or equivalent)
  - [ ] __version__ (or equivalent)
  - [ ] setup.py / setup.cfg
  - [ ] Cargo.toml
  - [ ] Any other version files
- [ ] Git tag created: `git tag v1.2.3`
- [ ] Release notes published
- [ ] Artifacts uploaded to release page

### Before Announce
- [ ] All tests pass
- [ ] Documentation deployed
- [ ] Changelog visible to users
- [ ] Migration guide visible (if breaking changes)
- [ ] Support team informed

---

## 🎯 SIGN-OFF

**Code Quality:** ✓ ☐  
**Documentation:** ✓ ☐  
**Testing:** ✓ ☐  
**Security:** ✓ ☐  
**Performance:** ✓ ☐  

**Approved by:** _________________ (Date: _________)  
**Ready for release:** YES ☐  NO ☐

---

## 📌 NOTES

```
Catatan tambahan, issue yang masih pending, atau hal khusus:


```

---

## 📞 POST-RELEASE

- [ ] Monitor logs for errors
- [ ] Track user feedback
- [ ] Prepare hotfix if needed
- [ ] Update issue tracker (close related issues)
- [ ] Announce release (changelog, blog, social media)
