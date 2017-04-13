from flask import Flask
from app.pages import pages


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.cfg', silent=True)
    app.config.from_object('config.production')

    app.register_blueprint(pages)

    return app
