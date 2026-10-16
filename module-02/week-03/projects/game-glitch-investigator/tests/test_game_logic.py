import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# --- Correct guess ---

def test_winning_guess():
    # Guess equals secret: outcome is "Win" with the success message.
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")


def test_winning_guess_at_range_boundary():
    # Equality must hold at the edges of the range too (1 and 100).
    assert check_guess(1, 1) == ("Win", "🎉 Correct!")
    assert check_guess(100, 100) == ("Win", "🎉 Correct!")


# --- Guess above the secret ---

def test_guess_too_high():
    # Guess 60 > secret 50: outcome "Too High", hint tells player to go lower.
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")


def test_guess_too_high_by_one():
    # Off-by-one above the secret must still be "Too High" (guards against >= / > mixups).
    assert check_guess(51, 50) == ("Too High", "📉 Go LOWER!")


# --- Guess below the secret ---

def test_guess_too_low():
    # Guess 40 < secret 50: outcome "Too Low", hint tells player to go higher.
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")


def test_guess_too_low_by_one():
    # Off-by-one below the secret must still be "Too Low".
    assert check_guess(49, 50) == ("Too Low", "📈 Go HIGHER!")


# --- Regression: original reversed-hint bug ---

def test_regression_high_guess_says_go_lower_not_higher():
    # Original bug: a guess above the secret returned "Go HIGHER!".
    outcome, message = check_guess(50, 6)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_regression_low_guess_says_go_higher_not_lower():
    # Original bug: a guess below the secret returned "Go LOWER!".
    outcome, message = check_guess(3, 6)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


# --- parse_guess: valid input ---

def test_parse_valid_guess():
    assert parse_guess("42", 1, 100) == (True, 42, None)


def test_parse_valid_guess_with_surrounding_whitespace():
    assert parse_guess("  7  ", 1, 20) == (True, 7, None)


# --- parse_guess: range boundaries ---

def test_parse_accepts_lower_boundary():
    assert parse_guess("1", 1, 20) == (True, 1, None)


def test_parse_accepts_upper_boundary():
    assert parse_guess("20", 1, 20) == (True, 20, None)


def test_parse_rejects_below_lower_boundary():
    assert parse_guess("0", 1, 20) == (False, None, "Guess must be between 1 and 20.")


def test_parse_rejects_above_upper_boundary():
    assert parse_guess("21", 1, 20) == (False, None, "Guess must be between 1 and 20.")


def test_parse_range_follows_difficulty_bounds():
    # 60 is valid on Normal (1-100) but out of range on Hard (1-50).
    assert parse_guess("60", 1, 100) == (True, 60, None)
    assert parse_guess("60", 1, 50) == (False, None, "Guess must be between 1 and 50.")


def test_parse_rejects_102_on_normal():
    assert parse_guess("102", 1, 100) == (False, None, "Guess must be between 1 and 100.")


# --- parse_guess: empty, whitespace, None ---

@pytest.mark.parametrize("raw", ["", " ", "   ", "\t"])
def test_parse_rejects_empty_and_whitespace_only(raw):
    assert parse_guess(raw, 1, 100) == (False, None, "Enter a guess.")


def test_parse_rejects_none():
    assert parse_guess(None, 1, 100) == (False, None, "Enter a guess.")


# --- parse_guess: decimals, negatives, text, odd formats ---

@pytest.mark.parametrize("raw", ["5.9", "5.0", ".5", "5."])
def test_parse_rejects_decimals(raw):
    assert parse_guess(raw, 1, 100) == (False, None, "Enter a whole number.")


@pytest.mark.parametrize("raw", ["-7", "+7"])
def test_parse_rejects_signed_numbers(raw):
    assert parse_guess(raw, 1, 100) == (False, None, "Enter a whole number.")


@pytest.mark.parametrize("raw", ["abc", "1e3", "1_0", "nan", "inf", "5 5", "12abc"])
def test_parse_rejects_text_and_odd_formats(raw):
    assert parse_guess(raw, 1, 100) == (False, None, "Enter a whole number.")


# --- get_range_for_difficulty ---

@pytest.mark.parametrize("difficulty, expected", [
    ("Easy", (1, 20)),
    ("Normal", (1, 100)),
    ("Hard", (1, 50)),
    ("Unknown", (1, 100)),  # unrecognized names fall back to Normal's range
])
def test_range_for_difficulty(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


@pytest.mark.parametrize("difficulty", ["Easy", "Normal", "Hard"])
def test_range_endpoints_are_valid_guesses(difficulty):
    low, high = get_range_for_difficulty(difficulty)
    assert parse_guess(str(low), low, high) == (True, low, None)
    assert parse_guess(str(high), low, high) == (True, high, None)


@pytest.mark.parametrize("difficulty", ["Easy", "Normal", "Hard"])
def test_values_just_outside_range_are_rejected(difficulty):
    low, high = get_range_for_difficulty(difficulty)
    assert parse_guess(str(low - 1), low, high)[0] is False
    assert parse_guess(str(high + 1), low, high)[0] is False


# --- update_score: winning points ---

@pytest.mark.parametrize("attempt, expected", [
    (1, 80),
    (2, 70),
    (5, 40),
    (8, 10),   # 100 - 90 = 10, exactly the minimum
    (9, 10),   # formula gives 0, raised to the minimum
    (20, 10),  # formula goes negative, still the minimum
])
def test_win_points_by_attempt(attempt, expected):
    assert update_score(0, "Win", attempt) == expected


# --- update_score: wrong-guess penalties ---

@pytest.mark.parametrize("attempt", range(1, 9))
def test_too_high_always_costs_five(attempt):
    assert update_score(0, "Too High", attempt) == -5


@pytest.mark.parametrize("attempt", range(1, 9))
def test_too_low_always_costs_five(attempt):
    assert update_score(0, "Too Low", attempt) == -5


# --- Regression: Too High used to add 5 points on even attempts ---

@pytest.mark.parametrize("attempt", [2, 4, 6, 8])
def test_regression_too_high_on_even_attempt_does_not_add_points(attempt):
    assert update_score(50, "Too High", attempt) == 45


@pytest.mark.parametrize("attempt", range(1, 11))
def test_wrong_guess_never_increases_score(attempt):
    assert update_score(50, "Too High", attempt) < 50
    assert update_score(50, "Too Low", attempt) < 50


@pytest.mark.parametrize("attempt", range(1, 9))
def test_too_high_and_too_low_cost_the_same(attempt):
    assert update_score(30, "Too High", attempt) == update_score(30, "Too Low", attempt)


# --- update_score: accumulation and unknown outcomes ---

def test_score_accumulates_from_current_total():
    assert update_score(10, "Win", 3) == 70   # 10 + (100 - 40)
    assert update_score(70, "Too Low", 4) == 65


def test_score_can_go_negative():
    assert update_score(0, "Too High", 1) == -5
    assert update_score(-5, "Too Low", 2) == -10


def test_full_game_score_sequence():
    # Same game as the walkthrough: 90, 80, 30, 70, then a win on attempt 5.
    score = 0
    for attempt, outcome in enumerate(["Too High", "Too High", "Too Low", "Too High", "Win"], start=1):
        score = update_score(score, outcome, attempt)
    assert score == -20 + 40


def test_unknown_outcome_leaves_score_unchanged():
    assert update_score(25, "Something else", 1) == 25
    assert update_score(25, "", 2) == 25
