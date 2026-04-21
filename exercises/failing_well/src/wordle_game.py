from evaluate_guess import evaluate_guess
from validate_guess import validate_guess


class WordleGame:
    def __init__(self, correct_answer, word_list):
        """
        Create a new game of Wordle.

        Raises ValueError if the correct answer is not in the word list.
        """
        if correct_answer not in word_list:
            raise ValueError("Answer must be in the word list")

        self.correct_answer = correct_answer
        self.word_list = word_list
        self.guesses = []
        self.evaluations = []

    def submit_guess(self, guess):
        """
        Submit a guess. If valid, evaluates and records it.
        If the game is already over, does nothing.
        Raises ValueError if the guess is invalid.
        """
        if (self.guesses and self.guesses[-1] == self.correct_answer) or len(self.guesses) >= 6:
            return None

        result = validate_guess(guess, self.word_list)
        if not result["valid"]:
            raise ValueError(result.get("error"))

        evaluation = evaluate_guess(guess, self.correct_answer)
        self.guesses.append(guess)
        self.evaluations.append(evaluation)
