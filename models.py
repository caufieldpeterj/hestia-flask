# import everything from peewee
from peewee import *
# part of base python language
from datetime import datetime 

# global variable referencing local database
# http://docs.peewee-orm.com/en/latest/peewee/database.html#initializing-a-database
DATABASE = PostgresqlDatabase('homes')

#Extend peewees Model class and add our own logic/schema on top of it to create our DB schema
class Homes(Model):
    bedrooms = CharField()
    bathrooms = CharField()
    sq_ft = CharField()
    price = CharField()
    created_at = DateTimeField(default=datetime.now)
    # need to specify metadata, telling peewee this is the database we're going to talk to.
    class Meta:
        database = DATABASE

# handles intialization, connect, creation of tables, debugging statement to let us know this function fires, close connection of our database
def initialize():
    DATABASE.connect()
    # safe ensures that we only create this table if it does not already exist
    DATABASE.create_tables([Homes], safe=True)
    print('TABLES created')
    DATABASE.close()