def game_status(guesses, target="whale"):
    """Determine the current status of the game."""
    if not guesses:
        return "playing"

    # Check if the last guess was correct
    if guesses[-1].lower() == target.lower():
        return "won"

    # Check if maximum guesses reached
    if len(guesses) >= 6:
        return "lost"

    return "playing"
