from playwright.sync_api import Page, expect


class NovelHomePage:
    URL = "http://novel.hctestedu.com/"

    def __init__(self, page: Page):
        self.page = page
        self.rank_list_item = page.get_by_role("listitem").filter(has_text="排行榜")
        self.all_works_link = page.get_by_role("link", name="全部作品")
        self.home_link = page.get_by_role("link", name="首页", exact=True)
        self.search_box = page.get_by_role("textbox", name="书名、作者、关键字")
        self.sample_book_link = page.get_by_role("link", name="重生学霸小甜妻")

    def open(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded", timeout=60000)

    def go_to_rankings(self) -> None:
        self.rank_list_item.click()

    def go_to_all_works(self) -> None:
        self.all_works_link.click()

    def go_home(self) -> None:
        self.home_link.click()

    def search(self, keyword: str) -> None:
        self.search_box.click()
        self.search_box.fill(keyword)
        self.search_box.press("Enter")

    def assert_home_visible(self) -> None:
        expect(self.home_link).to_be_visible()

    def assert_search_box_visible(self) -> None:
        expect(self.search_box).to_be_visible()

    def open_sample_book(self) -> None:
        self.sample_book_link.click()

    def assert_sample_book_link_visible(self) -> None:
        expect(self.sample_book_link).to_be_visible()
