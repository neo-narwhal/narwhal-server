from flask import Blueprint, Response
from flask_restplus import Api, Resource


blueprint = Blueprint('services', __name__)
api = Api(blueprint)


@api.route('')
class AvailableServices(Resource):
    def get(self):
        with open('app/docker/manifest.json') as f:
            response = Response(f.read(), status=200)
        return response
