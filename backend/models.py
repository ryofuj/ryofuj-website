from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import JSON  # Import JSON type

db = SQLAlchemy()

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    term = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(300), nullable=True)
    images = db.Column(JSON, nullable=True)  # Use JSON type for list of images
    role = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(300), nullable=True)
    model_url = db.Column(db.String(300), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "company": self.company,
            "title": self.title,
            "term": self.term,
            "image_url": self.image_url,
            "images": self.images,
            "role": self.role,
            "description": self.description,
            "link": self.link,
            "model_url": self.model_url
        }
