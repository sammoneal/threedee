from PIL import ImageColor

COLORS = ['red','orange','yellow','green','teal','blue','purple','magenta']

'''
Returns a generator the builds the flat squence of pixel values for a grayscale image.
Yields only a single value; this is not suitable for populating multiple channels.
'''
def bw_pixel_generator(tex_res):
    step = tex_res // 8
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
        score = (1 - score)
        #as int8
        value = round(255 * score)
        yield value

'''
Returns RGB pixels one channel at a time. Total values will be 3x the amount of pixels.
'''
def color_pixel_generator(tex_res):
    step = tex_res//8
    sub_area = step**2
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
        #position in local gradient
        local_x = global_x % step
        local_y = global_y % step
        #gradient value
        total_steps = (step * local_y) + local_x
        score = total_steps/sub_area
        score = (1 - score)
        #pick color from list
        color = scale_color(ImageColor.getrgb(COLORS[block_index]), score)
        for channel in color:
            yield channel


def scale_color(pure_color, scale):
    color = [int(i) for i in pure_color]
    if scale > 0.5:
        #lighten, increase if not 255
        amount = (scale - 0.5) * 2
        for i in range(3):
            if color[i] < 255:
                color[i] = round(255 * amount)
    elif scale < 0.5:
        #darken, decrease if not 0
        amount = (scale * 2)
        for i in range(3):
            if color[i]:
                color[i] = round(color[i] * amount)
    else:
        return tuple(pure_color)
    return tuple(color)

if __name__ == '__main__':
    my_color = (255,0,0)
    print(scale_color(my_color, 0.25))
    print(scale_color(my_color, 0.75))
    print(scale_color(my_color, 0.5))
    print(scale_color(my_color, 0.99))
    print(scale_color(my_color, 0.01))

