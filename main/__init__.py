from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


def create_app():
    # Crée une instance d'application
    app = Flask(__name__, instance_relative_config=True)

    # Charge la configuration qui se trouve config.py
    app.config.from_object('main.config.Config')
    app.logger.debug(app.config.get('SQLALCHEMY_DATABASE_URI'))

    # Autorise les autres applications à l'appeler
    # si l'adresse d'origine commence par http://localhost:3000
    cors = CORS(app, origins=["http://localhost:3000"])

    database = SQLAlchemy(app)
    database.init_app(app)

    from .hello.controller.helloController import bp
    from .logging.loggingController import bp as bp_logging

    #     Blueprints
    app.register_blueprint(bp)
    app.register_blueprint(bp_logging)

    return app
