from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import URL, DataRequired


class RecipeForm(FlaskForm):
    name = StringField("Recipe Name", validators=[DataRequired()])
    cookbook_title = StringField("Cookbook Title")
    website = StringField("Website", validators=[URL()])
    page_number = IntegerField("Page Number")
    image = StringField("Image", validators=[URL()])
    cuisine_type = StringField("Cuisine", validators=[DataRequired()])
    has_been_cooked = BooleanField("Cooked?", validators=[DataRequired()])
    submit = SubmitField("Submit")
