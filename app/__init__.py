"""demo

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__version__ = '0.0.1'
__author__ = 'Jaydon.T.Jin'

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, static_url_path='/seer/static')
    app.config.from_object('config.default')
    app.config.from_object('config.{0}'.format(config_name.lower()))
    app.config['VERSION'] = __version__

    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
