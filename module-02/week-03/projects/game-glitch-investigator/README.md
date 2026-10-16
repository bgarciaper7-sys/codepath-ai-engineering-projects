# 🎮 Game Glitch Investigator: The Impossible Guesser

## Project Overview

Game Glitch Investigator is a Python and Streamlit debugging project completed as part of CodePath AI Engineering 101. The application is an interactive number-guessing game with selectable difficulty levels, directional hints, attempt limits, and a scoring system.

The original AI-generated application contained defects involving incorrect hints, input validation, scoring, and game state management. I investigated these issues, used Claude in VS Code as an AI coding teammate, reviewed proposed changes, and validated the fixes through automated testing and manual gameplay.

The completed project demonstrates Python debugging, modular programming, Streamlit session state management, input validation, and AI-assisted software development.

## Technologies & Tools

| Technology / Tool | How I Used It |
|---|---|
| Python | Implemented game logic, input validation, and scoring |
| Streamlit | Built the interactive interface and managed game state |
| pytest | Tested game logic, edge cases, and regression scenarios |
| Streamlit AppTest | Automated testing of user interactions and application state |
| VS Code | Developed, debugged, and reviewed the application |
| Claude | AI coding teammate for debugging, refactoring, and test generation |
| ChatGPT | Helped explain programming concepts, debugging, and testing |

## Key Features

- **Three difficulty levels:** Easy (1–20, 6 attempts), Normal (1–100, 8 attempts), and Hard (1–50, 5 attempts).
- **Validated user input:** Rejects empty, nonnumeric, and out-of-range guesses without consuming an attempt.
- **Accurate directional hints:** Tells players to guess higher or lower based on the secret number.
- **Attempt tracking:** Updates the number of remaining attempts after each valid guess.
- **Scoring system:** Deducts 5 points for incorrect guesses and awards winning points based on the attempt number.
- **Reliable game resets:** Starting a new game or changing difficulty resets the secret number, attempts, score, history, and game status.
- **Developer debugging panel:** Displays internal game state to support troubleshooting and manual testing.

## 🛠️ Setup

1. Install dependencies:

   `pip install -r requirements.txt`

2. Start the Streamlit application:

   `python -m streamlit run app.py`

3. Open the local URL displayed in the terminal.

4. Select a difficulty level and start guessing.

## Game Purpose

The purpose of the game is to guess a randomly generated secret number within a limited number of attempts. Players use the hints after each guess to narrow down the possible answer.

## Debugging and Implementation

I investigated defects in the original AI-generated application by reproducing unexpected behavior, reviewing the Python logic, and verifying proposed fixes through testing.

| Issue Identified | Fix Implemented |
|---|---|
| Reversed high/low hints | Corrected comparisons in `check_guess()` to return accurate directional hints. |
| Invalid guesses accepted | Added `parse_guess()` validation to reject invalid inputs before updating game state. |
| Incorrect attempt tracking | Initialized attempts at zero and incremented only after valid guesses. |
| Difficulty changes retained old state | Reset the secret number and game state whenever difficulty changes. |
| New Game did not fully reset | Centralized game initialization and resets in `start_new_game()`. |
| Incorrect guesses sometimes increased score | Updated `update_score()` to deduct five points for every incorrect guess. |
| Delayed status updates | Used a Streamlit placeholder to render the latest attempts, score, and history after guess processing. |

I separated reusable logic into `logic_utils.py` and kept the Streamlit interface and interaction handling in `app.py`. This made the code easier to understand and test.

For detailed bug reproduction steps and lessons learned, see [Reflection](reflection.md).

## 📸 Demo Walkthrough

The following example illustrates how the repaired game works.

1. The player opens the application and selects **Easy**, which uses numbers from 1 to 20 and allows six attempts.
2. Suppose the secret number is **12**. The player enters **5**, and the game responds with **"Go HIGHER!"** The attempt counter increases to 1, and the score becomes -5.
3. The player enters **18**, and the game responds with **"Go LOWER!"** The attempt counter increases to 2, and the score becomes -10.
4. The player enters **25**, which is outside the Easy difficulty range. The game rejects the input without increasing the attempt counter or changing the score.
5. The player enters **12**, and the game recognizes the correct guess, displays a winning result, and updates the score.
6. The player clicks **New Game**, and the application generates another secret number within the selected difficulty's range. Attempts, score, and guess history reset.

## Testing and Validation

I used pytest and Streamlit AppTest to verify the corrected game logic and application behavior.

| Testing Method | What Was Verified |
|---|---|
| Unit tests (pytest) | Directional hints, input validation, difficulty ranges, scoring, and regression scenarios |
| Application tests (Streamlit AppTest) | Game initialization, difficulty switching, resets, attempt tracking, and invalid input handling |
| Manual browser testing | Gameplay, score changes, difficulty settings, and game resets |

### Recorded Test Results

- **107 automated tests passed, 0 failed** during the original project validation.
- **15 Streamlit AppTest cases** were included in the automated test suite.
- Manual browser testing was completed to verify the fixes.

To run the automated tests locally from the project directory:

```bash
python -m pytest -v
```

The complete automated test suite was rerun successfully in the AI Engineering portfolio repository, with **107 tests passing and 0 failures**.

## 🤖 AI Collaboration

I used Claude to investigate bugs, suggest code changes, refactor functions, and generate tests. I used ChatGPT to help explain Python logic, Streamlit session state, and testing concepts.

I reviewed AI suggestions before applying them and verified the results through automated tests and manual gameplay.

### Supporting Documentation

- [Learning Reflection](reflection.md) — Bug investigation, manual testing, Streamlit concepts, and lessons learned.
- [AI Interactions Log](ai_interactions.md) — Claude agent workflow, AI-assisted test generation, and verification decisions.

## 🚀 Stretch Features

- **SF7: Test Generation:** Used AI to generate and improve automated tests.
- **SF8: Agent Workflow:** Used Claude to assist with multi-file code changes and debugging.
