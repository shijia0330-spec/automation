from api_client.todos_client import create_todo, delete_todo

from api_client.todos_client import get_todo_by_id

def test_create_todo():
    todo = {
        "userId": 1,
        "title": "Learn API automation",
        "completed": False,
    }

    response = create_todo(todo)

    assert response.status_code == 201
    assert response.json()["title"] == "Learn API automation"


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
#     print(response.json())
