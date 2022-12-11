import numpy as np
import matplotlib.pyplot as plt
import cv2


def plot_histogram(image):
    im = cv2.imread(image)
    # print("im type: ", type(im))
    vals = im.mean(axis=2).flatten()
    counts, bins = np.histogram(vals, range(257))
    plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
    plt.xlim([-0.5, 255.5])
    plt.savefig('test.JPEG')
    #plt.show()



def plot_histogram_rgb(image):
    im = cv2.imread(image)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([im], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


img_one_ch = 'app/static/imagenet_subset/n01443537_goldfish.JPEG'
# print(img_one_ch)
# print(type(img_one_ch))
plot_histogram(img_one_ch)

# img_rgb = 'app/static/imagenet_subset/n01443537_goldfish.JPEG'
# plot_histogram_rgb(img_rgb)

