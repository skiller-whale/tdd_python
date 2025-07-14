import pytest
from tests.lib.browser import Browser
from tests.lib.test_server import TestServer


@pytest.fixture
def server():
    """Start a test server for the game."""
    test_server = TestServer()
    test_server.start(port=0)
    yield test_server
    test_server.stop()


@pytest.fixture
def browser(server):
    """Create a browser instance connected to the test server."""
    browser_instance = Browser(server.base_url)
    yield browser_instance
    browser_instance.close()


def test_shows_success_when_correct_answer_guessed_first_time(browser):
    """Test that the game shows success when the correct answer is guessed first time."""
    browser.visit("/")
    browser.enter_guess("whale")
    assert browser.get_status() == "You won!"


def test_shows_failure_and_correct_answer_when_game_is_lost(browser):
    """Test that the game shows failure and correct answer when lost."""
    browser.visit("/")
    browser.enter_guess("fishy")
    browser.enter_guess("shark")
    browser.enter_guess("shell")
    browser.enter_guess("trout")
    browser.enter_guess("salty")
    browser.enter_guess("ocean")

    assert browser.get_status() == "You lost!"
    assert browser.get_correct_answer() == "WHALE"


def test_shows_previous_guesses_in_game(browser):
    """Test that the game shows previous guesses."""
    browser.visit("/")
    browser.enter_guess("fishy")
    browser.enter_guess("shark")
    browser.enter_guess("shell")
    browser.enter_guess("trout")
    browser.enter_guess("salty")
    browser.enter_guess("ocean")

    assert browser.get_guess(0) == "FISHY"
    assert browser.get_guess(1) == "SHARK"
    assert browser.get_guess(2) == "SHELL"
    assert browser.get_guess(3) == "TROUT"
    assert browser.get_guess(4) == "SALTY"
    assert browser.get_guess(5) == "OCEAN"


@pytest.mark.skip(reason="TODO")
def test_shows_error_message_for_invalid_guesses(browser):
    """Test that the game shows error messages for invalid guesses."""
    # arrange
    browser.visit("/")

    # act
    ...

    # assert
    # NOTE: you can use `browser.get_error()` to get the text content of
    # the first element on the page with the class "error"


@pytest.mark.skip(reason="TODO")
def test_shows_colour_coded_feedback_for_previous_guesses(browser):
    """Test that the game shows color-coded feedback for guesses."""
    # arrange
    browser.visit("/")

    # act
    # a useful guess to try here would be "water", which should be reported as:
    #   - green for the first character (W)
    #   - yellow for the second character (A)
    #   - gray for the third character (T)
    #   - yellow for the fourth character (E)
    #   - gray for the fifth character (R)

    # assert
    # NOTE: you can use `browser.get_guess_char_class(n, m)` to get the class
    # of the mth character of the nth guess - and then check this is either
    # "green", "yellow", or "gray" (as appropriate)
