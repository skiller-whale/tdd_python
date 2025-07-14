import pytest
from src.server import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_returns_some_html(client):
    """Test that GET / returns some HTML."""
    response = client.get("/")

    # NOTE: this is a very basic test with minimal assertions
    # testing that the HTML is interactive in the right way is done higher up, in test_game.py
    assert b"<h1>Skiller Wordle</h1>" in response.data
    assert response.status_code == 200


def test_post_with_valid_guess_redirects_with_guess_added_to_url(client):
    """Test that POST / with valid guess in form data redirects with guess added to the URL."""
    response = client.post(
        "/?guesses=fishy&guesses=shark",
        data={"latestGuess": "whale"}
    )

    assert response.status_code == 302 # 302 means redirect to response.location
    assert "guesses=fishy&guesses=shark&guesses=whale" in response.location


@pytest.mark.skip(reason="TODO")
def test_post_with_invalid_guess_redirects_with_guess_not_added_to_url(client):
    pass


@pytest.mark.skip(reason="TODO")
def test_post_with_invalid_guess_redirects_with_error_message_added_to_url(client):
    # Note: The redirected url should include a query parameter like
    # `error=your+guess+is+too+long` if the guess is too long.
    pass
