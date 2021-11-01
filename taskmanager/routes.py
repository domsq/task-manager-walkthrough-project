from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    """ Define route to homepage file """
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    """ Define route to categories file """
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)



@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """ Define route to add category file """
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """ Define route to edit category file """
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)
