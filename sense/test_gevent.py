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


monkey.patch_all() # 程序中用到耗时，切换到gevent中自己实现的模块

def work(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.1)

g1 = gevent.spawn(work, 5)
g2 = gevent.spawn(work, 3)


g1.join()
g2.join()
