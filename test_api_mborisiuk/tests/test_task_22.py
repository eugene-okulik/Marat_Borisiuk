import allure
import pytest

NEGATIVE_DATA = [
    {"size": " ", "name": None},
    {"color": None, "size": None, "name": 1},
]


@allure.feature("Create object")
@pytest.mark.parametrize("name", ["first name", "second name", "third name"])
def test_post_object(create_object_endpoint, name):
    body = {"data": {"color": "white", "size": "big"}, "name": name}
    create_object_endpoint.create_new_obj(body)
    create_object_endpoint.check_status_code_correct(200)
    create_object_endpoint.check_response_title_is_correct(name)


@allure.feature("Create object")
@pytest.mark.parametrize("data", NEGATIVE_DATA)
def test_post_with_negative_data(create_object_endpoint, data):
    create_object_endpoint.create_new_obj(data)
    create_object_endpoint.check_status_code_correct(200)


@allure.feature("Get object")
@pytest.mark.critical
def test_get_object(get_object_endpoint, created_object_id):
    get_object_endpoint.get_object_by_id(created_object_id)
    get_object_endpoint.check_status_code_correct(200)
    get_object_endpoint.check_object_id_is_correct(created_object_id)


@allure.feature("Update object")
@allure.story("story 1")
@allure.title("Обновление объекта PUT")
@pytest.mark.medium
def test_put_object(update_object_endpoint, created_object_id):
    update_body = {"name": "Updated name", "data": {"size": "bigger"}}
    update_object_endpoint.make_changes_in_object(created_object_id, update_body)
    update_object_endpoint.check_status_code_correct(200)
    update_object_endpoint.check_response_title_is_correct("Updated name")


@allure.feature("Update object")
@allure.story("story 2")
@pytest.mark.critical
def test_patch_object(patch_object_endpoint, created_object_id):
    patch_body = {"name": "Patch create object"}
    patch_object_endpoint.patch_object(created_object_id, patch_body)
    patch_object_endpoint.check_status_code_correct(200)
    patch_object_endpoint.check_response_title_is_correct("Patch create object")


@allure.feature("Delete object")
def test_delete_object(delete_object_endpoint, created_object_id):
    delete_object_endpoint.delete_object_by_id(created_object_id)
    delete_object_endpoint.check_status_code_correct(200)
    delete_object_endpoint.check_object_is_deleted(created_object_id)