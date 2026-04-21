def get_game_status(guesses, target):
    """Returns the current status of a Wordle game.

    Args:
        guesses: list of guesses made so far (lowercase 5-letter strings)
        target: the target word (lowercase 5-letter string)

    Returns:
        "won", "lost", or "in_progress"
    """
    if guesses and guesses[-1] == target:
        return "won"
    if len(guesses) >= 6:
        return "lost"
    return "in_progress"
