from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options


db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # Initializing flask extensions
    db.init_app(app) 
    # db = SQLAlchemy(app)  

    # Registering the blueprint
    # from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # setting config
    # from .request import configure_request
    # configure_request(app)
    
    # Will add the views and forms

    return app