from flask import Blueprint, Response, request, jsonify, send_file
from flask_restplus import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_claims
import time

from flask_restplus.inputs import boolean

from sqlalchemy import and_

from app import db, docker_manager
from app.model.project import Project

import time

blueprint = Blueprint('container', __name__)
api = Api(blueprint)
BASE_PATH = '/Users/yaoandy107/narwhal/uplaod'


@api.route('/<id>')
class Container(Resource):

    def get(self, id):
        time.sleep(2)
        return send_file('./container.tar', as_attachment=True)
