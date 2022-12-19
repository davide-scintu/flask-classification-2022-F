import matplotlib.pyplot as plt
import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
# from app.forms.classification_form import ClassificationForm
from app.forms.transformation_form import TransformationForm
from ml.classification_utils import transformation_image
from config import Configuration


config = Configuration()


@app.route('/transformations', methods=['GET', 'POST'])
def transformations():
    """API for selecting a model and an image and running a
    classification job. Returns the output scores from the
    model."""
    form = TransformationForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data

        img_path = f'app/static/imagenet_subset/{image_id}'
        transformation_img_path = f'app/static/imagenet_transform/transform_{image_id}'

        transformation_image(img_path, transformation_img_path, color_factor=1.5, brightness_factor=1.8,
                             contrast_factor=1.9,
                             sharpness_factor=1.7)  # test values

        return render_template("transformation_output.html", image_id=image_id)

    # otherwise, it is a get request and should return the
    # image and transformation selector
    return render_template('transformation_select.html', form=form)


