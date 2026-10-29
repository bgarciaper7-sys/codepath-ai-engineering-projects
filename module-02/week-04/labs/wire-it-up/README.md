# StudySync: Wire It Up

**CodePath AI Engineering 101 | Module 2, Week 4 | Tinker Lab**

## Project Overview

Wire It Up is a Python and Streamlit lab that extends the StudySync application with session state management, input validation, dataclasses, recurring study schedules, and scheduling conflict detection.

The activity focuses on debugging common application behaviors, implementing reliable Python functions, and verifying that backend logic works correctly through a Streamlit interface.

## Lab Objectives and Implementation

### Part 1: Streamlit Session State

Investigated why ordinary Python variables reset when Streamlit reruns an application.

- Compared a broken counter with a persistent counter.
- Used `st.session_state` to preserve a counter across reruns.
- Verified that the fixed counter increases with repeated clicks.

### Part 2: Input Validation

Implemented validation for study session entries.

- Rejected empty and whitespace-only subjects.
- Rejected zero and negative session durations.
- Displayed specific error messages using `st.error()`.
- Used `.strip()` to normalize subject input.
- Verified that valid study sessions can still be added.

### Part 3: Python Dataclasses

Compared a manually implemented Python class with a dataclass.

- Examined `PlainSession` with handwritten `__init__()` and `__repr__()` methods.
- Created `SessionDC` using the `@dataclass` decorator.
- Verified that both classes initialize and display equivalent session data.
- Learned how dataclasses reduce repetitive class definitions.

### Part 4: Recurring Dates and Scheduling Conflicts

Implemented two scheduling functions.

**`next_occurrence()`**
- Used `FREQUENCY_DAYS` and `timedelta` to calculate recurring dates.
- Verified daily and weekly recurrence, including transitions between months.

**`find_conflicts()`**
- Used nested loops to compare study session time slots.
- Returned conflicting session pairs as tuples.
- Verified conflict detection and safe handling of empty input.
- Confirmed that the Streamlit interface displays detected conflicts.

## Technologies and Tools

- Python
- Streamlit
- Python `dataclasses`
- Python `datetime` and `timedelta`
- Git and GitHub
- Visual Studio Code

## Running the Application

From the `wire-it-up` directory, install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal.

## Verification

The completed exercises were verified through manual Python terminal tests and Streamlit interface testing.

| Feature | Verification |
|---|---|
| Session state | Fixed counter increases across reruns |
| Empty subject | Rejected with an error message |
| Whitespace-only subject | Rejected with an error message |
| Zero or negative duration | Rejected with an error message |
| Valid session | Successfully added |
| Dataclass | Output compared against the handwritten class |
| Daily recurrence | Correct next-day date |
| Weekly recurrence | Correct date seven days later |
| Conflict detection | Matching time slots identified |
| Empty conflict list | Returns `[]` without crashing |

## Key Concepts Learned

- Streamlit rerun behavior and persistent session state
- Input validation and defensive programming
- Python classes and dataclasses
- List indexing, nested loops, and tuples
- Date arithmetic using `timedelta`
- Testing application logic and user interface behavior

## Project Context

Completed as part of CodePath AI Engineering 101. This lab builds on the StudySync starter application and focuses on strengthening Python fundamentals through hands-on debugging, implementation, and verification.