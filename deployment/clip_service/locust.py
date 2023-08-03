from locust import HttpUser, task, between



class StressTest(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def test_text_endpoint(self):
        files = {'file': open('image.png', 'rb')}
        response=self.client.post("/file?text=a dog , a cat playing",files=files)
        # url = "http://13.233.139.90:8000/file?text=a dog playing on a beach"
        # res = self.client.get(
        #     url=url,
        #     headers={},
        #     data={}
        # )
    
