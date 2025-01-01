from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Experience(db.Model):
    __tablename__ = 'experiences'

    id = db.Column(db.Integer, primary_key=True)
    experience_type = db.Column(db.String(50))
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(200))
    short_description = db.Column(db.Text)
    long_description = db.Column(db.Text)
    main_link = db.Column(db.String(200))
    main_image = db.Column(db.String(200))
    tile_size = db.Column(db.String(10))
    tags = db.Column(db.Text)

    def __repr__(self):
        return f'<Experience {self.title}>'
