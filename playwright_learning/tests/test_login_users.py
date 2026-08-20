import re

import pytest
from playwright.sync_api import Page, expect

from playwright_learning.pages.login import LoginPage


@pytest.mark.smoke
def test_registered_user_can_log_in(page: Page, login_user):
    login_page = LoginPage(page)
    login_page.open()
    login_response = login_page.login(
        login_user["username"],
        login_user["password"],
    )

    assert login_response.status == 200, (
        f"Expected login API status 200, got {login_response.status}"
    )
    print(
        f"Login API status for {login_user['username']}: "
        f"{login_response.status}"
    )

    expect(page).to_have_url(re.compile(r".*/dashboard/.*"))
    expect(
        page.get_by_role("button", name=re.compile("sign out", re.IGNORECASE))
    ).to_be_visible()

    print(f"Login passed for user: {login_user['username']}")
