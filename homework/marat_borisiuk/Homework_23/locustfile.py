from locust import task, HttpUser, between


class ObjectUser(HttpUser):
    host = "http://objapi.course.qa-practice.com"
    wait_time = between(1, 2)
    object_id = None

    def on_start(self):
        response = self.client.post(
            '/object',
            json={
                'name': 'Locust object',
                'data': {
                    'color': 'white',
                    'size': 'big'
                }
            }
        )
        self.object_id = response.json()['id']

    @task(1)
    def get_all_objects(self):
        self.client.get('/object')

    @task(3)
    def get_one_object(self):
        self.client.get(f'/object/{self.object_id}')
