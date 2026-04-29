
---

## Test Strategy

### 1. Core Functionality
- Validates correct word matching
- Case-insensitive comparisons
- Multiple occurrences
- Ensures substrings are NOT counted

### 2. Edge Cases
- Empty inputs
- Extra spaces
- Leading/trailing spaces
- Punctuation handling limitations

### 3. Negative Testing
- Invalid input types (None, int, list)
- Ensures proper exception handling (`TypeError`)

---

## Known Limitation

The function uses `.split()` for word separation.  
This means punctuation (e.g. `"cat,dog"`) is not treated as a delimiter.

Example:
- `"cat,dog cat"` → counts only `1` match for `"cat"`

---

## How to Run

1. Install dependencies:
```bash
pip install pytest
