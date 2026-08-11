import os

import requests

BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com") # default to jsonplaceholder if not set
TIMEOUT = 10


def get_posts(params):
    return requests.get(f"{BASE_URL}/posts", params=params, timeout=TIMEOUT)


def assert_ok_list(response):
    assert response.status_code == 200, (
        f"Expected status 200, got {response.status_code}. Body: {response.text}"
    )
    data = response.json()
    assert isinstance(data, list), f"Expected list response, got {type(data).__name__}"
    return data


def assert_ok_dict(response):
    assert response.status_code == 200, (
        f"Expected status 200, got {response.status_code}. Body: {response.text}"
    )
    data = response.json()
    assert isinstance(data, dict), f"Expected dict response, got {type(data).__name__}"
    return data


def assert_todo_keys(item):
    required_keys = {"id", "userId", "title", "completed"}
    assert isinstance(item, dict), f"Expected todo item dict, got {type(item).__name__}"
    missing = required_keys - set(item.keys())
    assert not missing, f"Missing todo keys: {sorted(missing)}"


def assert_todo_schema(item):
    """Validate todo fields and value types."""
    assert_todo_keys(item)
    assert isinstance(item["id"], int), f"Expected id:int, got {type(item['id']).__name__}"
    assert isinstance(item["userId"], int), (
        f"Expected userId:int, got {type(item['userId']).__name__}"
    )
    assert isinstance(item["title"], str), (
        f"Expected title:str, got {type(item['title']).__name__}"
    )
    assert isinstance(item["completed"], bool), (
        f"Expected completed:bool, got {type(item['completed']).__name__}"
    )

def assert_post_schema(item):
    assert isinstance(item, dict), f"Expected post item dict, got {type(item).__name__}"
    required_keys = {"id", "userId", "title", "body"}
    missing = required_keys - set(item.keys()) # check if the required keys are in the item
    assert not missing, f"Missing post keys: {sorted(missing)}" # assert the missing keys
    assert isinstance(item["id"], int), f"Expected id:int, got {type(item['id']).__name__}"
    assert isinstance(item["userId"], int), (
        f"Expected userId:int, got {type(item['userId']).__name__}"
    )
    assert isinstance(item["title"], str), (
        f"Expected title:str, got {type(item['title']).__name__}"
    )
    assert isinstance(item["body"], str), (
        f"Expected body:str, got {type(item['body']).__name__}"
    )

def assert_schema_list(data, schema_assertion):
    """Validate each object in a response list with a schema helper."""
    assert isinstance(data, list), f"Expected data:list, got {type(data).__name__}"
    for idx, item in enumerate(data): # iterate through the list
        try:
            schema_assertion(item)# assert the item with the schema assertion
        except AssertionError as err: # if the assertion fails, raise an assertion error
            raise AssertionError(f"Schema validation failed at index {idx}: {err}") from err