from flask import Blueprint, Response, request, jsonify
from flask_restplus import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_claims
import json

from sqlalchemy import and_

from app import db, docker_manager
from app.model.project import Project

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
            project = Project.query.filter(and_(Project.user_id == user_id, Project.name == name)).first()
            if not project:
                description = request.form['description']
                image_tag = request.form['imageTag']
                cpu = request.form['cpu']
                memory = request.form['memory']
                storage = request.form['storage']
                is_custom = request.form['isCustom']

                project = Project(user_id=user_id, name=name, description=description,
                                  image_tag=image_tag, cpu=cpu,
                                  memory=memory, storage=storage, is_custom=is_custom)
                db.session.add(project)
                db.session.flush()
                port = project.id+2000
                container_name = docker_manager.create_container(mem=memory, cpu=cpu, os_name=image_tag, open_port=port)

                project.container_name = container_name

                db.session.commit()

                return Response('', status=201)
            else:
                return Response('', status=409)
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
            project = Project.query.filter(and_(Project.id == id, Project.user_id == user_id)).first()
            if project:
                db.session.delete(project)
                db.session.commit()
                if docker_manager.rm_container(project.container_name):
                    return Response('', status=200)
                else:
                    return Response('', status=404)
            else:
                return Response('', status=404)
        except Exception as e:
            print(e)
            return Response('', status=400)
