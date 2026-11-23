"""
This file serves as the routes file containing the view functions for the application
"""

from app import app
#imports the app variable containing the Flask instance from __init__.py
from flask import render_template


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

