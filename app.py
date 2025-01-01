from flask import Flask, render_template, jsonify, request
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    data_file = os.path.join('data', 'experiences.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        experiences_data = json.load(f)
    return render_template('index.html', experiences=experiences_data["experiences"])

@app.route('/api/experiences')
def api_experiences():
    data_file = os.path.join('data', 'experiences.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        experiences_data = json.load(f)
    return jsonify(experiences_data)

if __name__ == '__main__':
    app.run(debug=True)
