from locust import HttpUser, TaskSet, task


class Testlocust(TaskSet):
    def on_start(self):
        print("start")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }

    @task(1)
    def baidu_demo(self):
        r = self.client.get("/", headers=self.headers, verify=False)
        print(r.status_code)
        assert r.status_code == 200


class WebsiteUser(HttpUser):
    # task_set = Testlocust
    tasks = [Testlocust]
    min_wait = 1500
    max_wait = 5000


if __name__ == "__main__":
    import os

    os.system("locust -f Test_baidu.py --host=https://www.baidu.com")
