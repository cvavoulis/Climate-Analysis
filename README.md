## Surfs Up!

![surfs-up.jpeg](Images/surfs-up.jpeg)


# Climate Analysis and Exploration

I used python, SQLAlchemy ORM queries, pandas, and Matplotlib to do basic climate analysis and data exploration of my climate database. 

I used SQLAlchemy `create_engine` to connect to my sqlite database.

I use SQLAlchemy `automap_base()` to reflect my tables into classes and save a reference to those classes called `Station` and `Measurement`.

Then, I designed a Flask API based on the queries that I developed. Using the routes that I created, I returned a JSON representation of my dictionary. 

