# hestia-flask

# setting up virtual environment
python3 -m venv venv

# bash code that configures virtual env for us (locally) and manages it
. venv/bin/activate

# postgres is always running in the background of our computer, so flask just sends the requests o psql

# flask-bcrypt
# peewee - ORM, how flask stalks to PostgreSQL
# psycopg2-binary - db engine for psql, how we talk to postgres
# flask_login - 
# flask_cors - 
pip3 install flask-bcrypt peewee flask psycopg2-binary flask_login flask_cors

# pipe it
pip3 freeze > requirements.txt

# create 
touch app.py
--
from flask import Flask, jsonify

# telling flask we are running this in a production environment
DEBUG=True

# 8000 or 5000 are the common python ports
PORT=8000

# create the glue for our app, everything will stick to our app variable as it is an instance of our files
app = Flask(__name__)

#decorator references app, our flask application instance, which glues the function below to flask server
@app.route('/')
def index(): 
    return 'howdy partner'

@app.route('/test')
def test(): 
    my_list = ['I', 'cant', 'wait']
    # return jsonify(my_list)
    # ALWAYS WRAP RETURN IN JSONIFY
    # formats into a json object, web standard for sending data back and forth, things are in the format that you know your front and expects.
    return jsonify(name="Peter", fav_language='Python')


# So syntax is we are adding you're telling flask hey this route is going to listen to anything after the slash and we're going to call it name.
# And so that is what flask will do classical convert anything after the smash bros We then this decorator will pass the parameter name.
# down into our function below, so we have to have the grammar there and then we can use it in our function like any other friend so here's the syntax for adding a.

@app.route('/sayhi/<name>')
def hello(name):
    return f'Hello {name}'


# a filter that only runss when we run a command external to Python and invoke it this way. we are controlling how this file gets run in this environment 
if __name__ == '__main__': 
    app.run(debug=DEBUG, port=PORT)
--

python3 app.py
localhost:8000/test
localhost:8000/sayhi/peter

<!-- within separate terminal window, navigate to root of app.py file from above...  -->
touch models.py 
code .

---
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
---

AND THEN

app.py
---
# internal imports
import models
# ...
# AT THE BOTTOM OF THE FILE
if __name__ == '__main__':
    models.initialize() 
    app.run(debug=DEBUG, port=PORT)
---

WE MIGHT need to manually create the database ourselves, if so... within venv terminal window

$ createdb homes
$ psql homes
homes#= \q
python3 app.py

which should create a table within our homes db, within separate terminal window at the root directory of app.py
$ psql homes
homes#= \d

# should return our created table          
            List of relations
 Schema |     Name     |   Type   | Owner 
--------+--------------+----------+-------
 public | homes        | table    | peter
 public | homes_id_seq | sequence | peter
(2 rows)


then...

git checkout -b dev
git pull origin main
git status 
git add 
git commit 
git push origin dev -  sends changes to dev branch


DEV BRANCH CREATED



app.py
---
import g

# ===========================================================================
# MIDDLEWARE OPENING AND CLOSING DB CONNECTIONS EVERYTIME A REQUEST IS SENT TO OUR SERVER
# ===========================================================================
# decorator that fires before any db requests
@app.before_request
def before_request():
    '''
    connect to the db before each request
    '''
    print('before request')
    # creating new global variable called db which is = to our PostgreSQL db
    g.db = models.DATABASE
    # making connection to our db
    g.db.connect()


# decorator that closes db connection after requests
@app.after_request
def after_request(response):
    '''
    close connection to the db after each request
    '''
    print('after request')
    g.db.close()
    # pass the server response to the front-end from server after db conneciton is closed
    return response
# ===========================================================================
# END MIDDLEWARE
# ===========================================================================

test route in browser to see if db connection and 


in root of project
$ mkdir resources
# package directory, dont touch it
$ touch resources/__init__.py
# our controller
$ touch resources/homes.py

homes.py
---
import models

# blueprint records the operations helps execute. records the operation and helps execute them when registered on the application.
from flask import Blueprint, jsonify, request

# allows python data to be interpreted correctly
from playhouse.shortcuts import model_to_dict

# configure this blueprint

#first arg is the blueprint name
#second arg is the import name
#third arg is the url_prefix
home = Blueprint('homes', 'home')
---

app.py
---
# external
from flask_cors import CORS
# internal
from resources.homes import home

# after middleware...
# ===========================================================================
# CORS Configuration
# ===========================================================================
# arguments home being imported from resources, define origins which we will allow to make the request, and support_credentials allows us to pass credentials

CORS(home, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(home, url_prefix='/api/v1/homes')
# ===========================================================================
# End CORS 
# ===========================================================================


resources > homes.py
---
# create index route here, try / catch, if it works provide us with the list of homes 
@home.route('/', methods=['GET'])
def get_all_homes():
    try:
        homes = [model_to_dict(home) for home in models.Homes.select()]
        print(homes)
        return jsonify(data=homes, status={"code": 200, "message": "success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message":"Error getting the resources"})

---

test in postman or in browser
GET localhost:8000/api/v1/homes




resources > homes.py
---

@home.route('/', methods=['POST'])
def create_homes():
    # get_json turns json out of a request and turns into python data
    payload = request.get_json()
    # should print a dictionary
    print(type(payload), 'payload')
    # spread operator being used
    home = models.Homes.create(**payload)
    # print the dictionary version of the model version of the Home instance
    print(home.__dict__)
    # look at all the methods
    print(dir(home))
    #change the model into a dictionary
    print(model_to_dict(home), 'model to dictionary')
    home_dict = model_to_dict(home)
    return jsonify(data=home_dict, status={"code": 201, "message":"Successful home creation"})
---
test in postman or curl

POST localhost:8000/api/v1/homes/
Body > raw > JSON
{
    "bedrooms":"5",
    "bathrooms":"3",
    "sq_ft":"500",
    "price":"$250,000"
}

test GET request to ensure we see the POSTED home