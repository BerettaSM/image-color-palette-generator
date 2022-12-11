import secrets
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(32)

    from .views import views
    app.register_blueprint(views)

    return app
