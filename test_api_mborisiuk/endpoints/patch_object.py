import requests
import allure
from test_api_mborisiuk.endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step("Patch object")
    def patch_object(self, object_id, patch_body):
        self.response = requests.patch(f"{self.url}/{object_id}", json=patch_body)
        self.json = self.response.json()
        return self.response
