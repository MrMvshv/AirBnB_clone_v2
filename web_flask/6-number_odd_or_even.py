#!/usr/bin/python3
"""Starts a Flask web app.
The applistens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_t(text):
    """Displays'C' followed by <text> value.
    Replaces any underscores in <text> with slashes.
    """
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def p_t(text="is cool"):
    """Displays'Python' followed by <text> value.
    Replaces any underscores in <text> with slashes.
    """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Displays “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Displays a HTML page only if n is an integer:
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even(n):
    """display a HTML page only if <n> is an integer
    States whether <n> is odd or even in the body.
    """
    if n % 2 == 0:
        txt = "even"
    else:
        txt = "odd"
    return render_template("6-number_odd_or_even.html", n=n, txt=txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
