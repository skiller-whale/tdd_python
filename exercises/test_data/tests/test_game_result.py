"""Tests for game_result module."""

import pytest
from src.game_result import validate_game_result, summarize_game


class TestValidateGameResult:
    """Test suite for validate_game_result function."""

    def test_accepts_valid_game_result(self):
        result = {
            "player_name": "Alice",
            "answer": "whale",
            "guesses": ["crane", "slate", "whale"],
            "date": "2026-02-01",
        }
        assert validate_game_result(result) == {"valid": True}

    def test_rejects_result_that_isnt_an_object(self):
        invalid_results = [None, "not an object", 42, [], lambda: None]
        for invalid_result in invalid_results:
            assert validate_game_result(invalid_result) == {
                "valid": False,
                "reason": "Result must be an object",
            }

    def test_rejects_result_with_missing_player_name(self):
        result = {
            "answer": "whale",
            "guesses": ["crane", "slate", "whale"],
            "date": "2026-02-01",
        }
        assert validate_game_result(result) == {
            "valid": False,
            "reason": "player_name must be a non-empty string",
        }

    def test_rejects_result_with_missing_answer(self):
        result = {
            "player_name": "Alice",
            "guesses": ["crane", "slate", "whale"],
            "date": "2026-02-01",
        }
        assert validate_game_result(result) == {
            "valid": False,
            "reason": "answer must be a 5-letter lowercase word",
        }

    def test_rejects_result_with_answer_of_wrong_format(self):
        invalid_answers = ["whales", "WHALE", "wh4le", "whal", ""]
        for invalid_answer in invalid_answers:
            result = {
                "player_name": "Alice",
                "answer": invalid_answer,
                "guesses": ["crane", "slate", "whale"],
                "date": "2026-02-01",
            }
            assert validate_game_result(result) == {
                "valid": False,
                "reason": "answer must be a 5-letter lowercase word",
            }

    def test_rejects_result_with_missing_guesses(self):
        result = {
            "player_name": "Alice",
            "answer": "whale",
            "date": "2026-02-01",
        }
        assert validate_game_result(result) == {
            "valid": False,
            "reason": "guesses must be a non-empty array",
        }

    def test_rejects_result_with_non_array_guesses(self):
        result = {
            "player_name": "Alice",
            "answer": "whale",
            "guesses": "not an array",
            "date": "2026-02-01",
        }
        assert validate_game_result(result) == {
            "valid": False,
            "reason": "guesses must be a non-empty array",
        }

    def test_rejects_result_with_invalid_date_format(self):
        result = {
            "player_name": "Alice",
            "answer": "whale",
            "guesses": ["crane", "slate", "whale"],
            "date": "02-01-2026",
        }
        assert validate_game_result(result) == {
            "valid": False,
            "reason": "date must be a YYYY-MM-DD string",
        }

    def test_rejects_result_that_isnt_in_completed_state(self):
        result = {
            "player_name": "Alice",
            "answer": "whale",
            "guesses": ["crane", "slate"],  # not complete (won or lost)
            "date": "2026-02-01",
        }
        assert validate_game_result(result) == {
            "valid": False,
            "reason": "Game must be in a completed state (won or lost)",
        }


class TestSummarizeGame:
    """Test suite for summarize_game function."""

    @pytest.mark.parametrize(
        "player_name,guesses",
        [
            ("Alice", ["whale"]),
            ("Bob", ["crane", "slate", "flint"]),
            ("Charlie", ["stilt", "plumb", "vigor", "kayak", "monks", "crane"]),
        ],
    )
    def test_formats_winning_game(self, player_name, guesses):
        """Formats a winning game as 'Name: ANSWER n/6 ✓'."""
        answer = guesses[-1]
        result = {
            "player_name": player_name,
            "answer": answer,
            "guesses": guesses,
            "date": "2026-02-01",
        }
        expected = f"{player_name}: {answer.upper()} {len(guesses)}/6 ✓"
        assert summarize_game(result) == expected

    @pytest.mark.parametrize("player_name", ["Alice", "Bob", "Charlie"])
    def test_formats_losing_game(self, player_name):
        """Formats a losing game as 'Name: WHALE X/6 ✗'."""
        result = {
            "player_name": player_name,
            "answer": "whale",
            "guesses": ["crane", "slate", "flame", "blame", "frame", "grape"],
            "date": "2026-02-01",
        }
        assert summarize_game(result) == f"{player_name}: WHALE X/6 ✗"
