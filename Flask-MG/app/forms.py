from flask_wtf import FlaskForm
#imports flask form class base from flask_wtf to extend for LoginForm class

from wtforms import StringField, PasswordField, BooleanField, SubmitField
"""
Imports the classes that represents the field types for the form. 
This is done because Flask-WTF does not provide customized field types
"""

from wtforms.validators import DataRequired
#imports validator for datarequired = ensures field is not empty

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember me')
    submission = SubmitField("Sign in")

    