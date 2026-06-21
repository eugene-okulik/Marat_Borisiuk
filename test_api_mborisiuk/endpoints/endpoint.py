import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None

    @allure.step("Check status code is correct")
    def check_status_code_correct(self, status_code):
        assert self.response.status_code == status_code, "Wrong status code"

    @allure.step("Check response title is correct")
    def check_response_title_is_correct(self, name):
        assert self.json["name"] == name, f"Expected '{name}', got '{self.json['name']}'"
