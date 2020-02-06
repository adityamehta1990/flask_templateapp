## Setup

`pip install requirements.txt`

1. Webframework: Flask
2. Database: SQLALchemy and Alembic (using Flask-Migrate)
3. Admin, security: Flask-Admin, Flask-Login

### Webframework

Flask app is created in `templateapp\web\app` with settings in `.flaskenv` and `.env`

### Database

SQLAlchemy models go in `templateapp\models` . Database migrations go in `templateapp\migrations`
Views go in `templateapp\web\views`