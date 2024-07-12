# app/__init__.py
from flask import Flask
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///life_guide_game.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
