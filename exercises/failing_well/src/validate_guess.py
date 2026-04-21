def validate_guess(word, word_list):
    """
    Validate a word before accepting it as a Wordle guess.

    Returns {"valid": True} if the word is a valid guess, or
    {"valid": False, "reason": <str>} if it is not.
    """
    if len(word) != 5:
        return {"valid": False, "reason": "Guess must be 5 letters"}
    if not word.isalpha():
        return {"valid": False, "reason": "Guess must only contain letters"}
    if word not in word_list:
        return {"valid": False, "reason": "Not a recognised word"}
    return {"valid": True}
