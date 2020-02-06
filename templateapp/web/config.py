import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


# Your App secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

APP_NAME = "Template App"
# APP_ICON = "static/img/logo.jpg"

APP_THEME = os.environ.get('FLASK_ADMIN_SWATCH')
# APP_THEME = "cerulean.css"
