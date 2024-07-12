import os
from dotenv import load_dotenv
from flask import Flask
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] =  os.getenv('SECRET_KEY')
    app.config['BABEL_DEFAULT_LOCALE'] =  os.getenv('BABEL_DEFAULT_LOCALE')
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.getenv('BABEL_TRANSLATION_DIRECTORIES')

    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        return requests.accept_languages.best_match(['en', 'de', 'ar'])

    @app.context_processor
    def inject_get_locale():
        return dict(get_locale=get_locale)

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app