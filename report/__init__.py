from flask import Flask,request, jsonify, abort
from config import app_config

def service(env_name):
    app = Flask('report-service') # instace flask
    app.config.from_object(app_config[env_name]) # settings app

    @app.route('/',methods=['GET'])
    def index():
        """
        route / to info service
        """
        info = {
            'title': 'Report Service',
            'version': '1.0.0'
        }
        response = jsonify(info)
        response.status_code = 200
        return response

    return app
