from _pytest.nodes import Item
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.smoke
def test_filter_completed_true():
    # TODO 1:
    # 1) Send GET request to /todos?completed=true
    # 2) Assert status code is 200
    # 3) Convert response to json list
    # 4) Assert response is a list
    # 5) Assert list is not empty
    # 6) Assert every item has completed is True
    response = requests.get(f"{BASE_URL}/todos?completed=true")   # request to the API
    data = response.json()   # convert the response to a json list

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0  # assert the list is not empty
    assert all(item["completed"] is True for item in data)


@pytest.mark.smoke
def test_filter_by_user_id():
    # TODO 2:
    # 1) Send GET request to /todos?userId=1
    # 2) Assert status code is 200
    # 3) Convert response to json list
    # 4) Assert list is not empty
    # 5) Assert every item has userId == 1
    response = requests.get(f"{BASE_URL}/todos?userId=1")
    data = response.json()

    assert response.status_code ==200
    assert isinstance(data,list)
    assert len(data)>0
    assert all(item["userId"]==1 for item in data)


@pytest.mark.smoke
def test_pagination_limit_5():
    # TODO 3:
    # 1) Send GET request to /todos?_limit=5
    # 2) Assert status code is 200
    # 3) Convert response to json list
    # 4) Assert len(data) == 5
    response = requests.get(f"{BASE_URL}/todos?_limit=5")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 5


@pytest.mark.smoke
def test_pagination_start_and_limit():
    # TODO 4:
    # 1) Send GET request to first page: /todos?_start=0&_limit=5
    # 2) Send GET request to second page: /todos?_start=5&_limit=5
    # 3) Assert both status codes are 200
    # 4) Convert both responses to json lists
    # 5) Assert len(page1) == 5 and len(page2) == 5
    # 6) Assert first item id from page1 != first item id from page2
    response_page1 = requests.get(f"{BASE_URL}/todos?_start=0&_limit=5")
    response_page2 = requests.get(f"{BASE_URL}/todos?_start=5&_limit=5")
   # convert the response to a json list
    page1 = response_page1.json() 
    page2 = response_page2.json()

    assert response_page1.status_code == 200
    assert response_page2.status_code == 200
    assert isinstance(page1, list)
    assert isinstance(page2, list)
    assert len(page1) == 5
    assert len(page2) == 5
    assert page1[0]["id"] != page2[0]["id"]


@pytest.mark.negative
def test_negative_limit_behavior():
    # TODO 5:
    # 1) Send GET request to /todos?_limit=-1
    # 2) Assert status code is 200 (documenting API behavior)
    # 3) Convert response to json list
    # 4) Assert response type is list
    # 5) Optional: print or inspect actual behavior to learn API quirks
    response = requests.get(f"{BASE_URL}/todos?_limit=-1")
    data = response.json()

    # JSONPlaceholder is a demo API and accepts this invalid limit.
    assert response.status_code == 200
    assert isinstance(data, list)
