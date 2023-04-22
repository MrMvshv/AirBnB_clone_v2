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
#app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Ctext(text):
    """Displays  “C ”, followed by the value of the text variable

    replace underscore _ symbols with a space
    """
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Ptext(text):
    """Displays Python ", followed by the value of the text variable

    replace underscore _ symbols with a space
    """
    text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if <n> is an integer."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_t(n):
    """Displays a HTML page only if n is an integer.

    H1 tag: "Number: n" inside the tag BODY
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_o(n):
    """Displays a HTML page only if <n> is an integer.

    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if n % 2 != 0:
        txt = 'odd'
    else:
        txt = 'even'
    return render_template('6-number_odd_or_even.html', n=n, txt=txt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
