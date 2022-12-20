"""Contains generators that can be used with np.fromiter.
Array must be reshaped depending on number of channels.
"""

from typing import Iterator
from random import randint
from PIL import ImageColor
import numpy as np


COLORS = ('red','orange','magenta','purple','yellow','lime','cyan','blue')
LITTLE_COLORS = ('red','lime','cyan','magenta')
BIG_COLORS = ('pink','red','orangered','orange',
    'magenta','darkorchid','purple','indigo',
    'gold', 'yellow','lime','green',
    'cyan','deepskyblue','blue','gray')


def bw_pixel_generator(tex_res:int) -> Iterator[int]:
    """Returns a generator that builds the flat squence of pixel values for a grayscale image.
Yields one value per pixel.

    Args:
        tex_res (int): resolution

    Yields:
        int: pixel value
    """

    for i in range(tex_res ** 2):
        score = gradient_score(i, tex_res, invert=True)
        yield round(255 * score)


def mono_pixel_generator(tex_res:int, color:str=None) -> Iterator[int]:
    """Returns a generator that builds the flat squence of pixel values for a grayscale image.
    Yields one value per pixel.

    Args:
        tex_res (int): resolution
        color (str):

    Yields:
        int: pixel value
    """
    if not color:
        color = COLORS[randint(0, len(COLORS)-1)]
    rgb = ImageColor.getrgb(color)

    for i in range(tex_res ** 2):
        score = gradient_score(i, tex_res, invert=True)
        for channel in scale_color(rgb, score):
            yield channel


def color_pixel_generator(tex_res, *args) -> Iterator[int]:
    """Returns RGB pixels one channel at a time.
    Total values will be three times the amount of pixels.

    Args:
        tex_res (int): resolution

    Yields:
        int: channel value
    """
    if tex_res > 64:
        color_res = 8
    elif tex_res >16:
        color_res = 4
    else:
        color_res = 2

    if args:
        colors = (arg for arg in args)
    else:
        match color_res:
            case 8:
                colors = BIG_COLORS
            case 4:
                colors = COLORS
            case 2:
                colors = LITTLE_COLORS

    for i in range(tex_res ** 2):
        score = gradient_score(i, tex_res, invert=True)
        index = color_index(i, tex_res, color_res, len(colors))
        color = scale_color(ImageColor.getrgb(colors[index]), score)
        for channel in color:
            yield channel


def gradient_score(position:int, resolution:int, invert:bool=False) -> float:
    """Finds the gradient score of a flat pixel.

    Args:
        position (int): Postion in sequence
        resolution (int): Image resolution
        invert (bool, optional): Gradient direction. Defaults to False.

    Returns:
        float: Gradient score
    """
    #size 16x16 is 256 values
    step = max(min((resolution // 8), 16), 4)
    sub_area = step**2

    #local coordinates
    local_x = (position % resolution) % step
    local_y = (position // resolution) % step

    #gradient value
    score = ((step * local_y) + local_x) / sub_area

    if invert:
        return 1 - score
    return score


def color_index(position:int, resolution:int, color_blocks:int, length:int) -> int:
    """Finds the color block index of a flat pixel.

    Args:
        position (int): Position in sequence.
        resolution (int): Image resolution
        color_res (int): Number of color blocks
        length (int): Number of total colors

    Returns:
        int: Index value
    """
    #size of color blocks in pixels
    color_step = resolution // color_blocks

    #color block coordinates
    color_x = (position % resolution) // color_step
    color_y = (position // resolution) // color_step

    #cummulative block number wrapping according to length
    return ((color_blocks * color_y) + color_x) % length


def scale_color(base_color:tuple, scale:float) -> tuple:
    """Lighten or darken a color.

    Args:
        pure_color tuple: channels
        scale (float): value between 0 and 1.0

    Returns:
        tuple: scaled channels
    """
    color = [int(i) for i in base_color]
    result = []
    #don't want pure white or pure black back when given a color
    scale = np.interp(scale, [0, 1], [0.01, 0.99])

    if scale > 0.5:
        #lighten, increase if not 255
        upscale = (scale - 0.5) * 2
        for channel in color:
            if channel == 0:
                result.append(round(255 * upscale))
            elif channel < 255:
                result.append(min(channel + round(channel * upscale), 255))
            else:
                result.append(255)
    elif scale < 0.5:
        #darken, decrease if not 0
        downscale = (scale * 2)
        for channel in color:
            if channel > 0:
                result.append(round(channel * downscale))
            else:
                result.append(0)
    else:
        return tuple(color)

    return tuple(result)

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
