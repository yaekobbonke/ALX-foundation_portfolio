from flask import Flask
#from website.models import User
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
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://jackmanSoftware:password@jackmanS1@localhost/portfolio_project'

    #initializes database extension
    db.init_app(app)
    #creating an instance of the LoginManager class
    login_manager = LoginManager(app)
    #Associating it with my flask app
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        """retreves the user object based on the user_id"""
        return User.query.get(int(user_id))
    

    from .main import main_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    return app

