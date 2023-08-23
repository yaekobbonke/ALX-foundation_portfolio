from website import db

#creates db object from SQLAlchemy class

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

def create_all_tables():
    with db.app.app_context():
        db.create_all()
