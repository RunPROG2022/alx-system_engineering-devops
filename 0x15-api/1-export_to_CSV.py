#!/usr/bin/python3
'''Module 1-export_to_CSV
Exports data got from API to CSV'''
import csv
import requests
from sys import argv


def main():
    '''Program starts here'''
    data = []
    user_id = argv[1]
    user_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        user_id).json().get('username')
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={'userId': user_id}).json()
    for i in all_tasks:
        data.append([user_id, user_name,
                    i['completed'], i['title']])

    with open(user_id + '.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)


if __name__ == '__main__':
    main()
