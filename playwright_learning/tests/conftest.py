import json
import os
from pathlib import Path

import pytest


CREDENTIALS_FILE = (
    Path(__file__).resolve().parents[1] / "test_users.local.json"
)


def load_login_users():
    if CREDENTIALS_FILE.exists():
        with CREDENTIALS_FILE.open(encoding="utf-8") as credentials_file:
            users = json.load(credentials_file)
    else:
        environment_values = {
            "CLIENT_USER_1_USERNAME": os.getenv("CLIENT_USER_1_USERNAME"),
            "CLIENT_USER_1_PASSWORD": os.getenv("CLIENT_USER_1_PASSWORD"),
            "CLIENT_USER_2_USERNAME": os.getenv("CLIENT_USER_2_USERNAME"),
            "CLIENT_USER_2_PASSWORD": os.getenv("CLIENT_USER_2_PASSWORD"),
        }
        missing_variables = [
            name for name, value in environment_values.items() if not value
        ]
        assert not missing_variables, (
            "Missing login credential environment variables: "
            f"{missing_variables}"
        )
        users = [
            {
                "name": "first-user",
                "username": environment_values["CLIENT_USER_1_USERNAME"],
                "password": environment_values["CLIENT_USER_1_PASSWORD"],
            },
            {
                "name": "second-user",
                "username": environment_values["CLIENT_USER_2_USERNAME"],
                "password": environment_values["CLIENT_USER_2_PASSWORD"],
            },
        ]

    assert isinstance(users, list) and users, (
        "Expected at least one configured login user"
    )
    return users


@pytest.fixture(
    params=load_login_users(),
    ids=lambda user: user["name"],
)
def login_user(request):
    return request.param
