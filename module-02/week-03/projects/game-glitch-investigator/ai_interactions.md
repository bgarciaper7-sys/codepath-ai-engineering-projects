# AI Interactions Log

## Agent Workflow (SF8)

**What task did you give the agent?**

I asked Claude in VS Code to investigate and fix several bugs in my Streamlit guessing game, including incorrect high/low hints, invalid input handling, difficulty changes, and incomplete game resets. I also asked it to explain proposed changes before modifying the files so I could review them first.

**What did the agent do?**

After I reviewed and approved the proposed changes, Claude helped refactor reusable game logic into `logic_utils.py`, update the Streamlit application, and develop automated tests in `tests/test_game_logic.py` and `tests/test_app_state.py`.

**What did you have to verify or fix manually?**

I manually tested the game in my browser to confirm that invalid guesses were rejected, difficulty changes generated the correct number ranges, and New Game reset the game state. During testing, I encountered a `TypeError` even though pytest was passing, which led to discovering that an older Streamlit server was still running. I restarted Streamlit and confirmed that the updated code worked. I also tested the scoring fix by making two guesses that were too high and verifying that the score decreased from 0 to -5 to -10.

---

## Test Generation (SF7)

I used Claude to help generate unit tests and Streamlit AppTest tests for the bugs discovered during the project. I reviewed the suggested test cases and ran them to verify the results.

| Edge Case | Prompt Summary | AI-Suggested Test | Did It Pass? | Your Reasoning |
|---|---|---|---|---|
| Reversed high/low hints | Asked Claude to investigate and test the incorrect directional hints | Verify that guesses above the secret display "Go LOWER!" and guesses below display "Go HIGHER!" | Yes | The game should provide directions consistent with the secret number. |
| Out-of-range input | Asked Claude to validate guesses and add tests for invalid values | Test guesses of 0 and 102 on Normal difficulty | Yes | Invalid guesses should not consume attempts or appear in history. |
| Difficulty switching | Asked Claude to investigate difficulty changes and stale game state | Use Streamlit AppTest to verify that switching to Easy generates a secret between 1 and 20 | Yes | The game must follow the selected difficulty's range. |
| New Game after winning or losing | Asked Claude to test game resets after completion | Verify that New Game resets attempts, score, history, and status | Yes | A new game should not retain the previous game's progress. |
| Scoring on even attempts | Asked Claude to investigate why incorrect high guesses sometimes increased the score | Test that Too High guesses on attempts 2, 4, 6, and 8 subtract five points | Yes | Incorrect guesses should not be rewarded because of the attempt number. |
| Attempts-remaining display | Asked Claude to investigate why the displayed attempts count lagged behind | Use AppTest to verify that the count updates immediately after submitting a guess | Yes | The displayed attempts should match the actual game state. |

**Final testing results:** 107 automated tests passed, including 15 Streamlit AppTest tests. I also completed manual testing in the browser to verify the fixes.

---

## Linting & Style (SF9)

Not attempted.

---

## Model Comparison (SF11)

Not attempted.