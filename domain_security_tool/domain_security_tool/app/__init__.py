
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from celery import Celery

db = SQLAlchemy()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    celery.conf.update(app.config)

    from app import routes
    app.register_blueprint(routes.bp)

    return app
