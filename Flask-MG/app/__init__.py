from flask import Flask

app = Flask(__name__)
#defines instance of the Flask class from Flask
#Since defined here, it is a member of the app package

from app import routes
#route imported at the bottom to avoid circular imports related to Flask applications