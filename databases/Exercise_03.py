'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''

import sqlalchemy

passw = ''

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{passw}@localhost/sakila')
connection = engine.connect()
meta = sqlalchemy.MetaData()

films = sqlalchemy.Table('film', meta, autoload=True, autoload_with=engine)

request = sqlalchemy.update(films).values(rental_duration=10).where(films.columns.rental_duration > 150.00)

request_proxy = connection.execute(request)

