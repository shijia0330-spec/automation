import re

from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"


def test_standard_user_can_add_backpack_to_cart(page: Page):
    page.goto(BASE_URL)

    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(page.get_by_text("Products", exact=True)).to_be_visible()

    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")


def test_locked_user_cannot_log_in(page: Page):
    page.goto(BASE_URL)

    page.locator("[data-test='username']").fill("locked_out_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Sorry, this user has been locked out"
    )
