# app.py - a minimal flask api using flask_restful
from flask import Flask, request
from flask_restplus import Resource, Api, fields, Namespace
from datetime import datetime

app = Flask(__name__)
api = Api(app, 
    version='1.0.0',
    title='Python API: Flask, swagger',
    description='This is sample project to host Flask with swagger',
    validate=True)

from endpoints.date_api import *

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, host='0.0.0.0')