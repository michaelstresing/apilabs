'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!

'''

import sqlalchemy
from sqlalchemy import Column, MetaData, Table, Integer, String, Boolean, ForeignKey

passw = ""
dbname = 'lab4db'
engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{passw}@localhost/{dbname}')
connection = engine.connect()
meta = MetaData()

menutable = sqlalchemy.Table(
    'Menu',
    meta,
    autoload=True,
    autoload_with=engine)

ingtable = sqlalchemy.Table(
    'Ingredients',
    meta,
    autoload=True,
    autoload_with=engine)

stafftable = sqlalchemy.Table(
    'Staff',
    meta,
    autoload=True,
    autoload_with=engine)

ing_menu = sqlalchemy.Table(
    "ing_menu",
    meta,
    autoload=True,
    autoload_with=engine)


#
# def create_tables():
#
#     menutable = Table(
#         'Menu', meta,
#         Column('id', Integer, primary_key=True, autoincrement=True),
#         Column('name', String(45)),
#         Column('price', String(45)),
#     )
#
#     ingtable = Table(
#         'Ingredients', meta,
#         Column('id', Integer, primary_key=True, autoincrement=True),
#         Column('name', String(45)),
#         Column('supplier', String(45)),
#         Column('cost', Integer)
#     )
#
#     stafftable = Table(
#         'Staff', meta,
#         Column('id', Integer, primary_key=True, autoincrement=True),
#         Column('name', String(45)),
#         Column('salary', Integer),
#         Column('active', Boolean)
#     )
#
#     ing_menu = Table(
#         'Ing_Menu', meta,
#         Column('id', Integer, primary_key=True, autoincrement=True),
#         Column('menuid', Integer, ForeignKey(menutable.c.id)),
#         Column('ingid', Integer, ForeignKey(ingtable.c.id))
#     )
#
#     meta.create_all(engine)


def menu():

    print("\nWelcome to the Coding Nomads Database centre!\n\n"
          "Please let us know what you'd like to do by pressing the corresponding number:\n"
          "1 - Insert Data to Table\n"
          "2 - Update Data in Table\n"
          "3 - Select Data from Table\n"
          "4 - Delete Data in Table\n"
          "5 - Select Ingredients corresponding to Menu Item\n"
          "q - Quit\n"
          )

    selection = input(":")

    if selection == "1":
        return insert_data()

    elif selection == "2":
        return update_data()

    elif selection == '3':
        return select_data()

    elif selection == '4':
        return delete_data()

    elif selection == '5':
        return gettheingredients()

    elif selection == 'q':
        quit()

    else:
        print("That's not a valid command...")
        return menu()


def insert_data():

    table = input("Which table to insert data (menutable, ingtable, stafftable): ")

    if table == 'menutable':
        name = input("Name: ")
        price = input("Price: ")

        request = menutable.insert().values(
            name=name,
            price=price)

        connection.execute(request)

    elif table == 'ingtable':
        name = input('Name: ')
        supplier = input("Supplier: ")
        cost = int(input("Cost: "))

        request = ingtable.insert().values(
            name=name,
            supplier=supplier,
            cost=cost)

        connection.execute(request)

    elif table == 'stafftable':
        name = input('Name: ')
        salary = int(input('Salary: '))
        active = bool(input("Active (True) or Not (False)"))

        request = menutable.insert().values(
            name=name,
            salary=salary,
            active=active)

        connection.execute(request)

    else:
        pass

    return_menu()

def update_data():

    table = input("Which table to update data (menutable, ingtable, stafftable): ")
    data = int(input("Which id:"))

    if table == 'menutable':
        name = input("Name: ")
        price = input("Price: ")

        request = menutable.update().values(
            name=name,
            price=price)\
            .where(menutable.c.id == data)

        connection.execute(request)

    elif table == 'ingtable':
        name = input('Name: ')
        supplier = input("Supplier: ")
        cost = int(input("Cost: "))

        request = ingtable.update().values(
            name=name,
            supplier=supplier,
            cost=cost)\
            .where(ingtable.c.id == data)

        connection.execute(request)

    elif table == 'stafftable':
        name = input('Name: ')
        salary = int(input('Salary: '))
        active = bool(input("Active (True) or Not (False)"))

        request = menutable.update().values(
            name=name,
            salary=salary,
            active=active)\
            .where(stafftable.c.id == data)

        connection.execute(request)

    else:
        pass

    return_menu()

def select_data():

    table = input("Which table (menutable, ingtable, stafftable): ")
    data = int(input('Which id: '))

    if table == 'menutable':

        request = menutable.select().where(menutable.c.id == data)
        proxy = connection.execute(request)
        output = proxy.fetchall()

        print(output)

    elif table == 'ingtable':

        request = ingtable.select().where(ingtable.c.id == data)
        proxy = connection.execute(request)
        output = proxy.fetchall()

        print(output)

    elif table == 'stafftable':

        request = menutable.select().where(stafftable.c.id == data)
        proxy = connection.execute(request)
        output = proxy.fetchall()

        print(output)

    else:
        pass

    return_menu()


def delete_data():

    table = input("Which table (menutable, ingtable, stafftable): ")
    data = int(input('Which id: '))

    if table == 'menutable':

        request = menutable.delete().where(menutable.c.id == data)
        connection.execute(request)

        print("Success!")

    elif table == 'ingtable':

        request = ingtable.delete().where(ingtable.c.id == data)
        connection.execute(request)

        print("Success!")

    elif table == 'stafftable':

        request = menutable.delete().where(stafftable.c.id == data)
        connection.execute(request)

        print("Success!")

    else:
        pass

    return_menu()


def gettheingredients():

    item = int(input("Which menu item id do you need the ingredients for? "))

    menujoin = menutable.join(ing_menu, menutable.columns.id == ing_menu.columns.menuid)
    menujoin2 = menujoin.join(ingtable, ing_menu.columns.ingid == ingtable.columns.id)

    request = sqlalchemy.select([ingtable.columns.name]).where(menutable.columns.id == item).select_from(menujoin2)
    proxy = connection.execute(request)
    output = proxy.fetchall()

    print(output)

    return_menu()


def return_menu():

    back = str(input("Return to menu? (y/n):"))

    if back == "y":
        return menu()
    else:
        return return_menu()


if __name__ == "__main__":
    menu()