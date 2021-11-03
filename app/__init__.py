from flask_sqlalchemy import SQLAlchemy
from .main import main as main_blueprint
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
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)
    
    # Will add the views and forms

    return app