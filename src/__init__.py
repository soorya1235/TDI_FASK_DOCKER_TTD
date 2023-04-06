from flask import Flask,jsonify
from flask_restx import Resource,Api

#instantiate the APP

app = Flask(__name__)

api = Api(app)

# set config
app.config.from_object('src.config.DevelopmentConfig')  # new

class ping(Resource):
    def get(self):
        return {
            'successs' : 'success',
            'ping' : 'soorya pong'
        }

api.add_resource(ping,'/ping')

#Note we have to set 2 environmental variables.
#$env:FLASK_ENV = "1"
#$env:FLASK_APP=src/__init__.py
#python manage.py run