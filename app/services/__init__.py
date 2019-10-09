import json
import os

from flask import Blueprint, Response, request
from flask_restplus import Api, Resource

from app import db
from app.model import User

blueprint = Blueprint('services', __name__)
api = Api(blueprint)


@api.route('')
class AvailableServices(Resource):
    def get(self):
        with open('app/static/available_services.json') as f:
            response = Response(f.read(), status=200)
        return response
