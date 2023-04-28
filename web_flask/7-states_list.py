#!/usr/bin/python3
""" A script that starts a flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy session."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    """ Displays an HTML page with a list of all States"""
    data = storage.all(State)
    return render_template("7-states_list.html", states=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
