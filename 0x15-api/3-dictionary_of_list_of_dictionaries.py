#!/usr/bin/python3
"""script to export data in the JSON format"""

import json
import requests


if __name__ == "__main__":
    """script to export data in the JSON format"""
    url = "https://jsonplaceholder.typicode.com/users"
    url2 = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    response2 = requests.get(url2)
    json_obj = response.json()
    json_obj2 = response2.json()
    json_dict = {}

    for user in json_obj:
        json_dict[user.get('id')] = []
        for task in json_obj2:
            if task.get('userId') == user.get('id'):
                json_dict[user.get('id')].append({"username": user.get(
                    'username'), "task": task.get('title'),
                    "completed": task.get('completed')})
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_dict, jsonfile)
