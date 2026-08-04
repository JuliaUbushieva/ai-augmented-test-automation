"""UI tests for the login flow - happy path, negative, and edge cases.

Run: pytest tests/ui/test_login.py -v
"""
import allure
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage

VALID_USER = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"


@pytest.fixture
def login_page(page: Page, ui_base_url: str) -> LoginPage:
    return LoginPage(page, ui_base_url).open()


@allure.feature("Login")
class TestLogin:

    @allure.title("Login with valid credentials succeeds")
    def test_login_valid_credentials(self, login_page: LoginPage):
        login_page.login(VALID_USER, VALID_PASSWORD)
        login_page.expect_success("You logged into a secure area!")

    @allure.title("Login with invalid username shows error message")
    def test_login_invalid_username(self, login_page: LoginPage):
        login_page.login("wronguser", VALID_PASSWORD)
        login_page.expect_error("Your username is invalid!")

    @allure.title("Login with invalid password shows error message")
    def test_login_invalid_password(self, login_page: LoginPage):
        login_page.login(VALID_USER, "wrongpassword")
        login_page.expect_error("Your password is invalid!")

    @allure.title("Login with empty fields shows username error")
    def test_login_empty_fields(self, login_page: LoginPage):
        login_page.login("", "")
        login_page.expect_error("Your username is invalid!")
