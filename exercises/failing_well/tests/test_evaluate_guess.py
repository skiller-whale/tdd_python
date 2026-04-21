from src.evaluate_guess import evaluate_guess


def test_correct():
    assert evaluate_guess("crane", "crane") == "ggggg"


def test_incorrect():
    assert evaluate_guess("bumps", "crane") == "-----"


def test_yellow_letters():
    assert evaluate_guess("acorn", "crane") == "yy-yy"


def test_mixed():
    assert evaluate_guess("grace", "crane") == "-ggyg"


def test_duplicate_letters():
    assert evaluate_guess("error", "crane") == "yg---"
