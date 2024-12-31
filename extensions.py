# extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name='Admin', template_mode='bootstrap3')

def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
