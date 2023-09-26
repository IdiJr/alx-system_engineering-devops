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
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("Employee not found")
        exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get("username")
    file_name = "{}.json".format(employee_id)

    data_to_export = {str(employee_id): []}

    for task in todos_data:
        task_title = task.get("title")
        task_completed = task.get("completed")
        data_to_export[str(employee_id)].append({
            "task": task_title,
            "completed": task_completed,
            "username": employee_name
        })

    with open(file_name, 'w') as json_file:
        json.dump(data_to_export, json_file, separators=(',', ':'))

    print("Data exported to {}".format(file_name))
