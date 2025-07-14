from flask import Flask, request, redirect, Response
from .core.game_status import game_status
from .core.evaluate_guess import evaluate_guess
from .core.validate_guess import validate_guess
from .html.error_message import error_message
from .html.guess_form import guess_form
from .html.guesses_feedback import guesses_feedback
from .html.page import page
from .html.status_message import status_message
from .game_state import game_state_from_url, game_state_to_url


app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_game():
    """Return the current state of the game."""
    # Get base game state from the URL query parameters
    state = game_state_from_url(request.url)
    guesses = state["guesses"]
    error = state["error"]

    # Generate derived game state
    status = game_status(guesses)

    # TODO: get colour evaluations for each guess, and pass them on to the guesses_feedback function

    # Build HTML content
    # Hint: you can use content.extend(error_message(error)) to include an error message
    content = []
    content.extend(guesses_feedback(guesses))

    if status == "playing":
        content.extend(guess_form())

    content.extend(status_message(status))

    return Response(page(content), mimetype="text/html")


@app.route("/", methods=["POST"])
def post_guess():
    """Handle a new guess submitted via the form."""
    # Get base game state from the URL query parameters
    state = game_state_from_url(request.url)
    guesses = state["guesses"]

    # Get new guess from the form data
    latest_guess = request.form.get("latestGuess", "").strip()

    # Validate the guess
    # TODO: validate the guess, and return an error message if it is invalid
    # You can do this by adding "error": error_message to the next_state dictionary

    # Add the valid guess to the state
    next_state = {"guesses": guesses + [latest_guess]}
    return redirect(game_state_to_url(next_state))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
