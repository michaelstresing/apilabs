'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
# from pprint import pprint

email = "email"
source = 'http://demo.codingnomads.co:8080/tasks_api/users'

request = requests.get(source)
data = request.json()
# pprint(data)

emaillist = []

for i in data['data']:
    emaillist.append(i["email"])

print(emaillist)
