# 📝 Documentation yang HARUS Di-Update Sebelum PR

## 1. README.md

### Bagian yang perlu di-update:

#### A. Fitur Baru
Jika menambahkan fitur, tambahkan bagian di README:

```markdown
## Features

- Existing feature 1
- Existing feature 2
- **NEW: Deskripsi fitur baru yang ringkas**

## NEW: Nama Fitur

Jelaskan fitur baru dengan paragraf singkat.

### Usage

```bash
# Contoh kode/command
```

### Examples

- Example 1
- Example 2
```

#### B. Installation / Setup
Update kalau ada dependency baru atau perubahan install steps:

```markdown
## Installation

**Requires:** Python 3.8+, Node.js 14+

### From source

```bash
git clone https://github.com/...
cd project
npm install  # atau: pip install -r requirements.txt
npm run build  # kalau ada
```

### Via Package Manager

```bash
npm install package-name
# atau
pip install package-name
# atau
cargo install package-name
```
```

#### C. Configuration
Update kalau ada config baru:

```markdown
## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| NEW_VAR | Yes | - | Penjelasan variable baru |

Example `.env`:
```bash
NEW_VAR=value
OLD_VAR=value
```
```

#### D. API Changes
Update kalau ada API baru atau perubahan:

```markdown
## API Reference

### NEW: POST /api/v2/endpoint

Create something new.

**Request:**
```json
{
  "param1": "string",
  "param2": 123
}
```

**Response:**
```json
{
  "id": 1,
  "status": "success"
}
```

**Parameters:**
- `param1` (required): Description
- `param2` (optional): Description
```

#### E. Breaking Changes (PENTING!)
Update kalau ada perubahan yang breaking:

```markdown
## ⚠️ Breaking Changes

### v2.0.0

- `old_function()` removed → use `new_function()` instead
- API endpoint `/old-api/` → `/new-api/v2/`

**Migration Guide:**

```javascript
// Before (v1.x)
const result = old_function(data);

// After (v2.0+)
const result = new_function(data);
```
```

#### F. Troubleshooting
Add kalau ada error baru atau fix yang user-facing:

```markdown
## Troubleshooting

### Error: "X not found"

**Cause:** Description of why it happens

**Solution:** 
1. Check Y
2. Try Z
3. If still broken, ...
```

---

## 2. CHANGELOG.md atau HISTORY.md

### Format Standar (Keep a Changelog)

```markdown
# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New feature description
- Another new feature

### Changed
- Changed existing feature
- Updated dependency X from 1.0 to 2.0

### Fixed
- Bug fix 1
- Bug fix 2

### Deprecated
- API endpoint /old-api/ (use /new-api/ instead)
- Function old_function() (use new_function())

### Removed
- Removed support for Node.js 10
- Removed deprecated API v1

### Security
- Fixed XSS vulnerability in search
- Updated security headers

## [1.0.0] - 2024-01-15

### Added
- Initial release
- Core features

[Unreleased]: https://github.com/owner/repo/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/owner/repo/releases/tag/v1.0.0
```

### Apa yang harus ditulis:

```
### Added
- Feature 1 deskripsi lengkap
- Feature 2 deskripsi lengkap
- NEW: X component added untuk Y purpose

### Fixed
- Fixed bug where X caused Y
- Resolved memory leak in Z function
- Handle null case in getData()

### Changed
- API endpoint changed from /old to /new
- Updated Python requirement to 3.8+
- Improved error messages for better UX

### Deprecated
- Function oldFunc() is deprecated, use newFunc() instead

### Removed
- Support for Python 3.7 (EOL)
- Legacy authentication method

### Security
- CVE-XXXX-XXXXX: Fixed vulnerability in X
```

---

## 3. API Documentation (kalau applicable)

### A. Swagger/OpenAPI (spec file)
Update `swagger.yaml` atau `openapi.json`:

```yaml
paths:
  /api/v2/new-endpoint:
    post:
      summary: Create new thing
      description: Detailed description
      tags:
        - new-feature
      parameters:
        - name: param1
          in: query
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NewObject'
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NewObject'
        '400':
          description: Bad request

components:
  schemas:
    NewObject:
      type: object
      required:
        - field1
      properties:
        field1:
          type: string
          description: Description
        field2:
          type: integer
```

### B. Postman Collection
Update collection JSON (file atau environment):

```json
{
  "info": {
    "name": "API Collection",
    "version": "2.0.0"
  },
  "item": [
    {
      "name": "New Feature",
      "item": [
        {
          "name": "Create resource",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/api/v2/endpoint",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"param1\": \"value\"\n}"
            }
          }
        }
      ]
    }
  ]
}
```

---

## 4. Code Comments & Docstrings

### A. JSDoc (JavaScript)
```javascript
/**
 * Calculate something complex
 * 
 * @param {string} input - The input value
 * @param {Object} options - Configuration options
 * @param {boolean} options.verbose - Enable verbose logging
 * @returns {Promise<Object>} The result object
 * @throws {Error} When input is invalid
 * 
 * @example
 * const result = await calculate('data', { verbose: true });
 * console.log(result.value);
 */
async function calculate(input, options = {}) {
  // Implementation
}
```

### B. Python Docstring
```python
def calculate(input_data: str, verbose: bool = False) -> dict:
    """
    Calculate something complex.
    
    Args:
        input_data (str): The input value
        verbose (bool): Enable verbose logging. Defaults to False.
    
    Returns:
        dict: The result object with 'value' key
    
    Raises:
        ValueError: When input is invalid
    
    Example:
        >>> result = calculate('data', verbose=True)
        >>> print(result['value'])
        42
    """
    # Implementation
    pass
```

