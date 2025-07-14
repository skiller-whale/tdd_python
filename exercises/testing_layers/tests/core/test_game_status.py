import pytest
from src.core.game_status import game_status


def test_empty_guesses():
    result = game_status([])
    assert result == "playing"


def test_correct_guess():
    result = game_status(["hello", "whale"])
    assert result == "won"


def test_max_guesses_reached():
    result = game_status(["fishy", "shark", "shell", "trout", "salty", "ocean"])
    assert result == "lost"


def test_still_playing():
    result = game_status(["fishy", "shark"])
    assert result == "playing"
