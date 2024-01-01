#!/usr/bin/python3
"""Flask app that displays all cities of a state
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext(teardown_storage)
def teardown_storage(self):
    """Tear down storage session after each request"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays cities of every state"""
    cities = storage.all(City)
    return render_template('8-cities_by_states.html', cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
