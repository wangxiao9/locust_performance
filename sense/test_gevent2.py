"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description:
"""
import time

import gevent

from gevent import monkey
from gevent.lock import BoundedSemaphore

lock = BoundedSemaphore(2)

def work(n):
    for i in range(n):
        lock.acquire()
        print(f"{n}working acquire{i}")
        gevent.sleep(0.1)
        lock.release()
        print(f"{n}working release {i}")

gevent.joinall([gevent.spawn(work, 3), gevent.spawn(work, 4)])
