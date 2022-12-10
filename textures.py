import numpy as np
from PIL import Image
from pixels import bw_pixel_generator, color_pixel_generator, mono_pixel_generator


def bw_image(resolution):
    """_summary_

    Args:
        resolution (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = np.fromiter(bw_pixel_generator(resolution), np.int8)
    data = np.reshape(data, (resolution, resolution))
    im = Image.fromarray(data, mode='L')
    return im

def mono_image(resolution, color=None):
    """_summary_

    Args:
        resolution (_type_): _description_
        color (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    data = np.fromiter(mono_pixel_generator(resolution, color), np.int8)
    data = np.reshape(data, (resolution, resolution, 3))
    im = Image.fromarray(data, mode='RGB')
    return im

def color_image(resolution, *colors):
    """_summary_

    Args:
        resolution (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = np.fromiter(color_pixel_generator(resolution, *colors), np.int8)
    data = np.reshape(data, (resolution, resolution, 3))
    im = Image.fromarray(data, mode='RGB')
    return im

if __name__ == '__main__':
    my_res = 128
    my_img = bw_image(my_res)
    my_img.show()
    my_img = mono_image(my_res, 'crimson')
    my_img.show()
    my_img = color_image(my_res)
    my_img.show()
