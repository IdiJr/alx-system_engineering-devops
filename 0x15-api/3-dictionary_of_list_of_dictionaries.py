#!/usr/bin/python3
"""
This script retrieves and displays TODO list progress for a
given employee ID using a REST API and exports data in
the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 1:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    users_response = requests.get(users_url)

    if users_response.status_code != 200:
        print("Failed to fetch user data")
        exit(1)

    users_data = users_response.json()
    todo_dict = {}

    for user in users_data:
        user_id = user["id"]
        username = user["username"]
        todos_url = f"{base_url}/todos?userId={user_id}"
        todos_response = requests.get(todos_url)

        if todos_response.status_code != 200:
            print(f"Failed to fetch tasks for user {username}")
            continue

        todos_data = todos_response.json()
        user_tasks = []

        for task in todos_data:
            user_task = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            user_tasks.append(user_task)

        todo_dict[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todo_dict, json_file, separators=(',', ':'))
