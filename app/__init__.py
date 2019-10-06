import os

from flask import Flask
from flask_assets import Environment
from flask_compress import Compress
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
compress = Compress()


def create_app():
    app = Flask(__name__)

    # not using sqlalchemy event system, hence disabling it
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://yaoandy107:123qwe@localhost/narwhal'
    app.config['DEBUG'] = True
    app.config['JWT_SECRET_KEY'] = 'Let\'s Narwhal great again!'

    # Set up extensions
    db.init_app(app)
    compress.init_app(app)
    jwt = JWTManager(app)

    # Create app blueprints
    from .helloworld import blueprint as helloworld_api
    app.register_blueprint(helloworld_api, url_prefix='/api')

    from .accounts import blueprint as account_blueprint
    app.register_blueprint(account_blueprint, url_prefix='/api')

    from .projects import blueprint as project_api
    app.register_blueprint(project_api, url_prefix='/api/projects')

    from .services import blueprint as service_api
    app.register_blueprint(service_api, url_prefix='/api/services')

    return app
