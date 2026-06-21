import requests
import allure
from test_api_mborisiuk.endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step("Get object")
    def get_object_by_id(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        self.json = self.response.json()
        return self.response

    @allure.step("Check object id is correct")
    def check_object_id_is_correct(self, object_id):
        assert self.json["id"] == object_id, f"Expected id '{object_id}', got '{self.json['id']}'"