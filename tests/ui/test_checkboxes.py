import allure
import pytest
from playwright.sync_api import Page

from pages.checkboxes_page import CheckboxesPage


@pytest.fixture
def checkboxes_page(page: Page, ui_base_url: str) -> CheckboxesPage:
    return CheckboxesPage(page, ui_base_url).open()


@allure.feature("Checkboxes")
class TestCheckboxes:

    @allure.title("Page loads with exactly 2 checkboxes")
    def test_checkbox_count(self, checkboxes_page: CheckboxesPage):
        assert checkboxes_page.count() == 2

    @allure.title("First checkbox is unchecked by default")
    def test_first_checkbox_default_state(self, checkboxes_page: CheckboxesPage):
        assert checkboxes_page.is_checked(0) is False

    @allure.title("Second checkbox is checked by default")
    def test_second_checkbox_default_state(self, checkboxes_page: CheckboxesPage):
        assert checkboxes_page.is_checked(1) is True

    @allure.title("Clicking an unchecked checkbox checks it")
    def test_check_unchecked_checkbox(self, checkboxes_page: CheckboxesPage):
        checkboxes_page.toggle(0)
        assert checkboxes_page.is_checked(0) is True

    @allure.title("Clicking a checked checkbox unchecks it")
    def test_uncheck_checked_checkbox(self, checkboxes_page: CheckboxesPage):
        checkboxes_page.toggle(1)
        assert checkboxes_page.is_checked(1) is False

    @allure.title("Clicking a checkbox twice returns it to original state")
    def test_double_toggle_returns_to_original(self, checkboxes_page: CheckboxesPage):
        original_state = checkboxes_page.is_checked(0)
        checkboxes_page.toggle(0)
        checkboxes_page.toggle(0)
        assert checkboxes_page.is_checked(0) == original_state