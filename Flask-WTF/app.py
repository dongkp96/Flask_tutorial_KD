from flask import (Flask, render_template, redirect, flash, request, url_for, render_template_string)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "dev-only-change-me"

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign in")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods =["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        return render_template("login_info.html", title="Login Info", 
                               username = username,
                               password = password,
                               remember_me = remember_me)
    return render_template("login.html", title ="Sign in", form=form)


if __name__ == "__main__":
    app.run(debug=True)