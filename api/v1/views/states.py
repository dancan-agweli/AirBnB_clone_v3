#!/usr/bin/python3
"""states.py"""

from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(states)


@app_views.route('/states/<string:state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200  # Return an empty dictionary with status code 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a new State object"""
    request_data = request.json  # Use request.json to get JSON data
    if not request_data:
        abort(400, "Not a JSON")
    if 'name' not in request_data:
        abort(400, "Missing name")
    
    state = State(**request_data)
    storage.new(state)
    storage.save()
    
    return jsonify(state.to_dict()), 201  # Return the new State with status code 201


@app_views.route('/states/<string:state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    
    request_data = request.json  # Use request.json to get JSON data
    if not request_data:
        abort(400, "Not a JSON")
    
    # Update the State object with all key-value pairs from the request data
    for key, value in request_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    
    storage.save()
    
    return jsonify(state.to_dict()), 200  """ Return the updated State with status code 200"""




