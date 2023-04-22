#!/usr/bin/python3
"""
This script starts a Flask web app
Listening on 0.0.0.0:5000

Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
        - Displays the value of <n> in the body.
    /number_odd_or_even/<n>: Displays an HTML page only if <n> is an integer.
        - States whether <n> is even or odd in the body.
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


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
    """Displays 'n is a number' only if <n> is an integer."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_t(n):
    """Displays a HTML page only if <n> is an integer.

    Displays the value of <n> in the body.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_o(n):
    """Displays a HTML page only if <n> is an integer.

    States whether <n> is odd or even in the body.
    """
    if n % 2 != 0:
        txt = 'odd'
    else:
        txt = 'even'
    return render_template('6-number_odd_or_even.html', n=n, txt=txt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
