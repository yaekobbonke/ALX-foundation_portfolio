from flask import Blueprint, render_template, request, redirect, url_for, flash
from website import db
from .models import Blog


main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def home():
    return render_template("base.html")

@main_bp.route("/create", methods=['GET', 'POST'])
def create():
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
    blog_posts = Blog.query.all()
    
    return render_template('blog.html', blog_posts=blog_posts)

@main_bp.route("/contacts")
def contacts():
    return render_template("contacts.html")
