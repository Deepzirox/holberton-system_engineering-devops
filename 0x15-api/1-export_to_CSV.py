#!/usr/bin/python3
"""
export data in the CSV format
"""
from sys import argv
import csv
import requests


if __name__ == "__main__":
    """ to csv """
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    filename = user_id + ".csv"
    employer = requests.get(url + 'users/' + user_id)
    employer = employer.json()
    t = requests.get(url + "todos?userId=" + user_id)
    t = t.json()
    with open(filename, mode="w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for counter in t:
            writer.writerow((counter.get('userId'), employer.get(
                'username'), counter.get('completed'), counter.get('title')))
