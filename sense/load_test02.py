"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description:
"""
import os
from json import JSONDecodeError

from locust import TaskSet, task, between, HttpUser, run_single_user
import queue
import logging
from locust.exception import RescheduleTask

class LoadUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://10.68.36.153:5000"


    '''
    1. pre: 自己创建多个用户， 这里我用了rssss(0, 100)， 密码123456
    2. 实例化序列
    3. 把用户放入序列中
    4. TaskSet中取用户，实现登录压测
    '''
    def on_start(self):
        logging.info("start working----------------------")
        self.queue_username = queue.Queue()
        for i in range(0, 101):
            username = "rssss" + str(i)
            self.queue_username.put_nowait(username)

    def on_stop(self):
        logging.info("stop working----------------------")

    @task
    def login(self):
        self.login_user = {"account": self.queue_username.get(), "password": "123456"}
        with self.client.post('/v1/token', json=self.login_user) as response:
            if response.status_code == 201:
                self.token = response.json()['token']
            else:
                self.token = None
                RescheduleTask()




if __name__ == '__main__':
    # run_single_user(Load)
    os.system("locust -f load_test02.py --headless -u 100 -r 10 -t 1m")


