import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
# from app.forms.classification_form import ClassificationForm
from app.forms.transformation_form import TransformationForm
from ml.classification_utils import transformation_handler
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
        transformation_id = form.transformation.data

        redis_url = Configuration.REDIS_URL
        redis_conn = redis.from_url(redis_url)
        with Connection(redis_conn):
            q = Queue(name=Configuration.QUEUE)
            job = Job.create(transformation_handler, kwargs={
                "transformation_id": transformation_id,
                "img_id": image_id
            })
            # TODO: new handler
            task = q.enqueue_job(job)
            # transformation_handler()

        return render_template("transformation_output.html", image_id=image_id, jobID=task.get_id())

    # otherwise, it is a get request and should return the
    # image and transformation selector
    return render_template('transformation_select.html', form=form)