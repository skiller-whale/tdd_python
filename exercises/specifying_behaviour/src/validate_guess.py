import re


def validate_guess(word, word_list):
    """Validates a word before accepting it as a Wordle guess.

    Args:
        word: the word to validate
        word_list: list of valid 5-letter words

    Returns:
        {"valid": True} or {"valid": False, "reason": str}
    """
    if len(word) != 5:
        return {"valid": False, "reason": "Guess must be 5 letters"}
    if not re.match(r"^[a-z]+$", word):
        return {"valid": False, "reason": "Guess must only contain letters"}
    if word not in word_list:
        return {"valid": False, "reason": "Not a recognised word"}
    return {"valid": True}
