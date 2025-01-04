from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/search_filter')
def search_filter():
    return render_template('search_filter.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

if __name__ == '__main__':
    app.run(debug=True)
