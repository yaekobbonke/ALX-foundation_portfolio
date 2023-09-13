from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from website import db
from .models import Blog
from datetime import datetime

# from . import load_user

"""creates Blueprint for authentication"""
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/dashboard")
@login_required
def dashboard():
    """displays the profile/dashboard of user after successful loggingin"""
    user = current_user
    day = datetime.now().strftime('%A')
    formated_date =  datetime.now().strftime('%Y')
    return render_template('dashboard.html', user=user,day=day, formated_date=formated_date)
# login view

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    ""user login view""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('You are logged in successfully', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('auth.login'))
    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if password1 != password2:
            flash('Passwords do not match', 'error')
            return redirect(url_for('auth.register'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', 'error')
            return redirect(url_for("auth.register"))
        else:

            new_user = User(
                username=username,
                email=email,
                password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash("User registered successfully!", 'success')
            return redirect(url_for('auth.login'))
            
    return render_template("register.html")


@auth_bp.route("/logout")
@login_required
def logout():
    """used to logout active user"""
    logout_user()
    return redirect(url_for("auth.login"))
