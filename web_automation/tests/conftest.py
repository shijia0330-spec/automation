import sys
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

# Ensure local imports like `from pages...` work from any pytest cwd.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--show-browser",
        action="store_true",
        default=False,
        help="Run browser in headed (visible) mode.",
    )


@pytest.fixture(scope="session")
def playwright_browser(request):
    headed = request.config.getoption("--show-browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed, slow_mo=200 if headed else 0)
        yield browser
        browser.close()


@pytest.fixture
def page(playwright_browser):
    context = playwright_browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login
