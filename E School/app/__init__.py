from flask import Flask
from config import Config
from app.extensions import db,bcrypt , migrate ,login_manager


def create_app():
    app =Flask(__name__)

    # Load Configuration 
    app.config.from_object(Config)

    # Intialize Flask extention 
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    from app.blueprints.auth import auth
    from app import models
    app.register_blueprint(auth)
    from app.blueprints.software_admin import software_admin
    app.register_blueprint(software_admin)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"
    return app
