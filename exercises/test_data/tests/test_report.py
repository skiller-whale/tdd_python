"""Tests for report module."""

import pytest
from src.report import generate_player_report


class TestGeneratePlayerReport:
    """Test suite for generate_player_report function."""

    def test_includes_player_display_name_as_header(self):
        player_stats = {
            "player_id": "123",
            "email": "test@example.com",
            "player_name": "TestPlayer",
            "games_played": 50,
            "games_won": 25,
            "win_rate": 0.5,
            "average_attempts": 3.5,
            "fastest_win": 2,
            "first_played": "2024-01-01",
            "last_played": "2024-06-01",
            "rank": 10,
            "percentile": 90,
            "achievements": [],
        }

        report = generate_player_report(player_stats)
        assert "=== TestPlayer ===" in report

    def test_includes_player_id_and_email(self):
        player_stats = {
            "player_id": "123",
            "email": "test@example.com",
            "player_name": "TestPlayer",
            "games_played": 50,
            "games_won": 25,
            "win_rate": 0.5,
            "average_attempts": 3.5,
            "fastest_win": 2,
            "first_played": "2024-01-01",
            "last_played": "2024-06-01",
            "rank": 10,
            "percentile": 90,
            "achievements": [],
        }

        report = generate_player_report(player_stats)
        assert "ID: 123" in report
        assert "Email: test@example.com" in report

    def test_includes_stats_section_with_games_played_and_win_rate(self):
        player_stats = {
            "player_id": "123",
            "email": "test@example.com",
            "player_name": "TestPlayer",
            "games_played": 50,
            "games_won": 25,
            "win_rate": 0.5,
            "average_attempts": 3.5,
            "fastest_win": 2,
            "first_played": "2024-01-01",
            "last_played": "2024-06-01",
            "rank": 10,
            "percentile": 90,
            "achievements": [],
        }

        report = generate_player_report(player_stats)
        assert "--- Stats ---" in report
        assert "Games Played: 50" in report
        assert "Games Won: 25" in report
        assert "Win Rate: 50.0%" in report

    def test_includes_performance_section_with_average_attempts_and_fastest_win(self):
        player_stats = {
            "player_id": "123",
            "email": "test@example.com",
            "player_name": "TestPlayer",
            "games_played": 50,
            "games_won": 25,
            "win_rate": 0.5,
            "average_attempts": 3.5,
            "fastest_win": 2,
            "first_played": "2024-01-01",
            "last_played": "2024-06-01",
            "rank": 10,
            "percentile": 90,
            "achievements": [],
        }

        report = generate_player_report(player_stats)
        assert "--- Performance ---" in report
        assert "Average Attempts: 3.5" in report
        assert "Fastest Win: 2 guess(es)" in report

    def test_includes_activity_section_with_first_and_last_played_dates(self):
        player_stats = {
            "player_id": "123",
            "email": "test@example.com",
            "player_name": "TestPlayer",
            "games_played": 50,
            "games_won": 25,
            "win_rate": 0.5,
            "average_attempts": 3.5,
            "fastest_win": 2,
            "first_played": "2024-01-01",
            "last_played": "2024-06-01",
            "rank": 10,
            "percentile": 90,
            "achievements": [],
        }

        report = generate_player_report(player_stats)
        assert "--- Activity ---" in report
        assert "First Played: 2024-01-01" in report
        assert "Last Played: 2024-06-01" in report

    def test_includes_ranking_section_with_rank_and_percentile(self):
        player_stats = {
            "player_id": "123",
            "email": "test@example.com",
            "player_name": "TestPlayer",
            "games_played": 50,
            "games_won": 25,
            "win_rate": 0.5,
            "average_attempts": 3.5,
            "fastest_win": 2,
            "first_played": "2024-01-01",
            "last_played": "2024-06-01",
            "rank": 10,
            "percentile": 90,
            "achievements": [],
        }

        report = generate_player_report(player_stats)
        assert "--- Ranking ---" in report
        assert "Rank: #10" in report
        assert "Percentile: Top 90%" in report

    def test_includes_achievements_section(self):
        player_stats = {
            "player_id": "123",
            "email": "test@example.com",
            "player_name": "TestPlayer",
            "games_played": 50,
            "games_won": 25,
            "win_rate": 0.5,
            "average_attempts": 3.5,
            "fastest_win": 2,
            "first_played": "2024-01-01",
            "last_played": "2024-06-01",
            "rank": 10,
            "percentile": 90,
            "achievements": [],
        }

        report = generate_player_report(player_stats)
        assert "--- Achievements ---" in report
        assert "No achievements yet." in report

    def test_formats_each_achievement_with_trophy_emoji(self):
        player_stats = {
            "player_id": "123",
            "email": "test@example.com",
            "player_name": "TestPlayer",
            "games_played": 50,
            "games_won": 25,
            "win_rate": 0.5,
            "average_attempts": 3.5,
            "fastest_win": 2,
            "first_played": "2024-01-01",
            "last_played": "2024-06-01",
            "rank": 10,
            "percentile": 90,
            "achievements": ["First Win", "10-Game Streak"],
        }

        report = generate_player_report(player_stats)
        assert "🏆 First Win" in report
        assert "🏆 10-Game Streak" in report
