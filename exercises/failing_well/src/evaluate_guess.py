def evaluate_guess(guess, correct_answer):
    """
    Evaluate a Wordle guess against the correct answer.

    Returns a 5-character string where:
      'g' = correct letter in correct position (green)
      'y' = correct letter in wrong position (yellow)
      '-' = letter not in the answer (grey)
    """
    evaluation = ["-"] * 5
    remaining = list(correct_answer)

    # check for greens
    for i in range(5):
        if correct_answer[i] == guess[i]:
            evaluation[i] = "g"
            remaining[i] = ""

    # check for yellows
    for i in range(5):
        if correct_answer[i] != guess[i] and guess[i] in remaining:
            evaluation[i] = "y"
            remaining[remaining.index(guess[i])] = ""

    return "".join(evaluation)
