import requests
import allure
from test_api_mborisiuk.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Delete object")
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")
        return self.response

    @allure.step("Check object is deleted")
    def check_object_is_deleted(self, object_id):
        response = requests.get(f"{self.url}/{object_id}")
        assert response.status_code == 404, "Object was not deleted"