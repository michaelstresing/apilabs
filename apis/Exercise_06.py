
import requests
import time

user_source = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_source = "http://demo.codingnomads.co:8080/tasks_api/tasks"


def menu():

    print("\nWelcome to the Coding Nomads API centre!\n\n"
          "Please let us know what you'd like to do by pressing the corresponding number:\n"
          "1 - Create a new account\n"
          "2 - View all your tasks\n"
          "3 - View your completed tasks\n"
          "4 - View only your incomplete tasks\n"
          "5 - Create a new task\n"
          "6 - Update an existing task\n"
          "7 - Delete a task\n"
          "q - Quit\n"
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
        return create_new_task()

    elif selection == '6':
        return update_task()

    elif selection == '7':
        return delete_task()

    elif selection == 'q':
        quit()

    else:
        print("That's not a valid command...")
        return menu()

# 1) Create a new account (POST)


def new_account():
    print("You've selected: Create new account")
    time.sleep(1)

    first_name = str(input("Please enter the first name for new account: "))
    last_name = str(input("Please enter the last name for new account: "))
    email = str(input("Please enter the email for the account: "))

    entry = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
    }

    post = requests.post(user_source, json=entry)
    post

    if post.status_code == 200:
        print("Success!")

    else:
        print("uh, oh...")

    return_menu()

# 2) View all your tasks (GET)


def view_tasks():

    print("You've selected: View Tasks")
    time.sleep(1)
    print("Your tasks are: ")

    taskraw = requests.get(tasks_source).json()

    for task in taskraw['data']:
        print(f" * {task['name']}")

    return_menu()

# 3) View your completed tasks (GET)


def view_completed_tasks():

    print("You've selected: View Completed Tasks")
    time.sleep(1)
    print("Your completed tasks are: ")

    completedparams = {
       'completed': True
    }

    completedtaskraw = requests.get(tasks_source, params=completedparams).json()

    for task in completedtaskraw['data']:
        print(f" * {task['name']}")

    return_menu()

# 4) View only your incomplete tasks (GET)


def view_incomplete_tasks():

    print("You've selected: View Incomplete Tasks")
    time.sleep(1)
    print("Your incomplete tasks are: ")

    incompletedparams = {
        "completed": False
    }

    incompletetaskraw = requests.get(tasks_source, params=incompletedparams).json()

    for task in incompletetaskraw['data']:
        print(f" * {task['name']}")

    return_menu()

# 5) Create a new task (POST)


def create_new_task():

    print("You've selected: Create new task")
    time.sleep(1)

    description = str(input("Please enter the task description: "))
    name = str(input("Please enter the task name: "))

    tasktoenter = {
        "description": description,
        "name": name,
    }

    post = requests.post(tasks_source, json=tasktoenter)

    if post.status_code == 200:
        print("Success!")
        return_menu()
    else:
        print("uh oh...")
        return_menu()


# 6) Update an existing task (PATCH/PUT)


def update_task():

    print("You've selected: Update Task")
    time.sleep(1)

    tasktoupdate = int(input("Please enter the id of the task you'd like to modify: "))

    newdescription = str(input("Please enter a new description for the task: "))
    newname = str(input("Please enter a new name for the task: "))

    update = {
        "id": tasktoupdate,
        "description": newdescription,
        "name": newname
    }

    updateit = requests.put(tasks_source, json=update)

    if updateit.status_code == 200:
        print("Success!")
        return_menu()
    else:
        print("uh oh...")
        return_menu()

# 7) Delete a task (DELETE)


def delete_task():

    print("You've selected: Update Task")
    time.sleep(1)

    tasktodelete = int(input("Please enter the id of the task you'd like to delete: "))

    confirmation = str(input(f"Are you sure you'd like to delete task {tasktodelete}? (y/n):"))

    if confirmation == "y":

        deletereq = requests.delete(f'{tasks_source}/{tasktodelete}')

        if deletereq.status_code == 200:
            print("Success!")
            return_menu()
        else:
            print("uh oh...")
            return_menu()

    else:
        print("Delete aborted, returning to menu")
        return menu()


def return_menu():

    back = str(input("Return to menu? (y/n):"))

    if back == "y":
        return menu()
    else:
        return return_menu()


if __name__ == "__main__":
    menu()
