from flask import Flask
from app.config.config import Config
from app.extensions.extensions import db, migrate


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)


    # importar blueprints
    from app.main.routes.home import home_bp
    from app.main.routes.auth import auth_bp

    # registrar blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
