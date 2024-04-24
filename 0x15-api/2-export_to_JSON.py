#!/usr/bin/python3
"""
importation of important modules
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    username = user.get("username")
    data_to_export = {user_id: []}
    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params)
    todos = todos_response.json()

    for todo in todos:
        task_info = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username
            }
        data_to_export[user_id].append(task_info)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
