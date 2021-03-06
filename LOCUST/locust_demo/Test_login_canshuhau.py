# 导入locust的类，成员

from locust import HttpUser, TaskSet, task, between
from random import randint


# 任务类

class TestLogin(TaskSet):
    @task
    def doLogin(self):
        # 设置请求参数
        logindata = [{
            "user.email": "caofeng2012@126.com",
            "user.password": "caofeng",
            "uri": ""
        }, {
            "user.email": "test1",
            "user.password": "caofeng",
            "uri": ""
        }, {
            "user.email": "test2",
            "user.password": "caofeng",
            "uri": ""
        }]
        # 1000以内的随机数，对用户数据长度3进行取余。0,1,2
        ranIndex = randint(1, 1000) % len(logindata)
        # 发送post请求并得到响应
        response = self.client.post("/dangdang/user/login", data=logindata[ranIndex])
        if logindata[ranIndex]["user.email"] in response.text:
            print(logindata[ranIndex]["user.email"] + "------True")
        else:
            print(logindata[ranIndex]["user.email"] + "------false")


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

    os.system("locust -f Test_login_canshuhau.py --host=http://localhost:9090")
