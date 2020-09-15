#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress
"""
from sys import argv
import csv
import requests


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
    with open(filename, mode="w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for counter in get_json()[0]:
            writer.writerow((counter.get('userId'), get_json()[1].get(
                'username'), counter.get('completed'), counter.get('title')))
