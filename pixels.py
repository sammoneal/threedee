import numpy as np
from PIL import ImageColor

COLORS = ['red','orange','purple','magenta','yellow','lime','cyan','blue']

def bw_pixel_generator(tex_res):
    """Returns a generator the builds the flat squence of pixel values for a grayscale image.
Yields only a single value; this is not suitable for populating multiple channels.

    Args:
        tex_res (int): resolution

    Yields:
        int: pixel value
    """
    step = min(tex_res // 8, 16)
    sub_area = step**2

    for i in range(tex_res ** 2):
        #position in image
        global_x = i % tex_res
        global_y = i // tex_res
        #position in local gradient
        local_x = global_x % step
        local_y = global_y % step
        #gradient value
        total_steps = (step * local_y) + local_x
        score = total_steps/sub_area
        #as int8
        value = round(255 * (1 - score))
        yield value

def color_pixel_generator(tex_res):
    """Returns RGB pixels one channel at a time. Total values will be 3x the amount of pixels.

    Args:
        tex_res (int): resolution

    Yields:
        int: channel value
    """
    gradient_step = min(tex_res//8, 16)
    sub_area = gradient_step**2

    if tex_res > 64:
        color_res = 8
    elif tex_res >16:
        color_res = 4
    else:
        color_res = 2

    color_step = tex_res // color_res

    for i in range(tex_res ** 2):
        #position in image
        global_x = i % tex_res
        global_y = i // tex_res
        #position in local gradient
        local_x = global_x % gradient_step
        local_y = global_y % gradient_step
        #gradient value
        total_steps = (gradient_step * local_y) + local_x
        score = total_steps/sub_area
        score = (1 - score)
        #color block
        color_x = global_x // color_step
        color_y = global_y // color_step
        color_index = (color_res * color_y) + color_x
        #keep index in range
        color_index %= 8
        #pick color from list
        color = scale_color(ImageColor.getrgb(COLORS[color_index]), score)
        for channel in color:
            yield channel

def scale_color(pure_color, scale):
    """Lighten or darken a color.

    Args:
        pure_color sequence: channels
        scale (float): value between 0 and 1.0

    Returns:
        tuple: scaled channels
    """
    color = [int(i) for i in pure_color]
    #don't want pure white or pure black back when given a color
    scale = np.interp(scale, [0, 1], [0.01, 0.99])

    if scale > 0.5:
        #lighten, increase if not 255
        amount = (scale - 0.5) * 2
        for i, channel in enumerate(color):
            if channel == 0:
                color[i] = round(255 * amount)
            elif channel < 255:
                color[i] = min(color[i] + round(color[i] * scale), 255)
    elif scale < 0.5:
        #darken, decrease if not 0
        amount = (scale * 2)
        for i, channel in enumerate(color):
            if channel:
                color[i] = round(color[i] * amount)
    else:
        return tuple(pure_color)
    return tuple(color)

if __name__ == '__main__':
    my_color = (255,0,0)
    print(scale_color(my_color, 0.01))
    print(scale_color(my_color, 0.25))
    print(scale_color(my_color, 0.45))
    print(scale_color(my_color, 0.5))
    print(scale_color(my_color, 0.55))
    print(scale_color(my_color, 0.75))
    print(scale_color(my_color, 0.99))
    my_color = (255,128,0)
    print(scale_color(my_color, 0.01))
    print(scale_color(my_color, 0.25))
    print(scale_color(my_color, 0.45))
    print(scale_color(my_color, 0.5))
    print(scale_color(my_color, 0.55))
    print(scale_color(my_color, 0.75))
    print(scale_color(my_color, 0.99))
