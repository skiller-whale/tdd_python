#!/usr/bin/env python3
"""Wordle Stats CLI - Main entry point."""

import json
import sys
from pathlib import Path

from src.game_result import summarize_game
from src.player_stats import calculate_player_stats
from src.report import generate_player_report


# Load sample data
data_path = Path(__file__).parent.parent / "data" / "sample-results.json"
with open(data_path, "r", encoding="utf-8") as f:
    game_results = json.load(f)


# Helper: Get unique player names
def get_player_names():
    """Returns a list of unique player names from game results."""
    return list(set(r["playerName"] for r in game_results))


# Helper: Get games for a specific player
def get_player_games(player_name):
    """Returns all game results for a specific player."""
    return [r for r in game_results if r["playerName"] == player_name]


# Command implementations
def list_games():
    """Lists all game results with summary and date."""
    print("\n=== All Game Results ===\n")
    num_width = len(str(len(game_results)))
    for index, result in enumerate(game_results):
        print(f"{str(index + 1).rjust(num_width)}. {summarize_game(result)} [{result['date']}]")
    print(f"\nTotal: {len(game_results)} games\n")


def show_player_stats(player_name):
    """Shows statistics for a specific player."""
    player_games = get_player_games(player_name)
    if len(player_games) == 0:
        print(f"\nNo games found for player: {player_name}\n")
        return

    stats = calculate_player_stats(player_games)
    print(f"\n=== Stats for {player_name} ===\n")
    print(f"Games Played: {stats['gamesPlayed']}")
    print(f"Games Won: {stats['gamesWon']}")
    print(f"Win Rate: {stats['winRate'] * 100:.1f}%")
    print(f"Average Attempts: {stats['averageAttempts']:.1f}\n")


def show_player_report(player_name):
    """Generates and displays a full player report."""
    player_games = get_player_games(player_name)
    if len(player_games) == 0:
        print(f"\nNo games found for player: {player_name}\n")
        return

    stats = calculate_player_stats(player_games)
    all_player_stats = [
        {"playerName": name, **calculate_player_stats(get_player_games(name))}
        for name in get_player_names()
    ]
    ranked = rank_players(all_player_stats, sort_by="winRate", order="desc")
    player_rank = next(p for p in ranked if p["playerName"] == player_name)

    # Calculate additional stats
    wins = [g for g in player_games if g["guesses"][-1] == g["answer"]]
    fastest_win = min(len(g["guesses"]) for g in wins) if wins else 0
    dates = sorted(g["date"] for g in player_games)
    percentile = int((player_rank["rank"] / len(ranked)) * 100)

    # Generate sample achievements
    achievements = []
    if stats["winRate"] == 1.0:
        achievements.append("Perfect Record")
    if fastest_win == 1:
        achievements.append("Hole-in-One")
    if stats["gamesPlayed"] >= 5:
        achievements.append("Dedicated Player")
    if stats["averageAttempts"] < 3:
        achievements.append("Speed Solver")

    report = generate_player_report({
        "playerId": f"player-{player_name.lower()}",
        "email": f"{player_name.lower()}@example.com",
        "playerName": player_name,
        "gamesPlayed": stats["gamesPlayed"],
        "gamesWon": stats["gamesWon"],
        "winRate": stats["winRate"],
        "averageAttempts": stats["averageAttempts"],
        "fastestWin": fastest_win,
        "firstPlayed": dates[0],
        "lastPlayed": dates[-1],
        "rank": player_rank["rank"],
        "percentile": percentile,
        "achievements": achievements,
    })

    print("\n" + report + "\n")


def rank_players(player_stats_list, sort_by="winRate", order="desc"):
    """Ranks players based on a specific stat.
    
    Args:
        player_stats_list: List of player stats dictionaries
        sort_by: Key to sort by (default: "winRate")
        order: Sort order "asc" or "desc" (default: "desc")
    
    Returns:
        Sorted list with rank added to each player dict
    """
    reverse = order == "desc"
    sorted_players = sorted(player_stats_list, key=lambda p: p[sort_by], reverse=reverse)
    return [
        {**player, "rank": index + 1}
        for index, player in enumerate(sorted_players)
    ]


def show_help():
    """Displays help information for CLI commands."""
    players = ", ".join(get_player_names())
    print(f"""
Wordle Stats CLI
================

Commands:
  python -m wordle_stats list              List all game results
  python -m wordle_stats stats <player>    Show stats for a specific player
  python -m wordle_stats report <player>   Generate full player report
  python -m wordle_stats help              Show this help message

Interactive mode:
  python -m wordle_stats                   Start interactive menu

Available players: {players}
""")


def show_menu():
    """Displays the interactive menu."""
    print("""
╔═════════════════════════════════════╗
║     Wordle Stats - Main Menu        ║
╠═════════════════════════════════════╣
║  1. List all games                  ║
║  2. Show player stats               ║
║  3. Generate player report          ║
║  0. Exit                            ║
╚═════════════════════════════════════╝
""")


def run_interactive():
    """Runs the interactive menu mode."""
    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            list_games()
            input("Press Enter to continue...")
        elif choice == "2":
            players = ", ".join(get_player_names())
            print(f"\nAvailable players: {players}")
            player = input("Enter player name: ").strip()
            show_player_stats(player)
            input("Press Enter to continue...")
        elif choice == "3":
            players = ", ".join(get_player_names())
            print(f"\nAvailable players: {players}")
            player = input("Enter player name: ").strip()
            show_player_report(player)
            input("Press Enter to continue...")
        elif choice == "0":
            print("\nGoodbye!\n")
            sys.exit(0)
        else:
            print("\nInvalid option. Please try again.\n")
            input("Press Enter to continue...")


def main():
    """Main entry point for the CLI application."""
    args = sys.argv[1:]

    if len(args) == 0:
        # Interactive mode
        run_interactive()
    else:
        # Command-line mode
        command = args[0]

        if command == "list":
            list_games()
        elif command == "stats":
            if len(args) > 1:
                show_player_stats(args[1])
            else:
                players = ", ".join(get_player_names())
                print("\nError: Please specify a player name\n")
                print(f"Available players: {players}\n")
        elif command == "report":
            if len(args) > 1:
                show_player_report(args[1])
            else:
                players = ", ".join(get_player_names())
                print("\nError: Please specify a player name\n")
                print(f"Available players: {players}\n")
        elif command == "help":
            show_help()
        else:
            print(f"\nUnknown command: {command}\n")
            show_help()


if __name__ == "__main__":
    main()
