from src.get_game_status import get_game_status


def test_returns_won_when_last_guess_matches_the_target():
    assert get_game_status(["crane"], "crane") == "won"


def test_returns_lost_when_6_wrong_guesses_have_been_made():
    assert get_game_status(["audio", "ghost", "plumb", "fizzy", "words", "crane"], "blank") == "lost"


def test_returns_in_progress_when_fewer_than_6_guesses_have_been_made():
    assert get_game_status(["audio"], "ghost") == "in_progress"
