'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy
from pprint import pprint

passw = ''

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{passw}@localhost/sakila')
connection = engine.connect()
meta = sqlalchemy.MetaData()

film = sqlalchemy.Table("film_category", meta, autoload=True, autoload_with=engine)

# print(film.columns.keys())

query = sqlalchemy.select([film])
result = connection.execute(query)

set = result.fetchall()

# pprint(set)