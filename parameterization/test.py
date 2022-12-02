"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description: 
"""


import csv
import queue

queue_user = queue.Queue()
csv_reader = csv.reader(open('account.csv'))
for csvs in csv_reader:
    user = {
        "account": csvs[0],
        "password": csvs[1]
    }
    queue_user.put_nowait(user)
print(queue_user.get())