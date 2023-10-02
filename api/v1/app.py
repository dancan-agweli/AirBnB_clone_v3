#!/usr/bin/python3
"""Building first API"""

from flask import Flask
from models import storage
from api.v1.views import app_views


"""Initialize a Flask instance"""
app = Flask(__name__)

"""Register blueprint"""
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True)
