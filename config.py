import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):


    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bnm'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or\
        'sqlite:///' + os.path.join(basedir, 'app.db')
    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}