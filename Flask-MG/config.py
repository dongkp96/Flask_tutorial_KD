import os

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY') or "hard-coded-key"

"""
Configuration variable is defined as a class variable inside the Config class
If more configuration variables is needed, more can be added to this
"""