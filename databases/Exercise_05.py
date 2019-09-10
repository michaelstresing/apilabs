
'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

import requests
import sqlalchemy
import json
# from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean

user_source = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_source = "http://demo.codingnomads.co:8080/tasks_api/tasks"

user_request = requests.get(user_source).text
tasks_request = requests.get(tasks_source).text

user_json = json.loads(user_request)
tasks_json = json.loads(tasks_request)

passw = ""
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


# def create_tables():
#
#     users = Table(
#         'users',
#         meta,
#         Column('id', Integer, primary_key=True),
#         Column('first_name', String(45)),
#         Column('last_name', String(45)),
#         Column('email', String(45)),
#         Column('createdAt', String(45)),
#         Column('updatedAt', String(45))
#     )
#
#     tasks = Table(
#         'tasks', meta,
#         Column('id', Integer, primary_key=True),
#         Column('name', String(45)),
#         Column('description', String(45)),
#         Column('createdAt', String(45)),
#         Column('updatedAt', String(45)),
#         Column('completed', Boolean)
#     )
#
#     user_task = Table(
#         'user_task', meta,
#         Column('id', Integer, primary_key=True),
#         Column('userid', Integer, ForeignKey(users.id), ondelete='CASCADE', onupdate='CASCADE'),
#         Column('taskid', Integer, ForeignKey(tasks.id), ondelete='CASCADE', onupdate='CASCADE')
#     )
#
#     meta.create_all(engine)

# print(user_request)
# print(user_json)
# print(user_json['data'][1]['first_name'])


def addusers():

    usertotal = json.loads(user_request)
    userlen = len(usertotal['data'])

    for i in range(userlen):
        uid = user_json['data'][i]['id']
        first = user_json['data'][i]['first_name']
        last = user_json['data'][i]['last_name']
        email = user_json['data'][i]['email']
        created = user_json['data'][i]['createdAt']
        updated = user_json['data'][i]['updatedAt']

        # print(users.exists(uid))
        # print(type(users.exists(uid)))

        request = users.insert().values(
            id=uid,
            first_name=first,
            last_name=last,
            email=email,
            createdAt=created,
            updatedAt=updated).prefix_with("IGNORE")

        connection.execute(request)


def addtasks():

    taskstotal = json.loads(tasks_request)
    taskslen = len(taskstotal['data'])

    for i in range(taskslen):
        tid = tasks_json['data'][i]['id']
        name = tasks_json['data'][i]['name']
        description = tasks_json['data'][i]['description']
        created = tasks_json['data'][i]['createdAt']
        updated = tasks_json['data'][i]['updatedAt']
        completed = tasks_json['data'][i]['completed']

        request = tasks.insert().values(
            id=tid,
            name=name,
            description=description,
            createdAt=created,
            updatedAt=updated,
            completed=completed).prefix_with("IGNORE")

        connection.execute(request)


def addusertasks():

    taskstotal = json.loads(tasks_request)
    taskslen = len(taskstotal['data'])

    for i in range(taskslen):
        tid = tasks_json['data'][i]['id']
        uid = tasks_json['data'][i]['userId']

        request = user_task.insert().values(
            taskid=tid,
            userid=uid).prefix_with("IGNORE")

        connection.execute(request)


addusers()
addtasks()
addusertasks()



'''
Notes: 
Timecomplexity -> can use load everything then use database to clear duplicates: 

"delete from bitmex_quote as a using bitmex_quote as b where a.ctid < b.ctid and a.timestamp = b.timestamp; "

'''