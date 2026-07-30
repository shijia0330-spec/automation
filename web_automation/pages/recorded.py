import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://novel.hctestedu.com/")
    page.get_by_role("listitem").filter(has_text="排行榜").click()
    page.get_by_role("link", name="全部作品").click()
    page.get_by_role("link", name="首页", exact=True).click()
    page.get_by_role("textbox", name="书名、作者、关键字").click()
    page.get_by_role("textbox", name="书名、作者、关键字").fill("test")
    page.get_by_role("textbox", name="书名、作者、关键字").press("Enter")
    page.get_by_role("link", name="首页", exact=True).click()

    with open("dom_after_flow.html", "w", encoding="utf-8") as f:
        f.write(page.content())
    page.screenshot(path="after_flow.png", full_page=True)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
