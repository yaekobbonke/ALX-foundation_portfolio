from flask import Blueprint, render_template, request, redirect, url_for, flash
from website import db
from .models import Blog


main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def home():
    """displays landing page of the website"
    return render_template("base.html")

@main_bp.route("/create", methods=['GET', 'POST'])
def create():
    ""enables owner of this website create new blog""
    if request.method == 'POST':
        # Get the form data
        title = request.form['title']
        content = request.form['content']

        # Create a new blog post
        new_post = Blog(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        flash("Blog created successfully", 'success')
        return redirect("/blog")  # Redirect to the blog page after creating the post

    return render_template('create_blog.html')
@main_bp.route("/blog")
def blog(): 
    ""enables users access blog post""
    blog_posts = Blog.query.all()    
    return render_template('blog.html', blog_posts=blog_posts)

@main_bp.route("/contacts")
def contacts():
    """displays contact addresses of the owner"
    return render_template("contacts.html")
