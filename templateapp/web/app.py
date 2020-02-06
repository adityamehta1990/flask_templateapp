import logging
import socket
from urllib.parse import urlparse

from flask import Flask
from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from werkzeug.middleware import dispatcher

import dash
import dash_html_components as dash_html

from templateapp.web import config, views
from templateapp.models.base import db_session
from templateapp.utils.api import CustomJSONEncoder

admin = Admin(name=config.APP_NAME, template_mode=config.APP_THEME)
csrf = CSRFProtect()
migrate = Migrate()

LOGGER = logging.getLogger(__name__)


def create_app(config_object=None, testing=False, app_name=config.APP_NAME):
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY

    app.config.from_object(config)
    app.config['APP_NAME'] = app_name
    app.config['TESTING'] = testing
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = False
    app.config['SESSION_COOKIE_SAMESITE'] = False

    if config_object:
        app.config.from_mapping(config_object)

    app.json_encoder = CustomJSONEncoder

    csrf.init_app(app)

    db = SQLAlchemy(app)
    migrate.init_app(app, db)

    # from sample_app.web.blueprints import routes
    # app.register_blueprint(routes)

    with app.app_context():
        admin.init_app(app)

        @app.context_processor
        def jinja_globals():
            _globals = {
                'hostname': socket.getfqdn(),
                'navbar_color': 'blue',
            }
            return _globals

        @app.teardown_appcontext
        def shutdown_session(exception=None):  # pylint: disable=unused-argument
            db_session.remove()

    @app.route('/')
    @app.route('/index')
    def index():
        return "Hello, World!"

    dashapp = create_dashapp()
    server = Flask('server')
    server.wsgi_app = dispatcher.DispatcherMiddleware(app, {
        '/dash': dashapp.server
    })

    return server

def create_dashapp():
    dashapp = dash.Dash(
        __name__,
        requests_pathname_prefix='/dash/'
    )
    dashapp.layout = dash_html.Div('Dash app')
    return dashapp
