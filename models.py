# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Logo(db.Model):
    __tablename__ = 'logos'
    
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(100), nullable=False)
    # Removed the 'text' field
    # text = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Logo {self.image_filename}>'

class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Profile {self.image_filename}>'

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_filename = db.Column(db.String(100), nullable=False)
    grid_position = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

class Name(db.Model):
    __tablename__ = 'names'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(255), nullable=False)  # One sentence intro

    def __repr__(self):
        return f'<Name {self.full_name}>'
