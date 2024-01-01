#!/usr/bin/python3

"""Flask app with four routes
"""

from flask import Flask, abort, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Hello HBNB route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display C followed by the value of the text variable"""
    text = str(text).replace('_', ' ')
    return "C {}".format(escape(text))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text='is cool'):
    """Displays `Python` followed by the value of text"""
    text = str(text).replace('_', ' ')
    return "Python {}".format(escape(text))


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """Display `n is a number` only if it is an integer"""
    if n.isnumeric():
        return '{} is a number'.format(n)
    else:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    if n.isnumeric():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
