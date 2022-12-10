import math
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


if __name__ == '__main__':
    image_a = Image.open('./input/beach.jpg')
    #image_a.show()
    image_b = Image.open('./input/wine.png')
    #image_b.show()
    image_c = combine(image_a, image_b, image_a)
    image_c.show()
    image_d = tile(image_a, 2, 256)
    image_d.show()
