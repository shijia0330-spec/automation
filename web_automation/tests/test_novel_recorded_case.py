import pytest

from pages.novel_home_page import NovelHomePage


@pytest.mark.smoke
def test_tc_novel_001_navigation_and_search(page):
    novel_home = NovelHomePage(page)
    novel_home.open()
    novel_home.assert_home_visible()

    novel_home.go_to_rankings()
    novel_home.go_to_all_works()
    novel_home.go_home()

    novel_home.assert_search_box_visible()
    novel_home.search("test")
    novel_home.go_home()

    assert "novel.hctestedu.com" in page.url


@pytest.mark.smoke
def test_tc_novel_002_open_book_details(page):
    novel_home = NovelHomePage(page)
    novel_home.open()
    novel_home.assert_sample_book_link_visible()
    novel_home.open_sample_book()

    assert "novel.hctestedu.com" in page.url
    assert page.url.rstrip("/") != novel_home.URL.rstrip("/")
