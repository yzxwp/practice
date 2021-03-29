# 导入locust的类，成员

from locust import HttpUser, TaskSet, task, between
from random import randint


# 任务类

class TestLogin(TaskSet):
    # 任务开始前自动执行
    def on_start(self):
        # 设置请求参数
        print("-------on_start--------")
        self.logindata = [{
            "id": "14"
        }, {
            "id": "15"
        }, {
            "id": "16"
        }]

    @task
    def doLogin(self):
        # 1000以内的随机数，对用户数据长度3进行取余。0,1,2
        ranIndex = randint(1, 1000) % len(self.logindata)
        print(ranIndex)
        headers = {
            'Cookie': 'JSESSIONID=74F73035748E964BC58E4A044290EF1D'
        }
        # 发送post请求并得到响应
        response = self.client.get("/dangdang/cart/cartBuy?id=%2014", headers=headers,
                                   catch_response=True)
        if "true" in response.text:
            response.failure("is not finde")

            print("成功")
            # print(self.logindata[ranIndex]["user.email"] + "------True")
        else:
            response.success()
            # response.failure(self.logindata[ranIndex]["user.email"] + "is not finde")
            print("失败")
            # print(self.logindata[ranIndex]["user.email"] + "------false")


class WebSite(HttpUser):
    tasks = [TestLogin]
    # min_wait = 1000
    # max_wait = 2000
    wait_time = between(1, 2)


"""
1.实现登录基本功能，输出响应。
2.模拟多用户随机登录。 参数化
3.on_start:在每一次task执行前先执行一次。
4.添加检查点：断言
    在请求方法中设置catch_response参数为True
    调用sucess和failure方法标注成功或者失败
"""
if __name__ == "__main__":
    import os

    os.system("locust -f checkdemo.py --host=http://localhost:9090")
