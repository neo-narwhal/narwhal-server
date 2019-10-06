import time

from flask import Response
from flask_jwt import JWT, jwt_required

from app.model.user import User


class Auth():
    def error_handler(self, e):
        print(e)

    def authenticate(self, email, password):
        userInfo = User.query.\
            filter(User.email == email).\
            filter(User.password == password).first()
        if (userInfo is None):
            return Response('', status=401)
        else:
            return Response('', status=200)

    def identity(self, payload):
        id = payload['identity']
        return User.query.filter(User.id == id).first()
