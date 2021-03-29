# 导入locust的类，成员

from locust import HttpUser, TaskSet, task, between


# 任务类

class TestIndex(TaskSet):
    @task
    def getIndex(self):
        self.client.get("/get_message")
        print("Here")


class WebSite(HttpUser):
    tasks = [TestIndex]
    # min_wait = 1000
    # max_wait = 2000
    wait_time = between(1, 2)


"""
第一步：编写脚本
第二部：打开cmd，进入到源码文件的目录
第三部：执行locust -f TestIndex.py --host=http://localhost:8080
第四部：打开浏览器，访问：http://localhost:8089,配置，运行
"""
