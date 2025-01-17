import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
from app.forms.classification_form import ClassificationForm
from app.forms.classification_form_histogram import ClassificationFormHistogram
from ml.classification_utils import classify_image, plot_histogram, clear_dir, plot_histogram_rgb
from config import Configuration

config = Configuration()


@app.route('/classifications', methods=['GET', 'POST'])
def classifications():
    """API for selecting a model and an image and running a 
    classification job. Returns the output scores from the 
    model."""
    form = ClassificationForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data
        model_id = form.model.data
        redis_url = Configuration.REDIS_URL
        redis_conn = redis.from_url(redis_url)
        with Connection(redis_conn):
            q = Queue(name=Configuration.QUEUE)
            job = Job.create(classify_image, kwargs={
                "model_id": model_id,
                "img_id": image_id
            })
            task = q.enqueue_job(job)

        # returns the image classification output from the specified model
        # return render_template('classification_output.html', image_id=image_id, results=result_dict)
        return render_template("classification_output_queue.html", image_id=image_id, jobID=task.get_id())

    # otherwise, it is a get request and should return the
    # image and model selector
    return render_template('classification_select.html', form=form)


@app.route('/classifications_histogram', methods=['GET', 'POST'])
def classifications_histogram():
    """API for selecting an image and return the histogram
    of the image"""
    form = ClassificationFormHistogram()
    if form.validate_on_submit():  # POST
        image_id = form.image.data

        img_path = f'app/static/imagenet_subset/{image_id}'
        histogram_img_path = f'app/static/imagenet_histogram/hist_{image_id}'

        plot_histogram(img_path, histogram_img_path)
        # plot_histogram_rgb(img_path, histogram_img_path)

        # histogram viewer with the corresponding image feedback
        return render_template('histogram_output.html', image_id=image_id)
    # image selector
    return render_template('histogram_template.html', form=form)







