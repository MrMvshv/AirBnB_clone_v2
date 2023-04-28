#!/usr/bin/python3
"""Starts a Flask web app.
The applistens on 0.0.0.0, port 5000.
Routes:
    /states_list: Displays a HTML page
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and their cities.
    States/cities are sorted by name.
    """
    data = storage.all(State)
    return render_template("8-cities_by_states.html", data=data)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
