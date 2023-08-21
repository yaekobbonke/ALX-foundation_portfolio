from flask_login import UserMixin

class User (UserMixin, db.model):
    __tablename__ == 'users'
