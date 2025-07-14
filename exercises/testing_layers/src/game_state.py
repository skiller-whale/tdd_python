from urllib.parse import urlparse, parse_qs, urlencode


def game_state_from_url(url):
    """Extract game state from URL query parameters."""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    guesses = params.get("guesses", [])
    error = params.get("error", [None])[0]

    return {"guesses": guesses, "error": error}


def game_state_to_url(state):
    """Convert game state to URL query parameters."""
    params = {}

    if state.get("guesses"):
        params["guesses"] = state["guesses"]

    if state.get("error"):
        params["error"] = state["error"]

    query_string = urlencode(params, doseq=True)
    return f"/?{query_string}" if query_string else "/"
