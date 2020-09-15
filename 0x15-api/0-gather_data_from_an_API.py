#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress
"""
import requests
from sys import argv


def get_json():
    """ Get employes and task
    """
    url = 'https://jsonplaceholder.typicode.com/'
    uid = argv[1]
    employee = requests.get(url + 'users/' + uid)
    employee = employee.json()

    task = requests.get(url + "todos?userId=" + uid)
    return (task.json(), employee)


if __name__ == "__main__":
    list_done = []
    for counter in get_json()[0]:
        if counter.get("completed") is True:
            list_done.append(counter)
    task_done = len(list_done)
    task_total = len(get_json()[0])
    print("Employee {} is done with tasks({}/{}):".format(
        get_json()[1].get('name'), task_done, task_total))
    for count in list_done:
        print('\t {}'.format(count.get('title')))
