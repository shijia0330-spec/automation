import pytest

from utils.api_client import assert_ok_list, get_posts


@pytest.mark.smoke
def test_posts_content_type_is_json():
    response = get_posts({"_limit": 1})
    assert_ok_list(response)

    content_type = response.headers["Content-Type"]
    assert "application/json" in content_type, (
        f"Expected JSON Content-Type, got {content_type}"
    )


@pytest.mark.smoke
def test_posts_content_type_uses_utf8():
    response = get_posts({"_limit": 1})
    assert_ok_list(response)

    content_type = response.headers["Content-Type"]

    assert "charset=utf-8" in content_type, (
        f"Expected charset=utf-8, got {content_type}"
    )