### C. Rust Doc
```rust
/// Calculate something complex.
///
/// # Arguments
///
/// * `input` - A string input value
/// * `verbose` - Enable verbose logging
///
/// # Returns
///
/// A Result containing the calculated value
///
/// # Errors
///
/// Returns an error if input is invalid
///
/// # Example
///
/// ```
/// let result = calculate("data", true)?;
/// println!("{:?}", result);
/// ```
pub fn calculate(input: &str, verbose: bool) -> Result<Output, Error> {
    // Implementation
}
```

---

## 5. Migration Guide (kalau ada breaking changes)

### Format:

```markdown
# Migration Guide - v1.x to v2.0

## Overview

Version 2.0 introduces breaking changes untuk improve performance dan consistency.

## Breaking Changes

### 1. API Endpoint renamed

**Before (v1.x):**
```bash
GET /api/users/123
```

**After (v2.0):**
```bash
GET /api/v2/users/123
```

### 2. Function renamed

**Before (v1.x):**
```javascript
import { getUser } from 'library';
const user = getUser(123);
```

**After (v2.0):**
```javascript
import { fetchUser } from 'library';
const user = await fetchUser(123);
```

### 3. Response format changed

**Before (v1.x):**
```json
{
  "success": true,
  "data": { "id": 1, "name": "John" }
}
```

**After (v2.0):**
```json
{
  "id": 1,
  "name": "John",
  "status": "active"
}
```

## Deprecation Timeline

- **v1.9** (2024-01-01): Old APIs marked as deprecated
- **v2.0** (2024-03-01): Old APIs removed, breaking changes
- **v1.8** (2024-02-01): End of support for v1.x

## Upgrade Path

1. Update to latest v1.x
2. Review deprecation warnings
3. Update code using old APIs
4. Test thoroughly
5. Upgrade to v2.0
```

---

## 6. Install/Setup Documentation

### A. Installation Guide
```markdown
# Installation Guide

## System Requirements

- OS: macOS 10.14+, Ubuntu 18.04+, Windows 10+
- Node.js 14+ (or Python 3.8+)
- RAM: 2GB minimum, 4GB recommended
- Disk: 500MB

## Installation Methods

### Method 1: NPM (Recommended)

```bash
npm install package-name
```

### Method 2: From Source

```bash
git clone https://github.com/owner/repo.git
cd repo
npm install
npm run build
npm install -g .  # Install globally
```

### Method 3: Docker

```bash
docker build -t myapp .
docker run myapp
```

## Configuration

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env` dengan credentials mu:

```
API_KEY=your-key-here
DEBUG=false
```

## Verification

Check installation:

```bash
myapp --version
```

Run tests:

```bash
npm test
```
```

---

## 7. Docstring dalam Code

Setiap fitur baru harus punya docstring yang jelas:

```javascript
// ❌ BAD
function process(data) {
  // do stuff
  return result;
}

// ✅ GOOD
/**
 * Process input data dan return processed output.
 * 
 * Handles edge cases:
 * - Empty input → returns empty array
 * - Null values → skipped
 * - Duplicates → removed
 * 
 * @param {Array<Object>} data - Array of objects to process
 * @returns {Array<Object>} Processed data with duplicates removed
 */
function process(data) {
  // Validate input
  if (!Array.isArray(data)) {
    throw new TypeError('data must be an array');
  }
  
  // Process dan return
  return [...new Set(data)];
}
```

---

## ✅ Dokumentasi Checklist

Sebelum submit PR:

- [ ] **README.md updated**
  - [ ] Fitur baru dijelaskan
  - [ ] Setup/install updated (kalau ada)
  - [ ] Usage examples added
  - [ ] API changes documented

- [ ] **CHANGELOG.md updated**
  - [ ] Fitur di-list di "Added" section
  - [ ] Bug fixes di-list di "Fixed" section
  - [ ] Breaking changes di-list di "Removed/Changed"
  - [ ] Format consistent (Keep a Changelog)

- [ ] **Code comments added**
  - [ ] Complex logic explained
  - [ ] Edge cases documented
  - [ ] Docstrings on new functions/classes

- [ ] **API documentation updated** (kalau applicable)
  - [ ] Swagger/OpenAPI file updated
  - [ ] Endpoint examples added
  - [ ] Response format documented

- [ ] **Migration guide created** (kalau ada breaking changes)
  - [ ] Old vs new comparison
  - [ ] Step-by-step upgrade instructions
  - [ ] Timeline documented

---

## Template untuk mencopy

### README.md snippet
```markdown
## [Fitur Baru Name]

Jelaskan fitur singkat. Feature ini untuk...

### Usage

```bash
command
```

### Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| new_opt | string | value | Apa yang dia lakukan |

### Example

```javascript
// Contoh kode
```
```

### CHANGELOG.md snippet
```markdown
## [Unreleased]

### Added
- New feature: deskripsi lengkap apa yang ditambah
- Support untuk X dan Y

### Fixed
- Fixed bug dimana X terjadi dalam kondisi Y
- Handle null case di function Z

### Changed
- API endpoint /old → /new
- Improved error message untuk clarity
```

---

**PENTING:** Jangan lupa ini sebelum submit PR ke owner! Documentation adalah bagian penting dari kontribusi. ✨
