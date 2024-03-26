#!/usr/bin/python3
"""imports modules to handle http request
and coversion of json to csv
"""
import csv
import requests
from sys import argv


def json_to_csv():
    """stores json data to csv file"""
    userId = argv[1]
    user_res = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(
            userId))
    username = user_res.json()[0].get("username")
    todo_res = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            userId))
    filename = f"{userId}.csv"
    with open(filename, mode='w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_res.json():
            writer.writerow([
                f"{userId}", str(username),
                str(task.get("completed")), str(task.get("title"))
            ])


if __name__ == "__main__":
    json_to_csv()
