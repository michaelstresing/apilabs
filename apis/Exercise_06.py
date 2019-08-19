
import requests
import json
from pprint import pprint
import time

user_source = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_source = "http://demo.codingnomads.co:8080/tasks_api/tasks"


def menu():

    print("Welcome to the Coding Nomads API centre!\n"
          "Please let us know what you'd like to do by pressing the corresponding number:\n"
          "1 - Create a new account\n"
          "2 - View all your tasks\n"
          "3 - View your completed tasks\n"
          "4 - View only your incomplete tasks\n"
          "5 - Create a new task\n"
          "6 - Update an existing task\n"
          "7 - Delete a task\n"
          )

    selection = input(":")

    if selection == "1":
        return new_account()

    elif selection == "2":
        return view_tasks()

    elif selection == '3':
        return view_completed_tasks()

    elif selection == '4':
        return view_incomplete_tasks()

    elif selection == '5':
        return

    elif selection == '6':
        return

    elif selection == '7':
        return

    else:
        print("That's not a valid number...")

# 1) Create a new account (POST)


def new_account():
    print("You've selected: Create new account")
    time.sleep(1)

    first_name = str(input("Please enter the first name for new account: "))
    last_name = str(input("Please enter the last name for new account: "))
    email = str(input("Please enter the email for the account: "))
    id = int(input("Please enter the user_id"))

    entry = {
        "email": email,
        "first_name": first_name,
        "id": id,
        "last_name": last_name,
    }

    requests.post(user_source, json=entry)

    print(requests.get(user_source).text)

# 2) View all your tasks (GET)


def view_tasks():

    print("You've selected: View Tasks")
    time.sleep(1)
    print("Your tasks are: ")

    taskraw = requests.get(tasks_source).json()

    for task in taskraw['data']:
        print(f" * {task['name']}")

# 3) View your completed tasks (GET)


def view_completed_tasks():

    print("You've selected: View Completed Tasks")
    time.sleep(1)
    print("Your completed tasks are: ")

    params = {
       'completed': 'true'
    }

    completedtaskraw = requests.get(tasks_source, params=params).json()

    for task in completedtaskraw['data']:
        print(f" * {task['name']}")

    pprint(completedtaskraw)

# 4) View only your incomplete tasks (GET)


def view_incomplete_tasks():

    print("You've selected: View Incomplete Tasks")
    time.sleep(1)
    print("Your incomplete tasks are: ")

    incompletetaskraw = requests.get(tasks_source, params={"data['completed']": False}).json()

    for task in incompletetaskraw['data']:
        print(f" * {task['name']}")

    pprint(incompletetaskraw)

# 5) Create a new task (POST)


# def create_new_task():
#
#     print("You've selected: Create new task")
#     time.sleep(1)
#
#     description = str(input("Please enter the task description: "))
#     name = str(input("Please enter the task name: "))
#
#     taskentry = {
#         "description": description,
#         "name": name,
#     }
#
#     requests.post(tasks_source, json=taskentry)
#
#     print(requests.get(user_source).text)

# 6) Update an existing task (PATCH/PUT)


# 7) Delete a task (DELETE)



print(view_completed_tasks())