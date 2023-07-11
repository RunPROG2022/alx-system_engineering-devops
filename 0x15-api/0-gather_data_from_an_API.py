#!/usr/bin/python3
'''Module 0-gather_data_from_an_API
using a REST API, for a given employee ID, returns information
about his/her TODO list progress.'''
import requests
from sys import argv


def main():
    '''Program starts here'''
    user_id = argv[1]
    user_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        user_id).json().get('name')
    # print("USER: ", user)

    completed_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={'userId': user_id, 'completed': 'true'}).json()
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={'userId': user_id}).json()

    print("Employee", user_name, "is done with tasks(" +
          str(len(completed_tasks)) + "/" + str(len(all_tasks)) + "):")
    for i in completed_tasks:
        print("\t " + i['title'])


if __name__ == '__main__':
    main()
