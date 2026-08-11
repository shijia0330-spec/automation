import pytest
from requests.api import post
from utils.api_client import assert_schema_list, assert_post_schema
from utils.api_client import get_posts, assert_ok_list


@pytest.mark.smoke
def test_api_query_string_title_like():
    keyword = "eum"
    response = get_posts({"title_like": keyword})
    data = assert_ok_list(response)
    assert_schema_list(data, assert_post_schema)

    assert len(data) > 0
    assert all(keyword.lower() in item["title"].lower() for item in data)


@pytest.mark.smoke
@pytest.mark.parametrize(
    "user_id, should_be_empty",
    [
        (1, False),
        (2, False),
        (9999, True),
    ],
)
def test_api_query_filter_user_id_parametrize(user_id, should_be_empty):
    response = get_posts({"userId": user_id})

    data = assert_ok_list(response)

    if should_be_empty:
        assert len(data) == 0
    else:
        assert len(data) > 0
        assert all(item["userId"] == user_id for item in data)


@pytest.mark.smoke
def test_api_query_string_title_like_returns_empty_for_random_keyword():
    keyword = "zzzznotfound"
    response = get_posts({"title_like": keyword})
    data = assert_ok_list(response)

    assert len(data) == 0  # random keyword should return no matches

@pytest.mark.negative
def test_api_query_filter_user_id_invalid_value():
    response = get_posts({"userId":"abc"})  
    data = assert_ok_list(response) # assert the response is a list
    assert len(data) == 0 # assert the length of the data is 0

@pytest.mark.negative
def test_api_query_filter_title_like_invalid_value():
    response = get_posts({"title_like":"no_match_20260730_xyz123"})  
    data = assert_ok_list(response) # assert the response is a list
    assert len(data) == 0 # assert the length of the data is 0


@pytest.mark.smoke
def test_posts_limit_2_schema():
    response = get_posts({"_limit":2})
    data = assert_ok_list(response)
    assert_schema_list(data, assert_post_schema)
    assert len(data) == 2
    print(data)

def test_schema_error_shows_failed_index_1():
    posts = [
        {"id": 1, "userId": 1, "title": "Valid", "body": "Valid"},
        {"id": "wrong", "userId": 1, "title": "Invalid", "body": "Invalid"},
    ]

    with pytest.raises(
        AssertionError,
        match="Schema validation failed at index 1",
    ) as error:
        assert_schema_list(posts, assert_post_schema)

    print(error.value)

def test_schema_error_shows_failed_index_2():
    posts = [
        {"id": 1, "userId": 1, "title": "Valid", "body": "Valid"},
        {"id": 2, "userId": 1, "title": "Invalid", "body": "Valid"},
        {"id": 3, "userId": 1, "title": "Valid", "body": 123},
    ]

    with pytest.raises(
    AssertionError,
    match="Schema validation failed at index 2"
   ) as error:
        assert_schema_list(posts, assert_post_schema)
    print(error.value)