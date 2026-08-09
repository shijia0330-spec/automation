from api_client.base_client import ApiClient

client = ApiClient("https://jsonplaceholder.typicode.com")


def get_todos(params=None): # params is a dictionary of query parameters
    return client.get("/todos", params=params)


def get_todo_by_id(todo_id): # todo_id is the id of the todo to get
    return client.get(f"/todos/{todo_id}")


def create_todo(todo: dict): # todo is a dictionary of the todo to create
    return client.post("/todos", json=todo)


def update_todo(todo_id, todo: dict): # todo_id is the id of the todo to update, todo is a dictionary of the todo to update
    return client.put(f"/todos/{todo_id}", json=todo)


def delete_todo(todo_id): # todo_id is the id of the todo to delete
    return client.delete(f"/todos/{todo_id}")