from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
import app as app, json
from config import Config
from flask_cors import CORS
from flask_mqtt import Mqtt
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

# instantiate Flask functionality
app = Flask(__name__)

# set sqlalchemy URI in application config


db = SQLAlchemy()  # instance of SQL
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    from app.views import views_bp

    app.register_blueprint(views_bp, url_prefix="/")
    from app.api import api_bp

    app.register_blueprint(api_bp)

    return app
