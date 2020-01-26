from flask import Flask

from resources.users import users
from resources.api_info import api_info

app = Flask(__name__)

app.register_blueprint(users)
app.register_blueprint(api_info)

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)