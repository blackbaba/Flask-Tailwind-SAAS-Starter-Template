import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in [
    #     'true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flask Tailwind SAAS Template] '
    FLASKY_MAIL_SENDER = 'Admin <flasktailwindsaas@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    ASSETS_AUTO_BUILD = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(Config):
    ASSETS_AUTO_BUILD = False
    ASSETS_DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# postgresql://username:password@hostname/database
# sqlite:////absolute/path/to/database (Unix)
# sqlite:///c:/absolute/path/to/database (Windows)
