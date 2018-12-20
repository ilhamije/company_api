""" app factory file """
# import logging
# import logging.config
# import json

from flask import Flask
# from celery import Celery

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import SQLALCHEMY_DATABASE_URI
# from flask_marshmallow import Marshmallow
from models import db


def make_app():
    """ create app object """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # from .models import db
    db.init_app(app)
    # db = SQLAlchemy(app)
    # ma = Marshmallow(app)

    migrate = Migrate(app, db, compare_type=True)

    # logging.basicConfig()
    # with open("logging.json", "r") as lc:
    #     logging.config.dictConfig(json.load(lc))

    from .blueprints.companylist import api
    app.register_blueprint(api)

    return app


def Session():
    engine = db.create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=50)
    return db.scoped_session(db.sessionmaker(bind=engine))
