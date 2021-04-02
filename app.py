# external package imports
from flask import Flask, jsonify, g

# internal imports
import models

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