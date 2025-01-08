from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Junction table for the many-to-many relationship between Experience and Tag
experience_tags = db.Table(
    'experience_tags',
    db.Column('experience_id', db.Integer, db.ForeignKey('experience.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Profile(db.Model):
    """
    Profile table to store personal information about the owner of the website.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100))
    bio = db.Column(db.Text)
    img_path = db.Column(db.String(255))  # updated to match "img_path"

    def __repr__(self):
        return f'<Profile {self.name}>'

class ExperienceType(db.Model):
    """
    ExperienceType table to categorize different experiences, 
    e.g. "Work", "Project", "Leadership", "Publication", etc.
    """
    __tablename__ = 'experience_type'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    experiences = db.relationship("Experience", back_populates="experience_type")

    def __repr__(self):
        return f'<ExperienceType {self.name}>'

class Tag(db.Model):
    """
    Tag table, storing tags like "Python", "Flask", "Web Dev", "AI", etc.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Tag {self.name}>'

class Experience(db.Model):
    """
    Experience table with all requested fields. 
    Uses:
      - ForeignKey to ExperienceType
      - Many-to-many relationship with Tag through experience_tags
    """
    id = db.Column(db.Integer, primary_key=True)
    experience_type_id = db.Column(db.Integer, db.ForeignKey('experience_type.id'), nullable=False)
    
    title = db.Column(db.String(255), nullable=False)
    subtitle = db.Column(db.String(255))
    short_description = db.Column(db.Text)
    long_description = db.Column(db.Text)
    main_link = db.Column(db.String(500))
    main_image = db.Column(db.String(255))
    tile_size = db.Column(db.String(50))  # e.g., "1x1", "2x1", etc.

    experience_type = db.relationship("ExperienceType", back_populates="experiences")
    tags = db.relationship("Tag", secondary=experience_tags, backref="experiences")

    def __repr__(self):
        return f'<Experience {self.title}>'