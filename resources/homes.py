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


# create index route here, try / catch, if it works provide us with the list of homes 
@home.route('/', methods=['GET'])
def get_all_homes():
    try:
        homes = [model_to_dict(home) for home in models.Homes.select()]
        print(homes)
        return jsonify(data=homes, status={"code": 200, "message": "success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message":"Error getting the resources"})


# POST ROUTE 
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