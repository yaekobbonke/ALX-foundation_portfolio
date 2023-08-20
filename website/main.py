from flask import Blueprint, render_template

main_bp = Blueprint("main_bp", __name__)

main_bp.route("/")
def home():
    return "welcome to home"

main_bp.route("/about")
def about():
    return "welcome to about page"
