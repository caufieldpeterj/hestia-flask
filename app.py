# external package imports
from flask import Flask, jsonify, g
# import CORS
from flask_cors import CORS

# internal imports
import models
# import logic from dogs resources logic
from resources.homes import home

# telling flask we are running this in a production environment
DEBUG=True

# 8000 or 5000 are the common python ports
PORT=8000

# create the glue for our app, everything will stick to our app variable as it is an instance of our files
app = Flask(__name__)


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


# ===========================================================================
# CORS Configuration
# ===========================================================================
# arguments home being imported from resources, define origins which we will allow to make the request, and support_credentials allows us to pass credentials

CORS(home, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(home, url_prefix='/api/v1/homes')
# ===========================================================================
# End CORS 
# ===========================================================================



#decorator references app, our flask application instance, which glues the function below to flask server
@app.route('/')
def index(): 
    return 'howdy partner'

@app.route('/test')
def test(): 
    my_list = ['I', 'cant', 'wait']
    # return jsonify(my_list)
    # ALWAYS WRAP RETURN IN JSONIFY
    # formatS into a json object, web standard for sending data back and forth, things are in the format that you know your front and expects.
    return jsonify(name="Peter", fav_language='Python')


# So syntax is we are adding you're telling flask hey this route is going to listen to anything after the slash and we're going to call it name.
# And so that is what flask will do classical convert anything after the smash bros We then this decorator will pass the parameter name.
# down into our function below, so we have to have the grammar there and then we can use it in our function like any other friend so here's the syntax for adding a.

@app.route('/sayhi/<name>')
def hello(name):
    return f'Hello {name}'


# a filter that only runss when we run a command external to Python and invoke it this way. we are controlling how this file gets run in this environment 
if __name__ == '__main__':
    models.initialize() 
    app.run(debug=DEBUG, port=PORT)