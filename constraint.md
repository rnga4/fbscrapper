# FB Scraper System - AI Agent Constraints & Guidelines

## 🚨 CRITICAL: DO NOT TOUCH THE BACKEND SYSTEM

**Status:** Production System - LOCKED ✋

The core scraping system is **COMPLETE** and **FUNCTIONAL**. Any modifications to the backend can break the entire application.

---

## 📋 Project Scope

### ✅ WHAT YOU CAN DO
- **Frontend UI/UX Redesign & Improvement**
  - Refactor UI components
  - Improve styling and layout
  - Enhance user experience
  - Fix UI bugs and usability issues
  - Create new UI features (buttons, modals, forms, etc.)
  - Responsive design improvements
  - Animation and transitions

- **Display & Visualization**
  - Better data visualization
  - Improved result presentation
  - Status indicators and progress bars
  - Data filtering and sorting UI
  - Table/card layout improvements
  - Theme and color scheme enhancement

### ❌ WHAT YOU MUST NOT DO
- **DO NOT modify backend logic**
- **DO NOT touch system configuration**
- **DO NOT alter database schema or queries**
- **DO NOT change API endpoints or request/response structures**
- **DO NOT modify authentication/authorization logic**
- **DO NOT touch data processing pipeline**
- **DO NOT optimize or refactor backend code**
- **DO NOT install new backend dependencies**

---

## 🔗 Integration Rules (If Needed)

### When Integrating Backend Results into UI:

1. **OBSERVATION FIRST**
   - Study the existing API response structure
   - Document current data format
   - Test endpoints before integration
   - Never assume data structure

2. **READ-ONLY APPROACH**
   - Only READ from the backend
   - NEVER WRITE to backend systems
   - NEVER MODIFY data before sending to backend
   - Only pass data AS-IS from backend to UI

3. **SAFETY CHECKLIST**
   ```
   Before integrating with backend:
   ☐ Documented existing response format?
   ☐ Tested API endpoint with sample data?
   ☐ Verified no breaking changes to endpoint?
   ☐ Reviewed backend code for understanding (READ-ONLY)?
   ☐ Created UI component without modifying backend logic?
   ☐ Tested integration in development environment?
   ☐ Verified backend still works identically?
   ☐ Committed changes to version control?
   ```

4. **VERIFICATION AFTER INTEGRATION**
   - Backend system behaves identically
   - All existing features still work
   - No new errors in backend logs
   - Response times unchanged
   - Data integrity maintained

---

## 📁 File Structure Guidelines

### Safe to Modify
```
/frontend
├── components/         ← OK: Refactor, create new
├── pages/             ← OK: Improve, redesign
├── styles/            ← OK: Enhance styling
├── assets/            ← OK: Add new assets
└── utils/ui/          ← OK: UI utilities only
```

### DO NOT MODIFY
```
/backend/
├── api/               ← 🚫 LOCKED
├── scraper/           ← 🚫 LOCKED
├── database/          ← 🚫 LOCKED
├── config/            ← 🚫 LOCKED
├── middleware/        ← 🚫 LOCKED
└── services/          ← 🚫 LOCKED
```

---

## 🧪 Testing & Validation

### Before Submitting Changes:
1. **Frontend Testing**
   - UI renders correctly
   - No console errors
   - Responsive on all breakpoints
   - All interactive elements work

2. **Backend Validation**
   - Run backend tests (if exist)
   - Test API endpoints manually
   - Verify backend logs show no errors
   - Confirm no performance degradation

3. **Integration Testing**
   - Test UI with real backend data
   - Verify data displays correctly
   - Test all user workflows
   - Check error handling

---

## 🎨 UI/UX Improvement Focus Areas

### Recommended Improvements
- [ ] Replace outdated styling with modern design system
- [ ] Improve form UX and validation feedback
- [ ] Add loading states and skeleton screens
- [ ] Better error messages and user feedback
- [ ] Responsive mobile design
- [ ] Accessibility improvements (WCAG 2.1)
- [ ] Dark mode support (optional)
- [ ] Improved typography and spacing
- [ ] Consistent icon usage
- [ ] Better navigation and information hierarchy

---

## 🔄 Version Control Practices

### Commit Structure
```
frontend: [description of UI change]
  - Keep backend completely separate
  - One commit = one feature/fix
  - Clear, descriptive messages

Example:
  "frontend: improve search form layout and styling"
  "frontend: add loading skeleton for results table"
  "frontend: refactor buttons to use new design system"
```

### Never
- Don't mix backend and frontend commits
- Don't commit without testing
- Don't modify unrelated backend files

---

## 🚨 Red Flags - STOP Immediately

**STOP and do not proceed if:**
- [ ] You're about to modify `/backend` folder
- [ ] You're editing API routes or endpoints
- [ ] You're changing data models or database queries
- [ ] You're modifying authentication logic
- [ ] You're installing new backend packages
- [ ] You're touching scraper logic
- [ ] You're changing environment configuration
- [ ] You're modifying system dependencies

**Action:** Step back, review the constraint, and refocus on frontend UI only.

---

## 📞 Decision Flow

```
Task assigned:
  │
  ├─ Does it involve backend/system code?
  │  └─→ YES: ❌ DO NOT DO - Out of scope
  │
  ├─ Does it involve frontend UI/UX?
  │  └─→ YES: ✅ Proceed with caution
  │       │
  │       ├─ Does it require reading backend code?
  │       │  └─→ Document only, do not modify
  │       │
  │       └─ Test with backend before/after
  │
  └─ Unsure?
     └─→ Ask owner before proceeding
```

---

## 💾 File Checklist

Before submitting your work:

- [ ] Only modified `/frontend` directory
- [ ] Backend code is untouched
- [ ] No changes to API structures
- [ ] UI tested and looks good
- [ ] Backend still works (tested manually)
- [ ] No breaking changes introduced
- [ ] Code follows project conventions
- [ ] Changes committed with clear messages
- [ ] README updated if new features added

---

## 🎯 Summary

**The Golden Rule:**
> **Focus on making the UI beautiful and functional. The system works—don't break it. When in doubt, keep hands off the backend.**

- ✅ **Frontend:** Go wild, improve everything
- ❌ **Backend:** Look but don't touch
- 🤝 **Integration:** Read-only, test thoroughly
- 🔒 **System:** Protected and locked

Good luck! Make it beautiful! 🎨
