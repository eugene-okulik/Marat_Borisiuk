import requests
import allure
from test_api_mborisiuk.endpoints.endpoint import Endpoint

class UpdateObject(Endpoint):

    @allure.step('Update object')
    def make_changes_in_object(self, object_id, update_body):
        self.response = requests.put(f"{self.url}/{object_id}", json=update_body)
        self.json = self.response.json()
        return self.response