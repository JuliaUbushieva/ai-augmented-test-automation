"""UI tests for the dropdown page.

Run: pytest tests/ui/test_dropdown.py -v
"""
import allure
import pytest
from playwright.sync_api import Page

from pages.dropdown_page import DropdownPage


@pytest.fixture
def dropdown_page(page: Page, ui_base_url: str) -> DropdownPage:
    return DropdownPage(page, ui_base_url).open()


@allure.feature("Dropdown")
class TestDropdown:

    @allure.title("No option is selected by default")
    def test_default_has_no_selection(self, dropdown_page: DropdownPage):
        assert dropdown_page.selected_value() == ""

    @allure.title("Selecting Option 1 sets the value to 1")
    def test_select_option_1(self, dropdown_page: DropdownPage):
        dropdown_page.select_by_label("Option 1")
        assert dropdown_page.selected_value() == "1"

    @allure.title("Selecting Option 2 sets the value to 2")
    def test_select_option_2(self, dropdown_page: DropdownPage):
        dropdown_page.select_by_label("Option 2")
        assert dropdown_page.selected_value() == "2"

    @allure.title("Switching from Option 1 to Option 2 updates the selection")
    def test_change_selection(self, dropdown_page: DropdownPage):
        dropdown_page.select_by_label("Option 1")
        dropdown_page.select_by_label("Option 2")
        assert dropdown_page.selected_value() == "2"