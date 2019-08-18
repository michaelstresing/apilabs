'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests

source = 'http://demo.codingnomads.co:8080/tasks_api/users'

# body = {
#     "id": 30,
#     "first_name": "Michael",
#     "last_name": "Stresing",
#     "email": "mstresing@gmail.com"
# }

request = requests.delete('http://demo.codingnomads.co:8080/tasks_api/users/30')

print(request.status_code)
print(requests.get(source).text)