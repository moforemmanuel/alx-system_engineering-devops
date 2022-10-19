#!/usr/bin/python3
"""
Gather data from an API
"""
# from pprint import pprint
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    completed_tasks: list = []
    user_name = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{userId}')\
        .json().get('name')
    tasks = requests.\
        get(f'https://jsonplaceholder.typicode.com/todos?userId={userId}')\
        .json()
    # pprint(type(tasks))
    # pprint(user_name)

    for task in tasks:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))

    print(f'{user_name} is done with tasks \
    ({len(completed_tasks)}/{len(tasks)}):')
    for task in completed_tasks:
        print(f"\t{task}")
