# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the guessing game, it looked like a normal Streamlit application, but I quickly realized that several things were not working correctly. When the secret number was 6 and I guessed 50, the game incorrectly told me to go higher instead of lower. I also discovered that guesses outside the allowed range, such as 0 and 102, were accepted instead of rejected. Another issue was that the attempts counter started at 1 before I had even made a guess, and later I discovered that changing difficulty or starting a new game did not reset everything correctly.

### Bug Reproduction Log

| Input Used / Trigger | Expected Behavior | Actual Behavior | Console Error / Output |
|---|---|---|---|
| Secret = 6, guess = 50 | Display "Go LOWER!" | Displayed "Go HIGHER!" | No console error |
| Guess = 102 on Normal | Reject the guess because the maximum is 100 | Accepted the guess and added it to history | No console error |
| Guess = 0 on Normal | Reject the guess because the minimum is 1 | Accepted the invalid guess | No console error |
| Initial game load on Normal | Show 8 attempts remaining | Showed 7 attempts remaining | No console error |
| Switch to Easy with secret = 73 | Generate a secret between 1 and 20 | Kept secret 73 and displayed the old range | No console error |
| New Game after winning or losing | Reset all game values | Score, history, or game status were not reset | No console error |

---

## 2. How did you use AI as a teammate?

I used ChatGPT to help me understand the debugging process and Claude in VS Code to investigate the code, suggest changes, and create tests. One helpful suggestion was to move `parse_guess()` into `logic_utils.py` and validate inputs before updating the game state, which I verified by entering 102 and confirming that it was rejected without using an attempt. I did not immediately accept Claude's suggestion to change `update_score()` while we were fixing the difficulty and New Game bugs because I wanted to focus on one problem at a time. Instead, I asked Claude to explain the scoring logic separately before approving the change, and I verified the final version using automated tests and actual gameplay.

---

## 3. Debugging and testing your fixes

I learned to verify a fix by reproducing the original problem and checking whether the game now behaved as expected. Claude helped generate pytest and Streamlit AppTest tests, while ChatGPT helped me understand what the tests were checking. At one point, the tests passed but the browser still showed a `TypeError` because an older Streamlit server was running, so I had to restart it and test again. By the end, all 107 automated tests passed, and I manually tested difficulty changes, input validation, game resets, and scoring. I also confirmed that two incorrect high guesses reduced the score from 0 to -5 to -10 instead of rewarding the second guess.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the Python script whenever someone interacts with the application, such as submitting a guess or changing the difficulty. Session state is what allows the game to remember values like the secret number, attempts, score, and guess history between those reruns. Without managing session state correctly, the game can keep outdated information or fail to reset when starting over. I also learned that the order in which Streamlit displays information matters, because the attempts-remaining message originally showed the previous count until the next interaction.

---

## 5. Looking ahead: your developer habits

One habit I want to continue is testing bugs myself instead of assuming that AI-generated code works correctly. Next time, I want to practice reading Python functions and understanding error messages before asking AI to fix them. I also want to continue asking AI to explain proposed changes before allowing it to modify my files. This project changed how I think about AI-generated code because I realized that even when AI provides a solution, I still need to understand, review, and test it before trusting the results.