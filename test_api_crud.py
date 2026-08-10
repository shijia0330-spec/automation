import pytest
from api_client.todos_client import create_todo, delete_todo, get_todo_by_id, update_todo, patch_todo   

@pytest.fixture
def todo_data():
    return {
        "userId": 1,
        "title": "Learn API automation",
        "completed": False,

    }
@pytest.mark.smoke
def test_update_todo(todo_data):
    response = update_todo(1, todo_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Learn API automation"

@pytest.mark.smoke
def test_patch_todo():
    todo = {
    
        "completed": True,
    }
    response = patch_todo(1, todo) # patch the todo with the id 1 and the todo object
    assert response.status_code == 200
    assert response.json()["completed"] == True

@pytest.mark.smoke
def test_create_todo(todo_data):
    response = create_todo(todo_data)

    assert response.status_code == 201
    assert response.json()["title"] == "Learn API automation"

@pytest.mark.smoke
def test_read_todo():
    response = get_todo_by_id(1)

    assert response.status_code == 200 # check if the response status code is 200
    assert response.json()["id"] == 1 # check if the response json id is 1
    assert response.json()["title"] == "delectus aut autem" # check if the response json title is "Learn API automation"
    assert response.json()["completed"] == False # check if the response json completed is False


@pytest.mark.negative
def test_read_missing_todo():
    response = get_todo_by_id(999)
    assert response.status_code == 404
    assert response.json() == {}

@pytest.mark.negative
def test_patch_todo_invalid_id():
    payload = {"completed": True} #for patch todo, need to send a payload and which field needs to be updated
    response = patch_todo(999999, payload)
    assert response.status_code == 200
    assert response.json()["completed"] is True

@pytest.mark.negative
def test_patch_todo_invalid_payload_type():
    bad_payload = {"completed": "yes"}  # should be boolean 
    response = patch_todo(1, bad_payload) # patch the todo with the id 1 and the bad payload

    # JSONPlaceholder is permissive (fake API), so often still 200
    assert response.status_code == 200 # check if the response status code is 200
    assert response.json()["completed"] == "yes" # check if the response json completed is "yes"
    print(response.status_code, response.json()) # print the response status code and the response json


@pytest.mark.smoke
def test_delete_todo():
    response = delete_todo(1)
    assert response.status_code == 200
    assert response.json() == {}

# to check if the todo exists, you can call the get_todo_by_id function
# def test_todo_1_exists():
#     response = get_todo_by_id(1)
#     assert response.status_code == 200
#     assert response.json()["id"] == 1
#     print(response.status_code)
#     print(response.json())z
