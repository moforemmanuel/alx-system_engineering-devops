#!/usr/bin/python3
"""getting data from an api
"""

import requests
from sys import argv

if __name__ == "__main__":
    userId = argv[1]
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
        print(f"\t {task}")
