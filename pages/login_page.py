"""Page Object Model for the-internet.herokuapp.com login page."""
from playwright.sync_api import Page, expect


class LoginPage:
    """Encapsulates locators and actions for the /login page."""

    PATH = "/login"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        # Playwright locators are lazy - defined once, resolved at action time
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")
        self.logout_button = page.locator("a[href='/logout']")

    def open(self):
        self.page.goto(f"{self.base_url}{self.PATH}")
        return self

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return self

    def expect_success(self, message: str):
        expect(self.flash_message).to_contain_text(message)
        expect(self.logout_button).to_be_visible()

    def expect_error(self, message: str):
        expect(self.flash_message).to_contain_text(message)
