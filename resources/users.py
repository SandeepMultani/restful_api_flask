from flask import Blueprint
import json

users = Blueprint('users', __name__)

USERS = {
    "SM01":{
        "fname": "Sandeep",
        "lname": "Multani"
    },
    "GM01":{
        "fname": "Gagandeep",
        "lname": "Multani"
    },
    "NM01":{
        "fname": "Navdeep",
        "lname": "Multani"
    }
}

 #GET /api/users
@users.route('/api/users', methods=['GET'])
def get_users():
    return json.dumps(USERS)

# GET /api/users/<string:user_id>
@users.route('/api/users/<string:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    #return user_id
    return json.dumps(USERS[user_id])