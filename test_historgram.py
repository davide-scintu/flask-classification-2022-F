import numpy as np
import matplotlib.pyplot as plt
import cv2

# read image
im = cv2.imread('app/static/imagenet_subset/n01443537_goldfish.JPEG')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# calculate histogram
counts, bins = np.histogram(vals, range(257))
# plot histogram centered on values 0..255
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])
plt.show()

# plot histogram with 255 bins
#b, bins, patches = plt.hist(vals, 255)
#plt.xlim([0,255])


color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([im],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()