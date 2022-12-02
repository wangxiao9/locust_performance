"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description:
"""
import os

from locust import SequentialTaskSet, task, between, HttpUser, run_single_user
import queue
import logging
from locust.exception import RescheduleTask

class LoadUser(SequentialTaskSet):
    def on_start(self):
        logging.info("start working----------------------")
        self.queue_username = queue.Queue()
        for i in range(0, 101):
            username = "rssss" + str(i)
            self.queue_username.put_nowait(username)

    def on_stop(self):
        logging.info("stop working----------------------")

    @task
    def test(self):
        # self.schedule_task(self.test, first=True)
        print("execute test task")


    @task
    def login(self):
        # self.schedule_task(self.login, 2)

        print("execute login task")



class Load(HttpUser):
    tasks = { LoadUser }
    wait_time = between(1, 5)
    host = "http://10.68.36.153:5000"



if __name__ == '__main__':
    os.system("locust -f sequecner01.py --headless -u 100 -r 10 -t 10s")
    # run_single_user(Load)


