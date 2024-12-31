# app.py

from flask import Flask, render_template
from models import db, Logo, Profile, Project, Name
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    logo = Logo.query.first()
    profile = Profile.query.first()
    projects = Project.query.all()
    name = Name.query.first()
    return render_template('index.html', logo=logo, profile=profile, projects=projects, name=name)

if __name__ == '__main__':
    app.run(debug=True)
