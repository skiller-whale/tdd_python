from src.validate_guess import validate_guess


def test_validates_and_invalidates_guesses():
    words = ["crane", "rates", "towns"]
    assert validate_guess("crane", words)["valid"] is True
    assert validate_guess("cran", words)["valid"] is False
    assert validate_guess("cr4ne", words)["valid"] is False
    assert validate_guess("bumps", words)["valid"] is False


def test_returns_a_reason_for_invalid_guesses():
    words = ["crane"]
    too_short = validate_guess("cran", words)
    assert too_short.get("reason") is not None
    non_letter = validate_guess("cr4ne", words)
    assert non_letter.get("reason") is not None
    not_in_list = validate_guess("bumps", words)
    assert not_in_list.get("reason") is not None
