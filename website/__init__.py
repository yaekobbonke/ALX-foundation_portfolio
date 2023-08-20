from flask import Flask
"""
creates flask application
"""
def create_app():
    """creates app"""
    app = Flask(__name__)
    return app

from . import main_bp
from . import auth_bp

app.register_blueprint("main_bp")
app.register_blueprint("auth_bp")
