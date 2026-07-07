import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_todos():
    return requests.get(f"{BASE_URL}/todos")


def get_invalid_todos_endpoint():
    return requests.get(f"{BASE_URL}/invalid-todos-endpoint")
