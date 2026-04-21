import pytest

from src.evaluate_guess import evaluate_guess
from src.wordle_game import WordleGame


class TestWordleGame:
    class TestConstructor:
        def test_initializes_the_game_state(self):
            word_list = ["whale", "water", "fishy", "skill"]
            game = WordleGame("whale", word_list)
            assert game.correct_answer == "whale"
            assert game.word_list == word_list
            assert game.guesses == []
            assert game.evaluations == []

        def test_raises_an_error_if_the_answer_is_not_in_the_word_list(self):
            word_list = ["whale", "water", "fishy", "skill"]
            with pytest.raises(Exception):
                WordleGame("crane", word_list)

    class TestSubmitGuess:
        def test_correctly_evaluates_the_guess(self):
            word_list = ["whale", "water", "fishy", "skill"]
            game = WordleGame("whale", word_list)
            game.submit_guess("water")
            assert game.evaluations[0] == evaluate_guess("water", "whale")

        def test_does_not_accept_further_guesses_after_the_game_is_over(self):
            word_list = ["whale", "water", "fishy", "skill"]
            game = WordleGame("whale", word_list)
            game.submit_guess("whale")
            game.submit_guess("water")
            assert len(game.guesses) == 1

        def test_raises_an_error_for_invalid_guesses(self):
            word_list = ["whale", "water", "fishy", "skill"]
            game = WordleGame("whale", word_list)
            with pytest.raises(Exception):
                game.submit_guess("crane")
