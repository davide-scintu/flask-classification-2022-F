import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw
import uuid

def transformation_image(image, path, color_factor=1.0, brightness_factor=1.0,
                         contrast_factor=1.0,
                         sharpness_factor=1.0):
    """Transformation test fucntion adding sequentially enhancement factors, setting 1.0 as a default value"""
    im = Image.open(image)
    col = ImageEnhance.Color(im)
    im_col = col.enhance(color_factor)
    brh = ImageEnhance.Brightness(im_col)
    im_col_brh = brh.enhance(brightness_factor)
    con = ImageEnhance.Contrast(im_col_brh)
    im_cal_brh_con = con.enhance(contrast_factor)
    sharp = ImageEnhance.Sharpness(im_cal_brh_con)
    im_cal_brh_con_sharp = sharp.enhance(sharpness_factor)
    im_cal_brh_con_sharp.show()
    im_cal_brh_con_sharp.save(path)


id_image = uuid.uuid4()
img_test = 'app/static/imagenet_subset/n01443537_goldfish.JPEG'
path_test = f'app/static/imagenet_transform/{id_image}.JPEG'
transformation_image(img_test, path_test, color_factor=1.0, brightness_factor=1.3, contrast_factor=1.0, sharpness_factor=3.0)



