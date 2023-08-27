from flask import Flask
#from website.models import User
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

"""
creates flask application
"""

migrate = Migrate() # for database migration
bcrypt = Bcrypt()
db = SQLAlchemy()

def create_app():
    """creates app"""
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'yaibhbhs8385qjd'
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://portfolio:Portfolio1@localhost/my_portfolio'

    #initializes database extension
    db.init_app(app)
    #creating an instance of the LoginManager class
    login_manager = LoginManager(app)
    #Associating it with my flask app
    login_manager.init_app(app)
    bcrypt.init_app(app) # for password hashing
    migrate.init_app(app, db) # initializes the migration tool with the Flask application and the database


    @login_manager.user_loader
    def load_user(user_id):
        """retreves the user object based on the user_id"""
        return User.query.get(int(user_id))
    
    from .main import main_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        """creates tables within application context"""
        db.create_all()

    return app

