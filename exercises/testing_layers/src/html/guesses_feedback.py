def guesses_feedback(guesses):
    """Generate HTML for displaying all 6 guess rows."""
    # Ensure there are always 6 guesses displayed, with empty rows if needed
    html_parts = ['<div class="guesses">']

    for guess in guesses:
        # Get color evaluations for each guess
        html_parts.extend(guess_feedback(guess))

    for _ in range(6 - len(guesses)):
        # Add empty rows if there are fewer than 6 guesses
        html_parts.append(f'<div class="guess">{"<span></span>" * 5}</div>')

    html_parts.append('</div>')
    return html_parts


def guess_feedback(guess):
    """Generate the HTML for a single guess row."""
    html_parts = ['<div class="guess">']

    html_parts.extend([
        guess_char_feedback(char)
        for char in guess.upper()
    ])

    html_parts.append('</div>')
    return html_parts


def guess_char_feedback(char):
    """Generate HTML for a single character in a guess."""
    # NOTE: To add colour coding, you can add a class of "green", "yellow", or
    # "gray" to the span, like this: <span class="green">{char}</span>
    return f'<span>{char}</span>'
