from flask import Blueprint, Response, request, jsonify
from flask_restplus import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_claims
import json

from sqlalchemy import and_

from app import db
from app.model.project import Project
import os

blueprint = Blueprint('projects', __name__)
api = Api(blueprint)
BASE_PATH = '/Users/yaoandy107/narwhal/uplaod'


@api.route('')
class Projects(Resource):
    @jwt_required
    def get(self):
        claims = get_jwt_claims()
        user_id = claims['user_id']
        projects = Project.query. \
            filter(Project.user_id == user_id).all()
        data = []
        for project in projects:
            data.append(str(project.id))
        return Response(json.dumps(data), status=200)

    @jwt_required
    def post(self):
        try:
            claims = get_jwt_claims()
            user_id = claims['user_id']
            name = request.form['name']
            description = request.form['description']
            image_tag = request.form['imageTag']
            cpu = request.form['cpu']
            memory = request.form['memory']
            storage = request.form['storage']
            is_custom = request.form['isCustom']
            project = Project(user_id=user_id, name=name, description=description, image_tag=image_tag, cpu=cpu,
                              memory=memory, storage=storage, is_custom=is_custom)
            db.session.add(project)
            db.session.commit()
            return Response('', status=201)
        except Exception as e:
            print(e)
            return Response('', status=400)


@api.route('/<id>')
class TheProject(Resource):
    @jwt_required
    def get(self, id):
        claims = get_jwt_claims()
        user_id = claims['user_id']
        project = Project.query.filter(and_(Project.id == id, Project.user_id == user_id)).first()
        if project:
            return Response(json.dumps(project.as_dict()), status=200)
        else:
            return Response('', status=404)

    @jwt_required
    def delete(self, id):
        try:
            claims = get_jwt_claims()
            user_id = claims['user_id']
            Project.query.filter(and_(Project.id == id, Project.user_id == user_id)).delete()
            db.session.commit()
            return Response('', status=200)
        except Exception as e:
            print(e)
            return Response('', status=400)
