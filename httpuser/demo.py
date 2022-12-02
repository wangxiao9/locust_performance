"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description:
"""
import os

from locust import HttpUser, between, task, run_single_user
from locust.exception import RescheduleTask

from json import JSONDecodeError


class Demo(HttpUser):
    wait_time = between(1, 5)
    host = "http://10.68.36.150:5000"
    @task
    def login(self):
        login = {"account":"tester", "password":"123456"}
        with self.client.post('/v1/token', json=login) as response:
            print(response.status_code)
            if response.status_code == 201:
                self.token = response.json()['token']
            else:
                RescheduleTask()

    # @task
    # def baidu(self):
    #     with self.client.get("https://www.baidu.com", catch_response=True) as response:
    #         if response.status_code != 200:
    #             raise RescheduleTask()

    @task
    def getUser(self):
        with self.client.post('/v1/users', headers={"token": self.token}, json={"page": 1, "per_page": 100}, catch_response=True) as response:
            try:
                if response.json()["error_code"] != 0:
                    response.failure("Don't get expected value")
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure("Response can't contains this key")



if __name__ == '__main__':
    #os.system("locust -f demo.py --headless -u 1 -r 1 --host=http://10.68.36.150:5000 -t 2s")
    run_single_user(Demo)