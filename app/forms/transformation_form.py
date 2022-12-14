from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

from app.utils.list_images import list_images
from config import Configuration

conf = Configuration()


class TransformationForm(FlaskForm):
    transformation = SelectField('transformation', choices=list_images(), validators=[DataRequired()])
    # attributes added to only check if the routes work correctly
    image = SelectField('image', choices=list_images(), validators=[DataRequired()])
    submit = SubmitField('Submit')