#!/usr/bin/python3
"""
importaion of important modules
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    params = {"userId": employee_id}
    todo_response = requests.get(url + "todos", params)
    todos = todo_response.json()
    complete_response = []

    for todo in todos:
        if todo.get("completed") is True:
            complete_response.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
			    len(complete_response), len(todos)))

    for response in complete_response:
        print("\t {}".format(response))
