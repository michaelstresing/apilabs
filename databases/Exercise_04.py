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
'''
TODO: 
heaps of stuff..
'''

import sqlalchemy
from sqlalchemy import Column, MetaData, Table, Integer, String

passw = ""
engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{passw}@localhost/freshdb4lab')
connection = engine.connect()
meta = MetaData()


def create_table():


    tablename = str(input('Please enter a name for the table: '))
    usertable = Table(
        f'{tablename}', meta,
        Column('', Integer, primary_key=True),
        Column('', String),
        Column('', String)
    )

    cols = int(input('Please enter the number of columns for your table: '))

    for col in range(cols - 1):
        colname = str(input('Please enter the name of the first column: '))
        coltype = str(input(f'Please enter the data type for {colname} (s)tring, (i)nt, (d)atetime.'))

        if coltype == "s":

        usertable.

meta.create_all(engine)

def insert_data():

