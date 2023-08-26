from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from .models import User
from .models import Blog


#from . import load_user

"""creates Blueprint for authentication"""
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/dashboard")
@login_required
def dashboard():
    """displays the profile/dashboard of user after successful loggingin"""
    user = current_user
    return render_template('dashboard.html', user = user)
#login view
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """allows user to login"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            # searches the provided username in the database and 
            login_user(user)
            return redirect (url_for('dashboard'))
        else:
            return "user doesn't exist"
    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Registers up new user"""
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        
        if password1 != password2:
            flash('password doesnt match')

        user = User.query.filter_by(email=email).first()
        if user:
            
            flash("Email already exists.", category='error')
            redirect(url_for("auth.login"))
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
            flash('User added successfully')
            
    return render_template("register.html")

@auth_bp.route("/logout")
@login_required
def logout():
    """used to logout active user"""
    logout_user()
    return redirect(url_for("/"))