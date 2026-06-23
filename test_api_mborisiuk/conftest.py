import pytest
from test_api_mborisiuk.endpoints.create_object import CreateObject
from test_api_mborisiuk.endpoints.update_object import UpdateObject
from test_api_mborisiuk.endpoints.get_object import GetObject
from test_api_mborisiuk.endpoints.patch_object import PatchObject
from test_api_mborisiuk.endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture
def created_object_id(create_object_endpoint, delete_object_endpoint):
    body = {"name": "Test object", "data": {"color": "white", "size": "big"}}
    create_object_endpoint.create_new_obj(body)
    obj_id = create_object_endpoint.json["id"]
    yield obj_id
    delete_object_endpoint.delete_object_by_id(obj_id)
