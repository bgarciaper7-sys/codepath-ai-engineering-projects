"""End-to-end tests that drive the real Streamlit app with AppTest."""
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")

RANGES = {"Easy": (1, 20), "Normal": (1, 100), "Hard": (1, 50)}
ATTEMPT_LIMITS = {"Easy": 6, "Normal": 8, "Hard": 5}


def new_app():
    return AppTest.from_file(APP_PATH, default_timeout=20).run()


def select_difficulty(at, difficulty):
    at.selectbox[0].set_value(difficulty).run()


def click_new_game(at):
    next(b for b in at.button if b.label.startswith("New Game")).click().run()


def submit_guess(at, text):
    difficulty = at.selectbox[0].value
    at.text_input(key=f"guess_input_{difficulty}").set_value(text)
    next(b for b in at.button if b.label.startswith("Submit")).click().run()


def banner(at):
    return at.info[0].value


# --- Fresh load ---

def test_fresh_load_uses_normal_settings():
    at = new_app()
    assert not at.exception
    assert at.session_state["attempts"] == 0
    assert at.session_state["score"] == 0
    assert at.session_state["status"] == "playing"
    assert at.session_state["history"] == []
    assert 1 <= at.session_state["secret"] <= 100
    assert "between 1 and 100" in banner(at)
    assert "Attempts left: 8" in banner(at)


# --- All three difficulties ---

@pytest.mark.parametrize("difficulty", ["Easy", "Normal", "Hard"])
def test_difficulty_sets_range_banner_and_attempts(difficulty):
    low, high = RANGES[difficulty]
    at = new_app()
    select_difficulty(at, difficulty)
    assert not at.exception
    assert low <= at.session_state["secret"] <= high
    assert f"between {low} and {high}" in banner(at)
    assert f"Attempts left: {ATTEMPT_LIMITS[difficulty]}" in banner(at)


@pytest.mark.parametrize("difficulty", ["Easy", "Normal", "Hard"])
def test_new_game_secret_stays_in_selected_range(difficulty):
    low, high = RANGES[difficulty]
    at = new_app()
    select_difficulty(at, difficulty)
    for _ in range(25):
        click_new_game(at)
        assert low <= at.session_state["secret"] <= high


# --- Switching difficulty ---

def test_switching_difficulty_resets_old_game():
    at = new_app()
    at.session_state["secret"] = 50
    submit_guess(at, "10")
    assert at.session_state["attempts"] == 1
    assert at.session_state["history"] == [10]
    assert at.session_state["score"] != 0

    select_difficulty(at, "Hard")
    assert at.session_state["attempts"] == 0
    assert at.session_state["score"] == 0
    assert at.session_state["history"] == []
    assert at.session_state["status"] == "playing"
    assert 1 <= at.session_state["secret"] <= 50
    assert at.session_state["game_difficulty"] == "Hard"


def test_out_of_range_secret_is_replaced_when_switching_to_easy():
    at = new_app()
    at.session_state["secret"] = 73  # valid on Normal, impossible on Easy
    select_difficulty(at, "Easy")
    assert 1 <= at.session_state["secret"] <= 20


# --- Resetting after winning or losing ---

def test_new_game_after_win_resets_everything():
    at = new_app()
    at.session_state["secret"] = 50
    submit_guess(at, "50")
    assert at.session_state["status"] == "won"
    assert at.session_state["score"] > 0

    click_new_game(at)
    assert at.session_state["status"] == "playing"
    assert at.session_state["attempts"] == 0
    assert at.session_state["score"] == 0
    assert at.session_state["history"] == []
    assert "Attempts left: 8" in banner(at)


def test_new_game_after_loss_resets_everything():
    at = new_app()
    select_difficulty(at, "Easy")
    at.session_state["secret"] = 20
    for _ in range(ATTEMPT_LIMITS["Easy"]):
        submit_guess(at, "1")
    assert at.session_state["status"] == "lost"

    click_new_game(at)
    assert at.session_state["status"] == "playing"
    assert at.session_state["attempts"] == 0
    assert at.session_state["score"] == 0
    assert at.session_state["history"] == []
    assert 1 <= at.session_state["secret"] <= 20


def test_finished_game_still_shows_final_attempts_left():
    at = new_app()
    at.session_state["secret"] = 50
    submit_guess(at, "50")
    assert at.session_state["status"] == "won"
    assert "Attempts left: 7" in banner(at)


# --- Attempts-remaining display and invalid input ---

def test_attempts_left_updates_immediately_after_a_guess():
    at = new_app()
    at.session_state["secret"] = 50
    submit_guess(at, "10")
    assert at.session_state["attempts"] == 1
    assert "Attempts left: 7" in banner(at)
    submit_guess(at, "20")
    assert at.session_state["attempts"] == 2
    assert "Attempts left: 6" in banner(at)


def test_each_guess_is_processed_exactly_once():
    at = new_app()
    at.session_state["secret"] = 50
    submit_guess(at, "10")
    assert at.session_state["history"] == [10]
    assert at.session_state["attempts"] == 1


def test_invalid_guess_does_not_use_an_attempt_or_enter_history():
    at = new_app()
    submit_guess(at, "102")
    assert at.session_state["attempts"] == 0
    assert at.session_state["history"] == []
    assert "Attempts left: 8" in banner(at)
    assert at.error[0].value == "Guess must be between 1 and 100."
