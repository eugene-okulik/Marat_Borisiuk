import pytest
import requests
from data import BASE_URL


@pytest.fixture(scope="session", autouse=True)
def session_text():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def text_around_each_test():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def new_object_id():
    body = {"data": {"color": "white", "size": "big"}, "name": "Create object"}
    response = requests.post(BASE_URL, json=body)
    assert response.status_code == 200, "Object creation failed"
    data = response.json()
    assert "id" in data, "Object creation failed"
    obj_id = data["id"]
    yield obj_id
    requests.delete(f"{BASE_URL}/{obj_id}")
