"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description: 
"""
import os

from locust import User, task, between

# class MyUser(User):
#     wait_time = between(5, 15)
#
#     @task(3)
#     def task1(self):
#         pass
#
#     @task(6)
#     def task2(self):
#         pass


def task1(user):
    print("task1")


def task2(user):
    print("task2")


def task3(user):
    print("task3")


class MyTask(User):
#    tasks = [task1, task3]
    tasks = {task3:1, task1: 3}
    wait_time = between(2, 5)


if __name__ == '__main__':
    os.system("locust -f task.py --headless -u 10 -r 2 --host=baidu -t 20s")