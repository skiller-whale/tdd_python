import pytest
from src.core.evaluate_guess import evaluate_guess


@pytest.mark.skip(reason="Logic not yet implemented")
def test_identifies_letters_not_in_the_word():
    # characters nowhere in the correct answer should be marked as such
    pass


@pytest.mark.skip(reason="Logic not yet implemented")
def test_identifies_letters_in_the_right_place():
    # characters in the correct answer and in the right place should be marked as such
    pass


@pytest.mark.skip(reason="Logic not yet implemented")
def test_identifies_letters_in_the_wrong_place():
    """Characters that are in the correct answer but not in the right place should be marked as such."""
    pass


@pytest.mark.skip(reason="Logic not yet implemented")
def test_doesnt_display_duplicates():
    """E.g. if a letter appears twice in the guess, but only once in the correct answer, it should only be marked once."""
    pass
