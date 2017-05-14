from flask import Flask
from app.pages import pages


def create_app(config='config.production'):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)
    app.config.from_pyfile('config.cfg', silent=True)

    app.register_blueprint(pages)

    return app
