from PIL import Image
import numpy as np

im = Image.open("./input/beach.jpg", mode='r', formats=None)
print(im.size)
im.show()
g = np.asarray(im)
print(np.shape(g))
im = Image.fromarray(g, mode='RGB')
im.show()
print(im.size)

a = np.full((8, 8, 3), 128, dtype=np.uint8)
print(np.shape(a))
im = Image.fromarray(a, mode="RGB")
print(im.size)
b = np.asarray(im)
print(np.shape(b))
print(a)
print(b)
print(a == b)