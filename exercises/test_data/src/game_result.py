"""GameResult validation and summarization.

GameResult represents a single completed Wordle game.

Shape:
{
    player_name: string,   // display name (also used as identifier)
    answer:      string,   // the 5-letter target word (lowercase)
    guesses:     list,     // each guess (lowercase, 5 letters)
    date:        string,   // ISO date string, e.g. "2026-02-18"
}
"""

import re


def validate_game_result(result):
    """Validates that a value is a well-formed GameResult.

    A valid GameResult must have:
    - a non-empty string `player_name`
    - a 5-letter lowercase alphabetic `answer`
    - `guesses` as a non-empty list of 5-letter lowercase alphabetic strings
    - `date` as a string matching YYYY-MM-DD
    - the game must be in a completed state (won or lost, i.e. last guess
      matches answer or there are 6 guesses)

    Returns {"valid": True} or {"valid": False, "reason": "..."}.
    """
    if result is None or not isinstance(result, dict):
        return {"valid": False, "reason": "Result must be an object"}

    if not isinstance(result.get("player_name"), str) or len(result.get("player_name", "")) == 0:
        return {"valid": False, "reason": "player_name must be a non-empty string"}

    if not isinstance(result.get("answer"), str) or not re.match(r"^[a-z]{5}$", result.get("answer", "")):
        return {"valid": False, "reason": "answer must be a 5-letter lowercase word"}

    guesses = result.get("guesses")
    if not isinstance(guesses, list) or len(guesses) == 0:
        return {"valid": False, "reason": "guesses must be a non-empty array"}

    for guess in guesses:
        if not isinstance(guess, str) or not re.match(r"^[a-z]{5}$", guess):
            return {
                "valid": False,
                "reason": "Each guess must be a 5-letter lowercase word",
            }

    if not isinstance(result.get("date"), str) or not re.match(r"^\d{4}-\d{2}-\d{2}$", result.get("date", "")):
        return {"valid": False, "reason": "date must be a YYYY-MM-DD string"}

    if guesses[-1] != result["answer"] and len(guesses) < 6:
        return {
            "valid": False,
            "reason": "Game must be in a completed state (won or lost)",
        }

    return {"valid": True}


def summarize_game(result):
    """Returns a one-line summary of a game result.

    Format: "PlayerName: ANSWER n/6 ✓" (for wins)
        or: "PlayerName: ANSWER X/6 ✗" (for losses)

    The answer is displayed in uppercase.
    """
    answer = result["answer"].upper()
    status = "✓" if result["guesses"][-1] == result["answer"] else "✗"
    attempts = len(result["guesses"]) if status == "✓" else "X"
    return f"{result['player_name']}: {answer} {attempts}/6 {status}"
