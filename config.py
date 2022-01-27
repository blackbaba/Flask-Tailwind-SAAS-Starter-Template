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
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POST_MAX_LENGTH = 280
    FLASKY_POSTS_PER_PAGE = 100
    FLASKY_COMMENTS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 10
    FLASKY_MAX_FOLLOWERS = 1000
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_SLOW_DB_QUERY_TIME = 0.1
    AUTH_TOKEN_EXPIRY = 3600
    ASSETS_AUTO_BUILD = True
    ASSETS_DEBUG = True
    CACHE_NO_NULL_WARNING = True  # Supress warnings when cache set to null
    CACHE_TYPE = 'NullCache'  # SimpleCache, RedisCache
    # CACHE_REDIS_URL = 'redis://127.0.0.1:6379'
    CACHE_DEFAULT_TIMEOUT = 60  # seconds

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(Config):
    ASSETS_AUTO_BUILD = True
    ASSETS_DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # Logging
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


# UNI File Logs
class UnixConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)
        # log to stderr
        import logging
        from logging.handlers import RotatingFileHandler
        logs_path = os.path.join(BASEDIR, 'logs', 'flasky.log')
        file_handler = RotatingFileHandler(
            logs_path, maxBytes=10000, backupCount=5)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


# UNI Sys logs
class UnixConfig2(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

      # log to syslog
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)


class RenderConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)
        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)
        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'render': RenderConfig,
    'unix': UnixConfig,
    'unix2': UnixConfig2,
    'docker': DockerConfig,
    'default': DevelopmentConfig
}

# postgresql://username:password@hostname/database
# sqlite:////absolute/path/to/database (Unix)
# sqlite:///c:/absolute/path/to/database (Windows)
