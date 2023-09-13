from website import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """user model"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=True)

    def __init__(self, username, email, password):
        """constructor of user class"""
        self.username = username
        self.email = email
        self.password = password


class Blog(db.Model):
    """creates blog model to create blog post"""
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.String(30), nullable=False, default=datetime.utcnow())

    def __init__(self, title, content):
        self.title = title
        self.content = content
