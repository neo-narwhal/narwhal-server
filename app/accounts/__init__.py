from flask import Blueprint, Response, jsonify, make_response, request
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_restplus import Api, Resource

from app import db
from app.model.user import User
from sqlalchemy import or_

from app import ph

blueprint = Blueprint('accounts', __name__)
api = Api(blueprint)


# 登入
@api.route('/login')
class Login(Resource):
    def post(self):
        email = request.form['email']
        password = request.form['password']

        user = User.query.\
            filter(User.email == email).first()
        if user.check_password(password):
            access_token = create_access_token(identity=user.id)
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
        hashed_password = ph.hash(password)

        user = User.query.\
            filter(or_(User.email == email, User.username == username)).first()

        if not user:
            new_user = User(
                email=email, password=hashed_password, username=username, level=0)
            db.session.add(new_user)
            db.session.commit()

            return Response('', status=201)
        else:
            return Response('', status=409)

