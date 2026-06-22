import requests
import allure
from test_api_mborisiuk.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Delete object")
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")
        return self.response

    @allure.step("Check object is deleted")
    def check_object_is_deleted(self, get_object_endpoint, object_id):
        get_object_endpoint.get_object_by_id(object_id)
        get_object_endpoint.check_status_code_correct(404)
