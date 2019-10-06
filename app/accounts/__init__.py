import json

from flask import Blueprint, Response, jsonify, make_response, request
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_restplus import Api, Resource

from app import db
from app.model.user import User

blueprint = Blueprint('accounts', __name__)
api = Api(blueprint)


# 登入
@api.route('/login')
class Login(Resource):
    def post(self):
        email = request.form['email']
        password = request.form['password']
        user = User.query.\
            filter(User.email == email).\
            filter(User.password == password).first()
        if user:
            access_token = create_access_token(identity=email)
            return make_response(jsonify(access_token=access_token), 200)
        else:
            return Response('', status=401)


# 註冊
@api.route('/register', methods=['POST'])
class Register(Resource):
    def post(self):
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        user = User.query.\
            filter(User.email == email).first()
        if not user:
            try:
                new_user = User(email=email,
                                password=password,
                                username=username,
                                level=0)
                db.session.add(new_user)
                db.session.commit()
            except Exception as err:
                print(err)
                return Response('', status=500)
            else:
                return Response('', status=201)
        else:
            return Response('', status=409)
