"""Computes aggregate player statistics from game results.

PlayerStats shape:
{
    games_played:      int,
    games_won:         int,
    win_rate:          float,   // 0-1
    average_attempts:  float,   // mean attempts for wins only
}
"""


def calculate_player_stats(game_results):
    """Calculates aggregate player statistics from a list of GameResult objects."""
    if len(game_results) == 0:
        return {
            "games_played": 0,
            "games_won": 0,
            "win_rate": 0,
            "average_attempts": 0,
        }

    games_played = len(game_results)
    games_won = len([g for g in game_results if is_game_won(g)])
    win_rate = games_won / games_played
    average_attempts = calculate_average_attempts(game_results)
    
    return {
        "games_played": games_played,
        "games_won": games_won,
        "win_rate": win_rate,
        "average_attempts": average_attempts,
    }


def calculate_average_attempts(game_results):
    """Calculates the average number of attempts for winning games only.
    
    Returns 0 if there are no wins.
    """
    winning_games = [g for g in game_results if is_game_won(g)]
    if len(winning_games) == 0:
        return 0
    
    total_attempts = sum(len(g["guesses"]) for g in winning_games)
    return total_attempts / len(winning_games)


def is_game_won(game_result):
    """Determines whether a game is won or lost based on the guesses and answer."""
    return game_result["guesses"][-1] == game_result["answer"]
