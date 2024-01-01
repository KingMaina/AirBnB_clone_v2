#!/usr/bin/python3
"""Flask app that diplays state information on request
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__main__)


@app.teardown_appcontext(teardown_session)
def teardown_session(exc):
    """Removes the user database session"""
    storage.close()


@app.route("/hbnb_filters")
def hbnb_filters():
    """Display states in a filters section on the website"""
    states = storage.all(State)
    return render_template('10-hbnb_filters.html', strict_slashes=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
