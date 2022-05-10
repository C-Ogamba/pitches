from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
# migrate = Migrate(app, db)

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Will add the views and forms

    return app