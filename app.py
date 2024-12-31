# app.py

from flask import Flask, render_template
from models import db, Logo, Profile, Name, Project, Image

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

@app.route('/')
def index():
    logo = Logo.query.first()
    profile = Profile.query.first()
    name = Name.query.first()
    projects = Project.query.all()
    return render_template('index.html', logo=logo, profile=profile, name=name, projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
