from src.validate_guess import validate_guess


class TestValidateGuess:
    class TestWithAValidGuess:
        def test_returns_valid_for_a_recognised_5_letter_word(self):
            result = validate_guess("crane", ["crane", "rates"])
            assert result["valid"] is True

    class TestWithAnInvalidGuess:
        def test_returns_invalid_with_a_reason_for_a_guess_that_is_too_short(self):
            result = validate_guess("cran", ["crane", "rates"])
            assert result["valid"] is False
            assert result["reason"] == "Guess must be 5 letters"

        def test_returns_invalid_with_a_reason_for_non_letter_characters(self):
            result = validate_guess("cr4ne", ["crane", "rates"])
            assert result["valid"] is False
            assert result["reason"] == "Guess must only contain letters"

        def test_returns_invalid_with_a_reason_for_a_guess_not_in_the_word_list(self):
            result = validate_guess("bumps", ["crane", "rates"])
            assert result["valid"] is False
            assert result["reason"] == "Not a recognised word"
