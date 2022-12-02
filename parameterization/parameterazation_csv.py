"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description: 
"""
import os

from locust import HttpUser, task, constant, SequentialTaskSet
import csv
import queue, logging

from locust.exception import RescheduleTask


class LoadCsv(HttpUser):

    def on_start(self):
        self.queue_user = queue.Queue()
        csv_reader = csv.reader(open('account.csv'))
        for csvs in csv_reader:
            user = {
                "account": csvs[0],
                "password": csvs[1]
            }
            self.queue_user.put_nowait(user)


    @task
    def login(self):
        user = self.queue_user.get()
        logging.info(f"当前登录的用户是：{user}")

        self.login_user = {"account": user['account'], "password": user["password"]}
        with self.client.post('/v1/token', json=self.login_user) as response:
            if response.status_code == 201:
                self.token = response.json()['token']
            else:
                self.token = None
                RescheduleTask()


if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    os.system(f'locust -f {file_path}')