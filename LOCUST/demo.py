# 导入locust的类，成员

from locust import HttpUser, TaskSet, task, between

# 任务类

class TestIndex(TaskSet):
    @task
    def getIndex(self):
        with self.client.get("/get_message", catch_response=True) as resp:
            response = resp.json()
            # print(len(response["gonghang"]))
            if len(response["gonghang"]) == 16:
                resp.success()
            else:
                resp.failure("idcard is not found or len isn't 16")


class WebSite(HttpUser):
    tasks = [TestIndex]
    # min_wait = 1000
    # max_wait = 2000
    wait_time = between(1, 2)
