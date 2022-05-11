from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class= Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Creating the app ct(config_options[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']='qwerty'

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    # Will add the views and forms
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    return app

    from app import views, errors