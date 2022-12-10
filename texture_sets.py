from textures import bw_image, mono_image, color_image

MONO_COLORS = ('')

twos = (2**i for i in range(3,10))

for resolution in twos:
    print(resolution)
    im = color_image(resolution)
    im.show()
