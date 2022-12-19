from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FieldList, StringField, TextAreaField
from wtforms.validators import DataRequired

from app.utils.list_images import list_images
from config import Configuration

conf = Configuration()


class TransformationForm(FlaskForm):
    transformation = SelectField('transformation', choices=conf.transformation_parameters, validators=[DataRequired()])
    color = SelectField('color', choices=conf.color_input, validators=[DataRequired()])
    brightness = SelectField('brightness', choices=conf.brightness_input, validators=[DataRequired()])
    contrast = SelectField('contrast', choices=conf.contrast_input, validators=[DataRequired()])
    sharpness = SelectField('sharpness', choices=conf.sharpness_input, validators=[DataRequired()])
    # color_input = SubmitField('color_input')
    # brightness_input = SubmitField('brightness_input')
    # contrast_input = SubmitField('contrast_input')
    # sharpness_input = SubmitField('sharpness_input')
    image = SelectField('image', choices=list_images(), validators=[DataRequired()])
    submit = SubmitField('Submit')