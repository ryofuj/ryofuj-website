from flask import Flask, render_template
from models import db, Logo, Profile, Name, Project

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
