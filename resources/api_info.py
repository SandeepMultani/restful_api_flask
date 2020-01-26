from flask import Blueprint
import json

api_info = Blueprint('api_info', __name__)

@api_info.route('/', methods=['GET'])
def get_api_info():
    return json.dumps({
    "name": "My first flash api",
    "version": "1.0"
})