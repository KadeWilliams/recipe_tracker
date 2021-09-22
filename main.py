from flask import Flask, jsonify, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from forms import RecipeForm


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "any-secret-key-you-choose"
db = SQLAlchemy(app)
Bootstrap(app)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cookbook_title = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True)
    page_number = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String, nullable=False)
    cuisine_type = db.Column(db.String, nullable=False)
    has_been_cooked = db.Column(db.Boolean, nullable=False)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    recipe_form = RecipeForm()
    if recipe_form.validate_on_submit():
        recipe = Recipe(
            cookbook_title=recipe_form.cookbook_title.data,
            url=recipe_form.website.data,
            image=recipe_form.image.data,
            page_number=recipe_form.page_number.data,
            name=recipe_form.name.data,
            cuisine_type=recipe_form.cuisine_type.data,
            has_been_cooked=recipe_form.has_been_cooked.data,
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=recipe_form)


@app.route("/show_all", methods=["GET", "POST"])
def show_all():
    recipes = db.session.query(Recipe).all()
    return render_template("show_all.html", recipes=recipes)


if __name__ == "__main__":
    app.run(debug=True)
