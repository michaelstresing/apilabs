'''
Using sqlalchemy which the necessary code to:

'''

import sqlalchemy
from pprint import pprint

passw = ''

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{passw}@localhost/sakila')
connection = engine.connect()
meta = sqlalchemy.MetaData()

actor = sqlalchemy.Table("actor", meta, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table("film_actor", meta, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table("film_category", meta, autoload=True, autoload_with=engine)
films = sqlalchemy.Table('film', meta, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', meta, autoload=True, autoload_with=engine)


# - Select all the actors with the first name of your choice

actor_proxy = sqlalchemy.select([actor]).where(actor.columns.first_name == "Michael")
actor_result = connection.execute(actor_proxy)

actordata = actor_result.fetchall()

# pprint(actordata)

# - Select all the actors and the films they have been in

joinstatement = actor.join(film_actor, actor.columns.actor_id == film_actor.columns.actor_id)
join2 = joinstatement.join(films, film_actor.columns.film_id == films.columns.film_id)

film_actor_proxy = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name, films.columns.title]).select_from(join2)   # The statement appears to work without the .select_from(join2) at the end - though it runs much slower.

film_actor_result = connection.execute(film_actor_proxy)
film_actor_data = film_actor_result.fetchall()

# pprint(film_actor_data)

# - Select all the actors that have appeared in a category of you choice comedy

join3 = join2.join(film_category, film_actor.columns.film_id == film_category.columns.film_id)
join4 = join3.join(category, film_category.columns.category_id == category.columns.category_id)

funnyactors = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name]).where(category.columns.name == 'Comedy').select_from(join4)

funnyactors_result = connection.execute(funnyactors)
funnyactors_data = funnyactors_result.fetchall()

# pprint(funnyactors_data)

# - Select all the comedic films and that and sort them by rental rate

pricycomedies = sqlalchemy.select([films.columns.title, films.columns.rental_rate]).where(category.columns.name == 'Comedy').select_from(join4)
pricycomedies = pricycomedies.order_by(sqlalchemy.desc(films.columns.rental_rate))

pricycomedies_result = connection.execute(pricycomedies)
pricycomedies_data = pricycomedies_result.fetchall()

# pprint(pricycomedies_data) ... Revist the repeat data issue...

# - Using one of the statements above, add a GROUP BY

pricycomedies_age = pricycomedies.group_by(films.columns.rental_rate)

pricycomedies_age_result = connection.execute(pricycomedies_age)
pricycomedies_age_data = pricycomedies_age_result.fetchall()

pprint(pricycomedies_age_data)
# Leaving this one - to come back to...

# - Using on of the statements above, add a ORDER BY

