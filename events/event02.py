"""
Created on 09/22/2022 3:38 PM
@author: EstherWang
@site: locust
@email: 1012883981@qq.com
@description:
"""
import os

from locust import HttpUser, task, constant, events, User
from locust.runners import MasterRunner


# @events.test_start.add_listener
# def on_test_start(environment, **kwargs):
#     print("A new test is starting")
#     environment.total = 0
#     print(environment.runner.total)
#
# @events.test_stop.add_listener
# def on_test_stop(environment, **kwargs):
#     print("A new test is ending")


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--my-argument", type=str, env_var="LOCUST_MY_ARGUMENT", default="", help="It's working")
    # Set `include_in_web_ui` to False if you want to hide from the web UI
    parser.add_argument("--my-ui-invisible-argument", include_in_web_ui=False, default="I am invisible")


@events.test_start.add_listener
def _(environment, **kw):
    print(f"Custom argument supplied: {environment.parsed_options.my_argument}")


class MyUser(User):
    wait_time = constant(1)

    @task
    def task1(self):
        print("total")



if __name__ == '__main__':
    os.system("locust -f event02.py --headless -u 10 -r 2 --host=baidu -t 10s")