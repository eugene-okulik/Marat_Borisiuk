import requests
import pytest

BASE_URL = "http://objapi.course.qa-practice.com/object"


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


@pytest.mark.parametrize("name", ["first name", "second name", "third name"])
def test_post_object(name):
    body = {"data": {"color": "white", "size": "big"}, "name": name}
    response = requests.post(BASE_URL, json=body)
    assert response.status_code == 200, "Object not created"
    data = response.json()
    assert "id" in data, "Object not created"
    requests.delete(f"{BASE_URL}/{data['id']}")


@pytest.mark.critical
def test_get_object(new_object_id):
    response = requests.get(f"{BASE_URL}/{new_object_id}")
    assert response.status_code == 200, "Object not found"
    data = response.json()
    assert data["id"] == new_object_id, "Wrong object"


@pytest.mark.medium
def test_put_object(new_object_id):
    update_body = {
        "data": {"color": "black", "size": "bigger"},
        "name": "Create object updated",
    }
    response = requests.put(f"{BASE_URL}/{new_object_id}", json=update_body)
    assert response.status_code == 200, "Object update failed"
    data = response.json()
    assert data["data"]["size"] == "bigger", "Object update failed"


def test_patch_object(new_object_id):
    patch_body = {"name": "Patch create object"}
    response = requests.patch(f"{BASE_URL}/{new_object_id}", json=patch_body)
    assert response.status_code == 200, "Object patch failed"
    data = response.json()
    assert data["name"] == "Patch create object", "Object patch failed"


def test_delete_object(new_object_id):
    response = requests.delete(f"{BASE_URL}/{new_object_id}")
    assert response.status_code in [200, 204], "Object deletion failed"
    response_after = requests.get(f"{BASE_URL}/{new_object_id}")
    assert response_after.status_code == 404, "Object was not deleted"
