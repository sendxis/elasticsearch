from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api import Card, Sms, Info, Analytics
import os
# when run this script on platform.sh, use platformshconfig module to get default server configuration.
# when run this script on local, following line is not needed.
from platformshconfig import Config
config = Config()

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Card, '/carte')
api.add_resource(Info, '/info')
api.add_resource(Sms, '/sms')
api.add_resource(Analytics, '/analytics')

# when run this script on local, please remove parameters of a function "run" like app.run()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(config.port))
