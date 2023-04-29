#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display a HTML page like 8-index.html from static"""
    return render_template('temp.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
