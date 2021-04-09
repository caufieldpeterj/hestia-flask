# python module for interacting with our operating system
import os
# import everything from peewee
from peewee import *
# part of base python language
from datetime import datetime
# This is a Peewee extension for creating a database connection from a URL string.
from playhouse.db_url import connect

# global variable referencing local database
# http://docs.peewee-orm.com/en/latest/peewee/database.html#initializing-a-database

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))
else:
    DATABASE = PostgresqlDatabase('homes')
'''
DATABASE = PostgresqlDatabase(
    'dbnnt65aol8afg',  # Required by Peewee.
    user='jbiqmolkxjkyzy',  # Will be passed directly to psycopg2.
    password='1dd25d55268ad8e2292792dd9d0de144b70603b4eb6fc07782f70f9c3a8ee08d',
    host='ec2-18-233-83-165.compute-1.amazonaws.com',
    sslmode='require',
    port=5432)  
'''

#Extend peewees Model class and add our own logic/schema on top of it to create our DB schema
class Homes(Model):
    city = CharField()
    state = CharField()
    bedrooms = CharField()
    bathrooms = CharField()
    sq_ft = CharField()
    price = CharField()
    down_pmt = CharField()
    est_mtge = IntegerField()
    created_at = DateTimeField(default=datetime.now)
    # need to specify metadata, telling peewee this is the database we're going to talk to.
    class Meta:
        database = DATABASE

def seed_db():
    data_source = [
        {
            'city': 'srq', 
            'state': 'fl',
            'bedrooms': '', 
            'bathrooms': '', 
            'sq_ft': '', 
            'price':'', 
            'down_pmt': '', 
            'est_mtge': 20, 
            'created_at': datetime.now
        },
        {
            'city': 'hhk', 
            'state': 'nj',
            'bedrooms': '', 
            'bathrooms': '', 
            'sq_ft': '', 
            'price':'', 
            'down_pmt': '', 
            'est_mtge': 20, 
            'created_at': datetime.now
        },
        {
            'city': 'boca', 
            'state': 'fl',
            'bedrooms': '', 
            'bathrooms': '', 
            'sq_ft': '', 
            'price':'', 
            'down_pmt': '', 
            'est_mtge': 20, 
            'created_at': datetime.now 
        }
    ]
    for data_dict in data_source:
        Homes.create(**data_dict)

# handles intialization, connect, creation of tables, debugging statement to let us know this function fires, close connection of our database
def initialize():
    # OperationalError -- Exception raised for errors that are related to the database's operation and not necessarily under the control of the programmer, e.g. an unexpected disconnect occurs, the data source name is not found, a transaction could not be processed, a memory allocation error occurred during processing, etc.
    DATABASE.connect()
    # safe ensures that we only create this table if it does not already exist
    DATABASE.create_tables([Homes], safe=True)
    print('TABLES created')
    # DATABASE.seed_db()
    DATABASE.close()