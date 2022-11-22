from array import array
import numpy as np
from PIL import Image

base_colors = [
(0, 0, 0),
(255, 0, 0),
(0, 255, 0),
(0, 0, 255),
(255, 255, 0),
(255, 0, 255),
(0, 255, 255),
(255, 255, 255),
]

def generate_image(resolution, color=False):
    if color:
        data = color_list(resolution)
    else:
        data = pixel_list(resolution)
    im = Image.new(mode='RGB',size=(resolution,resolution))
    im.putdata(data)
    return im

def pixel_list(tex_res):
    pixels = []
    step = tex_res//8
    sub_area = step**2
    for i in range(tex_res ** 2):
        #position in image
        global_x = i % tex_res
        global_y = i // tex_res
        #color block
        local_area = i // step
        local_area %= step
        #position in local gradient
        local_x = global_x % step
        local_y = global_y % step
        #gradient value
        total_steps = (step*local_y)+local_x
        score = total_steps/sub_area
        value = round(255 - (255 * score))
        #load into array
        pixels.append((value,value,value))
    return pixels

'''
Returns a generator the builds the flat squence of pixel values for a grayscale image.
Yields only a single value; this is not suitable for populating multiple channels.
'''
def pixel_generator(tex_res):
    step = tex_res // 8
    sub_area = step**2
    for i in range(tex_res ** 2):
        global_x = i % tex_res #position in image
        global_y = i // tex_res
        local_area = i // step #color block
        local_area %= step
        local_x = global_x % step #position in local gradient
        local_y = global_y % step
        total_steps = (step * local_y) + local_x #gradient value
        score = total_steps/sub_area
        value = round(255 - (255 * score))
        yield value

def pixel_array(tex_res):
    #return array('B', pixel_generator(tex_res))
    #return np.array(pixel_generator(32))
    return np.fromiter(pixel_generator(tex_res), np.dtype(np.int16))

def color_list(tex_res):
    pixels = []
    step = tex_res//8
    for i in range(tex_res ** 2):
        #position in image
        global_x = i % tex_res
        global_y = i // tex_res
        #color block
        block_index = i // step
        block_index %= step
        block_index += global_y // step
        #keep index in range
        block_index %= step
        #pick color from list
        pixels.append(base_colors[block_index])
    return pixels

def color_array(tex_res):
    #array = np.array()
    pass


if __name__ == '__main__':
    my_array = pixel_array(32)
    print(type(my_array))

    arr_im = Image.fromarray(my_array, mode='L')
    arr_im.show()

    bw_img = generate_image(32)
    bw_img.show()
    color_img = generate_image(32,color=True)
    color_img.show()
