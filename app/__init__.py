from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
# migrate = Migrate(app, db)

def create_app(config_class= Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Creating the app ct(config_options[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']='qwerty'

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Will add the views and forms

    return app