'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests

source = 'http://demo.codingnomads.co:8080/tasks_api/users'

body = {
    "id": 30,
    "first_name": "Michael",
    "last_name": "Stresing",
    "email": "mstresing@gmail.com"
}

requests.post(source, json=body)

print(requests.get(source).text)