from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        api = Api(app, version='1.0', description='Movies API', prefix='/api')
        app.config['api'] = api

        from application import routes  # noqa

        return app
