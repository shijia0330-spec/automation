import pytest
from api_client.todos_client import create_todo, delete_todo, get_todo_by_id, patch_todo, update_todo


@pytest.fixture
def todo_id():
    return 1


@pytest.fixture
def todo_data():
    return {"userId": 1, "title": "Learn API automation", "completed": False}


@pytest.fixture
def patch_payload():
    return {"completed": True}


@pytest.mark.smoke
def test_update_todo(todo_id, todo_data):
    response = update_todo(todo_id, todo_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Learn API automation"


@pytest.mark.smoke
def test_patch_todo(todo_id, patch_payload):
    response = patch_todo(todo_id, patch_payload)
    assert response.status_code == 200
    assert response.json()["completed"] is True


@pytest.mark.smoke
def test_create_todo(todo_data):
    response = create_todo(todo_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Learn API automation"


@pytest.mark.smoke
@pytest.mark.parametrize("todo_id", [1, 2, 3])
def test_read_todo(todo_id):
    response = get_todo_by_id(todo_id)
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == todo_id
    assert "title" in data
    assert "completed" in data


@pytest.mark.negative
@pytest.mark.parametrize("todo_id", [999, 999999])
def test_read_missing_todo(todo_id):
    response = get_todo_by_id(todo_id)
    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.negative
def test_patch_todo_invalid_id(patch_payload):
    response = patch_todo(999999, patch_payload)
    assert response.status_code == 200
    assert response.json()["completed"] is True


@pytest.mark.negative
@pytest.mark.parametrize("invalid_value", ["yes", 1, None])
def test_patch_todo_invalid_payload_type(todo_id, invalid_value):
    bad_payload = {"completed": invalid_value}
    response = patch_todo(todo_id, bad_payload)
    # JSONPlaceholder is permissive (fake API), so this often returns 200.
    assert response.status_code == 200
    assert response.json()["completed"] == invalid_value


@pytest.mark.smoke
def test_delete_todo(todo_id):
    response = delete_todo(todo_id)
    assert response.status_code == 200
    assert response.json() == {}
