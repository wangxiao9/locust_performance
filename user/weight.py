"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description: 
"""
import os

from locust import User, task


class WebUser(User):
    weight = 1

    @task
    def web(self):
        print("webuser")


class MobileUser(User):
    weight = 3

    @task
    def mobile(self):
        print("mobile")


if __name__ == '__main__':
    os.system("locust -f weight.py")