import requests

TIMEOUT = 10


def create_todo(user_id, title, completed): # user_id is the id of the user who is creating the todo, title is the title of the todo, completed is a boolean value that indicates if the todo is completed
    url = "https://jsonplaceholder.typicode.com/todos" # this is the url of the api that we are using to create the todo
    new_todo = { # this is the data that we are sending to the api to create the todo
        "userId": user_id,
        "title": title,
        "completed": completed,
    }

    try:
        response = requests.post(url, json=new_todo, timeout=TIMEOUT) # this is the response from the api that we are using to create the todo
        response.raise_for_status() # this is the response from the api that we are using to create the todo
        return response
    except requests.exceptions.RequestException as err:
        print(f"Create TODO request failed: {err}")
        return None


response = create_todo(1, "Learn API automation", False) # this is the response from the api that we are using to create the todo
if response is not None:
    print(response.status_code)
    print(response.json())

def put_todo(todo_id,title,completed,user_id):
    url =  f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    updated_todo = {
        "title": title,
        "completed": completed,
        "userId": user_id,
    }
    try:
        response = requests.put(url, json=updated_todo, timeout=TIMEOUT)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as err:
        print(f"Update TODO request failed: {err}")
        return None


response = put_todo(1, "Learn API automation - updated", True, 2)
if response is not None:
    print(response.status_code)
    print(response.json())

def delete_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    try:
        response = requests.delete(url, timeout=TIMEOUT)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as err:
        print(f"delete TODO request failed: {err}")
        return None 

response = delete_todo(1)
if response is not None:
    print(response.status_code)
    print(response.json())  