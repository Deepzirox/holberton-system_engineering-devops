#!/usr/bin/python3
"""
script that, using this REST API, for a given employ ID,
returns information about his/her todo list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    ''' to csv '''
    url = 'https://jsonplaceholder.typicode.com/'
    uid = argv[1]
    employ = requests.get(url + 'users/' + uid)
    employ = employ.json()
    task = requests.get(url + "todos?userId=" + uid)
    with open(filename, mode="w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for counter in task.json():
            writer.writerow((counter.get('userId'), employ.get(
                'username'), counter.get('completed'), counter.get('title')))
