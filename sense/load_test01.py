"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description: 
"""
import os
from json import JSONDecodeError

from locust import TaskSet, task, between, HttpUser, run_single_user, User
import logging
from locust.exception import RescheduleTask

class LoadUser(TaskSet):

    def on_start(self):
        logging.info("start working----------------------")
        self.login_user = {"account":"tester", "password":"123456"}
        with self.client.post('/v1/token', json=self.login_user) as response:
            if response.status_code == 201:
                self.token = response.json()['token']
            else:
                self.token = None
                RescheduleTask()


    def on_stop(self):
        self.interrupt()


    @task
    def getUser(self):
        if self.token is None:
            RescheduleTask()
        with self.client.post('/v1/users', headers={"token": self.token}, json={"page": 1, "per_page": 100}, catch_response=True) as response:
            try:
                if response.json()["error_code"] != 0:
                    response.failure("Don't get expected value")
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure("Response can't contains this key")


class Load(HttpUser):
    tasks = {LoadUser}
    wait_time = between(1, 5)
    host = "http://10.68.36.153:5000"
    #
    # @task
    # def my_task(self):
    #     print("tessssssssssss")

#
if __name__ == '__main__':
    # run_single_user(Load)
    os.system("locust -f load_test01.py --headless -u 100 -r 10 -t 1m")


