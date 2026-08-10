import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def get_posts(params):
    return requests.get(f"{BASE_URL}/posts", params=params, timeout=TIMEOUT)


def assert_ok_list(response):
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    return data


def assert_ok_dict(response):
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    return data


def assert_todo_keys(item):
    required_keys = {"id", "userId", "title", "completed"}
    assert isinstance(item, dict)
    assert required_keys.issubset(item.keys())


def assert_todo_schema(item):
    """Validate todo fields and value types."""
    assert_todo_keys(item)
    assert isinstance(item["id"], int)
    assert isinstance(item["userId"], int)
    assert isinstance(item["title"], str)
    assert isinstance(item["completed"], bool)

def assert_post_schema(item):
    assert isinstance(item["id"], int)
    assert isinstance(item["userId"], int)
    assert isinstance(item["title"], str)
    assert isinstance(item["body"], str)