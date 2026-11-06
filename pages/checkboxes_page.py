"""Page Object Model for the-internet.herokuapp.com checkboxes page."""
from playwright.sync_api import Page


class CheckboxesPage:
    """Encapsulates locators and actions for the /checkboxes page."""

    PATH = "/checkboxes"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        # The page has no ids, just two plain checkboxes, so we select by position
        self.checkboxes = page.locator("input[type='checkbox']")

    def open(self):
        self.page.goto(f"{self.base_url}{self.PATH}")
        return self

    def checkbox(self, index: int):
        """Return the Nth checkbox locator (0-based)."""
        return self.checkboxes.nth(index)

    def toggle(self, index: int):
        self.checkbox(index).click()
        return self

    def is_checked(self, index: int) -> bool:
        return self.checkbox(index).is_checked()

    def count(self) -> int:
        return self.checkboxes.count()