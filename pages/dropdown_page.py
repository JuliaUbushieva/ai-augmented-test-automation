"""Page Object Model for the-internet.herokuapp.com dropdown page."""
from playwright.sync_api import Page


class DropdownPage:
    PATH = "/dropdown"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.dropdown = page.locator("#dropdown")

    def open(self):
        self.page.goto(f"{self.base_url}{self.PATH}")
        return self

    def select_by_label(self, label: str):
        self.dropdown.select_option(label=label)
        return self

    def selected_value(self) -> str:
        return self.dropdown.input_value()