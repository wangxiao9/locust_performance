"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description: 
"""
import json
import os
import random

import requests
from locust import HttpUser, between, task


class Performance(HttpUser):
    wait_time = between(0, 1)

    # @task
    # def register(self):
    #     # print("task1111")
    #     register_code = {"account": "rssss" + str(random.randint(0, 100)), "password": "123456"}
    #     response = self.client.post("/register", json=register_code)
    #     assert response.status_code == 200

    # priority
    @task
    def read(self):
        self.client.get("https://www.baidu.com")
    #
    @task(2)
    def write(self):
        print("task2")


if __name__ == '__main__':
    os.system("locust -f locustfile.py --headless -u 100 -r 10 --host=baidu -t 0.5m")