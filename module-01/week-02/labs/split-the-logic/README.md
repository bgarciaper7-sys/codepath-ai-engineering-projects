# Split the Logic — Python Refactoring & Unit Testing

**CodePath AI Engineering 110 | Module 1, Week 2 | StudySync Tinker**

## Project Overview

Split the Logic is a Python refactoring and testing exercise built around StudySync, a study-session scoring application.

The objective was to improve code organization by separating scoring logic into reusable modules while preserving existing functionality. The lab also introduced boundary testing, automated verification with pytest, and exploratory testing using unusual inputs.

## Technologies & Tools

- Python
- pytest
- Visual Studio Code
- Git and GitHub

## Implementation

### 1. Boundary Testing

Extended the existing pytest test suite by adding a second test for the `session_rating()` function.

Verified that both tests passed.

### 2. Modular Refactoring

Moved `apply_streak_bonus()` from `scoring.py` into `scoring_helpers.py` and imported it into the original module.

Preserved the existing streak bonus calculation, including the maximum score cap of 100.

### 3. Functional Verification

Executed the scoring application after refactoring to confirm that its five sample sessions produced the same scores and ratings.

### 4. Exploratory Testing

Investigated how `session_rating()` handled unexpected inputs:

| Input | Observation |
|---|---|
| `-5` | Classified as `Skip` |
| `105` | Revealed an out-of-range input case |
| `87.5` | Classified as `Good` |

The investigation highlighted the importance of distinguishing valid business inputs from values that Python can technically process.

## Testing

Run the automated tests:

```bash
python -m pytest
```

**Result: 2 tests passed.**

Run the application demonstration:

```bash
python scoring.py
```

## Skills Demonstrated

- Python modular programming
- Code refactoring
- Function imports and reusable helpers
- Unit testing with pytest
- Boundary-value analysis
- Exploratory testing
- Git version control

## Key Takeaway

This exercise reinforced that effective refactoring is not just about reorganizing code. It also requires verifying that existing functionality remains intact and using tests to detect unintended behavior changes.