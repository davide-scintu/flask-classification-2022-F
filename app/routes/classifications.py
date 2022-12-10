import redis
import numpy as np
import matplotlib.pyplot as plt
import cv2

from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
from app.forms.classification_form import ClassificationForm
from app.forms.classification_form_histogram import ClassificationFormHistogram
from ml.classification_utils import classify_image, fetch_image
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
        print("image_id type: ", type(image_id))
        print("image_id: ", image_id)
        get_image = fetch_image(image_id)
        print("get_image type: ", type(get_image))
        print("get_image: ", get_image)
        im = cv2.imread(image_id)
        print("im type: ", type(im))
        print("im: ", im)
        #im2 = cv2.imread(get_image)
        #print(type(im2))

        #result = ...
        return render_template('histogram_output.html', image_id=image_id, result_id=result)
    return render_template('histogram_template.html', form=form)

def plot_histogram(image):
    im = cv2.imread(image)
    vals = im.mean(axis=2).flatten()
    counts, bins = np.histogram(vals, range(257))
    plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
    plt.xlim([-0.5, 255.5])
    plt.show()



