from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
#from . import load_user

"""creates Blueprint for authentication"""
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("dashboard")
@login_required
def dashboard():
    """displays the profile/dashboard of user after successful loggingin"""
    usename = current_user.username
    return render_template('dashboard.html', username = usename)


auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """allows user to login"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.username == password:
            # searches the provided username in the database
            login_user()
            return redirect (url_for('dashboard'))
        else:
            return f"user doesn't exist"
    return "login.html"


auth_bp.route("/register", method=["GET", "POST"])
def register():
    """signs up new user"""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username = username).first()
        if user and user.username == password:
            flash("user already exists")
            redirect(url_for("login"))
        else:
            return f"successfully registered"
    return "register.html"

auth_bp.route("/logout")
@login_required
def logout():
    """used to logout active user"""
    logout_user()
    return redirect(url_for("/"))
