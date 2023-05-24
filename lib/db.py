from flask_sqlalchemy import flask_sqlalchemy
from flask_migrate import Migrate

db = SQLAlchemy()

import lib.models

def init_db(app):
    db.init_app(app)
    Migrate(app, db)