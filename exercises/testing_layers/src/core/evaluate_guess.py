def evaluate_guess(guess, target="whale"):
    """Evaluate a guess against the target word, returning color feedback."""
    guess = guess.lower()
    target = target.lower()

    result = []

    # First pass: mark exact matches (green)
    for i, char in enumerate(guess):
        # TODO: if the letter is in the correct position, mark it as correct
        # TODO: mark the letter in the target as not available for partial matches
        pass

    # Second pass: mark partial matches (yellow)
    for i, char in enumerate(guess):
        # TODO: if the letter is in the correct answer but not in the right place, mark it as yellow
        # TODO: _only_ mark the letter if it was't an exact match in the first pass
        # TODO: mark the letter in the target as not available for further partial matches
        pass

    return result
