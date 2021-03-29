# 导入locust的类，成员

from locust import HttpUser, TaskSet, task, between


# 任务类

class TestLogin(TaskSet):
    @task
    def doLogin(self):
        # 设置请求参数
        body = {
            "user.email": "caofeng2012@126.com",
            "user.password": "caofeng",
            "uri": ""
        }
        # 发送post请求并得到响应
        response = self.client.post("/dangdang/user/login", data=body)
        print("ok")


class WebSite(HttpUser):
    tasks = [TestLogin]
    # min_wait = 1000
    # max_wait = 2000
    wait_time = between(1, 2)


"""
1.实现登录基本功能，输出响应。
2.模拟多用户随机登录。 参数化
3.
"""
if __name__ == "__main__":
    import os

    os.system("locust -f Test_login.py --host=http://localhost:9090")
