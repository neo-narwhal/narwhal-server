from flask import Blueprint, Response, request, jsonify
from flask_restplus import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_claims
import json

from werkzeug.utils import secure_filename

from app.utils.zip_util import unzip
from app.model.project import Project as ProjectModel
from app.utils.docker_util import get_dockerfile
from app import client
import os

blueprint = Blueprint('projects', __name__)
api = Api(blueprint)
BASE_PATH = '/Users/yaoandy107/narwhal/uplaod'


@api.route('')
class Project(Resource):
    @jwt_required
    def get(self):
        claims = get_jwt_claims()
        user_id = claims['user_id']
        projects = ProjectModel.query. \
            filter(ProjectModel.user_id == user_id).all()
        data = []
        for project in projects:
            data.append({
                'id': project.id,
                'name': project.name,
                'port': project.port
            })
        return Response(json.dumps(data), status=200)

    @jwt_required
    def post(self):
        claims = get_jwt_claims()
        user_id = claims['user_id']

        name = request.form['name']
        port = request.form['port']
        project_type = request.form['type']
        file = request.files['file']

        if file:
            secure_filename(file.filename)

            project_path = '{}/{}/{}'.format(BASE_PATH, user_id, name)
            zip_path = '{}/{}'.format(project_path, file.filename)

            if not os.path.isdir(project_path):
                os.makedirs(project_path)
            file.save(zip_path)

            unzip(zip_path)

            dockerfile = get_dockerfile(type=project_type)
            with open('{}/Dockerfile'.format(project_path), 'w') as f:
                f.write(dockerfile)
            image, err = client.build(path='{}/'.format(project_path), target='{}/{}'.format(user_id, name))
            print(image)
            print(err)
            return Response('', status=200)
        else:
            print('No file')
            return Response('', status=400)


@api.route('/<id>')
class TheProject(Resource):
    @jwt_required
    def get(self, id):
        pass

    @jwt_required
    def put(self, id):
        pass

    @jwt_required
    def delete(self, id):
        pass
