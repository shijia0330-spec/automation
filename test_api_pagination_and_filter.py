import pytest

from api_client.todos_client import get_todos
from utils.api_client import assert_ok_list
from utils.api_client import assert_todo_schema




@pytest.mark.smoke
def test_filter_completed_true():
    # TODO 1:
    # 1) Send GET request to /todos?completed=true
    # 2) Assert status code is 200
    # 3) Convert response to json list
    # 4) Assert response is a list
    # 5) Assert list is not empty
    # 6) Assert every item has completed is True
    response = get_todos({"completed": "true"})
    data = assert_ok_list(response)
    for item in data:
        assert_todo_schema(item)


    assert len(data) > 0
    assert all(item["completed"] is True for item in data)

@pytest.mark.smoke
def test_filter_by_user_id():
    

    response = get_todos({"userId": 1})
    data = assert_ok_list(response)
    for item in data:
        assert_todo_schema(item)
    assert len(data) > 0
    assert all(item["userId"] == 1 for item in data)


@pytest.mark.smoke
def test_pagination_limit_5():
   
    response = get_todos({"_limit": 5})
    data = assert_ok_list(response)

    assert len(data) == 5


@pytest.mark.smoke
def test_pagination_start_and_limit():
  
    response_page1 = get_todos({"_start": 0, "_limit": 5})
    response_page2 = get_todos({"_start": 5, "_limit": 5})
   # convert the response to a json list
    page1 = assert_ok_list(response_page1)
    page2 = assert_ok_list(response_page2)

    assert len(page1) == 5
    assert len(page2) == 5
    assert page1[0]["id"] != page2[0]["id"]


@pytest.mark.negative
def test_negative_limit_behavior():

    response = get_todos({"_limit": -1})
    data = assert_ok_list(response)

    # JSONPlaceholder is a demo API and accepts this invalid limit.
    assert isinstance(data, list)

@pytest.mark.smoke
@pytest.mark.parametrize("limit", [1, 5, 20])
def test_pagination_limit_values(limit): # test the pagination limit values
    response = get_todos({"_limit": limit}) # send a GET request to the todos endpoint with the limit parameter
    data = assert_ok_list(response) # assert the response is a list
    assert len(data) == limit # assert the length of the data is equal to the limit