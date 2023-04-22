#!/usr/bin/python3
"""
This script starts a Flask web app
Listening on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Displays Hello HBNB."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Displays HBNB."""
    return 'HBNB'


@app.route('/c/<text>')
def Ctext(text):
    """Displays C text"""
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def Ptext(text):
    """Displays text"""
    text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>')
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
