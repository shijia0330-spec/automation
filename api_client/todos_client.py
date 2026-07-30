import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def get_todos(params=None):
    return requests.get(f"{BASE_URL}/todos", params=params, timeout=TIMEOUT)


def get_invalid_todos_endpoint():
    return requests.get(f"{BASE_URL}/invalid-todos-endpoint", timeout=TIMEOUT)


def get_todo_by_id(todo_id):
    return requests.get(f"{BASE_URL}/todos/{todo_id}", timeout=TIMEOUT)
