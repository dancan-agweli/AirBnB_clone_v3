#!/usr/bin/python3
"""
creates a status route
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def ststus():
    """returns a json """
    return jsonify({"status": "OK"})
