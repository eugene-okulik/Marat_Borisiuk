import allure
import requests
import pytest
from data import BASE_URL


@allure.feature('Create object')
@pytest.mark.parametrize("name", ["first name", "second name", "third name"])
def test_post_object(name):
    body = {"data": {"color": "white", "size": "big"}, "name": name}
    response = requests.post(BASE_URL, json=body)
    assert response.status_code == 200, "Object not created"
    data = response.json()
    assert "id" in data, "Object not created"
    requests.delete(f"{BASE_URL}/{data['id']}")


@allure.feature('Get object')
@pytest.mark.critical
def test_get_object(new_object_id):
    with allure.step(f"Get object with id {new_object_id}"):
        response = requests.get(f"{BASE_URL}/{new_object_id}")
    with allure.step("Check status cod is 200"):
        assert response.status_code != 200, "Object not found"
    data = response.json()
    with allure.step(f"Check id is {new_object_id}"):
        assert data["id"] == new_object_id, "Wrong object"


@allure.feature('Update object')
@allure.story('story 1')
@allure.title('Обновление объекта')
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


@allure.feature('Update object')
@allure.story('story 2')
@pytest.mark.critical
def test_patch_object(new_object_id):
    patch_body = {"name": "Patch create object"}
    response = requests.patch(f"{BASE_URL}/{new_object_id}", json=patch_body)
    assert response.status_code == 200, "Object patch failed"
    data = response.json()
    assert data["name"] == "Patch create object", "Object patch failed"


@allure.feature('Delete object')
def test_delete_object(new_object_id):
    response = requests.delete(f"{BASE_URL}/{new_object_id}")
    assert response.status_code in [200, 204], "Object deletion failed"
    response_after = requests.get(f"{BASE_URL}/{new_object_id}")
    assert response_after.status_code == 404, "Object was not deleted"
