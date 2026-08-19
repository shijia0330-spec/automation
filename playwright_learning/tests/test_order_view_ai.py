import os
import re

from playwright.sync_api import Page, expect


BASE_URL = "https://rahulshettyacademy.com/client"
USERNAME = os.getenv("CLIENT_USERNAME")
PASSWORD = os.getenv("CLIENT_PASSWORD")
ORDER_ID = os.getenv("CLIENT_ORDER_ID", "6a84130021054ba465dd0f2c")


def test_view_order_shows_thank_you_message(page: Page):
    assert USERNAME, "Set the CLIENT_USERNAME environment variable"
    assert PASSWORD, "Set the CLIENT_PASSWORD environment variable"

    page.goto(BASE_URL)
    page.locator("#userEmail").fill(USERNAME)
    page.locator("#userPassword").fill(PASSWORD)
    page.locator("#login").click()

    expect(page).to_have_url(re.compile(r".*/dashboard/.*"))
    page.get_by_role("button", name=re.compile("orders", re.IGNORECASE)).click()

    order_rows = page.locator("tbody tr")
    expect(order_rows.first).to_be_visible(timeout=15_000)

    available_order_ids = page.locator("tbody tr th").all_text_contents()
    order_row = order_rows.filter(has_text=ORDER_ID)
    assert order_row.count() == 1, (
        f"Order {ORDER_ID} was not found. "
        f"Available order IDs: {available_order_ids}"
    )
    order_row.get_by_role("button", name=re.compile("view", re.IGNORECASE)).click()

    expect(
        page.get_by_text("Thank you for Shopping With Us", exact=False)
    ).to_be_visible()
