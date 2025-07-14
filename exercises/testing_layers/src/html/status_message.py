def status_message(status):
    """Generate HTML for displaying game status messages."""

    messages = {
        "won": "You won!",
        "lost": "You lost!",
        "playing": ""
    }

    message = messages.get(status, "")
    if not message:
        return []

    html_parts = [f'<div class="status">{message}</div>']

    # Add correct answer when game is lost
    if status == "lost":
        html_parts.append('<div>The correct answer was: <span class="correct-answer">WHALE</span></div>')

    return html_parts
