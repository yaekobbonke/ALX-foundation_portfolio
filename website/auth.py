from flask import Blueprint,render_template

"""creates Blueprint for authentication"""
auth_bp = Blueprint("auth", __name__, url_prifix="/")

auth.route("/login", method=[("GET", "POST")])
def login():
    """allows user to login"""
    return "login"

auth_bp.route("/signup" method=[("GET", "POST")])
def signup():
    """signs up new user"""
    return "signup"

auth_bp.route("/logout")
def logout():
    """used to logout active user"""
    return "logout"
