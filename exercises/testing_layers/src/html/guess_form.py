def guess_form():
    """Generate HTML for the guess input form."""
    return ['''<form method="post">
        <label for="latestGuess">guess</label>
        <input type="text" name="latestGuess" aria-label="guess" autofocus autocomplete="off" required>
        <input type="submit" value="Submit Guess">
    </form>''']
