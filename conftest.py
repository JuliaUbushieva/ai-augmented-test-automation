"""Shared pytest fixtures for UI and API tests."""
import pytest


@pytest.fixture(scope="session")
def api_base_url():
    """Base URL for the public demo REST API (no auth required)."""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def ui_base_url():
    """Base URL for the public UI test practice site."""
    return "https://the-internet.herokuapp.com"
