from flask import Blueprint, render_template


main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def home():
    return render_template("base.html")
@main_bp.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@main_bp.route("/blog")
def blog():
    return render_template("blog.html")

@main_bp.route("/portfolio")
def portfolio():
    """allows users to visit and see the projects in this website"""
    return render_template("portfolio.html")

@main_bp.route("/contacts")
def contacts():
    return render_template("contacts.html")
