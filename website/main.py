from flask import Blueprint, render_template


main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def home():
    return render_template("base.html")


@main_bp.route("/about")
def about():
    return render_template("about.html")


@main_bp.route("/blog")
def blog():
    return render_template("blog.html")


@main_bp.route("/portfolio")
def portfolio():
    """allows users to visit and see the projects in this website"""
    return render_template("portfolio.html")


@main_bp.route("/services")
def services():
    """allows users to see the services we provide"""
    return render_template("services.html")


@main_bp.route("/contacts")
def contacts():
    return render_template("contacts.html")

@main_bp.route("/login")
def login():
    """ used to login registered user """
    return render_template("login.html")


@main_bp.route("/signup")
def signup():
    """allows new user to register"""
    return render_template("signup.html")
