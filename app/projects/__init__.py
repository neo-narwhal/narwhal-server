from flask import Blueprint, request, Response
from flask_restplus import Api, Resource

from app import db
from app.model import User

blueprint = Blueprint('projects', __name__)
api = Api(blueprint)


@api.route('/')
class Projects(Resource):
    def get(self):
        return Response('', status=200)


@api.route('/<id>')
class Project(Resource):
    def get(self, id):
        pass

    def post(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
