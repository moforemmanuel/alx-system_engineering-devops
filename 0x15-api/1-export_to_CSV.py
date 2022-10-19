#!/usr/bin/python3
"""getting data from an api
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get(endpoint + "users/{}".
                        format(userId)).json()
    todo = requests.get(endpoint + "todos?userId={}".
                        format(userId)).json()
    # completed_tasks = []
    # for task in todo:
    #     if task.get('completed') is True:
    #         completed_tasks.append(task.get('title'))
    # print("Employee {} is done with tasks({}/{}):".
    #       format(user.get('name'), len(completed_tasks), len(todo)))
    # print("\n".join("\t {}".format(task) for task in completed_tasks))
    with open(f"{userId}.csv", "w") as csv_file:
        # create the csv writer
        writer = csv.writer(csv_file)

        # write a row to the csv file
        for task in todo:
            writer.writerow([userId, user.get('username'), task.get('completed'),
                            task.get('title')])
