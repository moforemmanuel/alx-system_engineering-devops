#!/usr/bin/python3
"""
Gather data from an API
"""
# from pprint import pprint
import requests
import sys

completed_tasks: list = []
user_name = requests.get(f'https://jsonplaceholder.typicode.com/users/\
{sys.argv[1]}').json().get('name')
tasks = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId=\
{sys.argv[1]}').json()
# pprint(type(tasks))
# pprint(user_name)

for task in tasks:
    if task.get('completed') is True:
        completed_tasks.append(task.get('title'))

print(f'{user_name} is done with tasks ({len(completed_tasks)}/{len(tasks)}):')
for task in completed_tasks:
    print(f'\t{task}')
