from flask import Flask
# telling flask we are running this in a production environment
DEBUG=True
# 8000 or 5000 are the common python ports
PORT=8000
# create the glue for our app, everything will stick to our app variable as it is an instance of our files
app = Flask(__name__)

@app.route('/')
def index(): 
    return 'howdy'

# a filter that only runss when we run a command external to Python and invoke it this way. we are controlling how this file gets run in this environment 
if __name__ == '__main__': 
    app.run(debug=DEBUG, port=PORT)