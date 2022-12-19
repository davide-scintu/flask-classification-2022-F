import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw

"""IMAGE TRANSFORMATIONS"""

"""Open and image and show it"""
# im = Image.open('app/static/imagenet_subset/n01443537_goldfish.JPEG')
# print(im.format, im.size, im.mode)
# im.show()

"""Resize and rotate image"""
# out = im.resize((128, 128))
# out = im.rotate(45) # degrees counter-clockwise
# out.show()

"""Change color of the image"""
# with Image.open('app/static/imagenet_subset/n01443537_goldfish.JPEG') as im:
# im = im.convert("L")
# im.show()

"""Filter"""
# out = im.filter(ImageFilter.DETAIL)
# out.show()

"""Applying point transforms"""
# multiply each pixel by 5
# out = im.point(lambda i: i * 5)
# out.show()


"""IMAGE ENHANCE"""

# Reference: https://www.geeksforgeeks.org/python-pil-imageenhance-color-and-imageenhance-contrast-method/
#            https://www.programcreek.com/python/example/101765/PIL.ImageEnhance.Color

im = Image.open('app/static/imagenet_subset/n01443537_goldfish.JPEG')

"""Color"""
col = ImageEnhance.Color(im)
# col.enhance(5.0).show()


"""Brightness"""
brh = ImageEnhance.Brightness(im)
# brh.enhance(0.3).show()   # downgrade brightness


"""Contrast"""
con = ImageEnhance.Contrast(im)
# con.enhance(1.3).show("30% more contrast")


"""Sharpness"""
sharp = ImageEnhance.Sharpness(im)
# sharp.enhance(3.0).show() # upgrade sharpness


"""Add label to an image"""


# im = Image.open('app/static/imagenet_subset/n01443537_goldfish.JPEG')
# draw = ImageDraw.Draw(im)
# draw.text((100, 100),"Sample Text")
# im.save("with_text.png")


def transformation_image(image, color_factor=1.0, brightness_factor=1.0,
                         contrast_factor=1.0,
                         sharpness_factor=1.0):  # default values
    im = Image.open(image)  # open the image
    col = ImageEnhance.Color(im)
    im_col = col.enhance(color_factor)  # set the color factor
    brh = ImageEnhance.Brightness(im_col)
    im_col_brh = brh.enhance(brightness_factor)  # set brightness factor to the previous modified image
    con = ImageEnhance.Contrast(im_col_brh)
    im_cal_brh_con = con.enhance(contrast_factor)  # set contrast factor to the previous modified image
    sharp = ImageEnhance.Sharpness(im_cal_brh_con)
    im_cal_brh_con_sharp = sharp.enhance(sharpness_factor)  # set sharpness factor to the previous modified image
    im_cal_brh_con_sharp.show()


img_test = 'app/static/imagenet_subset/n01443537_goldfish.JPEG'
# im.show()
transformation_image(img_test, color_factor=1.0, brightness_factor=1.3, contrast_factor=1.0, sharpness_factor=3.0)

