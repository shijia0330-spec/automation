import re

import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://rahulshettyacademy.com/client"


@pytest.mark.smoke
def test_registered_user_can_log_in(page: Page, login_user):
    page.goto(BASE_URL)

    page.locator("#userEmail").fill(login_user["username"])
    page.locator("#userPassword").fill(login_user["password"])
    page.locator("#login").click()

    expect(page).to_have_url(re.compile(r".*/dashboard/.*"))
    expect(
        page.get_by_role("button", name=re.compile("sign out", re.IGNORECASE))
    ).to_be_visible()

    print(f"Login passed for user: {login_user['username']}")
