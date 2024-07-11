from flask import Flask
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///life_guide_game.db'
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

    db.init_app(app)
    babel.init_app(app)

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
