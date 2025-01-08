from flask import Flask, render_template
from models import db, Profile, Experience, Tag, ExperienceType

app = Flask(__name__)

# Configure SQLite (local) database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def create_tables():
    """ 
    Create all tables in the database before the first request.
    This is just a demo approach. In production, you might manage migrations 
    using Flask-Migrate or Alembic. 
    """
    db.create_all()
    seed_data()  # Optional: Insert sample data

def seed_data():
    """
    Insert some initial demo data if the tables are empty.
    You can remove or adjust this function to your liking.
    """
    if not Profile.query.first():
        profile = Profile(
            name="John Doe",
            title="Software Engineer",
            bio="Passionate developer with 10+ years of experience.",
            avatar_url="http://example.com/avatar.jpg"
        )
        db.session.add(profile)
    
    if not ExperienceType.query.first():
        job_type = ExperienceType(name="Job")
        project_type = ExperienceType(name="Project")
        award_type = ExperienceType(name="Award")
        db.session.add_all([job_type, project_type, award_type])

    if not Tag.query.first():
        t1 = Tag(name="Python")
        t2 = Tag(name="Flask")
        t3 = Tag(name="Web Dev")
        db.session.add_all([t1, t2, t3])

    # If no experiences exist, add some
    if not Experience.query.first():
        experience1 = Experience(
            experience_type=ExperienceType.query.filter_by(name="Project").first(),
            title="Personal Portfolio",
            subtitle="Flask + SQLAlchemy Project",
            short_description="A personal website showcasing my projects and experiences.",
            long_description="Built using Flask, SQLAlchemy, and a custom CSS layout. Deployed on Heroku/AWS/GCP.",
            main_link="http://example.com/my-portfolio",
            main_image="http://example.com/image.jpg",
            tile_size="2x1",
        )
        # Add tags: let's assume "Flask" and "Web Dev" exist
        flask_tag = Tag.query.filter_by(name="Flask").first()
        webdev_tag = Tag.query.filter_by(name="Web Dev").first()
        if flask_tag: experience1.tags.append(flask_tag)
        if webdev_tag: experience1.tags.append(webdev_tag)

        db.session.add(experience1)

    db.session.commit()

@app.route('/')
def home():
    """
    Example route rendering some data in a simple way.
    """
    profile = Profile.query.first()
    experiences = Experience.query.all()
    
    return render_template(
        'index.html',
        profile=profile,
        experiences=experiences
    )

if __name__ == '__main__':
    app.run(debug=True)
