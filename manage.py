import os
import subprocess

from flask_migrate import Migrate, MigrateCommand
from flask_script import Server, Manager, Shell
from redis import Redis

from app import create_app, db
from app.model import User

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
server = Server(host="0.0.0.0", port=65501)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command('runserver', server)

manager.add_command('db', MigrateCommand)

@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py app/'
    yapf = 'yapf -r -i *.py app/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


if __name__ == '__main__':
    manager.run()
