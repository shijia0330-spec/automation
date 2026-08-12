import os

import pytest
import requests


AUTH_BASE_URL = os.getenv("AUTH_BASE_URL", "https://dummyjson.com")
AUTH_USERNAME = os.getenv("AUTH_USERNAME", "emilys")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD", "emilyspass")
TIMEOUT = 10


@pytest.fixture(scope="module")
def access_token():
    response = requests.post(
        f"{AUTH_BASE_URL}/auth/login",
        json={
            "username": AUTH_USERNAME,
            "password": AUTH_PASSWORD,
        },
        timeout=TIMEOUT,
    )
    assert response.status_code == 200, (
        f"Fixture login failed with status {response.status_code}. "
        f"Body: {response.text}"
    )

    token = response.json()["accessToken"]
    assert token, "Expected fixture login to return an access token"
    print(f"Fixture token type: {type(token).__name__}")
    return token


@pytest.mark.smoke
def test_login_returns_access_token():
    response = requests.post(
        f"{AUTH_BASE_URL}/auth/login",
        json={
            "username": AUTH_USERNAME,
            "password": AUTH_PASSWORD,
        },
        timeout=TIMEOUT,
    )

    assert response.status_code == 200, (
        f"Expected login status 200, got {response.status_code}. "
        f"Body: {response.text}"
    )

    data = response.json()
    assert isinstance(data.get("accessToken"), str)
    assert data["accessToken"], "Expected a non-empty access token"


@pytest.mark.smoke
def test_access_token_returns_current_user(access_token):
    user_response = requests.get(
        f"{AUTH_BASE_URL}/auth/me",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=TIMEOUT,
    )
    print(f"User status: {user_response.status_code}")

    assert user_response.status_code == 200, (
        f"Expected authenticated status 200, got {user_response.status_code}. "
        f"Body: {user_response.text}"
    )

    user_data = user_response.json()
    username = user_data["username"]
    print(f"Username: {username}")

    assert username == AUTH_USERNAME

@pytest.mark.negative
def test_without_token_returns_error():
    response = requests.get(
    f"{AUTH_BASE_URL}/auth/me",
    timeout=TIMEOUT,
    )
    assert response.status_code == 401, (
        f"Expected me status 401, got {response.status_code}. "
        f"Body: {response.text}"
    )
    print(f"Me status: {response.status_code}")
    print(f"Me body: {response.text}")

@pytest.mark.negative
def test_invalid_token_returns_with_header_error():
    response = requests.get(
        f"{AUTH_BASE_URL}/auth/me",
        headers={"Authorization": "Bearer incorrect_token"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 401

    data = response.json()
    assert isinstance(data.get("message"), str) # Check if the message is a string
    assert data["message"] # Check if the message is not empty
    print(data["message"])
   
def test_empty_error_message_is_rejected():
    response = requests.get(
    f"{AUTH_BASE_URL}/auth/me",
    timeout=TIMEOUT,
    )
    data = response.json()
    message = data.get("message")

    assert isinstance(message, str)
    assert message.strip(), "Expected a non-empty error message"

def test_access_token_returns_user_id(access_token):
    response = requests.get(
        f"{AUTH_BASE_URL}/auth/me",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=TIMEOUT,
    )
    data = response.json()
    assert response.status_code == 200, (
        f"Expected authenticated status 200, got {response.status_code}. "
        f"Body: {response.text}"
    )
    data = response.json()
    assert isinstance(data.get("id"), int) 