import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from models import db, Project

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

# Configure the database (SQLite file named database.db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB and CORS
db.init_app(app)
CORS(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

# Serve React build (production mode)
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# If you're handling sub-routes like /about or /projects in React (client-side), 
# you can add a fallback route to always serve index.html:
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

# -------------------
# API ROUTES
# -------------------

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Return a list of all projects."""
    projects = Project.query.all()
    return jsonify([p.to_dict() for p in projects])

@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Return a single project by ID."""
    project = Project.query.get_or_404(project_id)
    return jsonify(project.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
