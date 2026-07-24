from api_client.todos_client import (
    get_todos,
    get_invalid_todos_endpoint,
    get_todo_by_id,
)
import pytest


@pytest.mark.smoke
def test_get_todos_status_code():
    response = get_todos()
    assert response.status_code == 200

@pytest.mark.smoke
def test_get_todos_response_shape():
    response = get_todos()
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    

    first = data[0]
    assert "id" in first
    assert "userId" in first
    assert "title" in first
    assert "completed" in first

@pytest.mark.smoke
def test_completed_todos_exist():
    response = get_todos()
    todos = response.json()
    completed_count = len([todo for todo in todos if todo["completed"] is True])
    assert completed_count > 0
    assert completed_count <= len(todos)

@pytest.mark.negative
def test_invalid_endpoint_returns_404():
    response = get_invalid_todos_endpoint()
    assert response.status_code == 404



@pytest.mark.negative
@pytest.mark.parametrize("todo_id", [-1, 0, 999999])
def test_invalid_todo_id_returns_404_and_empty_object(todo_id):
    response = get_todo_by_id(todo_id)
    assert response.status_code == 404
    assert response.json() == {}

@pytest.mark.smoke
@pytest.mark.parametrize("todo_id", [1])
def test_valid_todo_id_returns_200_and_todo_object(todo_id):
    response = get_todo_by_id(todo_id)
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert data["id"] == todo_id
    assert "userId" in data
    assert "title" in data
    assert "completed" in data