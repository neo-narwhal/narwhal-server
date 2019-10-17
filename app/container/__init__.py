from flask import Blueprint, Response, request, jsonify, send_file
from flask_restplus import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_claims
import json

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

    @jwt_required
    def post(self, id):
        claims = get_jwt_claims()
        user_id = claims['user_id']
        project = Project.query.filter(and_(Project.id == id, Project.user_id == user_id)).first()
        if project:
            return send_file('./ubuntu.tar', as_attachment=True)
        else:
            return Response('', status=404)
