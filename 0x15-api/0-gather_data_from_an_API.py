#!/usr/bin/python3
"""
This script retrieves and displays TODO list progress for a
given employee ID using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display TODO list progress for the specified employee.
    Args:
        employee_id (int): The ID of the employee.
    Returns:
        None
    """
    # Define the API endpoint URLs
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Send a GET request to the API to get user data
        user_response = requests.get(user_url)

        # Send a GET request to the API to get todos
        todos_response = requests.get(todos_url)

        # Check if both requests were successful (status code 200)
        if user_response.status_code == 200 and todos_response.status_code == 200:
            # Parse the JSON responses
            user_data = user_response.json()
            todos = todos_response.json()

            # Filter completed tasks
            completed_tasks = [task for task in todos if task.get('completed', False)]

            # Calculate the number of completed tasks and total tasks
            num_completed_tasks = len(completed_tasks)
            total_tasks = len(todos)

            # Get the employee's name from user data
            employee_name = user_data.get('username', "Unknown")

            # Print the progress report
            print(f"Employee {employee_name} is done with tasks "
                  f"({num_completed_tasks}/{total_tasks}):")

            # Print the titles of completed tasks
            for task in completed_tasks:
                print(f"\t{task['title']}")

        else:
            print(f"Error: Unable to fetch data. Status code: {user_response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./employee_todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
