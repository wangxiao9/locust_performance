### 什么是分布式压测
- 普通压测： 单台机器对目标机器压测
- 分布式压测：利用多台机器向目标机器压测，可以模拟几万并发用户


### step
1. --master模式下启动locust 实例， --master-host 主机IP --master-port 自定义master端口号
2. slave 机器上启动对应的脚本， locust -f xxx.py --worker --master-host= xx.xx.xx.xx --host=xxxx
