import numpy as np
from PIL import Image
from pixels import bw_pixel_generator, color_pixel_generator

def bw_image(resolution):
    data = np.fromiter(bw_pixel_generator(resolution), np.int8)
    data = np.reshape(data, (resolution, resolution))
    im = Image.fromarray(data, mode='L')
    return im

def color_image(resolution):
    data = np.fromiter(color_pixel_generator(resolution), np.int8)
    data = np.reshape(data, (resolution, resolution, 3))
    im = Image.fromarray(data, mode='RGB')
    return im

if __name__ == '__main__':
    my_res = 64
    my_img = bw_image(my_res)
    my_img.show()
    my_img = color_image(my_res)
    my_img.show()