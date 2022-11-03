from PIL import Image

def generate_image(resolution):
    data = pixel_array(resolution)
    im = Image.new(mode='RGB',size=(resolution,resolution))
    im.putdata(data)
    return im

def pixel_array(tex_res):
    pixels = []
    step = tex_res//8
    sub_area = step**2
    for i in range(tex_res ** 2):
        #position in image
        global_x = i % tex_res
        global_y = i // tex_res
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


"""
    img = Image.new(mode='RGB',size=(128,128))
    step = 2
    start = 0
    for index, pixel in enumerate(img.getdata()):
        print(index,pixel)
        if index >= 15:
            break
"""

if __name__ == '__main__':
    test_img = generate_image(64)
    test_img.show()