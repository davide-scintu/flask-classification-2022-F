from flask import render_template
from app import app
from app.forms.transformation_form import TransformationForm
from ml.classification_utils import transformation_image
from config import Configuration

config = Configuration()


@app.route('/transformations', methods=['GET', 'POST'])
def transformations():
    """API for selecting an image and running a
    transformation. Returns the enhanced image."""
    form = TransformationForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data

        img_path = f'app/static/imagenet_subset/{image_id}'
        transformation_img_path = f'app/static/imagenet_transform/transform_{image_id}'

        color_id = form.color.data
        brightness_id = form.brightness.data
        contrast_id = form.contrast.data
        sharpness_id = form.sharpness.data

        transformation_image(img_path, transformation_img_path, color_factor=color_id, brightness_factor=brightness_id,
                             contrast_factor=contrast_id,
                             sharpness_factor=sharpness_id)

        # transformation_image(img_path, transformation_img_path, color_factor=1.5, brightness_factor=1.8,
        #                     contrast_factor=1.9,
        #                    sharpness_factor=1.7)  # test values

        return render_template("transformation_output.html", image_id=image_id)

    # otherwise, it is a get request and should return the
    # image and transformation selector
    return render_template('transformation_select.html', form=form)
