from flask import Blueprint, render_template

# Create a Blueprint
project1 = Blueprint('project1', __name__, template_folder='templates', static_folder='static')

@project1.route('/')
def index():
    return render_template('index.html')
