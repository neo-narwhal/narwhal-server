from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required
from flask_restplus import Api, Resource

blueprint = Blueprint('helloworld', __name__)
api = Api(blueprint)


@api.route('/helloworld')
class helloworld(Resource):
    def get(self):
        return Response('Hello World', status=200)


@api.route('/helloworld/jwt')
class helloworld(Resource):
    @jwt_required
    def get(self):
        return Response('Hello JWT!', status=200)
