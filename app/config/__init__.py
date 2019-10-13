import os

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.getenv('SECRET_KEY', 'Let Narwhal great again!')

class Config:
    DEBUG = False
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://yaoandy107:123qwe@localhost/narwhal'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SERVER_NAME = 'narwhal.ntut.club'

config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
