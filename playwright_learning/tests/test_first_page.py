from playwright.sync_api import Page, expect


def test_open_example_page(page: Page):
    page.goto("https://example.com")

    expect(page).to_have_title("Example Domain")
