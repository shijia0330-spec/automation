import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.smoke
def test_posts_sorted_desc_limit_5():
    response = requests.get(f"{BASE_URL}/posts?_sort=id&_order=desc&_limit=5")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 5

    ids = [item["id"] for item in data]
    assert ids == sorted(ids, reverse=True)


@pytest.mark.smoke
def test_posts_page1_and_page2_no_overlap():
    page1_resp = requests.get(f"{BASE_URL}/posts?_start=0&_limit=5")
    page2_resp = requests.get(f"{BASE_URL}/posts?_start=5&_limit=5")
    page1 = page1_resp.json()
    page2 = page2_resp.json()

    assert page1_resp.status_code == 200
    assert page2_resp.status_code == 200
    assert len(page1) == 5
    assert len(page2) == 5

    ids1 = {item["id"] for item in page1}
    ids2 = {item["id"] for item in page2}
    assert ids1.isdisjoint(ids2)


@pytest.mark.negative
def test_invalid_sort_field_behavior():
    response = requests.get(f"{BASE_URL}/posts?_sort=notARealField")
    data = response.json()

    # JSONPlaceholder tolerates unknown sort fields.
    assert response.status_code == 200
    assert isinstance(data, list)
