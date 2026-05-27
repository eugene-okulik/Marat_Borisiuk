import requests


def create_object():
    body = {"data": {"color": "white", "size": "big"}, "name": "Create object"}
    create_response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body
    ).json()
    assert "id" in create_response, "Object creation failed"
    obj_id = create_response["id"]
    return obj_id


def clear_object(obj_id):
    clear_response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{obj_id}"
    )
    assert clear_response.status_code in [200, 204], "Object deletion failed"


def post_object():
    obj_id = create_object()
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{obj_id}")
    assert response.status_code == 200, "Object creation failed"
    clear_object(obj_id)


def put_object():
    obj_id = create_object()
    update_body = {
        "data": {"color": "black", "size": "bigger"},
        "name": "First object updated",
    }
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{obj_id}", json=update_body
    ).json()
    assert response["data"]["size"] == "bigger", "Object update failed"
    clear_object(obj_id)


def patch_object():
    obj_id = create_object()
    patch_body = {"name": "Patch First object"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{obj_id}", json=patch_body
    ).json()
    assert response["name"] == "Patch First object", "Object patch failed"
    clear_object(obj_id)


def delete_object():
    obj_id = create_object()
    clear_object(obj_id)


post_object()
put_object()
patch_object()
delete_object()
