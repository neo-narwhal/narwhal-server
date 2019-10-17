from flask import Blueprint, Response, request, jsonify, send_file
from flask_restplus import Api, Resource

import time

blueprint = Blueprint('container', __name__)
api = Api(blueprint)
BASE_PATH = '/Users/yaoandy107/narwhal/uplaod'


@api.route('/<id>')
class Container(Resource):

    def get(self, id):
        time.sleep(2)
        return send_file('./container/container.tar', as_attachment=True)
