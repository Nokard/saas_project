from flask import Flask

def create_app():
    app = Flask(__name__)

    # importar blueprints
    from app.main.routes.home import home_bp
    from app.main.routes.auth import auth_bp

    # registrar blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
