import math
import os
import re
from PIL import Image


def combine(*args:Image) -> Image:
    """Accepts any number of PIL Images and combines them into a single image

    Returns:
        Image: Composited image.
    """
    #read images and find size that fits every image
    base_images =[arg for arg in args]
    shared_res = (min(image.size[0] for image in base_images),
                    min(image.size[1] for image in base_images))

    #resize
    sized_images = [image.resize(shared_res) for image in base_images]

    #compute layout
    max_size = math.ceil(math.sqrt(len(sized_images)))
    min_size = max_size
    for i in range(max_size - 1, (max_size // 2) - 1, -1):
        if max_size * i >= len(sized_images):
            min_size = i
        else:
            break
    blocks = (max_size, min_size)

    #make new image
    new_image = Image.new('RGB',(blocks[0]*shared_res[0], blocks[1]*shared_res[1]), (128,128,128))
    for i, image in enumerate(sized_images):
        coords = (i % blocks[0], i // blocks[0])
        paste_coords = tuple(i * j for i, j in zip(shared_res, coords))
        new_image.paste(image, paste_coords)
    return new_image


def tile(image:Image, num_tiles:int, resolution:int,) -> Image:
    #doesn't crop rectangular images, result is distorted
    scaled_image = image.resize((resolution, resolution))
    tiled_image = combine(*(scaled_image for i in range(num_tiles**2)))
    return tiled_image


def tile_pbr(num_tiles:int, resolution:int):

    input = os.path.join(os.path.dirname(__file__), 'input')
    output = os.path.join(os.path.dirname(__file__), 'output')
    dir_list = [filename for filename in os.listdir(input) 
                if os.path.isdir(os.path.join(input, filename))]

    for dir in dir_list:
        input_dir = os.path.join(input, dir)
        output_dir = os.path.join(output, dir + '_' + str(resolution))
        os.makedirs(output_dir)
        for texture in os.listdir(input_dir):
            im = Image.open(os.path.join(input_dir, texture))
            im = tile(im, num_tiles, resolution)
            save_path = os.path.join(output_dir,dir+'_'+str(resolution)+'_'+pbr_channel(texture)+'.png')
            im.save(save_path, "PNG")


def pbr_channel(texture_name:str) -> str:
    texture_name = texture_name.lower()
    channel = ""
    if re.search("color", texture_name):
        channel = 'color'
    elif re.search('rough', texture_name):
        channel = 'rough'
    elif re.search('normal', texture_name) or re.search('bump', texture_name):
        channel = 'normal'
    elif re.search('height', texture_name):
        channel = 'height'
    elif re.search('ao', texture_name):
        channel = 'ao'
    return channel


if __name__ == '__main__':
    #image_a = Image.open('./input/beach.jpg')
    #image_a.show()
    #image_b = Image.open('./input/wine.png')
    #image_b.show()
    #image_c = combine(image_a, image_b, image_a)
    #image_c.show()
    #image_a = Image.open('./input/grungewall/GrungeWall03_4K_BaseColor.png')
    #image_d = tile(image_a, 4, 128)
    #image_d.show()
    print(tile_pbr(1,512))

