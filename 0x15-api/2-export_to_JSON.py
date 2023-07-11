#!/usr/bin/python3
'''Module 2-export_to_JSON
Exports data got from API to JSON'''
import json
import requests
from sys import argv


def main():
    '''Program starts here'''
    user_id = argv[1]
    data = {user_id: []}
    username = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        user_id).json().get('username')
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={'userId': user_id}).json()

    for i in all_tasks:
        data[user_id].append(
            {"task": i['title'],
             "completed": i['completed'],
             "username": username})

    with open(user_id + '.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
