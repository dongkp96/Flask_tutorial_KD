"""
This file serves as the routes file containing the view functions for the application
"""

from app import app
#imports the app variable containing the Flask instance from __init__.py
from flask import render_template
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    return render_template("login.html", title = "log in", form = form)

