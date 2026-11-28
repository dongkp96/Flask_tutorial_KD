from flask import Flask
from config import Config
#style of import = package is lowercase, class is uppercase

app = Flask(__name__)
#defines instance of the Flask class from Flask
#Since defined here, it is a member of the app package

app.config.from_object(Config)



from app import routes
#route imported at the bottom to avoid circular imports related to Flask applications