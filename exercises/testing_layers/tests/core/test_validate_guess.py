import pytest
from src.core.validate_guess import validate_guess


def test_allows_valid_guesses():
    assert validate_guess("hello") is None


@pytest.mark.skip(reason="TODO")
def test_invalidates_guesses_that_are_too_short():
    # TODO
    pass


@pytest.mark.skip(reason="TODO")
def test_invalidates_guesses_that_are_too_long():
    # TODO
    pass


@pytest.mark.skip(reason="TODO")
def test_invalidates_guesses_that_are_not_in_the_dictionary():
    # TODO
    pass
