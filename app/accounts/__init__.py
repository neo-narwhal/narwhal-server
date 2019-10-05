from flask import Blueprint, Response, request
from flask_restplus import Api, Resource

from app import db
from app.model.user import User

blueprint = Blueprint('accounts', __name__)
api = Api(blueprint)


# 登入
@api.route('/login')
class Login(Resource):
    def post(self):
        print(type(User()))
        email = request.form['email']
        password = request.form['password']
        user = User.query.\
                filter(User.email == email).\
                filter(User.password == password).first()
        print(user)
        if user:
            return Response('', status=200)
        else:
            return Response('', status=401)
        



# 註冊
@api.route('/register', methods=['POST'])
class Register(Resource):
    def post(self):
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        user = User(email=email, password=password, username=username, level=0)
        db.session.add(user)
        try:
            db.session.commit()
        except:
            return Response('', status=500)
        else:
            return Response('', status=201)
