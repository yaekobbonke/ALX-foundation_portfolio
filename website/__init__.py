from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy

"""
creates flask application
"""

db = SQLAlchemy()
def create_app():
    """creates app"""
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'yaibhbhs8385qjd'
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://jackmanSoftware:password@jackmanS1@localhost/portfolio_project'

    #initializes database extension
    db.init_app(app)
    #
    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        """retreves the user object based on the user_id"""
        return User.query.get(user_id)
    

    from .main import main_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    return app

