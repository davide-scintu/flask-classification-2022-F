from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

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






"""Image Enhance"""

# Reference: https://www.geeksforgeeks.org/python-pil-imageenhance-color-and-imageenhance-contrast-method/

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


def transformation_image(image):
    # ref: https://www.programcreek.com/python/example/101765/PIL.ImageEnhance.Color
    pass

# img_test = 'app/static/imagenet_subset/n01443537_goldfish.JPEG'
