#!/usr/bin/python3
"""getting data from an api
"""

import requests
import sys

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com"
    userId = sys.argv[1]
    user = requests.get(endpoint + "users/{}".
                        format(userId), verify=False).json()
    todo = requests.get(endpoint + "todos?userId={}".
                        format(userId), verify=False).json()
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))

# #!/usr/bin/python3
# """Gather data from an API
# """
#
# # from pprint import pprint
# import requests
# import sys
#
# if __name__ == "__main__":
#     userId = sys.argv[1]
#     completed_tasks: list = []
#     user_name = requests\
#         .get(f'https://jsonplaceholder.typicode.com/users/{userId}')\
#         .json().get('name')
#     tasks = requests.\
#         get(f'https://jsonplaceholder.typicode.com/todos?userId={userId}')\
#         .json()
#     # pprint(type(tasks))
#     # pprint(user_name)
#
#     for task in tasks:
#         if task.get('completed') is True:
#             completed_tasks.append(task.get('title'))
#
#     print(f'{user_name} is done with tasks \
#     ({len(completed_tasks)}/{len(tasks)}):')
#     for task in completed_tasks:
#         print(f"\t {task}")
