import os
from playwright.sync_api import sync_playwright


class Browser:
    """Browser automation for testing the word game."""

    def __init__(self, base_url):
        self.base_url = base_url
        self.timeout = 500
        self.playwright = None
        self.browser = None
        self.page = None

    def _start_browser(self):
        """Start the browser if not already started."""
        if self.playwright is None:
            self.playwright = sync_playwright().start()
            headless = os.environ.get("SHOW_BROWSER") != "true"
            self.browser = self.playwright.chromium.launch(headless=headless)
            context = self.browser.new_context()
            self.page = context.new_page()
            self.page.set_default_timeout(self.timeout)

    def _get_full_url(self, url):
        """Get the full URL by combining base URL with relative path."""
        if url.startswith("http"):
            return url
        return f"{self.base_url.rstrip('/')}{url}"

    def set_timeout(self, timeout):
        """Set the timeout for browser operations."""
        self.timeout = timeout
        if self.page:
            self.page.set_default_timeout(timeout)

    def visit(self, url):
        """Navigate to the given URL."""
        self._start_browser()
        full_url = self._get_full_url(url)
        self.page.goto(full_url)

    def enter_guess(self, guess):
        """Enter a guess into the form and submit it."""
        self._start_browser()
        input_field = self.page.get_by_label("guess")
        input_field.fill(guess)
        input_field.press("Enter")

    def get_status(self):
        """Get the current game status text."""
        self._start_browser()
        status_element = self.page.locator(".status")
        if status_element.count() == 0:
            raise Exception("Status element not found in page")
        return status_element.inner_text().strip()

    def get_error(self):
        """Get the current error message."""
        self._start_browser()
        error_element = self.page.locator(".error")
        if error_element.count() == 0:
            raise Exception("Error element not found in page")
        return error_element.inner_text().strip()

    def get_correct_answer(self):
        """Get the correct answer when game is lost."""
        self._start_browser()
        correct_element = self.page.locator(".correct-answer")
        if correct_element.count() == 0:
            raise Exception("Correct answer element not found in page")
        return correct_element.inner_text().strip()

    def get_guess(self, index):
        """Get the text of a specific guess by index."""
        self._start_browser()
        guess_element = self.page.locator(f".guess:nth-child({index + 1})")
        if guess_element.count() == 0:
            raise Exception(f"Guess element {index} not found in page")
        text = guess_element.inner_text().replace("\n", "").strip()
        return text

    def get_guess_char_class(self, guess_index, char_index):
        """Get the CSS class of a specific character in a guess."""
        self._start_browser()
        guess_element = self.page.locator(f".guess:nth-child({guess_index + 1})")
        if guess_element.count() == 0:
            raise Exception(f"Guess element {guess_index} not found in page")

        char_element = guess_element.locator(f"span:nth-child({char_index + 1})")
        if char_element.count() == 0:
            raise Exception(f"Character element {char_index} in guess {guess_index} not found in page")

        return char_element.get_attribute("class") or ""

    def close(self):
        """Close the browser."""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
