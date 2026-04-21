from src.validate_guess import validate_guess


def test_returns_valid_for_a_5_letter_word_in_the_word_list():
    assert validate_guess("crane", ["crane", "audio"]) == {"valid": True}


def test_returns_invalid_for_a_word_that_is_not_5_letters():
    assert validate_guess("cr", ["crane", "audio"]) == {
        "valid": False,
        "reason": "Guess must be 5 letters",
    }


def test_returns_invalid_for_a_word_containing_non_letter_characters():
    assert validate_guess("cr4ne", ["crane", "audio"]) == {
        "valid": False,
        "reason": "Guess must only contain letters",
    }


def test_returns_invalid_for_a_word_not_in_the_word_list():
    assert validate_guess("audio", ["crane"]) == {
        "valid": False,
        "reason": "Not a recognised word",
    }
