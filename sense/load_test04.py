"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description:
"""


import os
from json import JSONDecodeError

from locust import TaskSet, task, events, HttpUser
from gevent._semaphore import BoundedSemaphore
from locust.exception import RescheduleTask

all_locusts_spawned = BoundedSemaphore()

all_locusts_spawned.acquire()


def on_hatch_complete(**kwargs):
    # 创建钩子方法

    all_locusts_spawned.release()


# 挂在到locust钩子函数（所有的Locust示例产生完成时触发）
events.spawning_complete.add_listener(on_hatch_complete)  # 1.0之后的写法


class TestTask(TaskSet):
    def on_start(self):
        """所有任务启动前执行"""
        self.login()
        all_locusts_spawned.wait()
        print('所有任务启动前执行')

    def login(self):
        self.login_user = {"account": "tester", "password": "123456"}
        with self.client.post('/v1/token', json=self.login_user) as response:
            if response.status_code == 201:
                self.token = response.json()['token']
            else:
                self.token = None
                RescheduleTask()

    @task
    def getUser(self):
        all_locusts_spawned.wait()
        if self.token is None:
            RescheduleTask()
        with self.client.post('/v1/users', headers={"token": self.token}, json={"page": 1, "per_page": 100},
                              catch_response=True) as response:
            try:
                if response.json()["error_code"] != 0:
                    response.failure("Don't get expected value")
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure("Response can't contains this key")


class MyUser(HttpUser):
    tasks = [TestTask]
    host = "http://10.68.36.153:5000"
    min_wait = 1000
    max_wait = 3000


if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    os.system(f'locust -f {file_path}')