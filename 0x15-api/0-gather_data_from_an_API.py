#!/usr/bin/python3
"""import requests to handle http request"""
import requests
from sys import argv


def check_employee_task():
    """display on the standard output the employee TODO list progress"""
    employee_res = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(
                                                        argv[1]
        )
    )
    employee_name = employee_res.json()[0].get("name")
    todo_res = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                                                    argv[1]
                                                    )
    )
    total_tasks = len(todo_res.json())
    task_done = 0
    for task in todo_res.json():
        if task.get("completed"):
            task_done += 1
    print("Employee {} is done with task({}/{}):".format(
        employee_name,
        task_done,
        total_tasks))
    for task in todo_res.json():
        if task.get("completed"):
            print(f"\t {task.get('title')}")


if __name__ == "__main__":
    check_employee_task()
