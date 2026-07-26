import pytest
from pages.novel_home_page import NovelHomePage


@pytest.mark.smoke
def test_tc_003_recorded_flow(page):
    # TC_003
    # Page Name: Home
    # Test Object: Top nav and search
    # Scenario: Verify home page load and essential controls visibility
    novel_home = NovelHomePage(page)
    novel_home.open()

    novel_home.assert_home_visible()
    novel_home.assert_search_box_visible()

    assert "novel.hctestedu.com" in page.url
