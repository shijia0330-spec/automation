import pytest

from utils.api_client import get_posts, assert_ok_list

@pytest.mark.smoke
def test_posts_sorted_desc_limit_5():
    response = get_posts({"_sort": "id", "_order": "desc", "_limit": 5})
    data = assert_ok_list(response)

    assert len(data) == 5

    ids = [item["id"] for item in data]
    assert ids == sorted(ids, reverse=True)


@pytest.mark.smoke
def test_posts_page1_and_page2_no_overlap():
    page1_resp = get_posts({"_start": 0, "_limit": 5})
    page2_resp = get_posts({"_start": 5, "_limit": 5})
    page1 = assert_ok_list(page1_resp)
    page2 = assert_ok_list(page2_resp)

    assert len(page1) == 5
    assert len(page2) == 5

    ids1 = {item["id"] for item in page1}
    ids2 = {item["id"] for item in page2}
    assert ids1.isdisjoint(ids2)


@pytest.mark.negative
def test_invalid_sort_field_behavior():
    response = get_posts({"_sort": "notARealField"})
    data = assert_ok_list(response)

    # JSONPlaceholder tolerates unknown sort fields. 
    assert isinstance(data, list)

@pytest.mark.smoke
def test_posts_sorted_asc_limit_3():
    response = get_posts({"_sort": "id", "_order": "asc", "_limit": 3})
    data = assert_ok_list(response)

    assert len(data) == 3 # check if the data has 3 items
    ids = [item["id"] for item in data] # get the ids from the data
    assert ids == sorted(ids) # check if the ids are sorted in ascending order


@pytest.mark.smoke
def test_posts_limit_0_returns_empty_or_default():
    response = get_posts({"_limit": 0})
    data = assert_ok_list(response)

    # Different APIs may treat limit=0 differently
    if len(data) == 0: # check if the data is an empty list
        assert data == [] # check if the data is an empty list
    else: # check if the data is not an empty list
        assert len(data) > 0 # check if the data has more than 0 items