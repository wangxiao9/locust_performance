"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description: 
"""
import os

from locust import HttpUser, between, task, constant, constant_throughput
import datetime

class UserClass(HttpUser):
    # wait_time = between(5, 10)
    wait_time = constant_throughput(0.1)
    # wait_time = constant(5)
    # @task
    # def task1(self):
    #     print("task1", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

    # @task
    # def task2(self):
    #     print("task2", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

    @task
    def access_baidu(self):
        res = self.client.get("https://www.baidu.com")
        assert res.status_code == 200

if __name__ == '__main__':
    os.system("locust -f userClass.py --headless -u 5000 -r 100 --host=baidu -t 1m")