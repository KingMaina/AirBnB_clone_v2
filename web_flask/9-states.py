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


@app.route("/states")
def get_states():
    """Display states"""
    states = storage.all('State')


@app.route("/states/<id>")
def get_cities_of_a_state(id):
    """Display states and the cities in each"""
    states = storage.all('State')
    searched_state = {}
    for state in states:
        if state.id == id:
            searched_state = state
    cities = storage.all('City')
    state_cities = []
    for city in cities:
        if city.state_id == id:
            state_cities.append(city)
    return render_template('9-states.html', cities=state_cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
