from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Logo(db.Model):
    __tablename__ = 'logos'
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(255), nullable=False)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(255), nullable=False)

class Name(db.Model):
    __tablename__ = 'names'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    intro = db.Column(db.Text, nullable=False)

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    image_filename = db.Column(db.String(255), nullable=False)
    grid_position = db.Column(db.String(50), nullable=False)
    project_type = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(255), nullable=True)
    term = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    link = db.Column(db.String(255), nullable=True)

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    image_filename = db.Column(db.String(255), nullable=False)
    image_description = db.Column(db.Text, nullable=True)
