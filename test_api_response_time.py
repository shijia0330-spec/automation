from utils.api_client import assert_ok_list, get_posts


MAX_RESPONSE_SECONDS = 5


def test_posts_response_time_is_under_limit():
    response = get_posts({"_limit": 1})
    assert_ok_list(response)

    elapsed_seconds = response.elapsed.total_seconds()
    assert elapsed_seconds < MAX_RESPONSE_SECONDS, (
        f"Expected response under {MAX_RESPONSE_SECONDS}s, "
        f"got {elapsed_seconds:.3f}s"
    )