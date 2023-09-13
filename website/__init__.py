from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

"""
creates flask application
"""

db = SQLAlchemy()

def create_app():
    """creates app"""
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'yaibhbhs8385qjd'
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://portfolio:Portfolio1#@localhost/my_portfolio'


    db.init_app(app)
    login_manager = LoginManager(app)
    login_manager.init_app(app)
 
    from .models import User   


    @login_manager.user_loader
    def load_user(user_id):
        """retreves the user object based on the user_id"""
        return User.query.get(user_id)
    
    from .main import main_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        """creates tables within application context"""
        db.create_all()
    return app
