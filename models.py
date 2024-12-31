# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Logo(db.Model):
    __tablename__ = 'logos'
    
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(100), nullable=False)
    # Removed the 'text' field as per previous updates

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
    project_type = db.Column(db.String(20), nullable=False)  # New field: 'Project' or 'Experience'
    position = db.Column(db.String(100), nullable=True)
    term = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    link = db.Column(db.String(200), nullable=True)
    
    images = db.relationship('Image', back_populates='project', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'<Project {self.title} ({self.project_type})>'

class Image(db.Model):
    __tablename__ = 'images'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    image_filename = db.Column(db.String(100), nullable=False)
    
    project = db.relationship('Project', back_populates='images')

    def __repr__(self):
        return f'<Image {self.image_filename} for Project ID {self.project_id}>'

class Name(db.Model):
    __tablename__ = 'names'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(255), nullable=False)  # One sentence intro

    def __repr__(self):
        return f'<Name {self.full_name}>'
