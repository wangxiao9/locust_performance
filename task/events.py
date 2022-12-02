"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description:
"""
import os

from locust import User, task, constant, events


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")

class MyUser(User):
    wait_time = constant(1)

    @task
    def task1(self):
        print("task1")



if __name__ == '__main__':
    os.system("locust -f events.py --headless -u 10 -r 2 --host=baidu -t 10s")