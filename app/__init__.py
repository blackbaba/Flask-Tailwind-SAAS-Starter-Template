from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
from flask_login import LoginManager
from flask_pagedown import PageDown

from config import config

mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
assets = Environment()
pagedown = PageDown()

# Setup JS and CSS Assets Bundles
js = Bundle('src/js/index.js', filters='jsmin',
            output='dist/js/app.%(version)s.js')
css = Bundle('src/css/index.css', filters='cssmin',
             output='dist/css/app.%(version)s.css')
assets.register('js_all', js)
assets.register('main_css', css)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.debug = True
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    assets.init_app(app)
    pagedown.init_app(app)

    # Import Blueprints
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .api import api as api_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
