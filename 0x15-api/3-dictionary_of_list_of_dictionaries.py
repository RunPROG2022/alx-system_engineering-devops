#!/usr/bin/python3
'''Module 3-dictionary_of_list_of_dictionaries
Exports all users from the API to JSON file
'''
import json
import requests
from sys import argv


def main():
    '''Program starts here'''
    all_users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    data = {}
    for i in all_users:
        user_id = i['id']
        data[user_id] = []
        username = requests.get(
            'https://jsonplaceholder.typicode.com/users/' +
            str(user_id)).json().get('username')
        all_tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos',
            params={'userId': user_id}).json()

        for i in all_tasks:
            data[user_id].append(
                {"username": username,
                 "task": i['title'],
                 "completed": i['completed']
                 })

        with open('todo_all_employees.json', 'w') as f:
            json.dump(data, f)


if __name__ == '__main__':
    main()
