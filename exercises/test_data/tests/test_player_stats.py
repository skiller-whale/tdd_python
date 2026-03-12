"""Tests for player_stats module."""

import pytest
from src.player_stats import calculate_player_stats


class TestTotals:
    """Test suite for games played and won counts."""

    def test_returns_zeros_for_empty_array(self):
        stats = calculate_player_stats([])
        assert stats["games_played"] == 0
        assert stats["games_won"] == 0

    def test_counts_games_played_and_won_correctly(self):
        games = [
            {
                "player_name": "Alice",
                "answer": "whale",
                "guesses": ["whale"],
                "date": "2026-02-01",
            },
            {
                "player_name": "Alice",
                "answer": "crane",
                "guesses": ["stilt", "plumb", "vigor", "kayak", "monks", "brand"],
                "date": "2026-02-02",
            },
        ]
        stats = calculate_player_stats(games)
        assert stats["games_played"] == 2
        assert stats["games_won"] == 1


class TestWinRate:
    """Test suite for win rate calculations."""

    def test_returns_1_when_all_games_are_won(self):
        games = [
            {
                "player_name": "Alice",
                "answer": "whale",
                "guesses": ["whale"],
                "date": "2026-02-01",
            },
            {
                "player_name": "Alice",
                "answer": "crane",
                "guesses": ["crane"],
                "date": "2026-02-02",
            },
        ]
        stats = calculate_player_stats(games)
        assert stats["win_rate"] == 1

    def test_returns_correct_ratio_for_mix_of_wins_and_losses(self):
        games = [
            {
                "player_name": "Alice",
                "answer": "whale",
                "guesses": ["whale"],
                "date": "2026-02-01",
            },
            {
                "player_name": "Alice",
                "answer": "crane",
                "guesses": ["stilt", "plumb", "vigor", "kayak", "monks", "brand"],
                "date": "2026-02-02",
            },
            {
                "player_name": "Alice",
                "answer": "flint",
                "guesses": ["flint"],
                "date": "2026-02-03",
            },
        ]
        stats = calculate_player_stats(games)
        assert stats["win_rate"] == pytest.approx(2 / 3)


class TestAverageAttempts:
    """Test suite for average attempts calculations."""

    def test_returns_0_when_there_are_no_wins(self):
        games = [
            {
                "player_name": "Alice",
                "answer": "whale",
                "guesses": ["stilt", "plumb", "vigor", "kayak", "monks", "brand"],
                "date": "2026-02-01",
            },
        ]
        stats = calculate_player_stats(games)
        assert stats["average_attempts"] == 0

    def test_calculates_mean_attempts_for_winning_games(self):
        games = [
            {
                "player_name": "Alice",
                "answer": "whale",
                "guesses": ["crane", "slate", "whale"],
                "date": "2026-02-01",
            },
            {
                "player_name": "Alice",
                "answer": "crane",
                "guesses": ["stilt", "plumb", "vigor", "kayak", "monks", "brand"],
                "date": "2026-02-02",
            },
            {
                "player_name": "Alice",
                "answer": "flint",
                "guesses": ["flint"],
                "date": "2026-02-03",
            },
        ]
        stats = calculate_player_stats(games)
        assert stats["average_attempts"] == (3 + 1) / 2

    def test_ignores_lost_games_when_calculating_average(self):
        games = [
            {
                "player_name": "Alice",
                "answer": "whale",
                "guesses": ["stilt", "plumb", "vigor", "kayak", "monks", "brand"],
                "date": "2026-02-01",
            },
        ]
        stats = calculate_player_stats(games)
        assert stats["average_attempts"] == 0
