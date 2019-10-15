from flask import Blueprint, Response
from flask_restplus import Api, Resource
from app.model.user import User
from flask_jwt_extended import jwt_required, get_jwt_claims
import json

blueprint = Blueprint('users', __name__)
api = Api(blueprint)


@api.route('')
class Users(Resource):
    @jwt_required
    def get(self):
        claims = get_jwt_claims()
        user_id = claims['user_id']
        user = User.query.filter(User.id == user_id).first()
        data = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'level': user.level
        }
        return Response(json.dumps(data), status=200)
