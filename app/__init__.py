""" app factory file """
# import logging
# import logging.config
# import json

from flask import Flask
# from celery import Celery
from models import db
from flask_migrate import Migrate


def make_app(config='config.py'):
    """ create app object """
    app = Flask(__name__)
    app.config.from_pyfile(config)

    from models import db
    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)

    # logging.basicConfig()
    # with open("logging.json", "r") as lc:
    #     logging.config.dictConfig(json.load(lc))

    from .blueprints.companylist import api
    app.register_blueprint(api)

    return app
