from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(300), nullable=True)  # We can keep this for a main/thumbnail image

    # Relationship to project images (optional convenience relationship)
    images = db.relationship('ProjectImage', backref='project', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image_url": self.image_url,
            # Convert related images to dict
            "images": [img.to_dict() for img in self.images]
        }

class ProjectImage(db.Model):
    __tablename__ = 'project_images'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "image_url": self.image_url
        }
