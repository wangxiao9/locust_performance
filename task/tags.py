"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description:
"""
import os

from locust import User, task, constant, tag

class MyUser(User):
    wait_time = constant(1)

    @tag('tag1')
    @task
    def task1(self):
        print("task1")

    @tag('tag1', 'tag2')
    @task
    def task2(self):
        print("task2")


    @tag('tag3')
    @task
    def task3(self):
        print("task3")


if __name__ == '__main__':
    os.system("locust -f tags.py --headless -u 10 -r 2 --host=baidu --tags tag1 -t 10s")