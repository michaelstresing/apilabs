'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

'''
TODO: 
Figure out the range issue on addusers/addtasks
Figure out a way to prevent/address duplicates

'''

import requests
import sqlalchemy
import json
from pprint import pprint

user_source = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_source = "http://demo.codingnomads.co:8080/tasks_api/tasks"

user_request = requests.get(user_source).text
tasks_request = requests.get(tasks_source).text

user_json = json.loads(user_request)
tasks_json = json.loads(tasks_request)

passw = '.'
newdb = 'apilab'

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{passw}@localhost/{newdb}')
connection = engine.connect()
meta = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    meta,
    autoload=True,
    autoload_with=engine)

tasks = sqlalchemy.Table(
    'tasks',
    meta,
    autoload=True,
    autoload_with=engine)

user_task = sqlalchemy.Table(
    'user_task',
    meta,
    autoload=True,
    autoload_with=engine)

'''
TABLES CREATED: 
users: (id-PK, first_name, last_name, email, createdAt, updatedAt)
tasks; (id-PK, name, description, createdAt, updatedAt)
user_tasks (id-PK, userid FK to users.id, taskid FK to tasks.id)
'''

# print(user_request)
# print(user_json)
# print(user_json['data'][1]['first_name'])


def addusers():

    for i in range(5):
        uid = user_json['data'][i]['id']
        first = user_json['data'][i]['first_name']
        last = user_json['data'][i]['last_name']
        email = user_json['data'][i]['email']
        created = user_json['data'][i]['createdAt']
        updated = user_json['data'][i]['updatedAt']

        print(first, last, email, created, updated)

        request = users.insert().values(
            first_name=first,
            last_name=last,
            email=email,
            createdAt=created,
            updatedAt=updated)

        connection.execute(request)


def addtasks():

    for i in range(5):
        tid = tasks_json['data'][i]['id']
        name = tasks_json['data'][i]['name']
        description = tasks_json['data'][i]['description']
        created = tasks_json['data'][i]['createdAt']
        updated = tasks_json['data'][i]['updatedAt']
        completed = tasks_json['data'][i]['completed']

        print(name, description, created, updated, completed)

        request = tasks.insert().values(
            id=tid,
            name=name,
            description=description,
            createdAt=created,
            updatedAt=updated,
            completed=completed)

        connection.execute(request)

addusers()
addtasks()