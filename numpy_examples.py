from PIL import Image
import numpy as np
from textures import pixel_generator

a = np.full((64, 64), 128, dtype=np.uint8)
im = Image.fromarray(a, mode="L")
print(im.size)
im.show()

a = np.full((64, 64, 3), 128, dtype=np.uint8)
im = Image.fromarray(a, mode="RGB")
print(im.size)
im.show()

im = Image.open("./input/beach.jpg", mode='r', formats=None)
im.show()
g = np.asarray(im)
print(np.shape(g))

b = np.fromiter(pixel_generator(64), np.int8)
b = np.reshape(b, (64, 64))
im = Image.fromarray(b, mode='L')
im.show()
