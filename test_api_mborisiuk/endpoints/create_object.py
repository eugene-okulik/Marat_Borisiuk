import requests
import allure
from test_api_mborisiuk.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step("Create object")
    def create_new_obj(self, body):
        self.response = requests.post(self.url, json=body)
        self.json = self.response.json()
        return self.json
