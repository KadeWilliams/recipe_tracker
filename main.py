import sqlite3
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import URL, DataRequired


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
    page_number = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String, nullable=False)
    cuisine_type = db.Column(db.String, nullable=False)


class RecipeForm(FlaskForm):
    title = StringField("cookbook_title")
    url = StringField("website")
    page_number = IntegerField("page_number")
    name = StringField("recipe_name", validators=[DataRequired()])
    cuisine_type = StringField("cuisine_type", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    recipe_form = RecipeForm(request.form)
    return render_template("index.html", form=recipe_form)


if __name__ == "__main__":
    app.run(debug=True)
