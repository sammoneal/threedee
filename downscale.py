from PIL import Image

im = Image.open('./input/beach.png')
im.resize(256, 256)
im.show()

def downscale(image, size):
    return image.resize(size, size)
