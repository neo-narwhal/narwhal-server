from flask import Blueprint, request, Response
from flask_restplus import Api, Resource
import json
import os

from app import db
from app.model import User

blueprint = Blueprint('services', __name__)
api = Api(blueprint)


@api.route('/')
class AvailableServices(Resource):
    def get(self):
        with open('app/config/config.json') as f:
            data = json.loads(f.read())['availableService']
            response = Response(json.dumps(data), status=200)
        return response
