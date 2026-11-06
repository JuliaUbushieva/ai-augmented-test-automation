from playwright.sync_api import Page


class CheckboxesPage:

    PATH = "/checkboxes"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.checkboxes = page.locator("input[type='checkbox']")

    def open(self):
        self.page.goto(f"{self.base_url}{self.PATH}")
        return self

    def checkbox(self, index: int):
        return self.checkboxes.nth(index)

    def toggle(self, index: int):
        self.checkbox(index).click()
        return self

    def is_checked(self, index: int) -> bool:
        return self.checkbox(index).is_checked()

    def count(self) -> int:
        return self.checkboxes.count()