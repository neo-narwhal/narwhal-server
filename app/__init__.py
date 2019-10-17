import os

from flask import Flask
from flask_compress import Compress
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import config_by_name
from app.docker.docker_manager import DockerManager

from argon2 import PasswordHasher

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
compress = Compress()
docker_manager = DockerManager()
ph = PasswordHasher()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name])

    # Set up extensions
    db.init_app(app)
    compress.init_app(app)
    jwt = JWTManager(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        return {
            'user_id': str(identity)
        }

    # Create app blueprints
    from .helloworld import blueprint as helloworld_api
    app.register_blueprint(helloworld_api, url_prefix='/api')

    from .accounts import blueprint as account_blueprint
    app.register_blueprint(account_blueprint, url_prefix='/api')

    from .projects import blueprint as project_api
    app.register_blueprint(project_api, url_prefix='/api/projects')

    from .services import blueprint as service_api
    app.register_blueprint(service_api, url_prefix='/api/services')

    from .users import blueprint as user_api
    app.register_blueprint(user_api, url_prefix='/api/users')

    from .container import blueprint as container_api
    app.register_blueprint(container_api, url_prefix='/api/container')
    return app
