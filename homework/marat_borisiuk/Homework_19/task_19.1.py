import requests


def create_object():
    body = {"data": {"color": "white", "size": "big"}, "name": "First object"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body
    ).json()
    assert "id" in response
    obj_id = response["id"]
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{obj_id}")
    assert response.status_code == 200
    delete_response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{obj_id}"
    )


def put_object():
    body = {"data": {"color": "white", "size": "big"}, "name": "First object"}
    create_response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body
    ).json()
    obj_id = create_response["id"]

    update_body = {
        "data": {"color": "black", "size": "bigger"},
        "name": "First object updated",
    }
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{obj_id}", json=update_body
    ).json()
    assert response["data"]["size"] == "bigger"
    delete_response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{obj_id}"
    )


def patch_object():
    body = {"data": {"color": "white", "size": "big"}, "name": "First object"}
    create_response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body
    ).json()
    obj_id = create_response["id"]

    patch_body = {
        "data": {"color": "black", "size": "bigger"},
        "name": "Patch First object",
    }
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{obj_id}", json=patch_body
    ).json()
    assert response["name"] == "Patch First object"
    delete_response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{obj_id}"
    )


def delete_object():
    body = {"data": {"color": "white", "size": "big"}, "name": "First object"}
    create_response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body
    ).json()
    obj_id = create_response["id"]

    delete_response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{obj_id}"
    )
    assert delete_response.status_code in [200, 204]


create_object()
put_object()
patch_object()
delete_object()
