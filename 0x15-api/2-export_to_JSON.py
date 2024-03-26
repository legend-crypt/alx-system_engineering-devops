#!/usr/bin/python3
"""import to handle http and json formating"""
import json
import requests
from sys import argv


def to_json():
    """store api response in json file"""
    user_id = argv[1]
    user_res = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(
            user_id
        ))
    username = user_res.json()[0].get("username")
    todo_res = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id
        ))
    key = user_id
    data_obj = {}
    data = []
    for task in todo_res.json():
        data.append({
           "task": task.get("title"),
           "completed": task.get("completed"),
           "username": username})
    data_obj = {key: data}
    print(data_obj)

    filename = f"{user_id}.json"
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(data_obj, json_file)


if __name__ == "__main__":
    to_json()
